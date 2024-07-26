import io
import base64
import textwrap
from flask import Flask, render_template, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import re

app = Flask(__name__)


def parse_markdown_table(markdown):
    lines = markdown.strip().split('\n')
    headers = [h.strip() for h in re.findall(r'\|([^|]+)', lines[0])]
    rows = []
    for line in lines[2:]:  # Skip the separator line
        cells = [cell.strip() for cell in re.findall(r'\|([^|]+)', line)]
        if cells:  # Only add non-empty rows
            rows.append(cells)
    return headers, rows


def create_table_image(headers, rows, min_cell_width=100, cell_height=60, font_size=12, padding=5):
    font = ImageFont.load_default().font_variant(size=font_size)

    # Calculate cell widths based on content
    col_widths = [min_cell_width] * len(headers)
    for i, header in enumerate(headers):
        col_widths[i] = max(col_widths[i], font.getbbox(header)[2] + 2 * padding)
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], font.getbbox(cell)[2] + 2 * padding)

    img_width = sum(col_widths)
    img_height = cell_height * (len(rows) + 1)

    img = Image.new('RGB', (img_width, img_height), color='white')
    draw = ImageDraw.Draw(img)

    # Draw grid
    x_offset = 0
    for width in col_widths:
        draw.line([(x_offset, 0), (x_offset, img_height)], fill='black')
        x_offset += width
    draw.line([(img_width - 1, 0), (img_width - 1, img_height)], fill='black')

    for i in range(len(rows) + 2):
        draw.line([(0, i * cell_height), (img_width, i * cell_height)], fill='black')

    def draw_text_in_cell(text, cell_box):
        x, y, w, h = cell_box
        wrapped_text = textwrap.wrap(text, width=(w - 2 * padding) // (font_size // 2))
        for i, line in enumerate(wrapped_text[:3]):  # Limit to 3 lines
            left, top, right, bottom = font.getbbox(line)
            line_height = bottom - top
            draw.text((x + padding, y + padding + i * line_height), line, font=font, fill='black')

    # Write headers
    x_offset = 0
    for col, header in enumerate(headers):
        cell_box = (x_offset, 0, x_offset + col_widths[col], cell_height)
        draw_text_in_cell(header, cell_box)
        x_offset += col_widths[col]

    # Write data
    for row_idx, row in enumerate(rows):
        x_offset = 0
        for col, cell in enumerate(row):
            cell_box = (x_offset, (row_idx + 1) * cell_height, x_offset + col_widths[col], (row_idx + 2) * cell_height)
            draw_text_in_cell(cell, cell_box)
            x_offset += col_widths[col]

    return img


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    markdown = request.json['markdown']
    headers, rows = parse_markdown_table(markdown)
    print("Headers:", headers)
    print("Rows:", rows)
    img = create_table_image(headers, rows)

    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    img_data = base64.b64encode(img_io.getvalue()).decode()

    return jsonify({'image': f'data:image/png;base64,{img_data}'})


if __name__ == '__main__':
    app.run(debug=True)
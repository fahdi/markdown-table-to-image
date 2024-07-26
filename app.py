import io
import base64
from flask import Flask, render_template, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import re

app = Flask(__name__)

def parse_markdown_table(markdown):
    lines = markdown.strip().split('\n')
    headers = [h.strip() for h in re.findall(r'\|(.+?)\|', lines[0])]
    rows = []
    for line in lines[2:]:
        row = [cell.strip() for cell in re.findall(r'\|(.+?)\|', line)]
        rows.append(row)
    return headers, rows

def create_table_image(headers, rows, cell_width=100, cell_height=30, font_size=12):
    num_cols = len(headers)
    num_rows = len(rows) + 1  # +1 for header row
    
    img_width = cell_width * num_cols
    img_height = cell_height * num_rows
    
    img = Image.new('RGB', (img_width, img_height), color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", font_size)
    
    # Draw grid
    for i in range(num_rows + 1):
        draw.line([(0, i * cell_height), (img_width, i * cell_height)], fill='black')
    for i in range(num_cols + 1):
        draw.line([(i * cell_width, 0), (i * cell_width, img_height)], fill='black')
    
    # Write headers
    for col, header in enumerate(headers):
        x = col * cell_width + 5
        y = 5
        draw.text((x, y), header, font=font, fill='black')
    
    # Write data
    for row, data in enumerate(rows):
        for col, cell in enumerate(data):
            x = col * cell_width + 5
            y = (row + 1) * cell_height + 5
            draw.text((x, y), cell, font=font, fill='black')
    
    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    markdown = request.json['markdown']
    headers, rows = parse_markdown_table(markdown)
    img = create_table_image(headers, rows)
    
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    img_data = base64.b64encode(img_io.getvalue()).decode()
    
    return jsonify({'image': f'data:image/png;base64,{img_data}'})

if __name__ == '__main__':
    app.run(debug=True)
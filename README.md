# Markdown Table to Image Converter

This Flask-based web application converts Markdown tables to customizable PNG images. It features dynamic cell sizing, text wrapping, and support for multi-column tables, making it ideal for creating shareable table images from Markdown syntax.

## Features

- Convert Markdown tables to PNG images
- Dynamic cell sizing based on content
- Text wrapping for long content
- Support for multi-column tables
- Customizable cell padding and font size
- Web interface for easy usage

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/markdown-table-to-image.git
   cd markdown-table-to-image
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/`

3. Enter your Markdown table in the provided text area.

4. Click the "Generate Image" button to create and display the table image.

## Example

Input Markdown table:
```markdown
| Framework  | Key Feature           | Best For                    |
|------------|----------------------|----------------------------|
| Express.js | Lightweight & flexible | APIs & small projects      |
| Nest.js    | Structured & scalable  | Enterprise & complex apps  |
| Koa.js     | Minimalist & fast      | Custom servers & performance|
| Adonis.js  | Full-stack MVC         | Rapid full-stack development|
| LoopBack 4 | API-centric & robust   | Complex data-driven APIs   |
```

The application will generate a PNG image of this table, that will look like this:

| Framework  | Key Feature           | Best For                    |
|------------|----------------------|----------------------------|
| Express.js | Lightweight & flexible | APIs & small projects      |
| Nest.js    | Structured & scalable  | Enterprise & complex apps  |
| Koa.js     | Minimalist & fast      | Custom servers & performance|
| Adonis.js  | Full-stack MVC         | Rapid full-stack development|
| LoopBack 4 | API-centric & robust   | Complex data-driven APIs   |


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README provides:

1. A brief description of the project
2. Key features
3. Installation instructions
4. Usage guide
5. An example of input and output
6. Information on how to contribute
7. License information

You may want to customize this README further based on any specific details or additional features of your project. Also, don't forget to create a LICENSE file if you haven't already, and update the GitHub repository URL once you've created it.
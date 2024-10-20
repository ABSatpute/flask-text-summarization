# Flask-based Text Summarization Tool

This project is a Flask web application that integrates Hugging Face's BART model to summarize large bodies of text. Users can input text, specify a desired summary length, and get a real-time summary.

## Features
- User-friendly interface for text input
- Customizable summary length
- Real-time text summarization using Hugging Face's BART model
- Error handling for invalid inputs and API failures

## Technologies
- **Backend**: Flask (Python), Hugging Face API
- **Frontend**: Tailwind CSS, HTML5, JavaScript
- **API**: Hugging Face BART Model

## Screenshots

*Input Text Form*

![Input Form](static/images/input_form_screenshot.png)

*Summary Output*

![Summary Output](static/images/summary/output_screenshot.png)

## Live Demo
[Live Demo](https://your-live-demo-url.com)

## Installation

To get a local copy up and running, follow these steps:

### Prerequisites
- Python 3.x
- Hugging Face API token (Get it from [Hugging Face](https://huggingface.co/))

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/flask-text-summarization.git
    cd flask-text-summarization
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variable for Hugging Face API Token:
    ```bash
    export HF_API_TOKEN="your_hf_token"  # On Windows: set HF_API_TOKEN="your_hf_token"
    ```

5. Run the Flask app:
    ```bash
    flask run
    ```

6. Open your browser and go to `http://127.0.0.1:5000` to use the app.

## Usage
1. Enter the text you want to summarize in the input field.
2. Use the slider to select the desired summary length.
3. Click "Submit" to get a summary.
4. Optionally, click "Copy" to copy the summary to the clipboard.

## Future Improvements
- Add support for different summarization models (T5, GPT-3, etc.).
- Provide more options for text analysis (e.g., sentiment analysis, keyword extraction).
- Create a more polished UI with better design elements.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


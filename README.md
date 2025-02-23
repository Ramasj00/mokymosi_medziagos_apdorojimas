# Personalized Learning Report Generator

This project extracts text from PDF files, processes the extracted content using an LLM (Large Language Model), and generates a personalized learning report based on a student's profile.

## Features
- Extracts text from PDF files.
- Uses OCR (Tesseract) to extract text from images if text extraction fails.
- Analyzes content using Google Gemini AI.
- Generates personalized summaries, key concept explanations, questions, and further study recommendations.

## Requirements

### Mandatory Libraries
Ensure the following libraries are installed before running the script:
```bash
pip install pdfminer.six pytesseract Pillow pdf2image pandas matplotlib plotly google-generativeai
```

### Additional Dependencies
- `Tesseract OCR`: Install it separately for text extraction from images.
  - On Windows, download it from: [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
  - On Linux, install using:
    ```bash
    sudo apt install tesseract-ocr
    ```

## Usage

1. **Set up the environment**:
   - Install the required dependencies using the command above.
   - Ensure `Tesseract OCR` is installed and configured.
   - Obtain a Google Gemini API key and replace `"x"` in the script with your actual API key.

2. **Provide the PDF file path**:
   - Set the `local_pdf_path` variable to point to your PDF file.

3. **Run the script**:
   ```bash
   python main.py
   ```

4. **Output**:
   - The script extracts text, analyzes it using Google Gemini AI, and prints a personalized learning report.

## Troubleshooting
- If PDF text extraction fails, ensure `pdfminer.six` is installed.
- If images are not processed, install `pdf2image` and `pytesseract`.
- Set up `Tesseract OCR` correctly and ensure it is added to the system PATH.
- If the Google API call fails, verify your API key.

## License
This project is open-source and available under the MIT License.

## Contribution
Feel free to submit issues and pull requests for improvements.


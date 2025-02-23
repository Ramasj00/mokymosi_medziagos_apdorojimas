from google import genai
from google.genai import types
import pathlib
import httpx
import io
from PIL import Image
import pytesseract
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


local_pdf_path = ""

#example
student_profile = {
    {"Mokslinio tyrimo rašymo pagrindai" : 7,
     "Mašininis mokymas" : 6,
     "AI sistemos valdymo pagrindai" : 9
     }
}


def extract_text_from_pdf(pdf_bytes):
    try:
        from pdfminer.high_level import extract_text
        text = extract_text(io.BytesIO(pdf_bytes))
        return text
    except ImportError:
        print("Pdfminer.six biblioteka neįdiegta. Būtina ją įdiegti. (pip install pdfminer.six)")
        return ""

def extract_text_from_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)
    return text

def analyze_content_with_llm(content, student_profile):
    client = genai.Client(api_key="x")
    prompt = f"""
    Based on the following content:
    {content}

    And the student profile:
    {student_profile}

    Generate:
    - A personalized summary.
    - Explanations of key concepts.
    - Questions for the student.
    - Recommendations for further study.
    - Mainly Lithuanian language should be generated.
    """
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[prompt],
    )
    return response.text

def generate_report(analysis_result, student_profile):
    report = f"""
    Personalized Learning Report

    Studento dalykų pažymiai:
    {student_profile}

    Analysis Result:
    {analysis_result}
    """
    return report

# Pagrindinė logika
try:
    with open(local_pdf_path, 'rb') as pdf_file:
        pdf_bytes = pdf_file.read()

    text = extract_text_from_pdf(pdf_bytes)

    # Jei tekstas nepavyko išgauti iš pdf. Bandom išgauti iš atskirų puslapių kaip iš nuotraukų.
    if not text.strip():
        try:
            from pdf2image import convert_from_bytes
            images = convert_from_bytes(pdf_bytes)
            for img in images:
                img_bytes = io.BytesIO()
                img.save(img_bytes, format='PNG')
                img_bytes = img_bytes.getvalue()
                text += extract_text_from_image(img_bytes)
        except ImportError:
            print("pdf2image biblioteka neįdiegta. Būtina ją įdiegti. (pip install pdf2image)")

    analysis_result = analyze_content_with_llm(text, student_profile)
    report = generate_report(analysis_result, student_profile)
    print(report)

except FileNotFoundError:
    print(f"Failas nerastas: {local_pdf_path}")
except Exception as e:
    print(f"Klaida: {e}")
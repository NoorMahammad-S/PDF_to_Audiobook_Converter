import requests
import PyPDF2

# Replace 'YOUR_ISPEECH_API_KEY' with your actual iSpeech API key
API_KEY = 'YOUR_ISPEECH_API_KEY'

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

# Function to convert text to speech using iSpeech API
def text_to_speech(text, api_key):
    url = "http://api.ispeech.org/api/rest"
    data = {
        "apikey": api_key,
        "action": "convert",
        "format": "mp3",
        "text": text,
    }
    response = requests.post(url, data=data)
    return response.content

# Main function to convert PDF to speech
def pdf_to_audiobook(pdf_file_path, output_mp3_path):
    text = extract_text_from_pdf(pdf_file_path)
    audio_data = text_to_speech(text, API_KEY)
    with open(output_mp3_path, 'wb') as audio_file:
        audio_file.write(audio_data)

if __name__ == '__main__':
    pdf_file_path = 'your_pdf_file.pdf'  # Replace with the path to your PDF file
    output_mp3_path = 'output.mp3'  # Replace with the desired output MP3 file path
    pdf_to_audiobook(pdf_file_path, output_mp3_path)
    print(f"Conversion complete. Audiobook saved to {output_mp3_path}")

import base64
import concurrent.futures
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

with open(os.getenv('PROMPT_FILEPATH')) as f:
    system_prompt = f.read().strip()

def format_for_tts(pdf_filepath):
    print(f'Processing {pdf_filepath}')
    client = genai.Client(
        api_key=os.getenv('GEMINI_API_KEY'),
    )

    files = [
        client.files.upload(file=pdf_filepath),
    ]
    model = os.getenv('MODEL')
    contents = [
        types.Content(
            role='user',
            parts=[
                types.Part.from_uri(
                    file_uri=files[0].uri,
                    mime_type=files[0].mime_type,
                ),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0,
        response_mime_type='text/plain',
        system_instruction=[
            types.Part.from_text(text=system_prompt),
        ],
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )
    with open(os.path.splitext(pdf_filepath)[0] + '.txt', 'w') as f:
        f.write(response.text)

if __name__ == '__main__':
    filepaths = sys.argv[1:]

    with concurrent.futures.ThreadPoolExecutor(
            max_workers=int(os.getenv('MAX_WORKERS'))) as executor:
        for filepath in filepaths:
            if filepath.endswith('.pdf'):
                executor.submit(format_for_tts, filepath)

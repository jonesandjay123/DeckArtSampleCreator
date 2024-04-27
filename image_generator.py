import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

def setup_openai_client():
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    return OpenAI(api_key=api_key)

def generate_image(client, prompt, model="dall-e-2", size="256x256", quality="standard"):
    print("Generating image, please wait...")
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=1
    )
    print("Image generation complete.")
    return response.data[0].url

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        # 檢查Content-Type來決定是PNG還是JPEG
        content_type = response.headers['Content-Type']
        if 'image/png' in content_type:
            file_extension = 'png'
        else:
            file_extension = 'jpg'

        # 儲存文件
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = f"data/{filename}_{timestamp}.{file_extension}"
        with open(file_path, 'wb') as f:
            f.write(response.content)
        return file_path
    else:
        return None
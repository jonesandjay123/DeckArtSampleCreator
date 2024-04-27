from excel_reader import load_data_from_excel
from image_generator import download_image, setup_openai_client, generate_image
from tqdm import tqdm

def main():
    model = "dall-e-2"  # 預設模型
    size = "256x256"  # 預設大小
    quality = "standard"  # 預設質量

    client = setup_openai_client()
    data = load_data_from_excel('decks.xlsx')
    data = data.iloc[0:3]  # Only process the first row for testing

    for index, row in tqdm(data.iterrows(), total=data.shape[0], desc="Generating Images"):
        image_url = generate_image(client, row['English Prompt'], model=model, size=size, quality=quality)
        if image_url:
            file_path = download_image(image_url, row['Label'])
            if file_path:
                print(f"Image saved to {file_path}")
            else:
                print("Failed to download the image.")
        else:
            print("Failed to generate the image URL.")


if __name__ == '__main__':
    main()

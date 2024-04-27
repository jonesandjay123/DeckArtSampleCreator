from excel_reader import load_data_from_excel
from image_generator import setup_openai_client, generate_image

def main():
    # Set up OpenAI client
    setup_openai_client()
    # Load data from Excel
    data = load_data_from_excel('decks.xlsx')
    # Iterate through the data and generate images
    for index, row in data.iterrows():
        image = generate_image(row['English Prompt'])
        print(f"Generated image for {row['Label']}")

if __name__ == '__main__':
    main()

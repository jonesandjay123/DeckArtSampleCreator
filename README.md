# DeckArtSampleCreator

## Project Overview
DeckArtSampleCreator is an automated tool built with Python, utilizing OpenAI's DALL-E 3 API to generate digital artwork for trading cards. This project specifically targets creators and developers looking to quickly produce high-quality, thematic illustrations for card games. The images generated align with the vibrant and dynamic aesthetics of modern fantasy card games.

## Features
- Automates the generation of card images.
- Uses DALL-E 3 to ensure high-quality artwork.
- Customizable prompts to fit different thematic needs.

## Installation
Before you start using the DeckArtSampleCreator, you need to set up your Python environment and install several required packages. Follow the instructions below to get started:

### Prerequisites
Ensure you have Python 3.8 or newer installed on your machine. You can download Python [here](https://www.python.org/downloads/).

### Required Libraries
DeckArtSampleCreator uses several Python libraries. You can install all required libraries using `pip`. Run the following command in your terminal:

```bash
pip install pandas openai Pillow requests
```

### Configuration
1. Obtain an API key from OpenAI.
2. Create a .env file in the root directory of this project.
3. Add the following line to your .env file:
   
```
OPENAI_API_KEY='Your-OpenAI-API-Key-Here'
```

### Usage
To use DeckArtSampleCreator, follow these steps:

1. Update the deck.xlsx file with your desired card image descriptions.
2. Run the script using:
```
python deck_art_sample_creator.py
```
3. Generated images will be saved in the designated output folder.

### Contribution
Contributions are welcome! If you have improvements or bug fixes, please fork the repository and submit a pull request.

### License
This project is released under the MIT License. See the LICENSE file for details.












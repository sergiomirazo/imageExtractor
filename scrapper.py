import requests
from bs4 import BeautifulSoup
import json
import os

# URL from the page
url = 'web page url'

# HTTP headers for the request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# We send a GET request to the URL with the headers
response = requests.get(url, headers=headers)

# Verify the response status
if response.status_code != 200:
    print(f"Error: Bad request: {response.status_code}")
else:
    soup = BeautifulSoup(response.content, 'html.parser')

    # We obtain all the 'figure' tags
    figures = soup.find_all('figure')

    # Initialize the dictionary to store the data
    data = {}

    # We will iterate over each 'figure' tag starting from the second one
    for index, figure in enumerate(figures[0:], start=1):  # We start the index from 1
        img_tag = figure.find('img')
        div_tag = figure.find('div', class_='wp-block-uagb-image--layout-overlay__inner center-center')
        title_tag = div_tag.find('h3') if div_tag else None
        figcaption_tag = figure.find('figcaption')

        if img_tag and title_tag and figcaption_tag:
            img_url = img_tag['src'].replace('webp', 'png')  # Change the extension to .png
            title = title_tag.get_text(strip=True)
            figcaption = figcaption_tag.get_text(strip=True)
            
            # Download the image
            img_response = requests.get(img_url, headers=headers)
            img_name = f'fig{index}.png'
            with open(img_name, 'wb') as img_file:
                img_file.write(img_response.content)
            
            # Save the data in the dictionary
            data[f'fig{index}'] = {
                'title': title,
                'figcaption': figcaption,
                'imgURL': img_url
            }

    # Save the dictionary as JSON using utf-8
    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print('Data and downloads completed successfully.')

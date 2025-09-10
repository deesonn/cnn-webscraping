'''
Name: Daniel Nguyen
Date: April 19, 2025
Purpose:
'''

import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import schedule
import time
import tkinter as tk

urls = [
    "https://www.cnn.com/world",
    "https://www.cnn.com/politics",
    "https://www.cnn.com/business"
]

# Scrape multiple pages
def scrape_multiple_pages(urls):
    all_headlines = []
    for url in urls:
        html = urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        headlines = soup.find_all("h2")
        for headline in headlines:
            all_headlines.append(headline.text.strip())
    return all_headlines

# Categorize headlines by Section
def categorize_headlines(headlines):
    categorize_headlines = {
        "World": [],
        "Politics": [],
        "Business": []
    }
    for headline in headlines:
        if "World" in headline:
            categorize_headlines["World"].append(headline)
        elif "Politics" in headline:
            categorize_headlines["Politics"].append(headline)
        elif "Business" in headline:
            categorize_headlines["Business"].append(headline)
    return categorize_headlines

# Save each section's headline into single CSV file with section name
def save_headlines_to_csv(categorized_headlines):
    for section, headlines in categorized_headlines.items():
        df = pd.DataFrame(headlines, columns=["Headlines"])
        df.to_csv(f"{section}_headlines.csv", index=False)

# Main execution
categorize_headlines(scrape_multiple_pages(urls))
save_headlines_to_csv(categorize_headlines)

# Turn each headlines into a dataframe
# def headlines_to_dataframe(headlines):
#     df = pd.DataFrame(headlines, columns=["CNN Webpage Headlines"])
#     return df

# headlines = scrape_multiple_pages(urls)
# df = headlines_to_dataframe(headlines)
# print(df)

# # Save into CSV
# df.to_csv("headlines.csv", index=False)


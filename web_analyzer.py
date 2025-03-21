import requests
import matplotlib.pyplot as plt
import re
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:
    response = requests.get(url)
    response.raise_for_status()  # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

# Data Analysis
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
numHeadings = len(headings)
print(f"Number of headings: {numHeadings}")

links = soup.find_all('a')
numLinks = len(links)
print(f"Number of links: {numLinks}")

paragraphs = soup.find_all('p')
numParagraphs = len(paragraphs)
print(f"Number of paragraphs: {numParagraphs}")

# Keywords Analysis
print("Please enter a keyword that you want to search for:")
keyword = input().strip().lower()
text_elements = soup.find_all(string=True) # Extract all text content from paragraphs
text_content = " ".join(text.lower() for text in text_elements)

keyword_count = text_content.count(keyword) # Count occurrences of the keyword as a whole word
print(f"The word '{keyword}' appears {keyword_count} times in the webpage's content.")

# Word Frequency Analysis
text = soup.get_text().lower()
words = re.findall(r'\b\w+\b', text)

wordFrequency = {} # dictionary to count word frequency
for word in words:
    word = word.lower()
    wordFrequency[word] = wordFrequency.get(word, 0) + 1

# Get top 5 words by frequency
top_words = sorted(wordFrequency.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 most frequently occurring words:")
for word, count in top_words:
    print(f"{word}: {count}")

# Finding the Longest Paragraph
longestParagraph = ""
longestWordCount = 0

for paragraph in paragraphs:
    text = paragraph.get_text().strip()
    words = re.findall(r'\b\w+\b', text) # Use regex to find all words in the paragraph

    if len(words) < 5:
        continue

    if len(words) > longestWordCount:
        longestWordCount = len(words)
        longestParagraph = text

print("\nThe longest paragraph from the page:")
print(longestParagraph)
print(f"\nIt contains {longestWordCount} words\n")

# Visualizing Results
labels = ['Headings', 'Links', 'Paragraphs']
values = [numHeadings, numLinks, numParagraphs]
plt.bar(labels, values)
plt.title('Group 1')
plt.ylabel('Count')
plt.savefig('wiki_analysis_chart.png')
plt.show()

import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

# print(soup.prettify())

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
keywordCount = 0
text = soup.get_text()
punctuation = "`~!@#$%^&*()_+[}{]\\|;:'\"<,.>/?"
for word in text.split():
    cleanWord = word.strip(punctuation).lower()
    if keyword == cleanWord:
        keywordCount += 1
print(f"The word '{keyword}' appears {keywordCount} times in the webpages content.")

# Word Frequency Analysis
text = soup.get_text()
punctuation = "`~!@#$%^&*()_+[{]}\\|;:'\"<,>.?/"
words = text.split()
cleaned_words = []
for word in words:
    clean_word = word.strip(punctuation).lower()
    if clean_word: 
        cleaned_words.append(clean_word)

wordFrequency = {}
for word in cleaned_words:
    if word in wordFrequency:
        wordFrequency[word] += 1
    else:
        wordFrequency[word] = 1

top_words = sorted(wordFrequency.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 most frequently occurring words:")
for word, count in top_words:
    print(f"{word}: {count}")

# Finding the Longest Paragraph
longestParagraph = ""
longestWordCount = 0

for paragraph in paragraphs:
    text = paragraph.get_text().strip()
    words = text.split()

    if len(words) < 5:
        continue

    if len(words) > longestWordCount:
        longestWordCount = len(words)
        longestParagraph = text

print("\nThe longest paragraph is:\n")
print(longestParagraph)
print(f"\nIt contains {longestWordCount} words\n")

# Visualizing Results
import matplotlib.pyplot as plt
labels = ['Headings', 'Links', 'Paragraphs']
values = [numHeadings, numLinks, numParagraphs]
plt.bar(labels, values)
plt.title('1')
plt.ylabel('Count')
plt.show()






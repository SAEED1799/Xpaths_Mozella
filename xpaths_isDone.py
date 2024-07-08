import requests
import lxml.html
import json

# Load XPath expressions and descriptions from JSON file
with open('xpaths.json', 'r') as file:
    xpaths = json.load(file)

# URL of the Mozilla Support Forum for Firefox
url = "https://support.mozilla.org/en-US/questions/firefox?show=all"

# Fetch the HTML content of the page
response = requests.get(url)
html_content = response.content

# Parse the HTML content using lxml
tree = lxml.html.fromstring(html_content)

# Iterate over the XPath expressions and find the number of elements for each
results = []
for key, value in xpaths.items():
    xpath = value['xpath']
    description = value['description']
    elements = tree.xpath(xpath)
    count = len(elements)
    results.append((key, description, count))

# Print the results
for key, description, count in results:
    print(f"{key} ({description}): {count} elements found")

#pip install bs4 requests
#pip install requests beautifulsoup4
#pip install requests beautifulsoup4 pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Website URL
url = "https://www.dawn.com/"

# Step 2: Data fetch karna
response = requests.get(url)

# Step 3: HTML parse karna
soup = BeautifulSoup(response.text, "html.parser")


# 4-  Find all headings (h1–h6)
headings = []
for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
    text = heading.get_text(strip=True)
    if text:
        headings.append({"Tag": heading.name, "Text": text})

# 5-  Show data in a table (DataFrame)
df = pd.DataFrame(headings)
print(df)

# 6-  Save results to CSV file
df.to_csv("dawn_headings.csv", index=False)
print("\n Headings saved to 'dawn_headings.csv'")

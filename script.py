import requests
import pandas as pd

# Fetch data from the URL
url = "https://fantasy.premierleague.com/api/bootstrap-static/"
response = requests.get(url)
data = response.json()

# Extract 'elements' and save as CSV
try:
    elements = data.get('elements', [])
    if elements:
        df_elements = pd.DataFrame(elements)
        df_elements.to_csv("elements.csv", index=False)
    else:
        print("No 'elements' found.")
except ValueError as e:
    print(f"Couldn't convert 'elements' to DataFrame: {e}")
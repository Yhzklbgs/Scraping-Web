import requests
from bs4 import BeautifulSoup

# Define the URL you want to scrape
url = "http://qaz.wtf/u/convert.cgi?text=Yehezkiel+Bagas"

# Make a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the HTML content from the response
    html = response.text

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the table element with cellpadding=5
    table = soup.find('table', {'cellpadding': '5'})

    # Initialize a dictionary to store the extracted data
    data = {}

    if table:
        # Find all rows within the table
        rows = table.find_all('tr')

        for row in rows:
            # Find all cells within the row
            cells = row.find_all('td')

            if len(cells) == 2:
                # Extract the text from the first and second cells
                cell1 = cells[0].text.strip()
                cell2 = cells[1].text.strip()

                # Store the data in the dictionary
                data[cell1] = cell2

    # Print the extracted data
    for key, value in data.items():
        print(f"{key}\t{value}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

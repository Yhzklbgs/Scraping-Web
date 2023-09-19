import requests
from bs4 import BeautifulSoup

# Define the URL
tv_channels = ["rcti", "nettv", "antv", "gtv", "indosiar", "inewstv", "kompastv", "metrotv", "mnctv", "rtv", "sctv", "trans7", "transtv", "tvone", "tvri"]
url = "https://www.jadwaltv.net/channel/rcti"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all tables containing the schedule data
    schedule_tables = soup.find_all('table', class_='table-bordered')
    
    # Initialize variables to store the schedule data
    schedule_data = []
    
    # Iterate through the tables to extract the schedule data
    for schedule_table in schedule_tables:
        # Find the rows within each table
        rows = schedule_table.find_all('tr')
        
        # Iterate through rows to find the relevant data
        for i in range(len(rows)):
            row = rows[i]
            
            # Find the cells within each row
            cells = row.find_all('td')
            
            # Check if the row has at least two cells
            if len(cells) >= 2:
                # Extract the time and program name
                time = cells[0].text.strip()
                program = cells[1].text.strip()
                
                # Append the data to the schedule_data list
                schedule_data.append((time, program))
    
    # Print the "Jam" and "Acara" headers
    print("Jam\tAcara")
    
    # Print the schedule data
    for time, program in schedule_data:
        print(f"{time}\t{program}")
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)

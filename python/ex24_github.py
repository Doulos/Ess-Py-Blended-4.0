import requests
import pandas as pd

# GitHub repository information
owner = "python"
repo = "peps"

payload = {'state':'open'}

# API endpoint for listing pull requests
url = f"https://api.github.com/repos/{owner}/{repo}/issues"

# Make a GET request to the GitHub API
response = requests.get(url, params=payload)

if response.status_code == 200:
    read_data = response.json()
    df = pd.DataFrame(read_data)
    
    # Convert timestamps to datetime and format them
    df['created_at'] = pd.to_datetime(df['created_at']).dt.strftime('%d-%m-%Y')
    df['updated_at'] = pd.to_datetime(df['updated_at']).dt.strftime('%d-%m-%Y')
    
     
    for index, column in enumerate(df.columns):
        print(f"Column {index+1}: {column}")
        
    # Print information about each issue
    for index, (idx,row) in enumerate(df.iterrows()):
        print(f"{index+1} Issue #{row['number']}: {row['title']} was created on {row['created_at']} and updated at {row['updated_at']}")
        
else:
    print(f"Failed to fetch issues. Status code: {response.status_code}")
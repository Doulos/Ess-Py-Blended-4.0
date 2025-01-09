import requests
import zipfile
import os
import pandas as pd

# Send the GET request
r = requests.get('https://timezonedb.com/files/TimeZoneDB.csv.zip')

# Check if the request was successful
if r.status_code == 200:
    # Open a file in binary write mode
    zip_filename = 'TimeZoneDB.csv.zip'
    with open(zip_filename, 'wb') as f:
        f.write(r.content)  # Write the content to the file
    print('File saved as', zip_filename)

    # Unzip the downloaded file
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall('.')  # Extract to the current directory
    print('File unzipped successfully.')
else:
    print('Failed to retrieve the file. Status code:', r.status_code)
    
# Print border
print (80*'-') 

# Load the time_zone CSV file into a Pandas DataFrame(df) with specified column names
df = pd.read_csv('time_zone.csv', names=['zone_name', 'country_code', 'abbreviation', 'time_start', 'gmt_offset', 'dst'])

# Load the country CSV file into a Pandas DataFrame(df1) with specified column names
df1 = pd.read_csv('country.csv', names=['country_code', 'country_name'])

# Create a new dataframe df2 by merging df and df1 on country_code
df2 = pd.merge(df, df1, on='country_code', how='inner')

# Filter df2 for rows where country_name is 'united states' and gmt_offset is -28800 (8 hours behind in seconds)
filtered_df2 = df2[(df2['country_name'] == 'United States') & (df2['gmt_offset'] == -28800)]

# Drop duplicates to ensure each zone_name is only mentioned once
filtered_df2_unique = filtered_df2.drop_duplicates(subset='zone_name')

# Print filtered dataframe with names of zone/city in the US that are behind GMT by 8 hours
print("Filtered DataFrame with names of zone/city in the US that are behind GMT by 8 hours")
print()
print(filtered_df2_unique[['zone_name', 'gmt_offset', 'country_name']])

# Print border
print (80*'-')  

# Filter df2 for rows where gmt_offset is 28800 (8 hours ahead in seconds)
df3 = df2[df2['gmt_offset'] == 28800]

# Drop duplicates to ensure each zone_name is only mentioned once
df3_unique = df3.drop_duplicates(subset='zone_name')

# Print filtered dataframe with names of zone/city and country
print("Filtered DataFrame df3 of zones which are ahead of GMT by 8 hours")
print()
print(df3_unique[['zone_name','gmt_offset', 'country_name']])
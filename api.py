import requests
from prettytable import PrettyTable

url = "https://randomuser.me/api/"

headers = {}
payload = {}

response = requests.get(url, headers=headers)

data = response.json() # Assign json response to a variable

table = PrettyTable(["Gender", "City", "Age","version","ID"])

gender = data["results"][0]["gender"]
city = data["results"][0]["location"]["city"]
age = data["results"][0]["dob"]["age"]
version = data["info"]["version"]
id = data["results"][0]["id"]["name"]

# Add a row to the table
table.add_row([gender, city, age,version,id])

# Print the table
print(table)
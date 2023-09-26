import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

# Configura las credenciales
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)

url = 'https://docs.google.com/spreadsheets/d/1HLkFa8XFrGM-WpBXzj7S6V8NgRf34Lp_jrsM4Dg-Xng/edit#gid=468537384'

spreadsheet = client.open_by_url(url)
worksheet = spreadsheet.sheet1

# Elige la columna que deseas recorrer (por ejemplo, columna A)
columna = worksheet.col_values(6)



with open('archivo.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for value in columna:
        writer.writerow([value])

file.close()

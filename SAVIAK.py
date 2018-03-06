import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('Secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Sample").sheet1

# Extract and print all of the values
pp=pprint.PrettyPrinter()
list_of_hashes = sheet.get_all_records()
#pp.pprint(list_of_hashes)

email=list_of_hashes[3]['email']

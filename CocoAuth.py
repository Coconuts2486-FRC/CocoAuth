import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope  = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds  = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Zach\\Desktop\\CocoAuth-9999c276da21.json', scope)
client = gspread.authorize(creds)

# determines if a sheet exists within the document
def doesDocExist():
    global now
    now = datetime.datetime.today()
    global doc
    try:
        doc = client.open(str(now.year))
        print("Found a document for " + str(now.year) + ".")
    except gspread.exceptions.SpreadsheetNotFound:
        doc = client.create(str(now.year))
        doc.share('zachs@team2486.org', perm_type='user', role='writer')
        doc.share('apps@team2486.org', perm_type='user', role='writer')
        print("Could not find a document for " + str(now.year) + ". Creating...")

# determine if the doc contains the month
def doesSheetExist():
    global sheet
    try:
        sheet = doc.worksheet(str(now.month))
        print("Found the worksheet for month " + str(now.month) + ".")
    except gspread.exceptions.WorksheetNotFound:
        sheet = doc.add_worksheet(str(now.month), rows="800", cols="10")
        print("Could not find a worksheet for month " + str(now.month) + ". Creating...")

# formats a sheet
def formatSheet():
    sheet.update_cell(1, 1, "Person")
    sheet.update_cell(1, 2, "Date")

def addData():
    

# runtime code goes here
doesDocExist()
doesSheetExist()

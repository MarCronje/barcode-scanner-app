import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define API scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials
creds = ServiceAccountCredentials.from_json_keyfile_name("google_credentials.json", scope)
client = gspread.authorize(creds)

# Open Google Sheet by URL
sheet = client.open_by

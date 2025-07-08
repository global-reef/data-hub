import os
import json
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Load credentials
creds_json = os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]
creds_dict = json.loads(creds_json)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
gc = gspread.authorize(credentials)

# Sheets to export
sheets = {
    "ArtificialReefs_MASTER.csv": "https://docs.google.com/spreadsheets/d/1jpvxJ6ONqlqisBRHGjQlNpmFoPy5RXP0XdQg5R-1ayM",
    "FishSize_MASTER.csv": "https://docs.google.com/spreadsheets/d/1AKiXHNcAd9m1HwAptyv6tVf6EOprdIts"
}

# Output folder
output_folder = "Artificial_Reef_Research"
os.makedirs(output_folder, exist_ok=True)

# Export each sheet
for filename, url in sheets.items():
    sh = gc.open_by_url(url)
    worksheet = sh.worksheet("data")
    df = pd.DataFrame(worksheet.get_all_records())
    out_path = os.path.join(output_folder, filename)
    df.to_csv(out_path, index=False)

import os
import json
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Load service account credentials from GitHub secret
creds_json = os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]
creds_dict = json.loads(creds_json)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
gc = gspread.authorize(credentials)

# Mapping of file names to Sheet URLs
sheets = {
    "COTs_Abund_MASTER.csv": "https://docs.google.com/spreadsheets/d/1WT6ayn4WmTmQziXpSjSkODzqSdFHSVwyLDVvaRbFPd0",
    "COTs_Scars_MASTER.csv": "https://docs.google.com/spreadsheets/d/1m5zrMVO2mNV9u61dLHIfNC-TRsY2JRCTHhkF4hmJnnE",
    "COTs_Fish_MASTER.csv": "https://docs.google.com/spreadsheets/d/1oFo4foGdvK-9iLihYaTfO7iZJOuV5X8bn2BK5OgRUp0",
    "COTs_PITS_MASTER.csv": "https://docs.google.com/spreadsheets/d/1R-BkyEg5dfYG-yig8Hzr2SVRfUMVKSP4G2KNopEko8M"
}

# Output folder
output_folder = "COTS_Research"
os.makedirs(output_folder, exist_ok=True)

# Process each sheet
for filename, url in sheets.items():
    sh = gc.open_by_url(url)
    worksheet = sh.worksheet("data")
    df = pd.DataFrame(worksheet.get_all_records())
    out_path = os.path.join(output_folder, filename)
    df.to_csv(out_path, index=False)

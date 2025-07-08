import os
import json
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Load service account credentials
creds_json = os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]
creds_dict = json.loads(creds_json)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
gc = gspread.authorize(credentials)

# Sheet mapping
sheets = {
    "TimedFishSurveys_HTLP_MASTER.csv": "https://docs.google.com/spreadsheets/d/1xEFKeymFg6l-VU3aQtzNXvvWCgtep4K7n0VjvhxB9TY",
    "TimedFishSurveys_Shallow_MASTER.csv": "https://docs.google.com/spreadsheets/d/1lyFGzCdmtCC4tfdmY1Qh1AEMqOvdKHNnWsd0C8zzNX8"
}

# Output folder
output_folder = "Timed_Fish_Surveys"
os.makedirs(output_folder, exist_ok=True)

# Loop over each sheet
for filename, url in sheets.items():
    sh = gc.open_by_url(url)
    worksheet = sh.worksheet("data")
    df = pd.DataFrame(worksheet.get_all_records())
    out_path = os.path.join(output_folder, filename)
    df.to_csv(out_path, index=False)

# final_project.py

import json
import os
import requests
import statistics

from dotenv import load_dotenv

load_dotenv()




FRED_API_KEY = os.getenv("FRED_API_KEY")

print("----------")
print("Requested Data:")
query_response = requests.get("https://api.stlouisfed.org/fred/series?series_id=LNS14000024&api_key={FRED_API_KEY}&file_type=json")
query = json.loads(query_response.text)
print(query["Unemployment Rate - 20 Yrs. & Over"])
print("----------")






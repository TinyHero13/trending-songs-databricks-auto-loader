import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from io import StringIO
from datetime import datetime

URL = "https://kworb.net/ww/"

def scrape_kworb():
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(URL, headers=headers, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("span", class_="pagetitle").text.split(" - ")[1].split(" | ")[0].replace("/","-")
    
    match = re.search(r"(\d{4}/\d{2}/\d{2})", title)
    chart_date = match.group(1).replace("/", "-") if match else datetime.now().strftime("%Y-%m-%d")
    
    df = pd.read_html(StringIO(response.text))[0]
        
    df["chart_date"] = chart_date
    df["loaded_at"] = datetime.now().isoformat()
    
    return df, title

df, title = scrape_kworb()
df.to_parquet(f"data/trending_song_{title}.parquet")
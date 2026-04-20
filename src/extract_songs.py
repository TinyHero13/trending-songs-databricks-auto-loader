import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime

def scrape_kworb():
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get("https://kworb.net/ww/", headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("span", class_="pagetitle").text.split(" - ")[1].split(" | ")[0].replace("/","-")
    
    match = re.search(r"(\d{4}/\d{2}/\d{2})", title)
    chart_date = match.group(1).replace("/", "-") if match else datetime.now().strftime("%Y-%m-%d")
    
    df = pd.read_html("https://kworb.net/ww/")[0]
        
    df["chart_date"] = chart_date
    df["loaded_at"] = datetime.now().isoformat()

    df["Artist"] = df["Artist and Title"].apply(lambda x: x.split(" - ")[0])
    df["Title"] = df["Artist and Title"].apply(lambda x: x.split(" - ")[1])
    
    return df, title

df, title = scrape_kworb()
df.to_parquet(f"data/trending_song_{title}.parquet")
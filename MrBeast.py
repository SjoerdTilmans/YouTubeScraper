import scrapetube
import requests
import re
import pandas as pd
import time

videos = scrapetube.get_channel("UCX6OQ3DkcsbYNE6H8uQQuVA")
data = {
    "Title": [],
    "Date": []
}

for video in videos:
    title = video["title"]["runs"][0]["text"]
    url = "https://www.youtube.com/watch?v=" + video["videoId"]
    r = requests.get(url)

    page_text = r.text
    date = re.findall("(dateText[^0-9]+)([A-Za-z0-9 ]+)", page_text)[0][1]

    data["Title"].append(title)
    data["Date"].append(date)

    print(data)

    df = pd.DataFrame(data=data)
    df.to_excel("Channel Data.xlsx")

    time.sleep(1)
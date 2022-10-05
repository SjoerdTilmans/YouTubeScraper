import scrapetube
import requests
import re
import pandas as pd
import time
import datetime

# videos = scrapetube.get_channel("UCX6OQ3DkcsbYNE6H8uQQuVA")
# data = {
#     "Title": [],
#     "Date": []
# }
#
# for video in videos:
#     title = video["title"]["runs"][0]["text"]
#     url = "https://www.youtube.com/watch?v=" + video["videoId"]
#     r = requests.get(url)
#
#     page_text = r.text
#     date = re.findall("(dateText[^0-9]+)([A-Za-z0-9 ]+)", page_text)[0][1]
#
#     data["Title"].append(title)
#     data["Date"].append(date)
#
#     print(data)
#
#     df = pd.DataFrame(data=data)
#     df.to_excel("Channel Data.xlsx")
#
#     time.sleep(1)

df = pd.read_excel("Channel Data.xlsx", index_col=0)

df["Datetime"] = df['Date'].map(lambda x: datetime.datetime.strptime(x.replace("Sept", "Sep"), "%d %b %Y"))
df["Giveaway"] = df['Title'].map(lambda x: re.findall("\$([0-9,]+)", x.replace(",", "")) if ("$" in x and "10k" not in x) else "")
df["Giveaway"] = df['Giveaway'].map(lambda x: float(x[0]) if (isinstance(x, list) and len(x) == 1) else 0)
df["Giveaway Sum"] = df.loc[::-1, 'Giveaway'].cumsum()[::-1]
df.sort_values(by='Datetime', inplace=True)


df.to_excel("MrBeastGivaway.xlsx")

print(df)
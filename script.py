import datetime
import time
import winsound
import requests
import json


url_query = "https://d8b22lfluy-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.14.2)%3B%20Browser%3B%20JS%20Helper%20(3.11.1)%3B%20react%20(18.2.0)%3B%20react-instantsearch%20(6.38.1)"
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers =  {

"Host":"d8b22lfluy-dsn.algolia.net",
"Content-Length":"1488",
"X-Algolia-Application-Id":"D8B22LFLUY",
"Content-Type":"application/x-www-form-urlencoded",
"X-Algolia-Api-Key":"2d6c7cf80580d79d2b5f31a1908027bb",
"Sec-Ch-Ua-Mobile":"?0",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36",
"Sec-Ch-Ua-Platform":"Windows",
"Accept":"*/*",
"Origin":"https://app.rario.com",
"Sec-Fetch-Site":"cross-site",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Dest":"empty",
"Referer":"https://app.rario.com/",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"en-US,en;q=0.9",
"Connection":"close"
}
requirement = ["black"]#, "gold"]
payload = '{"requests":[{"indexName":"rario_nft_prod_listing_time_desc","params":"analytics=true&enablePersonalization=true&facetFilters=%5B%5B%22attributes.scarcity%3Ablack%22%5D%5D&facets=%5B%22associated_teams%22%2C%22attributes.scarcity%22%2C%22attributes.role%22%2C%22associated_leagues%22%2C%22attributes.nationality%22%2C%22attributes.player%22%2C%22sub_type%22%2C%22attributes.year%22%5D&filters=catalog_type%3Acard%20AND%20on_sale%3A%20true&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&highlightPreTag=%3Cais-highlight-0000000000%3E&hitsPerPage=50&maxValuesPerFacet=1000&page=0&query=&tagFilters="},{"indexName":"rario_nft_prod_listing_time_desc","params":"analytics=false&clickAnalytics=false&enablePersonalization=true&facets=attributes.scarcity&filters=catalog_type%3Acard%20AND%20on_sale%3A%20true&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&highlightPreTag=%3Cais-highlight-0000000000%3E&hitsPerPage=0&maxValuesPerFacet=1000&page=0&query="}]}'
payload1 = '{"requests":[{"indexName":"rario_nft_prod_listing_time_desc","params":"analytics=true&enablePersonalization=true&facetFilters=%5B%5B%22attributes.scarcity%3Agold%22%5D%5D&facets=%5B%22associated_teams%22%2C%22attributes.scarcity%22%2C%22attributes.role%22%2C%22associated_leagues%22%2C%22attributes.nationality%22%2C%22attributes.player%22%2C%22sub_type%22%2C%22attributes.year%22%5D&filters=catalog_type%3Acard%20AND%20on_sale%3A%20true&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&highlightPreTag=%3Cais-highlight-0000000000%3E&hitsPerPage=50&maxValuesPerFacet=1000&page=0&query=&tagFilters="},{"indexName":"rario_nft_prod_listing_time_desc","params":"analytics=false&clickAnalytics=false&enablePersonalization=true&facets=attributes.scarcity&filters=catalog_type%3Acard%20AND%20on_sale%3A%20true&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&highlightPreTag=%3Cais-highlight-0000000000%3E&hitsPerPage=0&maxValuesPerFacet=1000&page=0&query="}]}'
count = 0


chat_id ="-981475987"
token ="6143122932:AAGuH2HHTrdPvjNkW4VJ34mtOug6n-BtF6Y"
a = "https://core.telegram.org/bots/api"
send_message_endpoint = f"https://api.telegram.org/bot{token}/sendMessage?chat_id=-981475987"

url1 = f"api.telegram.org/bot{token}"

import requests


def send_telegram_notification(msg):
    base_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.post(base_url, verify=False)


dup = []

def check_listings(count):
    count=count+1
    print(count)
    for r in requirement:
        if r=="black":
            response = requests.post(url_query, data=payload, headers=headers, verify=False)
        else:
            response = requests.post(url_query, data=payload1, headers=headers, verify=False)

        listings = []
        aa =json.loads(response.text)
        if r == "black":
            min_price = 151
        else:
            min_price = 35
        for lst in aa["results"]:
            for k,v in lst.items():
                if k=="hits":
                    for item in v:
                        if item["name"] not in ["Kane Williamson","Prithvi Shaw","Bhuvneshwar Kumar", "Litton Das", "Sisanda Magala", "Dwaine Pretorius", "Ravi Bopara"]:
                            if item["min_sale_price"] <min_price:
                                 asset_id = item['asset_id']
                                 current_time = datetime.datetime.now()
                                 url = f"https://app.rario.com/listings/{asset_id}"
                                 data = f" {r} {item['min_sale_price']} {item['name']} {url}"
                                 if data not in listings and data not in dup:
                                     listings.append(data)
                                     dup.append(data)
                                     print(f"{current_time}, {data}")
                                     # send_message(data)
                                     if r =="black":
                                         frequency = 500  # Set Frequency To 2500 Hertz
                                         duration = 500  # Set Duration To 1000 ms == 1 second
                                         # winsound.Beep(frequency, duration)
                                         send_telegram_notification(data)
                                     else:
                                         frequency = 2500  # Set Frequency To 2500 Hertz
                                         duration = 1000  # Set Duration To 1000 ms == 1 second
                                         # winsound.Beep(frequency, duration)
                                 # data= requests.get("https://app.rario.com/api/token/listing"+f"?page=0&limit=20&catalogId={asset_id}&sortBy=price&sortDir=asc", verify=False)
    time.sleep(5)

for i in range(1000000):
    check_listings(i)


​

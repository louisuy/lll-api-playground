import requests
import json

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.lululemon.me',
    'Referer': 'https://www.lululemon.me/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'x-algolia-api-key': '8bc5c8ef0cadc497bdf3c17e33c735ec',
    'x-algolia-application-id': 'RPUQQW7I72',
}

data = '{"requests":[{"indexName":"p1_lulu_ae_en","params":"ruleContexts=category-page&facetFilters=%5B%5B%22categories%3Awomen-activity-on-the-move%7C%7CWomen\'s%20On%20the%20Move%22%5D%5D&hitsPerPage=48&facets=%5B%22*%22%5D&page=0&analytics=true&clickAnalytics=true&facetingAfterDistinct=true"},{"indexName":"p1_lulu_ae_en","params":"ruleContexts=category-page&facets=%5B%22categories%22%2C%22categories%24extras%22%5D&facetFilters=%5B%5D&hitsPerPage=0&page=0&maxValuesPerFacet=Infinity&analytics=false&clickAnalytics=false&enableABTest=false"}]}'

response = requests.post(
    'https://rpuqqw7i72-1.algolianet.com/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.25.2)%3B%20Browser',
    headers=headers,
    data=data,
)

print(f"Status Code: {response.status_code}")

with open(f"pdp_response.json", "w", encoding="utf-8") as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=2)
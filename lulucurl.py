import requests
import json
import re

page_size = 800
page_number = 1
referer_url = input("Enter referer URL: ").strip()
match = re.search(r'/c/([^/]+)/([^/?#]+)', referer_url)
if match:
    category = match.group(1)
    cdpHash = match.group(2)
else:
    raise ValueError("Could not parse category and cdpHash from referer_url")

print(f"✅ Category: {category}")
print(f"✅ cdpHash: {cdpHash}")

# TODO: Paste cookies and headers from curlconverter.com
cookies = {}
headers = {}

json_data = {
    'query': 'query CategoryPageDataQuery($category: String!, $cid: String, $forceMemberCheck: Boolean, $nValue: String, $cdpHash: String, $sl: String!, $locale: String!, $Ns: String, $storeId: String, $pageSize: Int, $page: Int, $onlyStore: Boolean, $useHighlights: Boolean, $abFlags: [String], $styleboost: [String], $fusionExperimentVariant: String) { categoryPageData(category: $category, nValue: $nValue, cdpHash: $cdpHash, locale: $locale, sl: $sl, Ns: $Ns, page: $page, pageSize: $pageSize, storeId: $storeId, onlyStore: $onlyStore, forceMemberCheck: $forceMemberCheck, cid: $cid, useHighlights: $useHighlights, abFlags: $abFlags, styleboost: $styleboost, fusionExperimentVariant: $fusionExperimentVariant) { products { productId } } }',
    'variables': {
        'pageSize': page_size,
        'page': page_number,
        'useHighlights': True,
        'onlyStore': False,
        'abFlags': [
            'cdpSeodsEnabled',
        ],
        'category': category,
        'cdpHash': cdpHash,
        'forceMemberCheck': False,
        'fusionExperimentVariant': '',
        'locale': 'en_US',
        'Ns': '',
        'nValue': None,
        'sl': 'US',
        'storeId': None,
        'styleboost': [],
    },
}

response = requests.post('https://shop.lululemon.com/snb/graphql', cookies=cookies, headers=headers, json=json_data)

print(f"Status Code: {response.status_code}")

# with open(f"{category}_response.json", 'w', encoding='utf-8') as f:
#     json.dump(response.json(), f, ensure_ascii=False, indent=2)

import pandas as pd

product_ids = [p['productId'] for p in response.json()['data']['categoryPageData']['products']]

df = pd.DataFrame(product_ids, columns=['productId'])

df.to_excel(f"{category}_product_ids.xlsx", index=False)
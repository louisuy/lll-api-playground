import requests
import pandas as pd

# --- request setup ---
cookies = {
    'ak_bmsc': '74D290106706576A0F70F7D1F4C4BA57~000000000000000000000000000000~YAAQHucVAtZXIueZAQAAen5p8R009lqxZmowH+ckSwHBct2GCAIeovwRpz7GVB3OFzzrUJ+chPg+iCQiDu99BlvpWD2wqv1auuf5B3elNLWHUDmmIX/sjIRa20AiNRLNf7dXu8hSnMgtqH3gK03xohCnHTimZ4a//sjky5WJzbknAkwSxJ3hoEBLkuFKZsUdH8aNbmExpzKpCXdJEfkf8go100zO0pkb1BELtk6naAYqkcUFLW1/DqOHW9Hdnir17/U4dIQVfcaVsGhk6hMSBQ8AfyeQj+smJjHQ5/z2GgyCCFBWjXYu4VNsHoMO4mWlC1wwRdIHiRlMJu2YhqpIgte467S9gwKKGt3BxTnpEJutO5OInb/u/tSUD/FJzS1FwJ/HwMWSVoM=',
    'ROUTE': '.api-784b947787-9mhnh',
    'rr_rcs': 'eF5jYSlN9kg2TTMwTbRI0k1LNDHSNUlJSdE1MbNI0bWwNDMzt7BIS0o1MeHKLSvJTBEwMjA10DXUNQQAqfMOqA',
    'bm_sv': '2493C2C51BF98851937E481964853A4E~YAAQHucVAi9oIueZAQAAjAJq8R3w6jCF7WUfVsKGn9Yi9GYxCu76tjm6ijopSd4ztwoY6G7Hwfm0mC8zeHQAN0ltJBLIQcGe+6APfqwOJd8gonElumeuEXk8rNU0WW2++QA6h9iIP+n6bjzhDv9zO/6rnhTw4PfBkZ/69xGHpW93dBhgJLblujXM2AQtqIYo5ztWAomsnpFrfLFDLkfs3NpFDNyqTfD8/s8OyCXuvP3Ofjizp0mIxxFnmeLcHLArcQ==~1',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.cb2.ae',
    'priority': 'u=1, i',
    'referer': 'https://www.cb2.ae/',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-anonymous-consents': '%5B%5D',
    # 'cookie': 'ak_bmsc=74D290106706576A0F70F7D1F4C4BA57~000000000000000000000000000000~YAAQHucVAtZXIueZAQAAen5p8R009lqxZmowH+ckSwHBct2GCAIeovwRpz7GVB3OFzzrUJ+chPg+iCQiDu99BlvpWD2wqv1auuf5B3elNLWHUDmmIX/sjIRa20AiNRLNf7dXu8hSnMgtqH3gK03xohCnHTimZ4a//sjky5WJzbknAkwSxJ3hoEBLkuFKZsUdH8aNbmExpzKpCXdJEfkf8go100zO0pkb1BELtk6naAYqkcUFLW1/DqOHW9Hdnir17/U4dIQVfcaVsGhk6hMSBQ8AfyeQj+smJjHQ5/z2GgyCCFBWjXYu4VNsHoMO4mWlC1wwRdIHiRlMJu2YhqpIgte467S9gwKKGt3BxTnpEJutO5OInb/u/tSUD/FJzS1FwJ/HwMWSVoM=; ROUTE=.api-784b947787-9mhnh; rr_rcs=eF5jYSlN9kg2TTMwTbRI0k1LNDHSNUlJSdE1MbNI0bWwNDMzt7BIS0o1MeHKLSvJTBEwMjA10DXUNQQAqfMOqA; bm_sv=2493C2C51BF98851937E481964853A4E~YAAQHucVAi9oIueZAQAAjAJq8R3w6jCF7WUfVsKGn9Yi9GYxCu76tjm6ijopSd4ztwoY6G7Hwfm0mC8zeHQAN0ltJBLIQcGe+6APfqwOJd8gonElumeuEXk8rNU0WW2++QA6h9iIP+n6bjzhDv9zO/6rnhTw4PfBkZ/69xGHpW93dBhgJLblujXM2AQtqIYo5ztWAomsnpFrfLFDLkfs3NpFDNyqTfD8/s8OyCXuvP3Ofjizp0mIxxFnmeLcHLArcQ==~1',
}

url = "https://api.cb2.ae/rest/v2/cb2/products/search"

params = {
    "fields": "keywordRedirectUrl,products(code),pagination(DEFAULT)",
    "query": ":relevance:allCategories:view-all-11267",
    "pageSize": "9999",
    "lang": "en",
    "curr": "AED"
}

# --- send request ---
response = requests.get(url, headers=headers, cookies=cookies, params=params)
data = response.json()

# --- extract product codes ---
product_codes = [p['code'] for p in data.get('products', [])]

# --- export to CSV ---
df = pd.DataFrame(product_codes, columns=['product_code'])
df.to_csv('cb2_product_codes.csv', index=False, encoding='utf-8-sig')

# --- print full CSV output to terminal ---
csv_output = df.to_csv(index=False, header=True)
print(csv_output)

print(f"\n✅ Exported {len(df)} product codes to cb2_product_codes.csv")

import json
from datetime import datetime
import requests

# --- Your cookies + headers go here ---
cookies = {
    'nt_page_init_referrer': 'NeotagEncrypt%3AU2FsdGVkX1%2B%2BaumWWznjak%2BegfGPyL3O6OO5TKYwKciuUh1PJLSm%2BlvjhKpqY5FB',
    'nt_page_init_referring_domain': 'NeotagEncrypt%3AU2FsdGVkX1832YYFpM95h1ruMFYq5D5kz9x7n4NvrGl68a0X9oaxV%2F5C9LrUALZV',
    '_ga': 'GA1.1.1778235579.1751527852',
    '_tt_enable_cookie': '1',
    '_ttp': '01JZ7K42HAATKB832YXA0ZTZF2_.tt.1',
    '_scid': 'VXJnKJznTMj6_EbR5qeUbjeHI6doV50r',
    'optimize_uuid': '2bd66cb0fe855497e983c3c507c2940b0e9901898630778ca9',
    '_sctr': '1%7C1752091200000',
    'neo_sc': 'NeotagEncrypt%3AU2FsdGVkX19gexijSj%2FsGATLZ%2FtnajbHCxWT2UL%2F1ik%3D',
    'nt_user_id': 'NeotagEncrypt%3AU2FsdGVkX1%2FLnj00p3CxtMRxvGj6aczAmAF1zlYve8Y%3D',
    'nt_trait': 'NeotagEncrypt%3AU2FsdGVkX18w%2BtlQygr2QTnmcCvURuNjREtxc8dROow%3D',
    'nt_group_id': 'NeotagEncrypt%3AU2FsdGVkX19XLObwnwOu4tt06kdkM5zM7O3nwWhodhg%3D',
    'nt_group_trait': 'NeotagEncrypt%3AU2FsdGVkX1%2BTXE3ikqj%2BuN9DxQUyHPyRuWS7E2o%2BwdI%3D',
    'nt_anonymous_id': 'NeotagEncrypt%3AU2FsdGVkX1%2FVIj5GwLubEbOzBuiZlhMSc6jaKq7j5ZUACARcEDQHPhKpspllxbTzpw0Nxq7x3601QgRWBab8yQ%3D%3D',
    '_scid_r': 'YvJnKJznTMj6_EbR5qeUbjeHI6doV50roZ-h3g',
    'neo_session': 'NeotagEncrypt%3AU2FsdGVkX19qIqk%2Bk8xJhdkZtdhPF09N%2FAtAaA%2BF%2FR9ejplWBtupW2oPiyqrzNXfSRf5a59wT6xU7LDOzIzbHuo%2BQVKi4duVtKywz3h2nTYYR0bNinavNZ8oFV9aD6aUhxGsN%2BGsOl1DheR%2F59%2FUAg%3D%3D',
    'ttcsid': '1752143748658::M7N52-ja_DWA5pyc97qq.13.1752144215469',
    'ttcsid_CDMCOURC77UDCMKM9MAG': '1752143748656::gFytBMyCjian-gtKL8SS.13.1752144217588',
    '_ga_2R511ZVHFM': 'GS2.1.s1752143747$o1$g1$t1752144459$j60$l0$h1412255825',
    '_ga_QQJRFVGY73': 'GS2.1.s1752498367$o15$g1$t1752498547$j60$l0$h2024746215',
    '_ga_RC54V0M6CC': 'GS2.1.s1752498368$o18$g1$t1752498547$j60$l0$h0',
    'ajs_anonymous_id': 'b0aa65a8-a419-462a-b8c7-55a1da114927',
    'AKA_A2': 'A',
    'bm_mi': '7586087E02C166C3E351085600577CEA~YAAQLecVApxxIaqaAQAAi7kith0luwbmO/AaXOaEhB5bg/equPl8Se2/UYlHMyMUcBGJUVU7JJ1up9800ejburmdsOgB1wiABjJwXob9mryiw1O3jIXs+j9PlIcbco/CumtFWlYpVvOayyuwo7YeLtiEiQHrau/U2rO0ddXft5o0YI90w71BPCuXimJa+2P0G5HEYoRM01BW41pAk3BAqgMKktKkmi6Nu/jniKqnFwNHJxByok77zmR0/yiM5ijLAeXITG+bfl1Y969v/8TC0spbd/PNu15Ni0wjQaZ/rB4KVdHcyDqyA6N+7JnnNRz4yCH/9wHgLU2gEAdWfYbD~1',
    'bm_sv': 'A7F86C00B3A8976986B971056BF5A060~YAAQLecVAp1xIaqaAQAAi7kith3qT6jx7afSHt8nwEBtN9I8TKfbWZwdUaJXiJ13kjp508kGVC2hkV5EN9D4TnErecBy6yZGGiKf9vP5+e/rBDB8mwRiTgOWCuHxlK4PY7k+YCib4jOmoHbUtPig/nB2v1LHQ5dmip4iZsM7rLZuIpfNUA1jsKXRmACDawh1+aCEJwc94bApaspi9vR9g/WhS8ORdSJtId4XfU0rZEckNfEe+3q1hTK5yoOLSLgXoShm~1',
    'ak_bmsc': 'FFAA6F66D86B23435090F2AEA171A2AA~000000000000000000000000000000~YAAQJsXOF1fT6KmaAQAA3vwrth33js2RjerHHFSS8qIq+gTmtkZ/s3+/QiH+jNOmhTYJruNfQt0l5CeE5m8EDDxb7X3edF//XBlkORM/zZ7BKAIOhOYApwpXdwhEhT/Kqt5aQEyAi1pASUcjeVHWJiGsNCZBU15UU9OuSqGgY6xWwdXMhpfErXYCCQaxmB3WjML99ucuIms67jSjKzadLe+lbQRoUtzka6k8aXFDJvu5t53x4d9aQcnnuDti2jhx/Yq5AQVyGZuhON+vI1mNNkk2NacPWWQgikVUNfwXcdp6XelsaH5xWH1TftLlWrWN/pXqA1uq1bA5h6P3Vep1Boh5e/z47Gyu4HZnzvnPV5L5Y39wfg23LrHmtBWSVSpqscMTdhxrvGcEAGfM3ViCQXZAhfpWW8ALdxdXWJixOJQXisoxXjvdmKXA8gEJU68=',
    'ROUTE': '.api-55bf889649-87dk7',
    'rr_rcs': 'eF5j4cotK8lMETAyMLfQNdQ1ZClN9jBJNjJKNjE01E1KSzbQNTExSNE1STZL0U1MMzNNM05OTE40NAAAlsQO2A',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.lululemon.me',
    'priority': 'u=1, i',
    'referer': 'https://www.lululemon.me/',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'x-anonymous-consents': '%5B%5D',
    # 'cookie': 'nt_page_init_referrer=NeotagEncrypt%3AU2FsdGVkX1%2B%2BaumWWznjak%2BegfGPyL3O6OO5TKYwKciuUh1PJLSm%2BlvjhKpqY5FB; nt_page_init_referring_domain=NeotagEncrypt%3AU2FsdGVkX1832YYFpM95h1ruMFYq5D5kz9x7n4NvrGl68a0X9oaxV%2F5C9LrUALZV; _ga=GA1.1.1778235579.1751527852; _tt_enable_cookie=1; _ttp=01JZ7K42HAATKB832YXA0ZTZF2_.tt.1; _scid=VXJnKJznTMj6_EbR5qeUbjeHI6doV50r; optimize_uuid=2bd66cb0fe855497e983c3c507c2940b0e9901898630778ca9; _sctr=1%7C1752091200000; neo_sc=NeotagEncrypt%3AU2FsdGVkX19gexijSj%2FsGATLZ%2FtnajbHCxWT2UL%2F1ik%3D; nt_user_id=NeotagEncrypt%3AU2FsdGVkX1%2FLnj00p3CxtMRxvGj6aczAmAF1zlYve8Y%3D; nt_trait=NeotagEncrypt%3AU2FsdGVkX18w%2BtlQygr2QTnmcCvURuNjREtxc8dROow%3D; nt_group_id=NeotagEncrypt%3AU2FsdGVkX19XLObwnwOu4tt06kdkM5zM7O3nwWhodhg%3D; nt_group_trait=NeotagEncrypt%3AU2FsdGVkX1%2BTXE3ikqj%2BuN9DxQUyHPyRuWS7E2o%2BwdI%3D; nt_anonymous_id=NeotagEncrypt%3AU2FsdGVkX1%2FVIj5GwLubEbOzBuiZlhMSc6jaKq7j5ZUACARcEDQHPhKpspllxbTzpw0Nxq7x3601QgRWBab8yQ%3D%3D; _scid_r=YvJnKJznTMj6_EbR5qeUbjeHI6doV50roZ-h3g; neo_session=NeotagEncrypt%3AU2FsdGVkX19qIqk%2Bk8xJhdkZtdhPF09N%2FAtAaA%2BF%2FR9ejplWBtupW2oPiyqrzNXfSRf5a59wT6xU7LDOzIzbHuo%2BQVKi4duVtKywz3h2nTYYR0bNinavNZ8oFV9aD6aUhxGsN%2BGsOl1DheR%2F59%2FUAg%3D%3D; ttcsid=1752143748658::M7N52-ja_DWA5pyc97qq.13.1752144215469; ttcsid_CDMCOURC77UDCMKM9MAG=1752143748656::gFytBMyCjian-gtKL8SS.13.1752144217588; _ga_2R511ZVHFM=GS2.1.s1752143747$o1$g1$t1752144459$j60$l0$h1412255825; _ga_QQJRFVGY73=GS2.1.s1752498367$o15$g1$t1752498547$j60$l0$h2024746215; _ga_RC54V0M6CC=GS2.1.s1752498368$o18$g1$t1752498547$j60$l0$h0; ajs_anonymous_id=b0aa65a8-a419-462a-b8c7-55a1da114927; AKA_A2=A; bm_mi=7586087E02C166C3E351085600577CEA~YAAQLecVApxxIaqaAQAAi7kith0luwbmO/AaXOaEhB5bg/equPl8Se2/UYlHMyMUcBGJUVU7JJ1up9800ejburmdsOgB1wiABjJwXob9mryiw1O3jIXs+j9PlIcbco/CumtFWlYpVvOayyuwo7YeLtiEiQHrau/U2rO0ddXft5o0YI90w71BPCuXimJa+2P0G5HEYoRM01BW41pAk3BAqgMKktKkmi6Nu/jniKqnFwNHJxByok77zmR0/yiM5ijLAeXITG+bfl1Y969v/8TC0spbd/PNu15Ni0wjQaZ/rB4KVdHcyDqyA6N+7JnnNRz4yCH/9wHgLU2gEAdWfYbD~1; bm_sv=A7F86C00B3A8976986B971056BF5A060~YAAQLecVAp1xIaqaAQAAi7kith3qT6jx7afSHt8nwEBtN9I8TKfbWZwdUaJXiJ13kjp508kGVC2hkV5EN9D4TnErecBy6yZGGiKf9vP5+e/rBDB8mwRiTgOWCuHxlK4PY7k+YCib4jOmoHbUtPig/nB2v1LHQ5dmip4iZsM7rLZuIpfNUA1jsKXRmACDawh1+aCEJwc94bApaspi9vR9g/WhS8ORdSJtId4XfU0rZEckNfEe+3q1hTK5yoOLSLgXoShm~1; ak_bmsc=FFAA6F66D86B23435090F2AEA171A2AA~000000000000000000000000000000~YAAQJsXOF1fT6KmaAQAA3vwrth33js2RjerHHFSS8qIq+gTmtkZ/s3+/QiH+jNOmhTYJruNfQt0l5CeE5m8EDDxb7X3edF//XBlkORM/zZ7BKAIOhOYApwpXdwhEhT/Kqt5aQEyAi1pASUcjeVHWJiGsNCZBU15UU9OuSqGgY6xWwdXMhpfErXYCCQaxmB3WjML99ucuIms67jSjKzadLe+lbQRoUtzka6k8aXFDJvu5t53x4d9aQcnnuDti2jhx/Yq5AQVyGZuhON+vI1mNNkk2NacPWWQgikVUNfwXcdp6XelsaH5xWH1TftLlWrWN/pXqA1uq1bA5h6P3Vep1Boh5e/z47Gyu4HZnzvnPV5L5Y39wfg23LrHmtBWSVSpqscMTdhxrvGcEAGfM3ViCQXZAhfpWW8ALdxdXWJixOJQXisoxXjvdmKXA8gEJU68=; ROUTE=.api-55bf889649-87dk7; rr_rcs=eF5j4cotK8lMETAyMLfQNdQ1ZClN9jBJNjJKNjE01E1KSzbQNTExSNE1STZL0U1MMzNNM05OTE40NAAAlsQO2A',
}


# --- Config ---
URL = "https://api.lululemon.me/rest/v2/lulu/products/search"
PARAMS = {
    "fields": ("products(code,sellable,name,urlName,summary,maxOrderQuantity,price(FULL),"
               "badges(code,name),images(DEFAULT),stock(FULL),crossedPrice(FULL),"
               "categories(name,code,url),variants(FULL),primaryCategory(FULL),baseProduct,"
               "priceRange,classifications(FULL),baseOptions(options(FULL),FULL),breadcrumbs)"),
    # "lang": "en",
    # "curr": "AED",
    "pageSize": 9999,
}

# --- Make request ---
print("Sending request...")

resp = requests.get(
    URL,
    params=PARAMS,
    cookies=cookies,   # <--- HERE
    headers=headers,   # <--- AND HERE
    timeout=20
)

print(f"Status: {resp.status_code}")

# --- Save result ---
stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
filename = f"lululemonME_{stamp}.json"

if resp.status_code == 200:
    try:
        data = resp.json()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ Saved {len(data.get('products', []))} products to {filename}")
    except Exception as e:
        print(f"⚠️ Failed to parse JSON: {e}")
        with open(filename.replace(".json", ".raw.txt"), "w", encoding="utf-8") as f:
            f.write(resp.text)
        print("📄 Saved raw response instead.")
else:
    print(f"❌ Error {resp.status_code}: {resp.text[:300]}...")

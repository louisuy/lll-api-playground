import requests
import json

cookies = {
    'nt_page_init_referrer': 'NeotagEncrypt%3AU2FsdGVkX1%2B%2BaumWWznjak%2BegfGPyL3O6OO5TKYwKciuUh1PJLSm%2BlvjhKpqY5FB',
    'nt_page_init_referring_domain': 'NeotagEncrypt%3AU2FsdGVkX1832YYFpM95h1ruMFYq5D5kz9x7n4NvrGl68a0X9oaxV%2F5C9LrUALZV',
    '_ga': 'GA1.1.1778235579.1751527852',
    '_tt_enable_cookie': '1',
    '_ttp': '01JZ7K42HAATKB832YXA0ZTZF2_.tt.1',
    '_gcl_au': '1.1.279699621.1751527853',
    '_scid': 'VXJnKJznTMj6_EbR5qeUbjeHI6doV50r',
    '_fbp': 'fb.1.1751527853908.647861637451623472',
    'optimize_uuid': '2bd66cb0fe855497e983c3c507c2940b0e9901898630778ca9',
    '_gcl_gs': '2.1.k1$i1751870391$u13425322',
    '_gcl_aw': 'GCL.1751870395.Cj0KCQjwvajDBhCNARIsAEE29WqsGZQa-iaM8w7Owdhox6DHFgTxZ4w6VTfOWfxrlr873RtRr72djYwaAq8cEALw_wcB',
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
    'ROUTE': '.api-5ccfcdb77-xjkqc',
    'ak_bmsc': 'C67D2D284D2D464488C06AF47E6F829E~000000000000000000000000000000~YAAQlfkUAtm97+uYAQAA9hJi8BzYhHY/sY6M0vYOWglKFCRH9Au1COwMZLe4f4yeqoGnq338gt0cBGpRmm50hYtmd9ZaDYN1x9mPK7ChXLbfJE3OQ0F0g4TOuyQdyl2daEpPKadO8DEwZm2jci1lS7tw7M0GlijCKMK2oh3pE56fLeUQOKNe01ahE0j4ov6pYXZ40w/VoywRk6k5S8Dq6E+vmJWAupGBcI7/vjNx1JLgj41NJo34BbSCAMw8qn1onF02mYFL2rGTWkMFdV050ydPZ1yoST8pPKHDVA2Wrn3U74BvHuwWHYvcI2K0z20gLZ26g1jG4TjR4mkAxkazPVJtsk0tflbUsauHua2VrU/gopD35H6ybDft8NjZOsNdhSmpzF7Tf1P9Uoc=',
    'AKA_A2': 'A',
    'rr_rcs': 'eF5jYSlN9jBJNjJKNjE01E1KSzbQNTExSNE1STZL0U1MMzNNM05OTE40NODKLSvJTBEwMjC30DXUNQQApIQO2A',
    'bm_mi': '39166A81DBE2D1D0AEC1E65603242DDE~YAAQlfkUApbY7+uYAQAAJHZm8BynNjIqdHjw+BIilG1BtfIeZ0QNDyT74DmK4CkOZcHCoBO6y/xdMSLZLNQoT74ZjVbO4AQcf3vUOMvZjrqTvrST9eq2EE3doE/mhlkep0XbnHWl9E78qRNuawJiTFRlvrUJeMXPcA4NOZ+lTE9OLLRQO7wzjpq4uhcNMn2SKm6zYUp4xa+x3+3ux1Ic6ff3gp9DbWXx8NAo/1mCw159cFKBLMaMYhip/E57XI9LWIhHtHN6R5pjScsMqfaRfV63DWaZiGjhlfgglkI3C9qDNxvYhGHr83y1w2Y+BYZQgscKtXKvN5Y9gTU3jAFU~1',
    'bm_sv': 'E7F3D19FE4DF7C81CAA189F0A6C8B21F~YAAQlfkUApDZ7+uYAQAAuLBm8BxVrE7pgF4+vDkxfTJI3KoCFqJIMaZfJdj2wz5WrZlBbQvDWn9PpdiLl+HaQR/o+JeWgKdqkUBBapIe6NSUwj+hs7LbzNiwY0YgWB3gEFMJfflY2tnSepKrWrrj1k1XIfIBLN+WpqpDPObak5EapojXTz856WYdfdNrlhp0iyMM//hEJ4VIctIORY02H/PysPCO0DB79R/ElIjHxgNRvwIkVDxpCCgwUK/is468uaf7~1',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.lululemon.me',
    'priority': 'u=1, i',
    'referer': 'https://www.lululemon.me/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'x-anonymous-consents': '%5B%5D',
    # 'cookie': 'nt_page_init_referrer=NeotagEncrypt%3AU2FsdGVkX1%2B%2BaumWWznjak%2BegfGPyL3O6OO5TKYwKciuUh1PJLSm%2BlvjhKpqY5FB; nt_page_init_referring_domain=NeotagEncrypt%3AU2FsdGVkX1832YYFpM95h1ruMFYq5D5kz9x7n4NvrGl68a0X9oaxV%2F5C9LrUALZV; _ga=GA1.1.1778235579.1751527852; _tt_enable_cookie=1; _ttp=01JZ7K42HAATKB832YXA0ZTZF2_.tt.1; _gcl_au=1.1.279699621.1751527853; _scid=VXJnKJznTMj6_EbR5qeUbjeHI6doV50r; _fbp=fb.1.1751527853908.647861637451623472; optimize_uuid=2bd66cb0fe855497e983c3c507c2940b0e9901898630778ca9; _gcl_gs=2.1.k1$i1751870391$u13425322; _gcl_aw=GCL.1751870395.Cj0KCQjwvajDBhCNARIsAEE29WqsGZQa-iaM8w7Owdhox6DHFgTxZ4w6VTfOWfxrlr873RtRr72djYwaAq8cEALw_wcB; _sctr=1%7C1752091200000; neo_sc=NeotagEncrypt%3AU2FsdGVkX19gexijSj%2FsGATLZ%2FtnajbHCxWT2UL%2F1ik%3D; nt_user_id=NeotagEncrypt%3AU2FsdGVkX1%2FLnj00p3CxtMRxvGj6aczAmAF1zlYve8Y%3D; nt_trait=NeotagEncrypt%3AU2FsdGVkX18w%2BtlQygr2QTnmcCvURuNjREtxc8dROow%3D; nt_group_id=NeotagEncrypt%3AU2FsdGVkX19XLObwnwOu4tt06kdkM5zM7O3nwWhodhg%3D; nt_group_trait=NeotagEncrypt%3AU2FsdGVkX1%2BTXE3ikqj%2BuN9DxQUyHPyRuWS7E2o%2BwdI%3D; nt_anonymous_id=NeotagEncrypt%3AU2FsdGVkX1%2FVIj5GwLubEbOzBuiZlhMSc6jaKq7j5ZUACARcEDQHPhKpspllxbTzpw0Nxq7x3601QgRWBab8yQ%3D%3D; _scid_r=YvJnKJznTMj6_EbR5qeUbjeHI6doV50roZ-h3g; neo_session=NeotagEncrypt%3AU2FsdGVkX19qIqk%2Bk8xJhdkZtdhPF09N%2FAtAaA%2BF%2FR9ejplWBtupW2oPiyqrzNXfSRf5a59wT6xU7LDOzIzbHuo%2BQVKi4duVtKywz3h2nTYYR0bNinavNZ8oFV9aD6aUhxGsN%2BGsOl1DheR%2F59%2FUAg%3D%3D; ttcsid=1752143748658::M7N52-ja_DWA5pyc97qq.13.1752144215469; ttcsid_CDMCOURC77UDCMKM9MAG=1752143748656::gFytBMyCjian-gtKL8SS.13.1752144217588; _ga_2R511ZVHFM=GS2.1.s1752143747$o1$g1$t1752144459$j60$l0$h1412255825; _ga_QQJRFVGY73=GS2.1.s1752498367$o15$g1$t1752498547$j60$l0$h2024746215; _ga_RC54V0M6CC=GS2.1.s1752498368$o18$g1$t1752498547$j60$l0$h0; ajs_anonymous_id=b0aa65a8-a419-462a-b8c7-55a1da114927; ROUTE=.api-5ccfcdb77-xjkqc; ak_bmsc=C67D2D284D2D464488C06AF47E6F829E~000000000000000000000000000000~YAAQlfkUAtm97+uYAQAA9hJi8BzYhHY/sY6M0vYOWglKFCRH9Au1COwMZLe4f4yeqoGnq338gt0cBGpRmm50hYtmd9ZaDYN1x9mPK7ChXLbfJE3OQ0F0g4TOuyQdyl2daEpPKadO8DEwZm2jci1lS7tw7M0GlijCKMK2oh3pE56fLeUQOKNe01ahE0j4ov6pYXZ40w/VoywRk6k5S8Dq6E+vmJWAupGBcI7/vjNx1JLgj41NJo34BbSCAMw8qn1onF02mYFL2rGTWkMFdV050ydPZ1yoST8pPKHDVA2Wrn3U74BvHuwWHYvcI2K0z20gLZ26g1jG4TjR4mkAxkazPVJtsk0tflbUsauHua2VrU/gopD35H6ybDft8NjZOsNdhSmpzF7Tf1P9Uoc=; AKA_A2=A; rr_rcs=eF5jYSlN9jBJNjJKNjE01E1KSzbQNTExSNE1STZL0U1MMzNNM05OTE40NODKLSvJTBEwMjC30DXUNQQApIQO2A; bm_mi=39166A81DBE2D1D0AEC1E65603242DDE~YAAQlfkUApbY7+uYAQAAJHZm8BynNjIqdHjw+BIilG1BtfIeZ0QNDyT74DmK4CkOZcHCoBO6y/xdMSLZLNQoT74ZjVbO4AQcf3vUOMvZjrqTvrST9eq2EE3doE/mhlkep0XbnHWl9E78qRNuawJiTFRlvrUJeMXPcA4NOZ+lTE9OLLRQO7wzjpq4uhcNMn2SKm6zYUp4xa+x3+3ux1Ic6ff3gp9DbWXx8NAo/1mCw159cFKBLMaMYhip/E57XI9LWIhHtHN6R5pjScsMqfaRfV63DWaZiGjhlfgglkI3C9qDNxvYhGHr83y1w2Y+BYZQgscKtXKvN5Y9gTU3jAFU~1; bm_sv=E7F3D19FE4DF7C81CAA189F0A6C8B21F~YAAQlfkUApDZ7+uYAQAAuLBm8BxVrE7pgF4+vDkxfTJI3KoCFqJIMaZfJdj2wz5WrZlBbQvDWn9PpdiLl+HaQR/o+JeWgKdqkUBBapIe6NSUwj+hs7LbzNiwY0YgWB3gEFMJfflY2tnSepKrWrrj1k1XIfIBLN+WpqpDPObak5EapojXTz856WYdfdNrlhp0iyMM//hEJ4VIctIORY02H/PysPCO0DB79R/ElIjHxgNRvwIkVDxpCCgwUK/is468uaf7~1',
}


url = (
    "https://api.lululemon.me/rest/v2/lulu/products/search"
    "?fields=products(code,sellable,name,urlName,summary,maxOrderQuantity,"
    "price(FULL),badges(code,name),images(DEFAULT),stock(FULL),crossedPrice(FULL),"
    "categories(name,code,url),variants(FULL),primaryCategory(FULL),baseProduct,"
    "priceRange,classifications(FULL),baseOptions(options(FULL),FULL),breadcrumbs)"
    "&query=:relevance"
    "&lang=en"
    "&curr=AED"
    "&pageSize=9999"
)

response = requests.get(url, cookies=cookies, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Save to JSON file
    with open("lululemon_products.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Saved to lululemon_products.json")
else:
    print(f"Error {response.status_code}: {response.text}")
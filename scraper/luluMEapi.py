import requests

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
    'bm_mi': '0529F443E744B54230C8E6C338BF8545~YAAQF5fYF8wlxKeYAQAAVFnGqBy+WwavhE7kPuEEZOAvHdEwj3EQIPuHsjFY2ZUA7fcUPAc+OSva7yHSyjhYCJ/Uw4hasZcKnVV1MRXxbq2JwCBne+YkIwwetWC926E+Sw8Kc7LjrSCYNiYYhYxaca6sjL3brWb/qoonV5tlZ9oapOPD+gIwQi4u6zSlFaBRKfp5/+mtuGWcUNRwbUhEAdm3NjS8LuF2AIMquzl17ZfpST17S5gQwURufdYw9/qOz86/J3Gbetg14ok/WW/spa1alwnOp7PpGRKyfqv2HzFIW8zmTO+YvqlS14Zxy8gsmBNKivltaJaH/u10m/ZmCspgGHu2PeiBGgqLB1cptXqNy+2yjjoBVozQ9qvn857sUSYEGiS0TbgssX3h~1',
    'bm_sv': '6C51F936D805751A8F958761B35638D9~YAAQF5fYFwQnxKeYAQAAUX3GqBznM2zclUap1u+gKRp2w6kjdThcUlHBKR2lMftdmMXKnznvEzOASHcCxKbRttwaWtWuRo8fRuMcKKObqtRz+eykgSVN4efTlRiXunLe6VdLk5wlPc748hnrk0Ez/mJHODZPrj/issWjNKSNwRT3zPBLSjjyRPAAjEDv8MxB4tIPGatLOD43S5T4LxgOdY0X/WDeuSclVq8j5y8PP3Ryfjk/KPn5IpKbnNB0EQPWDG/m~1',
    'ak_bmsc': '4467EF53B32EEA18F39E79D9B9BA4A72~000000000000000000000000000000~YAAQDpfYF6nBSoeYAQAA8kz2qByhtwdBxX8VNvLjqXy+ej2hPGXp8pQsOK7GJi3uvMC/kKOFviPJzYIVLCEE554SmkqGjuHnxqe59CJO8ovM2Diin0AuVgk4Q2qjzyjWUuiLOnBavc+Q9e2GlF0jHyGk+NMx4vdVZM1tkiuZPN+gsjoZr5wjJgUjRpkfjitVKxjbW+Ss+ZwBeVTFh/mK7DlZZ+65Q/F9GBEFgIoAjVFwvbPlsni6wvlSt5bXMkt1f8ZNvhC8LC6+LxWFBAkQiGVn+2c3pyWaiXy37ekjbvgEO/W5EV3rBGo+9aHPLbNlPt3XTLFc93ejknoOaHOwW9HGUJ4yCKZcgie8K9SBSspsLHN6NnFJ0M+tJ8jDW/b2o1inDZjNN8BBTxN1O8J+BjD/7gsamAH0PE66KO3PrhEWV3W/km0d7MiWLOmb2R/zC1nwOME/icTFUOZ0UT4nfehlQBjLZGc/TE+sJu0F3FQTam0saedDfMR3hHfLLMwSecMTYmc2',
    'ROUTE': '.api-6756b5499c-wrbgk',
    'rr_rcs': 'eF5jYSlN9jBJNjJKNjE01E1KSzbQNTExSNE1STZL0U1MMzNNM05OTE40NODKLSvJTBEwMjC30DXUNQQApIQO2A',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.lululemon.me',
    'priority': 'u=1, i',
    'referer': 'https://www.lululemon.me/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
    'x-anonymous-consents': '%5B%5D',
    # 'cookie': 'nt_page_init_referrer=NeotagEncrypt%3AU2FsdGVkX1%2B%2BaumWWznjak%2BegfGPyL3O6OO5TKYwKciuUh1PJLSm%2BlvjhKpqY5FB; nt_page_init_referring_domain=NeotagEncrypt%3AU2FsdGVkX1832YYFpM95h1ruMFYq5D5kz9x7n4NvrGl68a0X9oaxV%2F5C9LrUALZV; _ga=GA1.1.1778235579.1751527852; _tt_enable_cookie=1; _ttp=01JZ7K42HAATKB832YXA0ZTZF2_.tt.1; _gcl_au=1.1.279699621.1751527853; _scid=VXJnKJznTMj6_EbR5qeUbjeHI6doV50r; _fbp=fb.1.1751527853908.647861637451623472; optimize_uuid=2bd66cb0fe855497e983c3c507c2940b0e9901898630778ca9; _gcl_gs=2.1.k1$i1751870391$u13425322; _gcl_aw=GCL.1751870395.Cj0KCQjwvajDBhCNARIsAEE29WqsGZQa-iaM8w7Owdhox6DHFgTxZ4w6VTfOWfxrlr873RtRr72djYwaAq8cEALw_wcB; _sctr=1%7C1752091200000; neo_sc=NeotagEncrypt%3AU2FsdGVkX19gexijSj%2FsGATLZ%2FtnajbHCxWT2UL%2F1ik%3D; nt_user_id=NeotagEncrypt%3AU2FsdGVkX1%2FLnj00p3CxtMRxvGj6aczAmAF1zlYve8Y%3D; nt_trait=NeotagEncrypt%3AU2FsdGVkX18w%2BtlQygr2QTnmcCvURuNjREtxc8dROow%3D; nt_group_id=NeotagEncrypt%3AU2FsdGVkX19XLObwnwOu4tt06kdkM5zM7O3nwWhodhg%3D; nt_group_trait=NeotagEncrypt%3AU2FsdGVkX1%2BTXE3ikqj%2BuN9DxQUyHPyRuWS7E2o%2BwdI%3D; nt_anonymous_id=NeotagEncrypt%3AU2FsdGVkX1%2FVIj5GwLubEbOzBuiZlhMSc6jaKq7j5ZUACARcEDQHPhKpspllxbTzpw0Nxq7x3601QgRWBab8yQ%3D%3D; _scid_r=YvJnKJznTMj6_EbR5qeUbjeHI6doV50roZ-h3g; neo_session=NeotagEncrypt%3AU2FsdGVkX19qIqk%2Bk8xJhdkZtdhPF09N%2FAtAaA%2BF%2FR9ejplWBtupW2oPiyqrzNXfSRf5a59wT6xU7LDOzIzbHuo%2BQVKi4duVtKywz3h2nTYYR0bNinavNZ8oFV9aD6aUhxGsN%2BGsOl1DheR%2F59%2FUAg%3D%3D; ttcsid=1752143748658::M7N52-ja_DWA5pyc97qq.13.1752144215469; ttcsid_CDMCOURC77UDCMKM9MAG=1752143748656::gFytBMyCjian-gtKL8SS.13.1752144217588; _ga_2R511ZVHFM=GS2.1.s1752143747$o1$g1$t1752144459$j60$l0$h1412255825; _ga_QQJRFVGY73=GS2.1.s1752498367$o15$g1$t1752498547$j60$l0$h2024746215; _ga_RC54V0M6CC=GS2.1.s1752498368$o18$g1$t1752498547$j60$l0$h0; ajs_anonymous_id=b0aa65a8-a419-462a-b8c7-55a1da114927; bm_mi=0529F443E744B54230C8E6C338BF8545~YAAQF5fYF8wlxKeYAQAAVFnGqBy+WwavhE7kPuEEZOAvHdEwj3EQIPuHsjFY2ZUA7fcUPAc+OSva7yHSyjhYCJ/Uw4hasZcKnVV1MRXxbq2JwCBne+YkIwwetWC926E+Sw8Kc7LjrSCYNiYYhYxaca6sjL3brWb/qoonV5tlZ9oapOPD+gIwQi4u6zSlFaBRKfp5/+mtuGWcUNRwbUhEAdm3NjS8LuF2AIMquzl17ZfpST17S5gQwURufdYw9/qOz86/J3Gbetg14ok/WW/spa1alwnOp7PpGRKyfqv2HzFIW8zmTO+YvqlS14Zxy8gsmBNKivltaJaH/u10m/ZmCspgGHu2PeiBGgqLB1cptXqNy+2yjjoBVozQ9qvn857sUSYEGiS0TbgssX3h~1; bm_sv=6C51F936D805751A8F958761B35638D9~YAAQF5fYFwQnxKeYAQAAUX3GqBznM2zclUap1u+gKRp2w6kjdThcUlHBKR2lMftdmMXKnznvEzOASHcCxKbRttwaWtWuRo8fRuMcKKObqtRz+eykgSVN4efTlRiXunLe6VdLk5wlPc748hnrk0Ez/mJHODZPrj/issWjNKSNwRT3zPBLSjjyRPAAjEDv8MxB4tIPGatLOD43S5T4LxgOdY0X/WDeuSclVq8j5y8PP3Ryfjk/KPn5IpKbnNB0EQPWDG/m~1; ak_bmsc=4467EF53B32EEA18F39E79D9B9BA4A72~000000000000000000000000000000~YAAQDpfYF6nBSoeYAQAA8kz2qByhtwdBxX8VNvLjqXy+ej2hPGXp8pQsOK7GJi3uvMC/kKOFviPJzYIVLCEE554SmkqGjuHnxqe59CJO8ovM2Diin0AuVgk4Q2qjzyjWUuiLOnBavc+Q9e2GlF0jHyGk+NMx4vdVZM1tkiuZPN+gsjoZr5wjJgUjRpkfjitVKxjbW+Ss+ZwBeVTFh/mK7DlZZ+65Q/F9GBEFgIoAjVFwvbPlsni6wvlSt5bXMkt1f8ZNvhC8LC6+LxWFBAkQiGVn+2c3pyWaiXy37ekjbvgEO/W5EV3rBGo+9aHPLbNlPt3XTLFc93ejknoOaHOwW9HGUJ4yCKZcgie8K9SBSspsLHN6NnFJ0M+tJ8jDW/b2o1inDZjNN8BBTxN1O8J+BjD/7gsamAH0PE66KO3PrhEWV3W/km0d7MiWLOmb2R/zC1nwOME/icTFUOZ0UT4nfehlQBjLZGc/TE+sJu0F3FQTam0saedDfMR3hHfLLMwSecMTYmc2; ROUTE=.api-6756b5499c-wrbgk; rr_rcs=eF5jYSlN9jBJNjJKNjE01E1KSzbQNTExSNE1STZL0U1MMzNNM05OTE40NODKLSvJTBEwMjC30DXUNQQApIQO2A',
}

# Base URL without the relatedAlgonomyIds filter
url = (
    "https://api.lululemon.me/rest/v2/lulu/products/search"
    # "?fields=products(code,sellable,name,urlName,summary,maxOrderQuantity,"
    "?fields=products"
    # "price(FULL),badges(code,name),images(DEFAULT),stock(FULL),crossedPrice(FULL),"
    # "categories(name,code,url),variants(FULL),primaryCategory(FULL),baseProduct,"
    # "priceRange,classifications(FULL),baseOptions(options(FULL),FULL),breadcrumbs)"
    # "&lang=en&curr=AED"
    "&pageSize=1000"
)

response = requests.get(url, cookies=cookies, headers=headers)

import json

if response.status_code == 200:
    data = response.json()
    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Saved API result to result.json")
else:
    print(f"Request failed with status {response.status_code}")
import requests

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
    'ROUTE': '.api-784b947787-hdr6n',
    'AKA_A2': 'A',
    'bm_mi': '399C6BFBEA6B394C586DCA97DB1B7A26~YAAQLecVAuGSEzCaAQAAQuUfNR21f+EyNmGtDYWrBWURw5HCV5fNnmp1WKWOHXIbsllzV0J1G5MRLT9i7LgI0Y2LRrDCSG7WZQNWmGOjq4XSWMnsLLfUdyNdYp8wNJyEPxGIDhBMtttEmjStyCp7icMg17dAAxV5kXjQhee3+q+c7UmeJCgAXIhG6Zc1u9G2thWdLORwQ1pcAXa5Xdsw9ZoViBUQCg0J6SNucVxyh31nqBIfiTqeKtGnPHwLaZ90zdc2OPRIH1lI7bW4KToK+BkzYLRrRtttwG0u41LRpgamNCXx3RwK0kMfHZNr62ip1jMJrI0=~1',
    'rr_rcs': 'eF5j4cotK8lMETAyMLfQNdQ1ZClN9jBJNjJKNjE01E1KSzbQNTExSNE1STZL0U1MMzNNM05OTE40NAAAlsQO2A',
    'bm_sv': '4CFAFA3CFFB78C234F9D99C65DCD0B0B~YAAQLecVAmWbEzCaAQAAdiMgNR2+0J26/vfv1PWIX7atUTzpfJJ3GcaLhxfNj7rTkScxaC2WF44i+xfqmw1H2GE3e99f9eefGq2cXFZPB5XI01bwA2XdcRKnwHSA6YyuGFHkftwxtQFR3mKAA1TxHVp8iSHytfy/Nn8V8QFpScLmMUnvuS2eWlI4oPHHj/4hRECW53/9Y7xo3McKKUjoL/u/3SB3tflTeQZ8txx8Q4+nBAkf9UqWv+Dqwg6MYGtD8r3V~1',
    'ak_bmsc': '19E8FCB46EBE628945B74BE694291823~000000000000000000000000000000~YAAQLecVAiOqEzCaAQAABKAgNR3RI0pkPwOQh97GHKGvF3DCNVAjcFfPftfcfrVKvM+QGZ6WqEiu14SCvxT7yRsgVl7Yh63xv3CwyPsI9VFXQRtP9jxVcJjsQYUGbO8wf4kEzKklykzNB4n3XUpUxdq17R5E7MVnlotm0C26HP1I+cqb39udj88tfaDgUyTyJFMZ5v8+bB9Tn5zVLOAHmplPPJc1g8VAy5N62E34i8qFTdgq1NujIYwzkStIO0bybvZUBYIgMutbo9SCxeEppm6/FnFruKEEfO41bmT/eP/Is7T+IHKPCTxk0ymA+QpcMaJq6FSCdrSE6OF70xuYNCQo5ENVYzDXYTQ/BGRZrrkz6Lw6jwZ8hfWZ9h/+6aON5K7oKH1yAyV6iOgoy778GhKdZfTekbf0OUoZXvUuOR1kDn2VKtUS7w==',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6UXpRekpFTlVNeE16aEdOemcwUlRjeVF6VXdRVEkyTWpoRlJEZEROVE0xTVVNM1F6TTJPUSJ9.eyJodHRwczovL21hZi5ncmF2dHkuYXV0aC9kZXYvYXBpL21lbWJlcklkIjoiOTQ3ODQwMDA1NjA0MjMwOCIsImh0dHBzOi8vbWFmLmdyYXZ0eS5hdXRoL2Rldi9hcGkvdm94Q2FyZE51bWJlciI6Ijk0Nzg0MDAwNTYwNDIzMDgiLCJodHRwczovL21hZi5ncmF2dHkuYXV0aC9kZXYvYXBpL2VtYWlsIjoiYW50aG9ueS5sb3Vpc0BtYWYuYWUiLCJodHRwczovL21hZi5ncmF2dHkuYXV0aC9kZXYvYXBpL3V1aWQiOiI4MDFjZWU4MC02MjU0LTExZjAtYjQ2Zi01MTU2ZGU5ZjJkYjIiLCJodHRwczovL21hZi5pZGVudGl0eS5hdXRoL2Rldi9hcGkvdXVpZCI6IjgwMWNlZTgwLTYyNTQtMTFmMC1iNDZmLTUxNTZkZTlmMmRiMiIsImh0dHBzOi8vbWFmLmlkZW50aXR5LmF1dGgvZGV2L2FwaS9lbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaHR0cHM6Ly9tYWYuaWRlbnRpdHkuYXV0aC9kZXYvYXBpL2VtYWlsIjoiYW50aG9ueS5sb3Vpc0BtYWYuYWUiLCJodHRwczovL21hZi5pZGVudGl0eS5hdXRoL2Rldi9hcGkvcmlkIjoiZmRlYjc4MTgtZmFmYi00YzNlLTg3ZTUtN2UyOGRjYmY0YzE2IiwiaHR0cHM6Ly9tYWYuaWRlbnRpdHkuYXV0aC9kZXYvYXBpL21pcmFrbF9zaG9wX2lkIjpudWxsLCJodHRwczovL21hZi5pZGVudGl0eS5hdXRoL2Rldi9hcGkvdGltZSI6IjIwMjUtMDgtMDdUMjA6MTI6NDQuNjEyWiIsImlzcyI6Imh0dHBzOi8vaWRlbnRpdHkubWFqaWRhbGZ1dHRhaW0uY29tLyIsInN1YiI6ImF1dGgwfDY4NjRmMzk1N2E5ODVkOGU4MmEyYTEwZSIsImF1ZCI6WyJtYWZpZCIsImh0dHBzOi8vcHJvZHVjdGlvbi5tYWYuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTc1NDU5NzU2NCwiZXhwIjoxNzU0NTk5MzY0LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIiwiYXpwIjoia2Z3UE11Q1ZieE5QdlBwZkRLaXl2Z1Z2SFdtVGhYYzgifQ.VPsC5vj163B0AVxUZocLV8-HxWnNILijskoR0ISqcE-72uv3tMHpsBMPGv5K1_6tofc5bP4ggpsNcgqTpz4RJk3eKo5xBiA-TMLDkF-BBKivXs7Z9zlZSz4ReA8o1EIhZ7AEydSmNe9MCgUGtJWkgyuW3YC0HVA0nHQvfLmdvfIfxiY6p8wykzQOutBo6PKNNe-MyG-xWI13ZHIY1ra31OqmC6qFYfNjZkEIDZZn5a1a7pwQQ5ZCBVY5GiuwuEqB-_Hlcq40XTpe7uGsr7OF3EDtrU32KvKBAdZcVhCmtn4-6feAR_SZjOOzPz5bPqVtcwZueqBGo-IwW9hlnT2Tnw',
    'origin': 'https://www.allsaints.me',
    'priority': 'u=1, i',
    'referer': 'https://www.allsaints.me/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
    'x-anonymous-consents': '%5B%5D',
    # 'cookie': 'nt_page_init_referrer=NeotagEncrypt%3AU2FsdGVkX1%2BsJwiJkVZpz%2B%2Bbgy26OZ1VdMaIGEZ5G64%3D; nt_page_init_referring_domain=NeotagEncrypt%3AU2FsdGVkX18z0G7ItqAY0GZere%2F5gC6IHvmoDdxwz%2Fc%3D; _ga=GA1.1.1964284017.1751977271; _tt_enable_cookie=1; _ttp=01JZMZQ8178KYJ2S8ZNE1TC4EV_.tt.1; _gcl_au=1.1.1054453579.1751977274; _fbp=fb.1.1751977273743.554124561164126957; _scid=F-dYMQitund0c-17xRDg3gr8FLD-1qh1; _sctr=1%7C1751918400000; _gcl_gs=2.1.k1$i1752048577$u58825213; _gcl_aw=GCL.1752058563.CjwKCAjwprjDBhBTEiwA1m1d0i1DyJ3S7cBa2LQ0PfwlWyLpwGZFcjAf02xNCYpuJ_33PwxDmuwJfBoC4DoQAvD_BwE; neo_sc=NeotagEncrypt%3AU2FsdGVkX1%2FSVMITZlMnRj1DpLfwRLEh4vJO3vgTAdw%3D; nt_user_id=NeotagEncrypt%3AU2FsdGVkX1%2Bl1GenLaZa9YL7qkAgMD857ERl7m%2FKqlk%3D; nt_trait=NeotagEncrypt%3AU2FsdGVkX19ONc%2FZtoEt%2FdheRbkyGQ2XVL%2FY4Fdx3cg%3D; nt_group_id=NeotagEncrypt%3AU2FsdGVkX18%2B19WtTv9%2B4BT5wvQKOz1wKapi74J2yx0%3D; nt_group_trait=NeotagEncrypt%3AU2FsdGVkX19A7iN%2FL5xMJ2H99UjnRFkcgXlC7v4I3JU%3D; nt_anonymous_id=NeotagEncrypt%3AU2FsdGVkX19VnO6xUz4vy1MZLX0SGVccz92Qr5t6yG2hVBS9bxiz%2BlFd%2BJ5SdkrUlYyjq3evmYkQJ2Ybvc13kA%3D%3D; _scid_r=FGdYMQitund0c-17xRDg3gr8FLD-1qh1gAj9Pw; _ga_JCZ0JR3KPC=GS2.1.s1752143860$o6$g1$t1752144070$j60$l0$h644044425; neo_session=NeotagEncrypt%3AU2FsdGVkX19msusgSkvean2%2F5tdsMTQAg8RjOmalFQPUFho5k5hJ3XrNwCbB7lmKTE2N8eZC2avEW5Ii42SXvZzKHN9K1bDnSuQXZ2GDAtf8SAzZkRAYETIvCvuDbvhg28tpbLvGd6gajIzIxC4Y%2FA%3D%3D; ttcsid=1752143732995::GvDKpVQEAsFuffv1TpkV.7.1752144233285; ttcsid_CC1ON5JC77U4JJ3BHHHG=1752143732994::Zef3YwuLXz7Nq0eIDojm.6.1752144234551; _ga_RC54V0M6CC=GS2.1.s1752143731$o6$g1$t1752144252$j60$l0$h0; _ga_083HX4D5KG=GS2.1.s1752143731$o1$g1$t1752144252$j41$l0$h1241084185; ROUTE=.api-6756b5499c-m22nm; bm_mi=1C49CF35C05F325CEF57979228516EE4~YAAQFpfYFy2f6VaYAQAAclAohhzSSRwEmKyntSyaneNWO2QaJhVqpTCAv2bV6GvaPqZfAEMGZ08llNhBzNsarEpHXf7wJKty8UlNjfOxUsHmProhBIXgGnTXqxQ4Pp2xsEKOo9tLc1sghSU1YkaCTY1W4kE/wBi+QAjN2IfiZ79ttbdCSshR7j0nInAdZQxfYUUE1C8NjhGLG46LfP9hci4dwH5vNE4bQn99L+JXSS6m+OeDG1EOPpdSpK9y8xBxOSNDic6/IZ46plJMEJA16CnEC2T/Be/u+/1WkVV1TcID29BV0vgvMr9B1KqVlhlx2Kcv7Rq/z4jZuCPXoXxH~1; bm_sv=C4387896D7BD2122BB5A9816A279E36A~YAAQFpfYF0yj6VaYAQAAx4IohhxoUN1FawPmqW9C+z91wJi7TAf+kgxh4RSwJQcDngo2Ele2EqdhXCpDNMCl4Hy1NxOb6Y7CaJRr6Hwvr5DKx7wiyOyGUznKCBIDL+lxU8uWFLOmAJlqJtYsLNC3n/a+2AKeZ2Ro8LMBa3fWW2miskw+/4wytN3h2xp/A+c42B1+0n1IwbKNvFGQ0pXSrz/eDVs7eOaUTtqCBaoIPNTn7UZLK3GmYkEui/vYRtOS5wp3~1; ak_bmsc=A5F8645826BF4218A920BA0FD92BD085~000000000000000000000000000000~YAAQFpfYFwH+6VaYAQAAvQEthhzll5Ts2IzxyKQZKI/a7aLVR4alcwrO0mRkpbkHJHlfO7DoVEUaZlzZ7LTILz/DJGN53VnPXmZSP7RQ/9OpqhILTgS7uhITPKEc54aDpfh7JcffC+FRNZoMC6Z3BWKz0/SrqG5eB3t0tc3NHqbcQPh7/c6ZvqchPQj7w6CmiHonQE4RVMtKMEFFmMETAwmxkaYOgG0iTWrCniYzzE5e9rDJGGVs0wIzbbiU5jZGONr/eFXRM56YDYHiAzOrj4UIVgBktFKiHNOJmI1bEV/fiJYMWJ+EJnvhfgdhVueJKR/P3RG8sv2+8xCI0W59yx9YbIXUhKStBYkHeg+8Rz6edc4PdRlj5QtWRLCRL/uOlAkOSSAss+8vC8r4U4WWOxsAVxd0WB866W32HFnKdr9ElZdLDxsqNw7ZB/TdsMP0rkcxmv8eksLJEc8=; rr_rcs=eF5jYSlN9kg2MzIySDE30E1LNDHSNUlJSdFNMjIw0zU3MTNNSzRPtUxONuPKLSvJTBEwMrA01TXUNQQAnasOlA',
}

response = requests.get(
    'https://api.allsaints.me/rest/v2/alls/products/search?fields=products(baseOptions(FULL),baseProduct,code,sellable,name,summary,maxOrderQuantity,price(FULL),badges(code,name),images(DEFAULT),stock(FULL),crossedPrice(FULL),categories(name,code,url),variants(FULL),breadcrumbs)&query=:relevance&lang=en&curr=AED&pageSize=1200',
    cookies=cookies,
    headers=headers,
)

import json

# Check if the request was successful
if response.status_code == 200:
    # Save the response to a JSON file
    with open('products.json', 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)
    print("Data has been successfully exported to 'products.json'.")
else:
    print("Failed to fetch data. Status code:", response.status_code)
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
cookies = {
    '_ga_14J17NW0K4': 'GS2.2.s1751890298$o1$g0$t1751890300$j58$l0$h0',
    '_lfa': 'LF1.1.cabc1bb242347854.1751890302222',
    '_ga_V1VQCPSY6V': 'GS2.1.s1751957660$o2$g0$t1751957660$j60$l0$h0',
    '_ga_GQP33VCV1E': 'GS2.1.s1751957660$o2$g0$t1751957660$j60$l0$h0',
    'sat_track': 'true',
    'kameleoonVisitorCode': '4i8ulubslwypslau',
    'ajs_anonymous_id': '86da3fa5-7393-413c-977b-cf3ca069ebda',
    '_ttp': '28-waHDKO7tGyHsemr-0l5PGtY_',
    '_scid': 'LwPoAZXzLO1BoqC6hLyDRwnxAZfy8aYX',
    '_fbp': 'fb.1.1752127612468.307145000',
    '_ga': 'GA1.1.1260579579.1751890297',
    '__pdst': '3ec3fcb533cc4ac2a5e2cd0f87b4ab59',
    'kampyle_userid': 'd104-008b-d31a-7d46-5eaa-17fd-3241-a450',
    '_pin_unauth': 'dWlkPVl6TTJNelV6WlRRdE5XVXpOUzAwT1RFeExXRmlNemt0TTJaaE56aGhZemc0T0RRdw',
    'digitalData.page.a1Token': '$2a$10$tNGLzxgFy.YH1jVIvc.LIOY4ORTw.fW7fXfpWyGQgsH.ZWRjuyyyi',
    '_evga_8f06': '{%22uuid%22:%229ec5c2631c240b31%22}',
    '_sfid_cc29': '{%22anonymousId%22:%229ec5c2631c240b31%22%2C%22consents%22:[{%22consent%22:{%22provider%22:%22Consent%20Provider%22%2C%22purpose%22:%22Personalization%22%2C%22status%22:%22Opt%20In%22}%2C%22lastUpdateTime%22:%222025-07-10T06:06:55.435Z%22%2C%22lastSentTime%22:%222025-07-10T06:06:55.439Z%22}]}',
    '_ttp': '28-waHDKO7tGyHsemr-0l5PGtY_.tt.1',
    '_tt_enable_cookie': '1',
    '_fbp': 'fb.1.1752127612468.307145000',
    '_gcl_au': '1.1.1388619635.1752127616',
    'a1ashgd': '4b8j6vwzg3p000004b8j6vwzg3p00000',
    '_sctr': '1%7C1752091200000',
    'bttnsessionid': 'sess-H2qHL643wyETBr7pgU3Yx41xHW4NF5kZHtFJZd49IbUw_',
    'QuantumMetricUserID': '86831e065cf43c36ac4b56fde3222bff',
    '_rdt_uuid': '1752127613494.a76d7d73-f628-4de0-88ff-078d5535cfba',
    'kampyleUserSession': '1752129062551',
    'kampyleUserSessionsCount': '3',
    'kampyleUserPercentile': '14.551039287714485',
    'kampyleSessionPageCounter': '1',
    '_scid': 'I3Km-6s9xltlYS7dc8AysCMHYnqqbMxjPrhP8A',
    'ttcsid_C65BFLPR48GN82KJE2E0': '1752127616136::25526VBqZoBaTt-QbCai.1.1752129063135',
    '_ga_4ZRJ21056F': 'GS2.1.s1752131300$o2$g0$t1752131300$j60$l0$h0',
    '_ga_CCD7VVYPZ7': 'GS2.1.s1752131300$o2$g0$t1752131300$j60$l0$h0',
    'intlOTConsent': 'C0004:1,C0001:1,C0003:1,C0002:1',
    'NoCookie': 'true',
    '__cq_uuid': '2ab6ce80-5d6c-11f0-8bb0-47509f0499fd',
    '_scid_r': 'JXKm-6s9xltlYS7dc8AysCMHYnqqbMxjPrhP8g',
    '_ga_BXZE3SJMWL': 'GS2.1.sD84drOFtA18hFH51RDTXopGOmFqnQ69vpXc%3D$o1$g1$t1752137983$j37$l0$h0',
    'a1ashgd': 'cqlz5hkklui00000cqlz5hkklui00000',
    '_uetvid': '13c9c8605d5411f0a0fdaf8fca2d1181|jjcgek|1752129063687|4|1|bat.bing.com/p/insights/c/e',
    'ttcsid_CNK2R5JC77U8IUSPJBFG': '1752137960452::GtBuI1LXA4A6tL5T5oTU.1.1752137983701',
    'ttcsid': '1752137960454::xDW5y-BLQEYmZznaYhtD.2.1752137983701',
    'mbox': 'PC#bdf3d85951b14ca48c0c2159000bc260.37_0#1817621992|session#7f13025d373846b9b6ae5c3c2bc5fb3f#1754379052',
    'lll-ix-wl': 'true',
    'lll-ix-dash': 'true',
    'lll_digital_id': '52375525777371028292491689370830964215',
    'PersadIDExp': 'db2996cec38e5f0da55661b47f033fcf',
    'lll_client_id': '52375525777371028292491689370830964215',
    'UsrLocale': 'en_US',
    'sl': 'US',
    'bm_s': 'YAAQV+cVAmIOm+aYAQAAmo2HDgQuh5JLtrLWrjQKE/RBi7/FK0rDeAPHHcN0Vc+e/OjPjApY/JB4OlNGbj8K6KLR79sZfwZHO4fYFS7MqmPh6GVr2UbFTPM1FYGNypH3P0XiArNPpbjdD5mrMhGxurCbh+zjv4h2q1+H/cEtl5uTCegxH5C8L5krjIJ9e1/chCwbfZqCsvl/GLPncRjpF/S60P/4jkrn6sEY+zh+99RrMbtEcvchTY+FAg9N5oOpLnCeF3lYOp31vfvwH+v71qYoPZaKCWnaV9fGqv/PthxYDnIEp39eJDcsYld+jNHJLBEtJA20z42jOx1zfqzZT1xK33+RTw3OAdYllRJqkG6n93u2oveHnicIG/YLlJigzVCvX8oQCLDhgUCmCuWia/kqLmKL37wbW1khj5cbJfCI6lQtTW7ipA6I7QHcM5cudc76lGrUKsf/6s7efWRofGYTNSbTgo6ierdn5nzY6gHswtMeq5TXi0Ksdv/XzgNZSo1c+5pMrG4ihvi+N7nCTuqCm+tT6EtsQCtfaQkThv4bR47WTc1KNF9bW0PVqm2B9Oe/tlrG61Y=',
    'cf_clearance': 'k_AbK0hfUwMOSGTdX0D4UygQsRZAiFgvfO9XFWT4t4Y-1759402424-1.2.1.1-3KOHwY3fCwngka2NPdvzzaNeZxX_lr7h7nyNvDBYdt9_f5bOL9WJhUO29SaQmgXJ1xyNGN.QoM5.ekYCqjZsk6lJ8NIneZvmNq0DAWnfa98Bq0yCwHklQhS.IPBZykMFeUe0a34tRyaj4ApoRKOBxXW2LLQ6xFnm46fKx.6bYekdIYz7wfXKJmwu5aY9PaAiCYAiZAqljuhXTbZ1C3ZOqw02MteDDFUwhEz0a18TSi0',
    'tfc-l': '%7B%22k%22%3A%7B%22v%22%3A%223vm79qikjbsm7aqfh6ta2egvcg%22%2C%22e%22%3A1818575671%7D%2C%22c%22%3A%7B%22v%22%3A%22adult%22%2C%22e%22%3A1818575670%7D%2C%22a%22%3A%7B%22v%22%3A%2289adc922-17cc-4e52-94c5-0ec5e2b543f2%22%2C%22e%22%3A1759488830%7D%7D',
    'alaPPN': 'pdp:prod11790330',
    'Prg5BMu0': 'A5V7TXqYAQAAjUEQTLZjmz8a6VA_ZxWD0rYp_8ZPSH-TPF1ZHEz3dua0d_u5AV7L1u2uchxGwH8AAEB3AAAAAA|1|1|e7aea4d618cbf530d8ef3c8e9374c6701864d5cf',
    'lll_edge_geo_data': 'city=DUBAI&state=&zip=&country=AE&lat=25.25&long=55.28',
    'lll-ecom-correlation-id': '95503BE2-6D8A-A304-C2FC-6E2CE54CBE9B',
    'AMCVS_A92B3BC75245B1030A490D4D%40AdobeOrg': '1',
    'ek8_guest': 'true',
    'apigeeToken': 'eyJqa3UiOiJodHRwczpcL1wvcHJvZC5hcGlzLmxsbGV4dC5jb21cL2FwaW1cL3YxXC9qd3R2ZXJpZmljYXRpb25cL2p3a3MiLCJraWQiOiJyc2FfXzZidW14bnUzNWVqOW11OGZscSIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJyb2xlIjoiZ3Vlc3QiLCJpc3MiOiJodHRwczpcL1wvcHJvZC5hcGlzLmxsbGV4dC5jb21cL2p3dFwvdjEiLCJJRCI6InhWR1NVZXVndm9nUHRnaUprYmo4aUY3U2FjYW5WSUE5IiwiVVVJRCI6IjZjODhkZjY3LTg2N2QtNGI5Yi1hNDg5LWI1NTNmNDRlNjcxZiIsImV4cCI6MTc1OTQ3NzE1NiwiaWF0IjoxNzU5NDczNTU2LCJqdGkiOiJlOWRjOGNmYS0yOWEyLTQwNTAtYjhhZC0wOWI1NzU0OGI2ZGIifQ.ltz9QAAUXX-duGuRtM158DSgAPJ_qLYKI9Miig57Jzm3NqSL4mLVY9g9l5cYyMdQLyiXO1a4V0bQrvWj185EdyoQB9T9b0-lZhiAq7pnH-GR0PfNS6RbzihEcRmck94FyydXDYtWnp76oStwIP0dgOKcNo1mPFEZBghmiGFdKn3Ku7kHPfis1beAwJkWG1i98xe3I6t7P_RyyRm9YD2kZjSJ2kEmWgj7cQ0Ng2F1nwrXfe6BmQwGg90CKQD_gBslpYR5fwAb2o_FMuWYLF2vn7JXkqEZ-P5nzfYRTIojDBY3rcNO2zVIuouV5jEAA2nQhiehNX0D9yeY4VjmY4RSPQ',
    'ak_bmsc': '4D58F307662B218015BF2275ED71FBB8~000000000000000000000000000000~YAAQZucVAkSQK4GZAQAAP04IqR3kYUk2QTBKsLAVrmF1EvSOR8+MU9iju0dY69Vo2KjlqsvnrU4Sec1R65ITBSyOaim6QJIyiPdhiGZr9HhHoVnfYZ6Q1u/NjUMjhaP/dIzVkzq/Vxstn8uKsuQPWolaHGMPK5ag3clp04AAJHMnHcZqzkbicejwwDVLs2X3gZ7+mcyGPDorCUHaF9AS+7oyKFSU2W0feTISUrnj01FHQ5rO2XvST+jLDs7qOo3YGWAs/zv/Y/gq6PLHsG5SGOmFtstIWLncSRXCvKNVO3sBo31OrGwU1gWjSUFUIzUwH29yccyL4c69tuJWj03JeOq+0S1PRC/phHMaCSsKdYp/anygx2TKErw/Y6mXGbU67ZXPRW1riQX1EUZJTSKIxKB8xX7S',
    'bm_mi': '079B92F23FC1ADFAC13333345354BFC0~YAAQZucVAkWQK4GZAQAAP04IqR0kpNSbDU9MDi6N+JueuNe5XR0g1pI+jIdZp1BVdt9tw93hEFv1QCJQehxCIr1qlI/C8OFwNU6pFPSBebbbhG3pmEbOCJGIiBCYqW/r1R40UNMNjxPBBRyDzvX3g8gxqpUQ7Vc6yVA7NGlqRwHwHXDI6h7zBGwyL/BPGnVJhCDrkEtfR6r+ro0Y/vPmaQamtCh25N1zP9K+ydSsl8rNwrpmQxrAZbQ4qT2hnEN1qwPEGkuo+NUI2a3HtKSBdU3jhEenu2yTvrWnBpq6J+LupB4K/Edzk5iXaohD9kIqAxZPz3ckoOZXFUDgG9ZpASnE4uATMdXmCQP9j5icX9o=~1',
    'bm_sv': '9C2A466F5198F802270D3BAD6CA1CCC8~YAAQZucVAkaQK4GZAQAAP04IqR0wx20uECVyzSvDjRd5ZO/ZnhENO6xQRwD7tIY7Nn25Bl79DThDt6vbMHz0RqAbWMKEpv7co3M2wxFep6ppCsQXei/N9wSnO8ApE2ujckq2hilAYsnHozaK3dPo4E/l2+m+a40fd8rusqwaJGmDtuGZiGRxk5bYTPs+C1GYgmSTqhYoj8SvqDIHZywuQnc/eslOgSpqm6ktJcS2XHgZhy7gKOld/3XY+ADDvkFDun0u~1',
    'bm_sz': '27E3C1AA328B1B175A5A1165ED2E3798~YAAQZucVAkeQK4GZAQAAP04IqR1KR8m3cAoxRFdMNCstPsdgR/kRqOn8ncym1oCaM/ewJ0WckB/kwCrQk4tbCM49x4hRC8maN3vrhN81/Ieunk80JeIKPzCgK+8amPo6tEXLvBDtiXvdQhRigv2mLdGKlvMGgxuCbVVdeo38ZmadRqipiCH+ItzQfn1+Quv+f2+AabY8wds3YKj6zkwRhU24Bdov/Fw/ererk+27g6mbawMa9Pufm96e/lQGTBE6GsOaxZJgdk6AfAeKDAGptOHSmYuqYgnXkH4NzZyWcQzeMInqvNYlSbRiw/IwrjWWnMbZtybn9T9IAAbaAoByYuiRzSgHJs4EVo8l1R61pPLjL5jzCpshTN2wT2zLsmL4ADsVJJEcNc1YG+xEWd/Pd+AHbZS/Hos/qbBw98XzQA==~4403249~3622466',
    '_abck': '59D7DD48E6A90EEB131BA027556B192D~0~YAAQZucVAlyQK4GZAQAA6k8IqQ4bTtVMBNncEc5DAzKxbf5dhYsKtIyhmm/OVj31KOnDSPo5T4s/uufYFXyvpRlkwR0pNoAS9zsU6YWP+eQG35klfTPTVbmA8fiGSZX1GhxSLPHckYkWhSdRIfWVRiuR1k3KOMNTyf8tCllgVHHNS0AUq5kHfDnA2xhSgxnCpQusSgUojXAHKjujz66j+oe5ssIAx9RYVhlI9R1sFM0nH/wZwCWGVDBSJsICu2BwzU3MT8H8f9l92m3XOcTX1FhMcUTeMxp6dWCfBk4s36wCM/OyjV0q+FolAOlv5S4oFiL3x2NrKGgmPGMbfdktXEb+BBlCEQy4VBEkO1DWqRtmQgp1XvgyNZTT1uMEs6plCPpydMoRZt6hJSzi4/ASewUOMDn394PGdrC2Ee1qaFWWOyk9n7fprO2+4caWXTj4FWSV6a0AR9TpTOdD5lkORjsQXWwHwmU9iGsT9mnS5Kvvi5Xune72oYiyHWLGjW++NGKnjkXtjrdzWnzn7I8YIeLJcLA8abYjTrcKqPzzjzv/nAdR8aKiMSGpy7pns7MQ5osR3ypEc0jyKv2nm3ZAa1uMJSxCbhUXHVJcOoymubHAll9MT/C5btsESaSqnHndDnxepBlsAegk9aJ9OZccNAEBhHsxuzs9OZYtq9pLn8/K64NQtWcp/peb9LI00DPiSJglROIyeQig9CCkBE7kQHGy6+iQf+4KCUa9MJ9T0Lw/IlgvF5Y38ACQsVjmJ9oloq33a/0Trre/6bOhqs4+bdUj6AuKO08rMvCDNmjZTrktpqbLshfqEa8UHGa/Vf2d4sK31wB3lSh/mnwkkN1/J/s1BsWPSRdKpZ4bxygHZ3EXRjk9l5AmR7QxYt0qF91w~-1~-1~-1~AAQAAAAE%2f%2f%2f%2f%2f0iAQgvhOE259zxvLXinkKnry7h+RTV2BCsCSdWpOh8RtUoTv1Ts7bySD91xcFnLnyPXL1MM8K+4McrVYYFPgPV2SJap90FT2dia~-1',
    'akaalb_Shop_ALB_instance1': '~op=shop_upperfunnel_static:shop-upperfunnel-1|shop_mwa_shared:mwa-shared-usw-2|~rv=60~m=shop-upperfunnel-1:0|mwa-shared-usw-2:0|~os=3ad3acca926c302b084e12bf3b209756~id=ed4b0a88a32a794cf5bfc421e80bd6d3',
    'AMCV_A92B3BC75245B1030A490D4D%40AdobeOrg': '179643557%7CMCIDTS%7C20364%7CMCMID%7C52375525777371028292491689370830964215%7CMCAAMLH-1752732403%7C6%7CMCAAMB-1759391618%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1759484720s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=2025-10-03T07%3A45%3A24.067Z&version=202509.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=62bc537c-d2bd-4c0f-b103-826359a79cf2&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=TAB01%3A1%2CC0004%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CTAB02%3A1&AwaitingReconsent=false',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://shop.lululemon.com',
    'priority': 'u=1, i',
    'referer': 'https://shop.lululemon.com/c/women-yoga-clothes/n14uwkzpofs',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36',
    'x-lll-client-repo-name': 'navrec',
    # 'cookie': '_ga_14J17NW0K4=GS2.2.s1751890298$o1$g0$t1751890300$j58$l0$h0; _lfa=LF1.1.cabc1bb242347854.1751890302222; _ga_V1VQCPSY6V=GS2.1.s1751957660$o2$g0$t1751957660$j60$l0$h0; _ga_GQP33VCV1E=GS2.1.s1751957660$o2$g0$t1751957660$j60$l0$h0; sat_track=true; kameleoonVisitorCode=4i8ulubslwypslau; ajs_anonymous_id=86da3fa5-7393-413c-977b-cf3ca069ebda; _ttp=28-waHDKO7tGyHsemr-0l5PGtY_; _scid=LwPoAZXzLO1BoqC6hLyDRwnxAZfy8aYX; _fbp=fb.1.1752127612468.307145000; _ga=GA1.1.1260579579.1751890297; __pdst=3ec3fcb533cc4ac2a5e2cd0f87b4ab59; kampyle_userid=d104-008b-d31a-7d46-5eaa-17fd-3241-a450; _pin_unauth=dWlkPVl6TTJNelV6WlRRdE5XVXpOUzAwT1RFeExXRmlNemt0TTJaaE56aGhZemc0T0RRdw; digitalData.page.a1Token=$2a$10$tNGLzxgFy.YH1jVIvc.LIOY4ORTw.fW7fXfpWyGQgsH.ZWRjuyyyi; _evga_8f06={%22uuid%22:%229ec5c2631c240b31%22}; _sfid_cc29={%22anonymousId%22:%229ec5c2631c240b31%22%2C%22consents%22:[{%22consent%22:{%22provider%22:%22Consent%20Provider%22%2C%22purpose%22:%22Personalization%22%2C%22status%22:%22Opt%20In%22}%2C%22lastUpdateTime%22:%222025-07-10T06:06:55.435Z%22%2C%22lastSentTime%22:%222025-07-10T06:06:55.439Z%22}]}; _ttp=28-waHDKO7tGyHsemr-0l5PGtY_.tt.1; _tt_enable_cookie=1; _fbp=fb.1.1752127612468.307145000; _gcl_au=1.1.1388619635.1752127616; a1ashgd=4b8j6vwzg3p000004b8j6vwzg3p00000; _sctr=1%7C1752091200000; bttnsessionid=sess-H2qHL643wyETBr7pgU3Yx41xHW4NF5kZHtFJZd49IbUw_; QuantumMetricUserID=86831e065cf43c36ac4b56fde3222bff; _rdt_uuid=1752127613494.a76d7d73-f628-4de0-88ff-078d5535cfba; kampyleUserSession=1752129062551; kampyleUserSessionsCount=3; kampyleUserPercentile=14.551039287714485; kampyleSessionPageCounter=1; _scid=I3Km-6s9xltlYS7dc8AysCMHYnqqbMxjPrhP8A; ttcsid_C65BFLPR48GN82KJE2E0=1752127616136::25526VBqZoBaTt-QbCai.1.1752129063135; _ga_4ZRJ21056F=GS2.1.s1752131300$o2$g0$t1752131300$j60$l0$h0; _ga_CCD7VVYPZ7=GS2.1.s1752131300$o2$g0$t1752131300$j60$l0$h0; intlOTConsent=C0004:1,C0001:1,C0003:1,C0002:1; NoCookie=true; __cq_uuid=2ab6ce80-5d6c-11f0-8bb0-47509f0499fd; _scid_r=JXKm-6s9xltlYS7dc8AysCMHYnqqbMxjPrhP8g; _ga_BXZE3SJMWL=GS2.1.sD84drOFtA18hFH51RDTXopGOmFqnQ69vpXc%3D$o1$g1$t1752137983$j37$l0$h0; a1ashgd=cqlz5hkklui00000cqlz5hkklui00000; _uetvid=13c9c8605d5411f0a0fdaf8fca2d1181|jjcgek|1752129063687|4|1|bat.bing.com/p/insights/c/e; ttcsid_CNK2R5JC77U8IUSPJBFG=1752137960452::GtBuI1LXA4A6tL5T5oTU.1.1752137983701; ttcsid=1752137960454::xDW5y-BLQEYmZznaYhtD.2.1752137983701; mbox=PC#bdf3d85951b14ca48c0c2159000bc260.37_0#1817621992|session#7f13025d373846b9b6ae5c3c2bc5fb3f#1754379052; lll-ix-wl=true; lll-ix-dash=true; lll_digital_id=52375525777371028292491689370830964215; PersadIDExp=db2996cec38e5f0da55661b47f033fcf; lll_client_id=52375525777371028292491689370830964215; UsrLocale=en_US; sl=US; bm_s=YAAQV+cVAmIOm+aYAQAAmo2HDgQuh5JLtrLWrjQKE/RBi7/FK0rDeAPHHcN0Vc+e/OjPjApY/JB4OlNGbj8K6KLR79sZfwZHO4fYFS7MqmPh6GVr2UbFTPM1FYGNypH3P0XiArNPpbjdD5mrMhGxurCbh+zjv4h2q1+H/cEtl5uTCegxH5C8L5krjIJ9e1/chCwbfZqCsvl/GLPncRjpF/S60P/4jkrn6sEY+zh+99RrMbtEcvchTY+FAg9N5oOpLnCeF3lYOp31vfvwH+v71qYoPZaKCWnaV9fGqv/PthxYDnIEp39eJDcsYld+jNHJLBEtJA20z42jOx1zfqzZT1xK33+RTw3OAdYllRJqkG6n93u2oveHnicIG/YLlJigzVCvX8oQCLDhgUCmCuWia/kqLmKL37wbW1khj5cbJfCI6lQtTW7ipA6I7QHcM5cudc76lGrUKsf/6s7efWRofGYTNSbTgo6ierdn5nzY6gHswtMeq5TXi0Ksdv/XzgNZSo1c+5pMrG4ihvi+N7nCTuqCm+tT6EtsQCtfaQkThv4bR47WTc1KNF9bW0PVqm2B9Oe/tlrG61Y=; cf_clearance=k_AbK0hfUwMOSGTdX0D4UygQsRZAiFgvfO9XFWT4t4Y-1759402424-1.2.1.1-3KOHwY3fCwngka2NPdvzzaNeZxX_lr7h7nyNvDBYdt9_f5bOL9WJhUO29SaQmgXJ1xyNGN.QoM5.ekYCqjZsk6lJ8NIneZvmNq0DAWnfa98Bq0yCwHklQhS.IPBZykMFeUe0a34tRyaj4ApoRKOBxXW2LLQ6xFnm46fKx.6bYekdIYz7wfXKJmwu5aY9PaAiCYAiZAqljuhXTbZ1C3ZOqw02MteDDFUwhEz0a18TSi0; tfc-l=%7B%22k%22%3A%7B%22v%22%3A%223vm79qikjbsm7aqfh6ta2egvcg%22%2C%22e%22%3A1818575671%7D%2C%22c%22%3A%7B%22v%22%3A%22adult%22%2C%22e%22%3A1818575670%7D%2C%22a%22%3A%7B%22v%22%3A%2289adc922-17cc-4e52-94c5-0ec5e2b543f2%22%2C%22e%22%3A1759488830%7D%7D; alaPPN=pdp:prod11790330; Prg5BMu0=A5V7TXqYAQAAjUEQTLZjmz8a6VA_ZxWD0rYp_8ZPSH-TPF1ZHEz3dua0d_u5AV7L1u2uchxGwH8AAEB3AAAAAA|1|1|e7aea4d618cbf530d8ef3c8e9374c6701864d5cf; lll_edge_geo_data=city=DUBAI&state=&zip=&country=AE&lat=25.25&long=55.28; lll-ecom-correlation-id=95503BE2-6D8A-A304-C2FC-6E2CE54CBE9B; AMCVS_A92B3BC75245B1030A490D4D%40AdobeOrg=1; ek8_guest=true; apigeeToken=eyJqa3UiOiJodHRwczpcL1wvcHJvZC5hcGlzLmxsbGV4dC5jb21cL2FwaW1cL3YxXC9qd3R2ZXJpZmljYXRpb25cL2p3a3MiLCJraWQiOiJyc2FfXzZidW14bnUzNWVqOW11OGZscSIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJyb2xlIjoiZ3Vlc3QiLCJpc3MiOiJodHRwczpcL1wvcHJvZC5hcGlzLmxsbGV4dC5jb21cL2p3dFwvdjEiLCJJRCI6InhWR1NVZXVndm9nUHRnaUprYmo4aUY3U2FjYW5WSUE5IiwiVVVJRCI6IjZjODhkZjY3LTg2N2QtNGI5Yi1hNDg5LWI1NTNmNDRlNjcxZiIsImV4cCI6MTc1OTQ3NzE1NiwiaWF0IjoxNzU5NDczNTU2LCJqdGkiOiJlOWRjOGNmYS0yOWEyLTQwNTAtYjhhZC0wOWI1NzU0OGI2ZGIifQ.ltz9QAAUXX-duGuRtM158DSgAPJ_qLYKI9Miig57Jzm3NqSL4mLVY9g9l5cYyMdQLyiXO1a4V0bQrvWj185EdyoQB9T9b0-lZhiAq7pnH-GR0PfNS6RbzihEcRmck94FyydXDYtWnp76oStwIP0dgOKcNo1mPFEZBghmiGFdKn3Ku7kHPfis1beAwJkWG1i98xe3I6t7P_RyyRm9YD2kZjSJ2kEmWgj7cQ0Ng2F1nwrXfe6BmQwGg90CKQD_gBslpYR5fwAb2o_FMuWYLF2vn7JXkqEZ-P5nzfYRTIojDBY3rcNO2zVIuouV5jEAA2nQhiehNX0D9yeY4VjmY4RSPQ; ak_bmsc=4D58F307662B218015BF2275ED71FBB8~000000000000000000000000000000~YAAQZucVAkSQK4GZAQAAP04IqR3kYUk2QTBKsLAVrmF1EvSOR8+MU9iju0dY69Vo2KjlqsvnrU4Sec1R65ITBSyOaim6QJIyiPdhiGZr9HhHoVnfYZ6Q1u/NjUMjhaP/dIzVkzq/Vxstn8uKsuQPWolaHGMPK5ag3clp04AAJHMnHcZqzkbicejwwDVLs2X3gZ7+mcyGPDorCUHaF9AS+7oyKFSU2W0feTISUrnj01FHQ5rO2XvST+jLDs7qOo3YGWAs/zv/Y/gq6PLHsG5SGOmFtstIWLncSRXCvKNVO3sBo31OrGwU1gWjSUFUIzUwH29yccyL4c69tuJWj03JeOq+0S1PRC/phHMaCSsKdYp/anygx2TKErw/Y6mXGbU67ZXPRW1riQX1EUZJTSKIxKB8xX7S; bm_mi=079B92F23FC1ADFAC13333345354BFC0~YAAQZucVAkWQK4GZAQAAP04IqR0kpNSbDU9MDi6N+JueuNe5XR0g1pI+jIdZp1BVdt9tw93hEFv1QCJQehxCIr1qlI/C8OFwNU6pFPSBebbbhG3pmEbOCJGIiBCYqW/r1R40UNMNjxPBBRyDzvX3g8gxqpUQ7Vc6yVA7NGlqRwHwHXDI6h7zBGwyL/BPGnVJhCDrkEtfR6r+ro0Y/vPmaQamtCh25N1zP9K+ydSsl8rNwrpmQxrAZbQ4qT2hnEN1qwPEGkuo+NUI2a3HtKSBdU3jhEenu2yTvrWnBpq6J+LupB4K/Edzk5iXaohD9kIqAxZPz3ckoOZXFUDgG9ZpASnE4uATMdXmCQP9j5icX9o=~1; bm_sv=9C2A466F5198F802270D3BAD6CA1CCC8~YAAQZucVAkaQK4GZAQAAP04IqR0wx20uECVyzSvDjRd5ZO/ZnhENO6xQRwD7tIY7Nn25Bl79DThDt6vbMHz0RqAbWMKEpv7co3M2wxFep6ppCsQXei/N9wSnO8ApE2ujckq2hilAYsnHozaK3dPo4E/l2+m+a40fd8rusqwaJGmDtuGZiGRxk5bYTPs+C1GYgmSTqhYoj8SvqDIHZywuQnc/eslOgSpqm6ktJcS2XHgZhy7gKOld/3XY+ADDvkFDun0u~1; bm_sz=27E3C1AA328B1B175A5A1165ED2E3798~YAAQZucVAkeQK4GZAQAAP04IqR1KR8m3cAoxRFdMNCstPsdgR/kRqOn8ncym1oCaM/ewJ0WckB/kwCrQk4tbCM49x4hRC8maN3vrhN81/Ieunk80JeIKPzCgK+8amPo6tEXLvBDtiXvdQhRigv2mLdGKlvMGgxuCbVVdeo38ZmadRqipiCH+ItzQfn1+Quv+f2+AabY8wds3YKj6zkwRhU24Bdov/Fw/ererk+27g6mbawMa9Pufm96e/lQGTBE6GsOaxZJgdk6AfAeKDAGptOHSmYuqYgnXkH4NzZyWcQzeMInqvNYlSbRiw/IwrjWWnMbZtybn9T9IAAbaAoByYuiRzSgHJs4EVo8l1R61pPLjL5jzCpshTN2wT2zLsmL4ADsVJJEcNc1YG+xEWd/Pd+AHbZS/Hos/qbBw98XzQA==~4403249~3622466; _abck=59D7DD48E6A90EEB131BA027556B192D~0~YAAQZucVAlyQK4GZAQAA6k8IqQ4bTtVMBNncEc5DAzKxbf5dhYsKtIyhmm/OVj31KOnDSPo5T4s/uufYFXyvpRlkwR0pNoAS9zsU6YWP+eQG35klfTPTVbmA8fiGSZX1GhxSLPHckYkWhSdRIfWVRiuR1k3KOMNTyf8tCllgVHHNS0AUq5kHfDnA2xhSgxnCpQusSgUojXAHKjujz66j+oe5ssIAx9RYVhlI9R1sFM0nH/wZwCWGVDBSJsICu2BwzU3MT8H8f9l92m3XOcTX1FhMcUTeMxp6dWCfBk4s36wCM/OyjV0q+FolAOlv5S4oFiL3x2NrKGgmPGMbfdktXEb+BBlCEQy4VBEkO1DWqRtmQgp1XvgyNZTT1uMEs6plCPpydMoRZt6hJSzi4/ASewUOMDn394PGdrC2Ee1qaFWWOyk9n7fprO2+4caWXTj4FWSV6a0AR9TpTOdD5lkORjsQXWwHwmU9iGsT9mnS5Kvvi5Xune72oYiyHWLGjW++NGKnjkXtjrdzWnzn7I8YIeLJcLA8abYjTrcKqPzzjzv/nAdR8aKiMSGpy7pns7MQ5osR3ypEc0jyKv2nm3ZAa1uMJSxCbhUXHVJcOoymubHAll9MT/C5btsESaSqnHndDnxepBlsAegk9aJ9OZccNAEBhHsxuzs9OZYtq9pLn8/K64NQtWcp/peb9LI00DPiSJglROIyeQig9CCkBE7kQHGy6+iQf+4KCUa9MJ9T0Lw/IlgvF5Y38ACQsVjmJ9oloq33a/0Trre/6bOhqs4+bdUj6AuKO08rMvCDNmjZTrktpqbLshfqEa8UHGa/Vf2d4sK31wB3lSh/mnwkkN1/J/s1BsWPSRdKpZ4bxygHZ3EXRjk9l5AmR7QxYt0qF91w~-1~-1~-1~AAQAAAAE%2f%2f%2f%2f%2f0iAQgvhOE259zxvLXinkKnry7h+RTV2BCsCSdWpOh8RtUoTv1Ts7bySD91xcFnLnyPXL1MM8K+4McrVYYFPgPV2SJap90FT2dia~-1; akaalb_Shop_ALB_instance1=~op=shop_upperfunnel_static:shop-upperfunnel-1|shop_mwa_shared:mwa-shared-usw-2|~rv=60~m=shop-upperfunnel-1:0|mwa-shared-usw-2:0|~os=3ad3acca926c302b084e12bf3b209756~id=ed4b0a88a32a794cf5bfc421e80bd6d3; AMCV_A92B3BC75245B1030A490D4D%40AdobeOrg=179643557%7CMCIDTS%7C20364%7CMCMID%7C52375525777371028292491689370830964215%7CMCAAMLH-1752732403%7C6%7CMCAAMB-1759391618%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1759484720s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; OptanonConsent=isGpcEnabled=0&datestamp=2025-10-03T07%3A45%3A24.067Z&version=202509.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=62bc537c-d2bd-4c0f-b103-826359a79cf2&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=TAB01%3A1%2CC0004%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CTAB02%3A1&AwaitingReconsent=false',
}

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

df.to_csv(f"{category}_product_ids.csv", index=False)
# df.to_excel(f"{category}_product_ids.xlsx", index=False)

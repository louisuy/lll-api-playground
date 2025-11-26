import requests
import json
import re

raw_input_code = input("Enter product code (e.g., prod00000000 or PROD00000000_LULU): ").strip()
product_code = re.search(r'(prod\d+)', raw_input_code, re.IGNORECASE)

if product_code:
    product_code = product_code.group(1).lower()
else:
    raise ValueError("❌ Could not extract a valid product code.")

print(f"✅ Normalized product code: {product_code}")

cookies = {
    '_ga_14J17NW0K4': 'GS2.2.s1751890298$o1$g0$t1751890300$j58$l0$h0',
    '_lfa': 'LF1.1.cabc1bb242347854.1751890302222',
    '_ga_V1VQCPSY6V': 'GS2.1.s1751957660$o2$g0$t1751957660$j60$l0$h0',
    '_ga_GQP33VCV1E': 'GS2.1.s1751957660$o2$g0$t1751957660$j60$l0$h0',
    'sat_track': 'true',
    'kameleoonVisitorCode': '4i8ulubslwypslau',
    'UsrLocale': 'en_US',
    'sl': 'US',
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
    'alaPPN': 'pdp:prod11680106',
    '_scid_r': 'JXKm-6s9xltlYS7dc8AysCMHYnqqbMxjPrhP8g',
    '_ga_BXZE3SJMWL': 'GS2.1.sD84drOFtA18hFH51RDTXopGOmFqnQ69vpXc%3D$o1$g1$t1752137983$j37$l0$h0',
    'a1ashgd': 'cqlz5hkklui00000cqlz5hkklui00000',
    '_uetvid': '13c9c8605d5411f0a0fdaf8fca2d1181|jjcgek|1752129063687|4|1|bat.bing.com/p/insights/c/e',
    'ttcsid_CNK2R5JC77U8IUSPJBFG': '1752137960452::GtBuI1LXA4A6tL5T5oTU.1.1752137983701',
    'ttcsid': '1752137960454::xDW5y-BLQEYmZznaYhtD.2.1752137983701',
    'AMCV_A92B3BC75245B1030A490D4D%40AdobeOrg': '179643557%7CMCIDTS%7C20306%7CMCMID%7C52375525777371028292491689370830964215%7CMCAAMLH-1752732403%7C6%7CMCAAMB-1754377189%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1754384390s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0',
    'mbox': 'PC#bdf3d85951b14ca48c0c2159000bc260.37_0#1817621992|session#7f13025d373846b9b6ae5c3c2bc5fb3f#1754379052',
    'cf_clearance': 'hwpudf0t3DVW8tPz29QLJfXpTeDkJ9cnCdbEfkOm3DM-1754383476-1.2.1.1-hBmsU0JPbNLY7QresnIPgaC92QEu3e5RWr4zx8URdOH.zaxvE.b.1QYxjvyyEqNeXuJV71JIjXTvp_K._L2fiEW6B3JO0jqe7OWDA2ME7Zo7yzkxHjwBDDEPwVoepiIfC0ANCD6mW_xzCYJt72pPRORDRC4F.J6i0hnPeM.i6em5A11LcHrLf81lrAmPJ3FCG_asH3rYoiweia.WuoNeBkpxOUGkrfmpV3CO1EK9IRc',
    'lll-ix-wl': 'true',
    'lll-ix-dash': 'true',
    'lll_digital_id': '52375525777371028292491689370830964215',
    'lll_edge_geo_data': 'city=DUBAI&state=&zip=&country=AE&lat=25.25&long=55.28',
    'lll-ecom-correlation-id': 'E60ED0CA-AAA1-0899-A0BE-1B597DB6AE47',
    'akaalb_Shop_ALB_instance1': '~op=shop_upperfunnel_static:shop-upperfunnel-1|shop_mwa_shared:mwa-shared-usw-2|~rv=34~m=shop-upperfunnel-1:0|mwa-shared-usw-2:0|~os=3ad3acca926c302b084e12bf3b209756~id=0367cd63924f633d33ba14ee23da8b40',
    'ek8_guest': 'true',
    'Prg5BMu0': 'A5V7TXqYAQAAjUEQTLZjmz8a6VA_ZxWD0rYp_8ZPSH-TPF1ZHEz3dua0d_u5AV7L1u2uchxGwH8AAEB3AAAAAA|1|1|e7aea4d618cbf530d8ef3c8e9374c6701864d5cf',
    'lll_oidc_token': 'eyJraWQiOiJfd2dUU1ZQTFdwdUd1OXh0U1AzbkhhbDQwVUY4bnFDUnVsZnRFNzZ5bURRIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULnRpYUkxOFNXcUllTUhaeWRBMHNld3ZTaFUxZHhnOTJYT0lPR3VOOFp1encub2FyMzh6MmFsNUFjVzhUMVg0eDciLCJpc3MiOiJodHRwczovL2lkZW50aXR5Lmx1bHVsZW1vbi5jb20vb2F1dGgyL2F1c2FvczlkMldqM2d3NmtyNHg2IiwiYXVkIjoiZ3Vlc3RzIiwiaWF0IjoxNzU1MDY5ODQxLCJleHAiOjE3NTUwNzcwNDEsImNpZCI6IjBvYWFvcnVxNG9Gc2g1TzNlNHg2IiwidWlkIjoiMDB1c25vcmY3b081TjBZQjk0eDciLCJzY3AiOlsib2ZmbGluZV9hY2Nlc3MiLCJwaWkiLCJvcGVuaWQiLCJlbWFpbCJdLCJhdXRoX3RpbWUiOjE3NTQzOTg2MTgsInN1YiI6ImFudGhvbnkubG91aXNAbWFmLmFlIn0.ZrgLS_7O4mh52APEUv9-RPtRqtccPAA8zO8A5K5SxY1Bz1AYn9S9Nl4FPzrZltN67hIE28VQUvI6YfA0gIk9f5UnjFbMrI4yDyQJdjhaIxB_2luANyu6XI5zx3s4PjWnk7mCWY_VzpUtEVLiTuIOm1V2dPHBkAv_mn87UWZcMDD-KFgjs-D4E3JiQwz2QsnZTVL4vU4obdiZkOaJstpmTAhlqLcDTj298lOy0lrhIJ1MJE380lTp1LSmihbNB8y9aAxN-H6ZB-QbtWy2foQGm-ks_PqVlt6qShfcDOk653Gv3Z4gBZ_XGYK4ZFhJuZpo_8PFU4qQrqfGGFzKlyQ4DA',
    'lll_refresh_token': 'true',
    'pers_seg': 'eyJnZW5kZXJBZmZpbml0eSI6IndvbWVuIn0=',
    'bm_mi': 'E1D693CF0A60A2CF6E0145C4499804EC~YAAQres/F4nSv56YAQAAxzhXohwkR84GzAof2P2zxzEnpdWbcVCHngaDvTfjuwTKuTouEAYZp1a/PpuhDTVVzHUvbbLv21lViFGKPtVTDr5JWgIQiu1cQ836goHV//0jXuyy0LTCMcQT3GMohMuKkywH4AqHZDepSFJJV26zCCQzsORDsNYcnLq0xJnM8VT3zuYT0Ef4GHV+MIdcvksyiHerwEAincR5mtwFq9U9kW33C/5qAhwCeB/gnAIoPJoVUSWD3yu87Bg+Pj9jeEzoBqLBTLLZiddnw49sIiQfpcwbTJWLd4b0t22PcAckj/0Ez+UJVJJSbxZvqRblZhABF14N5nxzVskb77JPQkc=~1',
    'bm_sv': '84E138F19C9D78AFFE457B3D7BDEE6A3~YAAQres/F0LUv56YAQAA+FlXohwDfY1cogzmIXCZ7NCgS5QNKnYep065MvqI3/R+fE1wX5E4uGX0EkIb+YhB9Oa+dfcaA/h5hWF6wPxYKpJwL/gnjg5aDO963LczY93AjgTLVXH+Wci2V62XZJ5psuppghUE9nY9QRtcKnJl9MP3MLVBMXA+HMT5c6XnYjlQUsgPYWbTgUaedp5viG3BWEk9ADt90Vk7UM6ekiA4K0nnYixdDOqxzK4k+rPR7AHqOdcd4A==~1',
    'ak_bmsc': '03A2A8AC610A620A1054B4246484AB43~000000000000000000000000000000~YAAQres/Fz/Pwp6YAQAAWvybohwT9NkodwkHuEPDPFOUVXXCb98fP/U22CnkhC1y3MAqhALzZhtuccbdG3iGMUAFgeqqcn/+0cGtPfNfWYnI4FSRRa9gjOSChJXxn1KNrJDOwLS+ENs1sbZYA6QZ97gTjiI56DylK13czrwauG0VjpSVcrN5TOW8oQns/s156P1cFfK1QKycHuZ6TeuvPJ6J5HwuxELuxNDQvJGAvzy/RiSbBXpOIgKGyr3AJZ+wEHVR7ZnLZwQKlNCN6xYW9yzcRdndrpivxY6VU6Ly/N+8vmf2WgNfg8r/z52nIsh64oED8idjCbXyd/jfmDrNLR1qhccW4xy/9/AbR1xT0RolqspEyh82bnOQAUQRljcB+mvnVVTV8516z1ozswwTp3Qu/FnhDDEsA786817OKlRszQXVs24fUXm5Hk3I2Tvd9nG4GCXO/GnG+k5JgKa1HXE=',
    '_abck': '59D7DD48E6A90EEB131BA027556B192D~0~YAAQres/F03Pwp6YAQAAq/6bog4F+ryXNt82eaTxlufYSJZfRZTaT8Jvep+L9Vi9cBk5Yc36+V51UFSMWddAiX/VLTfNd2So13r8lvqG1SyctpR9tUlagQRE0LOlCZ2144aX/f/8mCsLcpxh+wy5PvxXHyxi2LXjUCyXM2lFzRIXXiPP6Ga+5ynOzOhZc87nG1+il5UF+AYhCma9U8/UbyFn8e2RJnCUbDDbUbY+cBGvxcwSv+cx3ff9TaDztrObAcqTAYJvGuz4BF2wARTjHADGi0NszhSVK1GJ23oTFPruledreJyvV3h1k9PGLyOXJIdgIYpiYT4rYe6fIVtbUYauTja9OMbGSgwM3avIG9xL0c1Qz+de1P1CkQCb25KENG6Gr6AwmvemdCo8+ArIbuS9vha0cWoVywGKH09+VScoP2RiFHJm+nbAv2Znv+3ib3XB/RE1p0YBUQ0A3zoMsLEb/rnY/3Pq64BUVAz7DcDpXvrggLzu+tq+7q+11lT4eiPh/3VdXxDG41jfJGS79B2Ev0VM5dDfEUfdFKUpl6UM4h6No4TLBgFvbQVjFZDaKwmsr1r7JAbRFIqWcgVBIUvU09ePKp6HsLQI4LVh+wqQaCdvX3TP28vrvYeN6VOLhkIA+cjyCIx1gNLvM9450rUh2pshMWJuE22NyNB2pB5P3BNDzzx3kcJwvOS7Pe/6KnM/NyQcOUWCPSreZku9Ds44GlQv+IzhlU2zw/GV0Bt4vNHuJp0SdAORUXpC3W65F+xPTG+Gnb/N4Dg25b6TNpc9xnUzsONdIy01iDDIvmXBHh6EpfLXbdR10nXM6lrAL02Stuph4/TN9fqyXZFTqTRD7Ji1H0+6rz5Pxb/CXp8BIHcH2F30bsD7abhV/NEvFeyWRgSBYNj2l8hoWF8=~-1~-1~1755077036',
    'tfc-l': '%7B%22k%22%3A%7B%22v%22%3A%22idap4hda1kcsh55m486ug1sph9%22%2C%22e%22%3A1815027743%7D%2C%22a%22%3A%7B%22v%22%3A%22e834e722-1ae3-4423-8462-beb5cf955776%22%2C%22e%22%3A1753181187%7D%2C%22c%22%3A%7B%22v%22%3A%22adult%22%2C%22e%22%3A1815027743%7D%7D',
    'bm_sz': 'A49F6DF10EC9D549032FCF542D21C4FA~YAAQres/F4XRwp6YAQAAz0icohz6XWrhdQO/9QpWtvkiKrgjCSQa/LIuE5VrTRfy3wK+lNGHvzXYjRXJ9Jzg7t2YH8eI6NtV5mkwAn/9R3cfykHvlwX/rSH/WBnPtXts40PfYAz4iVvNZwqUoV0jk5Kn4CE07rpv5ydg1xjXRytZ9j5lADoD8NnYxt0OVotO1mgvsDZOvmItbeXzRRb9JIm6Y7Ue4JweZsw9hGaReoWOJvi5vclZuQopt4yVrCzNYqCCdinrkdYi41I9uW6FeQMwk8OGXZlycJeftD75NhbO6BsKmz3TcCoLnJir/NqLlCIS2LUxCU6JN32lnvN9V3eHX7dWYHm+iSrWhpaBIptIURHJRLqJzetPA/BvAlwrGunkRCuEx5fP0CfXs1Cy7tRXbqy8OhfFMFKJXaYHQ1gFXCkkqZK31pWansegwg==~4600118~3687729',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=2025-08-13T08%3A46%3A51.694Z&version=202507.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=62bc537c-d2bd-4c0f-b103-826359a79cf2&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=TAB01%3A1%2CC0004%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CTAB02%3A1&AwaitingReconsent=false',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://shop.lululemon.com',
    'priority': 'u=1, i',
    'referer': 'https://shop.lululemon.com/p/women-shorts/Scuba-High-Rise-Short-5-Waffle/_/prod20005307?color=71400',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'f9828dd7f10f430eb6a1df9ab966eba0',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
    'x-lll-client': 'product-sdk',
    'x-lll-ecom-correlation-id': 'E60ED0CA-AAA1-0899-A0BE-1B597DB6AE47',
    'x-lll-referrer': 'Channel=Web,Page=pdp',
    'x-lll-request-correlation-id': '9ca0bfaa-6cb7-4211-8989-513c4c2a911f',
    # 'cookie': '_ga_14J17NW0K4=GS2.2.s1751890298$o1$g0$t1751890300$j58$l0$h0; _lfa=LF1.1.cabc1bb242347854.1751890302222; _ga_V1VQCPSY6V=GS2.1.s1751957660$o2$g0$t1751957660$j60$l0$h0; _ga_GQP33VCV1E=GS2.1.s1751957660$o2$g0$t1751957660$j60$l0$h0; sat_track=true; kameleoonVisitorCode=4i8ulubslwypslau; UsrLocale=en_US; sl=US; ajs_anonymous_id=86da3fa5-7393-413c-977b-cf3ca069ebda; _ttp=28-waHDKO7tGyHsemr-0l5PGtY_; _scid=LwPoAZXzLO1BoqC6hLyDRwnxAZfy8aYX; _fbp=fb.1.1752127612468.307145000; _ga=GA1.1.1260579579.1751890297; __pdst=3ec3fcb533cc4ac2a5e2cd0f87b4ab59; kampyle_userid=d104-008b-d31a-7d46-5eaa-17fd-3241-a450; _pin_unauth=dWlkPVl6TTJNelV6WlRRdE5XVXpOUzAwT1RFeExXRmlNemt0TTJaaE56aGhZemc0T0RRdw; digitalData.page.a1Token=$2a$10$tNGLzxgFy.YH1jVIvc.LIOY4ORTw.fW7fXfpWyGQgsH.ZWRjuyyyi; _evga_8f06={%22uuid%22:%229ec5c2631c240b31%22}; _sfid_cc29={%22anonymousId%22:%229ec5c2631c240b31%22%2C%22consents%22:[{%22consent%22:{%22provider%22:%22Consent%20Provider%22%2C%22purpose%22:%22Personalization%22%2C%22status%22:%22Opt%20In%22}%2C%22lastUpdateTime%22:%222025-07-10T06:06:55.435Z%22%2C%22lastSentTime%22:%222025-07-10T06:06:55.439Z%22}]}; _ttp=28-waHDKO7tGyHsemr-0l5PGtY_.tt.1; _tt_enable_cookie=1; _fbp=fb.1.1752127612468.307145000; _gcl_au=1.1.1388619635.1752127616; a1ashgd=4b8j6vwzg3p000004b8j6vwzg3p00000; _sctr=1%7C1752091200000; bttnsessionid=sess-H2qHL643wyETBr7pgU3Yx41xHW4NF5kZHtFJZd49IbUw_; QuantumMetricUserID=86831e065cf43c36ac4b56fde3222bff; _rdt_uuid=1752127613494.a76d7d73-f628-4de0-88ff-078d5535cfba; kampyleUserSession=1752129062551; kampyleUserSessionsCount=3; kampyleUserPercentile=14.551039287714485; kampyleSessionPageCounter=1; _scid=I3Km-6s9xltlYS7dc8AysCMHYnqqbMxjPrhP8A; ttcsid_C65BFLPR48GN82KJE2E0=1752127616136::25526VBqZoBaTt-QbCai.1.1752129063135; _ga_4ZRJ21056F=GS2.1.s1752131300$o2$g0$t1752131300$j60$l0$h0; _ga_CCD7VVYPZ7=GS2.1.s1752131300$o2$g0$t1752131300$j60$l0$h0; intlOTConsent=C0004:1,C0001:1,C0003:1,C0002:1; NoCookie=true; __cq_uuid=2ab6ce80-5d6c-11f0-8bb0-47509f0499fd; alaPPN=pdp:prod11680106; _scid_r=JXKm-6s9xltlYS7dc8AysCMHYnqqbMxjPrhP8g; _ga_BXZE3SJMWL=GS2.1.sD84drOFtA18hFH51RDTXopGOmFqnQ69vpXc%3D$o1$g1$t1752137983$j37$l0$h0; a1ashgd=cqlz5hkklui00000cqlz5hkklui00000; _uetvid=13c9c8605d5411f0a0fdaf8fca2d1181|jjcgek|1752129063687|4|1|bat.bing.com/p/insights/c/e; ttcsid_CNK2R5JC77U8IUSPJBFG=1752137960452::GtBuI1LXA4A6tL5T5oTU.1.1752137983701; ttcsid=1752137960454::xDW5y-BLQEYmZznaYhtD.2.1752137983701; AMCV_A92B3BC75245B1030A490D4D%40AdobeOrg=179643557%7CMCIDTS%7C20306%7CMCMID%7C52375525777371028292491689370830964215%7CMCAAMLH-1752732403%7C6%7CMCAAMB-1754377189%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1754384390s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; mbox=PC#bdf3d85951b14ca48c0c2159000bc260.37_0#1817621992|session#7f13025d373846b9b6ae5c3c2bc5fb3f#1754379052; cf_clearance=hwpudf0t3DVW8tPz29QLJfXpTeDkJ9cnCdbEfkOm3DM-1754383476-1.2.1.1-hBmsU0JPbNLY7QresnIPgaC92QEu3e5RWr4zx8URdOH.zaxvE.b.1QYxjvyyEqNeXuJV71JIjXTvp_K._L2fiEW6B3JO0jqe7OWDA2ME7Zo7yzkxHjwBDDEPwVoepiIfC0ANCD6mW_xzCYJt72pPRORDRC4F.J6i0hnPeM.i6em5A11LcHrLf81lrAmPJ3FCG_asH3rYoiweia.WuoNeBkpxOUGkrfmpV3CO1EK9IRc; lll-ix-wl=true; lll-ix-dash=true; lll_digital_id=52375525777371028292491689370830964215; lll_edge_geo_data=city=DUBAI&state=&zip=&country=AE&lat=25.25&long=55.28; lll-ecom-correlation-id=E60ED0CA-AAA1-0899-A0BE-1B597DB6AE47; akaalb_Shop_ALB_instance1=~op=shop_upperfunnel_static:shop-upperfunnel-1|shop_mwa_shared:mwa-shared-usw-2|~rv=34~m=shop-upperfunnel-1:0|mwa-shared-usw-2:0|~os=3ad3acca926c302b084e12bf3b209756~id=0367cd63924f633d33ba14ee23da8b40; ek8_guest=true; Prg5BMu0=A5V7TXqYAQAAjUEQTLZjmz8a6VA_ZxWD0rYp_8ZPSH-TPF1ZHEz3dua0d_u5AV7L1u2uchxGwH8AAEB3AAAAAA|1|1|e7aea4d618cbf530d8ef3c8e9374c6701864d5cf; lll_oidc_token=eyJraWQiOiJfd2dUU1ZQTFdwdUd1OXh0U1AzbkhhbDQwVUY4bnFDUnVsZnRFNzZ5bURRIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULnRpYUkxOFNXcUllTUhaeWRBMHNld3ZTaFUxZHhnOTJYT0lPR3VOOFp1encub2FyMzh6MmFsNUFjVzhUMVg0eDciLCJpc3MiOiJodHRwczovL2lkZW50aXR5Lmx1bHVsZW1vbi5jb20vb2F1dGgyL2F1c2FvczlkMldqM2d3NmtyNHg2IiwiYXVkIjoiZ3Vlc3RzIiwiaWF0IjoxNzU1MDY5ODQxLCJleHAiOjE3NTUwNzcwNDEsImNpZCI6IjBvYWFvcnVxNG9Gc2g1TzNlNHg2IiwidWlkIjoiMDB1c25vcmY3b081TjBZQjk0eDciLCJzY3AiOlsib2ZmbGluZV9hY2Nlc3MiLCJwaWkiLCJvcGVuaWQiLCJlbWFpbCJdLCJhdXRoX3RpbWUiOjE3NTQzOTg2MTgsInN1YiI6ImFudGhvbnkubG91aXNAbWFmLmFlIn0.ZrgLS_7O4mh52APEUv9-RPtRqtccPAA8zO8A5K5SxY1Bz1AYn9S9Nl4FPzrZltN67hIE28VQUvI6YfA0gIk9f5UnjFbMrI4yDyQJdjhaIxB_2luANyu6XI5zx3s4PjWnk7mCWY_VzpUtEVLiTuIOm1V2dPHBkAv_mn87UWZcMDD-KFgjs-D4E3JiQwz2QsnZTVL4vU4obdiZkOaJstpmTAhlqLcDTj298lOy0lrhIJ1MJE380lTp1LSmihbNB8y9aAxN-H6ZB-QbtWy2foQGm-ks_PqVlt6qShfcDOk653Gv3Z4gBZ_XGYK4ZFhJuZpo_8PFU4qQrqfGGFzKlyQ4DA; lll_refresh_token=true; pers_seg=eyJnZW5kZXJBZmZpbml0eSI6IndvbWVuIn0=; bm_mi=E1D693CF0A60A2CF6E0145C4499804EC~YAAQres/F4nSv56YAQAAxzhXohwkR84GzAof2P2zxzEnpdWbcVCHngaDvTfjuwTKuTouEAYZp1a/PpuhDTVVzHUvbbLv21lViFGKPtVTDr5JWgIQiu1cQ836goHV//0jXuyy0LTCMcQT3GMohMuKkywH4AqHZDepSFJJV26zCCQzsORDsNYcnLq0xJnM8VT3zuYT0Ef4GHV+MIdcvksyiHerwEAincR5mtwFq9U9kW33C/5qAhwCeB/gnAIoPJoVUSWD3yu87Bg+Pj9jeEzoBqLBTLLZiddnw49sIiQfpcwbTJWLd4b0t22PcAckj/0Ez+UJVJJSbxZvqRblZhABF14N5nxzVskb77JPQkc=~1; bm_sv=84E138F19C9D78AFFE457B3D7BDEE6A3~YAAQres/F0LUv56YAQAA+FlXohwDfY1cogzmIXCZ7NCgS5QNKnYep065MvqI3/R+fE1wX5E4uGX0EkIb+YhB9Oa+dfcaA/h5hWF6wPxYKpJwL/gnjg5aDO963LczY93AjgTLVXH+Wci2V62XZJ5psuppghUE9nY9QRtcKnJl9MP3MLVBMXA+HMT5c6XnYjlQUsgPYWbTgUaedp5viG3BWEk9ADt90Vk7UM6ekiA4K0nnYixdDOqxzK4k+rPR7AHqOdcd4A==~1; ak_bmsc=03A2A8AC610A620A1054B4246484AB43~000000000000000000000000000000~YAAQres/Fz/Pwp6YAQAAWvybohwT9NkodwkHuEPDPFOUVXXCb98fP/U22CnkhC1y3MAqhALzZhtuccbdG3iGMUAFgeqqcn/+0cGtPfNfWYnI4FSRRa9gjOSChJXxn1KNrJDOwLS+ENs1sbZYA6QZ97gTjiI56DylK13czrwauG0VjpSVcrN5TOW8oQns/s156P1cFfK1QKycHuZ6TeuvPJ6J5HwuxELuxNDQvJGAvzy/RiSbBXpOIgKGyr3AJZ+wEHVR7ZnLZwQKlNCN6xYW9yzcRdndrpivxY6VU6Ly/N+8vmf2WgNfg8r/z52nIsh64oED8idjCbXyd/jfmDrNLR1qhccW4xy/9/AbR1xT0RolqspEyh82bnOQAUQRljcB+mvnVVTV8516z1ozswwTp3Qu/FnhDDEsA786817OKlRszQXVs24fUXm5Hk3I2Tvd9nG4GCXO/GnG+k5JgKa1HXE=; _abck=59D7DD48E6A90EEB131BA027556B192D~0~YAAQres/F03Pwp6YAQAAq/6bog4F+ryXNt82eaTxlufYSJZfRZTaT8Jvep+L9Vi9cBk5Yc36+V51UFSMWddAiX/VLTfNd2So13r8lvqG1SyctpR9tUlagQRE0LOlCZ2144aX/f/8mCsLcpxh+wy5PvxXHyxi2LXjUCyXM2lFzRIXXiPP6Ga+5ynOzOhZc87nG1+il5UF+AYhCma9U8/UbyFn8e2RJnCUbDDbUbY+cBGvxcwSv+cx3ff9TaDztrObAcqTAYJvGuz4BF2wARTjHADGi0NszhSVK1GJ23oTFPruledreJyvV3h1k9PGLyOXJIdgIYpiYT4rYe6fIVtbUYauTja9OMbGSgwM3avIG9xL0c1Qz+de1P1CkQCb25KENG6Gr6AwmvemdCo8+ArIbuS9vha0cWoVywGKH09+VScoP2RiFHJm+nbAv2Znv+3ib3XB/RE1p0YBUQ0A3zoMsLEb/rnY/3Pq64BUVAz7DcDpXvrggLzu+tq+7q+11lT4eiPh/3VdXxDG41jfJGS79B2Ev0VM5dDfEUfdFKUpl6UM4h6No4TLBgFvbQVjFZDaKwmsr1r7JAbRFIqWcgVBIUvU09ePKp6HsLQI4LVh+wqQaCdvX3TP28vrvYeN6VOLhkIA+cjyCIx1gNLvM9450rUh2pshMWJuE22NyNB2pB5P3BNDzzx3kcJwvOS7Pe/6KnM/NyQcOUWCPSreZku9Ds44GlQv+IzhlU2zw/GV0Bt4vNHuJp0SdAORUXpC3W65F+xPTG+Gnb/N4Dg25b6TNpc9xnUzsONdIy01iDDIvmXBHh6EpfLXbdR10nXM6lrAL02Stuph4/TN9fqyXZFTqTRD7Ji1H0+6rz5Pxb/CXp8BIHcH2F30bsD7abhV/NEvFeyWRgSBYNj2l8hoWF8=~-1~-1~1755077036; tfc-l=%7B%22k%22%3A%7B%22v%22%3A%22idap4hda1kcsh55m486ug1sph9%22%2C%22e%22%3A1815027743%7D%2C%22a%22%3A%7B%22v%22%3A%22e834e722-1ae3-4423-8462-beb5cf955776%22%2C%22e%22%3A1753181187%7D%2C%22c%22%3A%7B%22v%22%3A%22adult%22%2C%22e%22%3A1815027743%7D%7D; bm_sz=A49F6DF10EC9D549032FCF542D21C4FA~YAAQres/F4XRwp6YAQAAz0icohz6XWrhdQO/9QpWtvkiKrgjCSQa/LIuE5VrTRfy3wK+lNGHvzXYjRXJ9Jzg7t2YH8eI6NtV5mkwAn/9R3cfykHvlwX/rSH/WBnPtXts40PfYAz4iVvNZwqUoV0jk5Kn4CE07rpv5ydg1xjXRytZ9j5lADoD8NnYxt0OVotO1mgvsDZOvmItbeXzRRb9JIm6Y7Ue4JweZsw9hGaReoWOJvi5vclZuQopt4yVrCzNYqCCdinrkdYi41I9uW6FeQMwk8OGXZlycJeftD75NhbO6BsKmz3TcCoLnJir/NqLlCIS2LUxCU6JN32lnvN9V3eHX7dWYHm+iSrWhpaBIptIURHJRLqJzetPA/BvAlwrGunkRCuEx5fP0CfXs1Cy7tRXbqy8OhfFMFKJXaYHQ1gFXCkkqZK31pWansegwg==~4600118~3687729; OptanonConsent=isGpcEnabled=0&datestamp=2025-08-13T08%3A46%3A51.694Z&version=202507.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=62bc537c-d2bd-4c0f-b103-826359a79cf2&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=TAB01%3A1%2CC0004%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CTAB02%3A1&AwaitingReconsent=false',
}

json_data = {
    "query": '''
        query GetPdpDataById(
          $id: String!
          $category: String! = ""
          $unifiedId: String! = ""
          $locale: String
        ) {
          productDetailPage(
            id: $id
            category: $category
            unifiedId: $unifiedId
            locale: $locale
          ) {
            productSummary {
              productId
              displayName
              parentCategoryUnifiedId
              activity
              gender
              productCategory
            }
          }
        }
    ''',
    "variables": {
        "id": product_code,
        "category": "",
        "unifiedId": "",
        "locale": "en-us"
    }
}

response = requests.post('https://shop.lululemon.com/cne/graphql', cookies=cookies, headers=headers, json=json_data)

print(f"Status Code: {response.status_code}")

with open(f"pdp_response.json", "w", encoding="utf-8") as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=2)
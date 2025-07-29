import requests
import json

# Variables
filename = "casual"
page_size = 800
page_number = 1
referer_url = 'https://shop.lululemon.com/c/women-casual-clothes/n14uwkzyk1r'

cookies = {
    'sat_track': 'true',
    'kameleoonVisitorCode': 'u5ptp1dixct1dznw',
    'UsrLocale': 'en_US',
    'sl': 'US',
    'ajs_anonymous_id': '4550986a-4bd2-40fb-a86f-7e4d3758b793',
    'mbox': 'session#1751615548944_88fec9e8-505c-46ef-a437-bd76f925606d#|PC#1751615548944_88fec9e8-505c-46ef-a437-bd76f925606d.35_0#',
    'a1ashgd': 'iq0v750eo9l00000iq0v750eo9l00000',
    'QuantumMetricUserID': '4b357c9663bdc53c0b76deccd935be5f',
    'lll_edge_geo_data': 'city=DUBAI&state=&zip=&country=AE&lat=25.25&long=55.28',
    'lll-ecom-correlation-id': 'D31F4E41-AE72-AC4E-F257-FE759B43315A',
    'AMCVS_A92B3BC75245B1030A490D4D%40AdobeOrg': '1',
    'AMCV_A92B3BC75245B1030A490D4D%40AdobeOrg': '179643557%7CMCIDTS%7C20299%7CMCMID%7C81339717232275361390196317311145638224%7CMCAAMLH-1754417130%7C6%7CMCAAMB-1754417130%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1753819530s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0',
    'ak_bmsc': '2482888F3C3C18B21D8278A04B4B889A~000000000000000000000000000000~YAAQTPttaBD+0lSYAQAA5mlcVxyzSdVZGPsm+30WNzBpp4YgVcZeQ5VQQS9bHuGufsmBdPN07N/U6jtL1butpjWViunXtzK12eQ5g3UHYY+OsIlXaPmG5ZqHiwiOJ1WeX4Xf5toq2ZfJ4Rggc+gKDtHB17+beMTKwHcH2Y/t4dfLQbQPVeBtDuIeexVuT3Rp+pYfV5FkzSQz1pxGNDcmxANkproGlL3EfGGdnJ/3jjoM2M9J4tCRUQSi17/6E6eLBHIKp2EdzaCKGLAc3eCi6TrtpjDMkCfIJZJ9c/vKog1t3trgSQvPdSTPoIP+ko9BWLRPrN9EZJtf5S4EIXFzHDXE73FhNxLH+NxJurGt+e3i0watx9+iTzopAT/Z06HhIqUosQTpZlyJV3G2p3kUXE1HL04LhnTXcpsXdX0C9ZCOytmIjR9FeAXZnqgMBxkRi/CCBzPV',
    'akaalb_Shop_ALB_instance1': '~op=shop_mwa_shared:mwa-shared-usw-2|shop_upperfunnel_static:shop-upperfunnel-1|~rv=49~m=mwa-shared-usw-2:0|shop-upperfunnel-1:0|~os=3ad3acca926c302b084e12bf3b209756~id=dd29b6ce2b1385fefb48dbdbf7131af6',
    's_cc': 'true',
    'ek8_guest': 'true',
    'pers_seg': 'eyJnZW5kZXJBZmZpbml0eSI6ImFsbCJ9',
    'apigeeToken': 'eyJqa3UiOiJodHRwczpcL1wvcHJvZC5hcGlzLmxsbGV4dC5jb21cL2FwaW1cL3YxXC9qd3R2ZXJpZmljYXRpb25cL2p3a3MiLCJraWQiOiJyc2FfXzNkbmdqZWJ1YjBudm9ib2Z0MCIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJyb2xlIjoiZ3Vlc3QiLCJpc3MiOiJodHRwczpcL1wvcHJvZC5hcGlzLmxsbGV4dC5jb21cL2p3dFwvdjEiLCJJRCI6InhWR1NVZXVndm9nUHRnaUprYmo4aUY3U2FjYW5WSUE5IiwiVVVJRCI6IjI4MmU3MjU4LTRiODctNDFjMS05ZjZiLTQ0ZGUxM2NmNTVlZCIsImV4cCI6MTc1MzgxNTkzNSwiaWF0IjoxNzUzODEyMzM1LCJqdGkiOiIxNmZjY2E1My0zYmYyLTQ2NDUtODYzMS02ZjY0ZjkyZTFmYjYifQ.52kq3cW6p8ZWWVZXFOxc0E0l-R6-rGxCEOCadOXg-Q1hmoiPImk3TiSQQagnsdmO6_Oo9J4e6xVjfZflwOFWhzpfR7NTylUKrzTH-Fq9tE4i8DQrboFoSrTJutdl38_qFBruvrU1uwqVoLR0d7XZxcAEv3ohvIfmVYvl5nVAZTfdf6Q9P8MDn0IrMe8cvVK_KmCUuUGFkvmTnHv12ydjS53YCbk8Mj1ZaKvyi_m1YI_FUgTcka9zOldM0QiOHvMoz8-S8kUD3GlrWXLBKxPa6oYahQCxes0RKLCJoF-gL5epPZ9Ehw4GRbcstVY2n7Qu4OU9-0p34Zd6FmeI1fb-6A',
    'digitalData.page.a1Token': '$2a$10$d2R2J7iv0M0TCIt.fKdh/eqGi42BoBEQGrEE1ggGI67ENWqzt52TW',
    'QuantumMetricSessionID': '089eda84711664d27ff7084035b00c65',
    'mboxEdgeCluster': '35',
    'lll_adobe_geo_postal_zip': '0',
    'bm_sz': '893E6A88151FEE62503AA1012D84F041~YAAQTPttaPIB01SYAQAAzfBeVxz+qoWqJ4LJbuP67sHPxEFldzB/WHP8RjdNFWYrUqRRoP45tIPT3vjnmQfms87Z6z1NEWtoJT70JKjJD0rkmVdzSVz9RNMoK5550JNaVQh0QetlM0+WEvtAPAh2Z2AdZX2oVBal9dYsQ4n9BKaganb7GFIxZvD/Tg5UYHkT8YhQiQIz9rTlcYszKXnxLQY3eDhl1mugCoOYtl/OD0f7VyVsQgoTLIEVY/HH01ZfuwhgcVjs6pTU19DFlIYPMDHlyW5sueWSZi7WWhrKRYz5984NfU2P4esY2WqLRSSeW5kkgSpCdw3rsXhwvPDQT+iZqugnXHiWlWdbYD3Gtku6RozOHGIvKCyH7KDKiLk/c9yi9WKG3gcyqFwuqaqHJzIir2MSyw==~4273204~3290435',
    '_abck': '3E067681BFFA618590FE066AD0AD904B~0~YAAQTPttaPUB01SYAQAAf/FeVw6CjggmmXufmWaUzALw/8X+akacfiAoElOlAw1qNZLOh7L/lf/WmzfnuAKkJOFk8eJzcH/r/7WrLKq3ZNFheqX3MGVSgt+WKrjjdAa9UDE0PMr594dj/Y/Lgga7c6WjfVsCJ4kQrCXkjIMw2rLyGc9fGwLai6X5UWTHhjm8u4i9fbl8/NwOipSqIVN2Y+g1FDVYlxIT/fwpXvHiPdfgOyJTgfpGdhDqHrxhEjVqhd3grMCrSx3cdJX3xCwx6sG6MOjxxIk3k3pxJLs8N3fbAuYlH9f3CeLjudEl9nFxM9bE9xHa+9Vcmydp1K56620i60hJLOHCzuCcY1zHOwk0NVsyEhhTPo1FW8yUsakxFtC4OWO9/cGX5Bz/Lx+r4c5hFWtA2yeXpNa467R2+j5up9A7Do/a81O+dWdvdEntX9d0MBRO/E6ic5lS1R53sNqdDdAcBSNIYszAf2RpmGvo0qKaawn4Rqt0h2D2BTnAMFWS5FDhV2fbB0ANPGoXEJt7tr03mCItkJvYpnssR+lIFT3/Q2GpKBoq/mluxhO9zzy+LvxyptOLhh//YtciLah9wB98FApcyGSasMX74y9tx3kY5TFvvJTf0lWHtjqyWQwHdfKBAwwScM4w7bUCsfZTh8y+dKk=~-1~-1~1753815930',
    'lll_adobe_geo_city': 'Dubai',
    'lll_adobe_geo_country': 'United%20Arab%20Emirates',
    'lll_adobe_geo_latitude': '25.10190',
    'lll_adobe_geo_longitude': '55.17120',
    'lll_adobe_geo_state': 'Dubai',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=2025-07-29T18%3A08%3A18.078Z&version=202505.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=658f76fc-ac02-4d91-9e39-877a9c37228c&interactionCount=0&isAnonUser=1&landingPath=NotLandingPage&groups=TAB01%3A0%2CC0004%3A0%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CTAB02%3A1&AwaitingReconsent=false',
    's_sq': '%5B%5BB%5D%5D',
    'bm_sv': 'C3BC2CC03EA92337F1A5AACFE3A9C749~YAAQTPttaBwC01SYAQAAcfxeVxyUt3VSU6pBxzCQjnq1Ilfl94Sc/leW1VsCLwbEU8nwXCJBuWL3pa31S6wt/UlDmLgMUYQxJZLndQPkkiK6x6bftylIS+mw9sqkAN6PZNU1MV1dedsl+67B8KbbpyQUwXVy8kEzhZqt/zYBfSfycDmOcGCZqOV/nqu4WtOq0OAZ8Fgcp0pNedeU9SNyLDWnsu8/EhjV4mmWbZbsfDIkRD8GQOcaeHzrCQ/Us2awqGs43w==~1',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://shop.lululemon.com',
    'priority': 'u=1, i',
    'referer': referer_url,
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'aa9aaec06a2046bda08499e7ad692c76',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'x-lll-client': 'cdp-api',
    # 'cookie': 'sat_track=true; kameleoonVisitorCode=u5ptp1dixct1dznw; UsrLocale=en_US; sl=US; ajs_anonymous_id=4550986a-4bd2-40fb-a86f-7e4d3758b793; mbox=session#1751615548944_88fec9e8-505c-46ef-a437-bd76f925606d#|PC#1751615548944_88fec9e8-505c-46ef-a437-bd76f925606d.35_0#; a1ashgd=iq0v750eo9l00000iq0v750eo9l00000; QuantumMetricUserID=4b357c9663bdc53c0b76deccd935be5f; lll_edge_geo_data=city=DUBAI&state=&zip=&country=AE&lat=25.25&long=55.28; lll-ecom-correlation-id=D31F4E41-AE72-AC4E-F257-FE759B43315A; AMCVS_A92B3BC75245B1030A490D4D%40AdobeOrg=1; AMCV_A92B3BC75245B1030A490D4D%40AdobeOrg=179643557%7CMCIDTS%7C20299%7CMCMID%7C81339717232275361390196317311145638224%7CMCAAMLH-1754417130%7C6%7CMCAAMB-1754417130%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1753819530s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; ak_bmsc=2482888F3C3C18B21D8278A04B4B889A~000000000000000000000000000000~YAAQTPttaBD+0lSYAQAA5mlcVxyzSdVZGPsm+30WNzBpp4YgVcZeQ5VQQS9bHuGufsmBdPN07N/U6jtL1butpjWViunXtzK12eQ5g3UHYY+OsIlXaPmG5ZqHiwiOJ1WeX4Xf5toq2ZfJ4Rggc+gKDtHB17+beMTKwHcH2Y/t4dfLQbQPVeBtDuIeexVuT3Rp+pYfV5FkzSQz1pxGNDcmxANkproGlL3EfGGdnJ/3jjoM2M9J4tCRUQSi17/6E6eLBHIKp2EdzaCKGLAc3eCi6TrtpjDMkCfIJZJ9c/vKog1t3trgSQvPdSTPoIP+ko9BWLRPrN9EZJtf5S4EIXFzHDXE73FhNxLH+NxJurGt+e3i0watx9+iTzopAT/Z06HhIqUosQTpZlyJV3G2p3kUXE1HL04LhnTXcpsXdX0C9ZCOytmIjR9FeAXZnqgMBxkRi/CCBzPV; akaalb_Shop_ALB_instance1=~op=shop_mwa_shared:mwa-shared-usw-2|shop_upperfunnel_static:shop-upperfunnel-1|~rv=49~m=mwa-shared-usw-2:0|shop-upperfunnel-1:0|~os=3ad3acca926c302b084e12bf3b209756~id=dd29b6ce2b1385fefb48dbdbf7131af6; s_cc=true; ek8_guest=true; pers_seg=eyJnZW5kZXJBZmZpbml0eSI6ImFsbCJ9; apigeeToken=eyJqa3UiOiJodHRwczpcL1wvcHJvZC5hcGlzLmxsbGV4dC5jb21cL2FwaW1cL3YxXC9qd3R2ZXJpZmljYXRpb25cL2p3a3MiLCJraWQiOiJyc2FfXzNkbmdqZWJ1YjBudm9ib2Z0MCIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJyb2xlIjoiZ3Vlc3QiLCJpc3MiOiJodHRwczpcL1wvcHJvZC5hcGlzLmxsbGV4dC5jb21cL2p3dFwvdjEiLCJJRCI6InhWR1NVZXVndm9nUHRnaUprYmo4aUY3U2FjYW5WSUE5IiwiVVVJRCI6IjI4MmU3MjU4LTRiODctNDFjMS05ZjZiLTQ0ZGUxM2NmNTVlZCIsImV4cCI6MTc1MzgxNTkzNSwiaWF0IjoxNzUzODEyMzM1LCJqdGkiOiIxNmZjY2E1My0zYmYyLTQ2NDUtODYzMS02ZjY0ZjkyZTFmYjYifQ.52kq3cW6p8ZWWVZXFOxc0E0l-R6-rGxCEOCadOXg-Q1hmoiPImk3TiSQQagnsdmO6_Oo9J4e6xVjfZflwOFWhzpfR7NTylUKrzTH-Fq9tE4i8DQrboFoSrTJutdl38_qFBruvrU1uwqVoLR0d7XZxcAEv3ohvIfmVYvl5nVAZTfdf6Q9P8MDn0IrMe8cvVK_KmCUuUGFkvmTnHv12ydjS53YCbk8Mj1ZaKvyi_m1YI_FUgTcka9zOldM0QiOHvMoz8-S8kUD3GlrWXLBKxPa6oYahQCxes0RKLCJoF-gL5epPZ9Ehw4GRbcstVY2n7Qu4OU9-0p34Zd6FmeI1fb-6A; digitalData.page.a1Token=$2a$10$d2R2J7iv0M0TCIt.fKdh/eqGi42BoBEQGrEE1ggGI67ENWqzt52TW; QuantumMetricSessionID=089eda84711664d27ff7084035b00c65; mboxEdgeCluster=35; lll_adobe_geo_postal_zip=0; bm_sz=893E6A88151FEE62503AA1012D84F041~YAAQTPttaPIB01SYAQAAzfBeVxz+qoWqJ4LJbuP67sHPxEFldzB/WHP8RjdNFWYrUqRRoP45tIPT3vjnmQfms87Z6z1NEWtoJT70JKjJD0rkmVdzSVz9RNMoK5550JNaVQh0QetlM0+WEvtAPAh2Z2AdZX2oVBal9dYsQ4n9BKaganb7GFIxZvD/Tg5UYHkT8YhQiQIz9rTlcYszKXnxLQY3eDhl1mugCoOYtl/OD0f7VyVsQgoTLIEVY/HH01ZfuwhgcVjs6pTU19DFlIYPMDHlyW5sueWSZi7WWhrKRYz5984NfU2P4esY2WqLRSSeW5kkgSpCdw3rsXhwvPDQT+iZqugnXHiWlWdbYD3Gtku6RozOHGIvKCyH7KDKiLk/c9yi9WKG3gcyqFwuqaqHJzIir2MSyw==~4273204~3290435; _abck=3E067681BFFA618590FE066AD0AD904B~0~YAAQTPttaPUB01SYAQAAf/FeVw6CjggmmXufmWaUzALw/8X+akacfiAoElOlAw1qNZLOh7L/lf/WmzfnuAKkJOFk8eJzcH/r/7WrLKq3ZNFheqX3MGVSgt+WKrjjdAa9UDE0PMr594dj/Y/Lgga7c6WjfVsCJ4kQrCXkjIMw2rLyGc9fGwLai6X5UWTHhjm8u4i9fbl8/NwOipSqIVN2Y+g1FDVYlxIT/fwpXvHiPdfgOyJTgfpGdhDqHrxhEjVqhd3grMCrSx3cdJX3xCwx6sG6MOjxxIk3k3pxJLs8N3fbAuYlH9f3CeLjudEl9nFxM9bE9xHa+9Vcmydp1K56620i60hJLOHCzuCcY1zHOwk0NVsyEhhTPo1FW8yUsakxFtC4OWO9/cGX5Bz/Lx+r4c5hFWtA2yeXpNa467R2+j5up9A7Do/a81O+dWdvdEntX9d0MBRO/E6ic5lS1R53sNqdDdAcBSNIYszAf2RpmGvo0qKaawn4Rqt0h2D2BTnAMFWS5FDhV2fbB0ANPGoXEJt7tr03mCItkJvYpnssR+lIFT3/Q2GpKBoq/mluxhO9zzy+LvxyptOLhh//YtciLah9wB98FApcyGSasMX74y9tx3kY5TFvvJTf0lWHtjqyWQwHdfKBAwwScM4w7bUCsfZTh8y+dKk=~-1~-1~1753815930; lll_adobe_geo_city=Dubai; lll_adobe_geo_country=United%20Arab%20Emirates; lll_adobe_geo_latitude=25.10190; lll_adobe_geo_longitude=55.17120; lll_adobe_geo_state=Dubai; OptanonConsent=isGpcEnabled=0&datestamp=2025-07-29T18%3A08%3A18.078Z&version=202505.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=658f76fc-ac02-4d91-9e39-877a9c37228c&interactionCount=0&isAnonUser=1&landingPath=NotLandingPage&groups=TAB01%3A0%2CC0004%3A0%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CTAB02%3A1&AwaitingReconsent=false; s_sq=%5B%5BB%5D%5D; bm_sv=C3BC2CC03EA92337F1A5AACFE3A9C749~YAAQTPttaBwC01SYAQAAcfxeVxyUt3VSU6pBxzCQjnq1Ilfl94Sc/leW1VsCLwbEU8nwXCJBuWL3pa31S6wt/UlDmLgMUYQxJZLndQPkkiK6x6bftylIS+mw9sqkAN6PZNU1MV1dedsl+67B8KbbpyQUwXVy8kEzhZqt/zYBfSfycDmOcGCZqOV/nqu4WtOq0OAZ8Fgcp0pNedeU9SNyLDWnsu8/EhjV4mmWbZbsfDIkRD8GQOcaeHzrCQ/Us2awqGs43w==~1',
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
        'category': 'women-casual-clothes',
        'cdpHash': 'n14uwkzyk1r',
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

# Make request
response = requests.post('https://shop.lululemon.com/snb/graphql', cookies=cookies, headers=headers, json=json_data)

print(f"Status Code: {response.status_code}")

# Save full JSON response
with open(f"{filename}_response.json", 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=2)

import pandas as pd

# Extract product IDs
product_ids = [p['productId'] for p in response.json()['data']['categoryPageData']['products']]

# Convert to DataFrame
df = pd.DataFrame(product_ids, columns=['productId'])

# Save to Excel
df.to_excel(f"{filename}_product_ids.xlsx", index=False)
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
    'akaalb_Shop_ALB_instance1': '~op=shop_mwa_shared:mwa-shared-usw-2|shop_upperfunnel_static:shop-upperfunnel-1|~rv=49~m=mwa-shared-usw-2:0|shop-upperfunnel-1:0|~os=3ad3acca926c302b084e12bf3b209756~id=dd29b6ce2b1385fefb48dbdbf7131af6',
    's_cc': 'true',
    'ek8_guest': 'true',
    'pers_seg': 'eyJnZW5kZXJBZmZpbml0eSI6ImFsbCJ9',
    'digitalData.page.a1Token': '$2a$10$d2R2J7iv0M0TCIt.fKdh/eqGi42BoBEQGrEE1ggGI67ENWqzt52TW',
    'mboxEdgeCluster': '35',
    'lll_adobe_geo_postal_zip': '0',
    'tfc-l': '%7B%22k%22%3A%7B%22v%22%3A%22h520eu3g0jb9i5fval966582d7%22%2C%22e%22%3A1816714956%7D%7D',
    'QuantumMetricSessionID': '400c1878c164a4ef8f1ecebaedd087c9',
    'apigeeToken': 'eyJqa3UiOiJodHRwczpcL1wvcHJvZC5hcGlzLmxsbGV4dC5jb21cL2FwaW1cL3YxXC9qd3R2ZXJpZmljYXRpb25cL2p3a3MiLCJraWQiOiJyc2FfXzNkbmdqZWJ1YjBudm9ib2Z0MCIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJyb2xlIjoiZ3Vlc3QiLCJpc3MiOiJodHRwczpcL1wvcHJvZC5hcGlzLmxsbGV4dC5jb21cL2p3dFwvdjEiLCJJRCI6InhWR1NVZXVndm9nUHRnaUprYmo4aUY3U2FjYW5WSUE5IiwiVVVJRCI6IjI4MmU3MjU4LTRiODctNDFjMS05ZjZiLTQ0ZGUxM2NmNTVlZCIsImV4cCI6MTc1MzgyMjM3NCwiaWF0IjoxNzUzODE4Nzc0LCJqdGkiOiJiNjVkZWI1Mi1iZGViLTQ4NDItOTY2NC0xYjYxNjEyNmJjMzUifQ.lWAusScsFOoW13pWLylLe_pNk6W7YISk2vioxGuaDLTnLGNIiIxIn6Mq6QCIZaDOG0pOVX-t5i9Yn7PykXTLZ14op48uYHXG8mn4RQpv9w42tfggfr4c-YbiSmynEvcnCLTrWn3RsZA_myl3XZsd31pQbtxj7LVYkOKqYm7W2VCMJQ3o4oOF0O78DZKe-5WxuCjGo1s195FjYxHToOL2J3z4DXvjTTpKLEUT7CyIZMkcXTa2PDQIbro1C6ZBB0qAT_dLg-RM8tYQ66KfOB0ZEvHViJrU7qQbRvOOWZJK4-iaNbFDvxvpCNGW0XdP-Ttp_Num_IB0WrjMzcgeZaFQDA',
    '_abck': '3E067681BFFA618590FE066AD0AD904B~0~YAAQPfttaPi0r1WYAQAACqbJVw4+lNIh/Tq63sGSFstJk362ovVls1lDMnUPEy8Kyn9CMNM7Tx5hEW+ErjZajqrqBgf3/41WN4U95MCwdHN47o8I6Thdwr4m6A+HL+Bo3OWSkc8Ir7elu8DvpEA5hl6uGiKoBLnlmLvDfnj/27javOqziWPQJsnI2Rl4JTExL8bTcKEXOviqRNSFyxQtpw5AO4N3tSh6nIJCQSaesC56/rP0kV/eDF3/Dq7xcckh+1sXL6h62zBe7tJUiJ5xTPdLNdUfz95ZJJVENVAJFHnwHv1xEpAhnBG2OznqWZK9yUheN7j2LTFgWSXq+oqGoOFXMgShRxh+kbtlPCD5ST5OiUWd3fa/Sd3T/fhmbxLi5reZXo5c4np1UmKVsfUXIBSwQwiOwuN8kpkkinEAxXuQRcPCcRjv/qnuRZaKml3wDNQYwv3X2SqR65ufbn2t8WPIxlJOgCS0Kiu6K8ZkipKCV/dB0n0voiMwchOpWUp7NC0sZCo8//WrM6QZ304RvC5X1dbP3hkaB7bla8VTn6f9JI/ZaGJR/urLfl4/TNx1qwquVumJcbc/89DdOmIvYb6c81PsUdi6qV52emH0aisMNULn2ymvr9v8zzRtoXJ6+GrPyFLmZNDRKsmpBQyq8AJe7qROYwnwntTVdQqx542PHGGNasC856A97kzZvUHk1vjIZw44RcuGo3tX4qdNyW2RJuTA02I8gWmm~-1~-1~1753823075',
    'BVBRANDID': '645e135e-3898-4b0a-b90d-af9811ce9496',
    'bm_mi': '4A6084860583CFE87F248C7A2E1E55BB~YAAQPfttaNy4r1WYAQAAv/7KVxwCta5uxRi6pBaXij1gUVU+zkGCDmKSaTUEQD9Tz5D/3r4gLvhVIReniZdXJNOb9GfSbEKzgW6GmF36IU5XwhF2Z8ClRMhhWF02FD4JJxpqS2CBTCRtW6Y7EEqf106rJaMRWuQetS7LwLGquJlHPVFezW3gLyfiwfgpqhGLV78UPOPmIwSMSzWSbBfNyQaeOg3/bYFsqbUefCCDVHy1akFRP6EBD7eigeQk0wDOeYOH/DJbM1VUJ4Oh9E2CBRbg+AwbSDCpahnb4wKBIY8Gq0qxt87vOswul1lyl1Ffrbh6f1IdAF6qbFteDUv6eQk5SEbsB/oBd4WA41lu/MFmAlkOvG2eQ59EHblAxjR8PJ4C0KRpASmW/th9/YGhXGtD+pMENvc=~1',
    'ak_bmsc': 'A2BB845ED95150F1387F486B5D51680F~000000000000000000000000000000~YAAQPfttaBK5r1WYAQAA8xbLVxx5gao/HBjbt19OIT7XWfR+p9ckl6l8ZatHXTUQDQaH7MYtqEL9bgZn63crFNIcREIi2stOUMkMQs2HBXpmSSBzU3G/tRKu6TLhPDDR4pTCJbODdJbvwyzH4yc9rXGe8FEUBCMjMBYFW5sIdfv5TEgZFnAY2q9sOQyAbppDQryLgZuMgOyL2QPDao41wrj/yqDzNUez7P9ZcYQClnDJ1FC7GdnQFu6Hci5hKWqWAN//qAlT/91iBVQS735dykRPax6X8tiwh5XDUSfeAZ0VRAjXP+Z17SsGbjZBsupuznAS4LU+ly5Pl4iMN+DbkErHx0NeahJzAzFcbX8Vuz6GWI6ic+QzsGBkRnFDcqlH1TpKTTyS6+EYlGKSIT1UYxelQ9we1o7r1lzqEZvQ4Dw8qz7OFjt0kZIpcZcSHTwnHXUTFtUf1E+e8PaVdS4VYg38cLOEgwcSzneFs5cqpTxReHmwBN1FdLdNuEuVxi1yOijSojRwQOPL4rMaaYSkHSH3GGlNgfeIkYBgpo6EFT4vsu0XrzCE2n4ZQm8D67k=',
    'AMCV_A92B3BC75245B1030A490D4D%40AdobeOrg': '179643557%7CMCIDTS%7C20299%7CMCMID%7C81339717232275361390196317311145638224%7CMCAAMLH-1754424392%7C6%7CMCAAMB-1754424392%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1753826792s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0',
    'bm_sz': '893E6A88151FEE62503AA1012D84F041~YAAQTPttaO7D01SYAQAAUBHXVxysqUlYmvHtt2KOjHdJZ7kY6s3s9p+IDQqO6WlYLp7ccm7y3Lr7QVFDBfG5weMjIUNZpI2wEAUzvKSw6VLgNWqGgZZbQP/ZEZoJV/FkAaBojyu7hoKTb32r0K1KlWVL3tO5ytT1CAjyaccOziV2GSU1/nYxWP7ypGrYq7ngWd0FGwjYhnTdD+mT3CIrHWctW2Zak3Ct/4VNVRP9O990sWHFOUrSuk2Y0RaIMGGDTxo1dQvN6FbPXOxaf8Pljn8ZRHxi7tBTa7pRL+QtF8ajFTyUX8Da+ssRofoqAK2KqWtsPLM6oVK4Xx8LL/5i6JlSh2u6hFAaEHnVAL7yxrAM/COMbxFYZfHKKjrCIMkfT/F7MMOIMUZMgI4cKbZyyQWXORWTB98hjVPeed+q7HL6pON+ETt+y5BIpB3ErPMEVWDZbrfq2X9SJQg1WigNbsTR5Uj5T0LZ6uZyioH35I2GAjM2dVigFV4YCm8=~4273204~3290435',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=2025-07-29T20%3A19%3A32.185Z&version=202505.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=658f76fc-ac02-4d91-9e39-877a9c37228c&interactionCount=0&isAnonUser=1&landingPath=NotLandingPage&groups=TAB01%3A0%2CC0004%3A0%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CTAB02%3A1&AwaitingReconsent=false',
    'lll_adobe_geo_country': 'united%20arab%20emirates',
    'lll_adobe_geo_state': 'dubai',
    'lll_adobe_geo_city': 'dubai',
    'lll_adobe_geo_latitude': '25.1019',
    'lll_adobe_geo_longitude': '55.1712',
    'bm_sv': 'D395AD25BB3AB3E2B99DABDDAF0BE6E2~YAAQPfttaBT8r1WYAQAAcBX6Vxy8SaYTtv8lQ3EZBRRCHZYb+8PeDe3+MH/zK5GREVzajKXeaKQfgPG46kRBe2NtRzpCfppKXK94HESw/sLgW+EguDWLYZasTuvt9TclWW1orjn2F7aoIegFXVIsV7+uyXUvk1h0Y/QJBI9FSMEbvo7hcBGcOF13Uot1Gkr8cKzhXCk0W+S8serTcXpKku23DiLdI5EUNw/bUmZ49PIy9TofvZTWz7SSLz/ee+8kKHzQIw==~1',
    's_sq': 'llmnprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dcdp%25253Awomens-back-to-school%2526link%253DView%252520details%252520of%252520Nulu%252520Cropped%252520Short-Sleeve%252520Shirt%252520Retro%252520Remix%252520Set%2526region%253Dproduct-list%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dcdp%25253Awomens-back-to-school%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fshop.lululemon.com%25252Fp%25252Ftops-short-sleeve%25252FNulu-Cropped-Short-Sleeve-Shirt-Retro-Remix-Set%25252F_%25252Fpro%2526ot%253DA',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://shop.lululemon.com',
    'priority': 'u=1, i',
    'referer': 'https://shop.lululemon.com',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '388391b19eff4687a70934725f225a31',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'x-lll-client': 'product-sdk',
    'x-lll-ecom-correlation-id': 'nonprod',
    'x-lll-referrer': 'Channel=Web,Page=pdp',
    'x-lll-request-correlation-id': 'ba8491cf-a5ef-4c31-aa34-285e551b60be',
    # 'cookie': 'sat_track=true; kameleoonVisitorCode=u5ptp1dixct1dznw; UsrLocale=en_US; sl=US; ajs_anonymous_id=4550986a-4bd2-40fb-a86f-7e4d3758b793; mbox=session#1751615548944_88fec9e8-505c-46ef-a437-bd76f925606d#|PC#1751615548944_88fec9e8-505c-46ef-a437-bd76f925606d.35_0#; a1ashgd=iq0v750eo9l00000iq0v750eo9l00000; QuantumMetricUserID=4b357c9663bdc53c0b76deccd935be5f; lll_edge_geo_data=city=DUBAI&state=&zip=&country=AE&lat=25.25&long=55.28; lll-ecom-correlation-id=D31F4E41-AE72-AC4E-F257-FE759B43315A; AMCVS_A92B3BC75245B1030A490D4D%40AdobeOrg=1; akaalb_Shop_ALB_instance1=~op=shop_mwa_shared:mwa-shared-usw-2|shop_upperfunnel_static:shop-upperfunnel-1|~rv=49~m=mwa-shared-usw-2:0|shop-upperfunnel-1:0|~os=3ad3acca926c302b084e12bf3b209756~id=dd29b6ce2b1385fefb48dbdbf7131af6; s_cc=true; ek8_guest=true; pers_seg=eyJnZW5kZXJBZmZpbml0eSI6ImFsbCJ9; digitalData.page.a1Token=$2a$10$d2R2J7iv0M0TCIt.fKdh/eqGi42BoBEQGrEE1ggGI67ENWqzt52TW; mboxEdgeCluster=35; lll_adobe_geo_postal_zip=0; tfc-l=%7B%22k%22%3A%7B%22v%22%3A%22h520eu3g0jb9i5fval966582d7%22%2C%22e%22%3A1816714956%7D%7D; QuantumMetricSessionID=400c1878c164a4ef8f1ecebaedd087c9; apigeeToken=eyJqa3UiOiJodHRwczpcL1wvcHJvZC5hcGlzLmxsbGV4dC5jb21cL2FwaW1cL3YxXC9qd3R2ZXJpZmljYXRpb25cL2p3a3MiLCJraWQiOiJyc2FfXzNkbmdqZWJ1YjBudm9ib2Z0MCIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJyb2xlIjoiZ3Vlc3QiLCJpc3MiOiJodHRwczpcL1wvcHJvZC5hcGlzLmxsbGV4dC5jb21cL2p3dFwvdjEiLCJJRCI6InhWR1NVZXVndm9nUHRnaUprYmo4aUY3U2FjYW5WSUE5IiwiVVVJRCI6IjI4MmU3MjU4LTRiODctNDFjMS05ZjZiLTQ0ZGUxM2NmNTVlZCIsImV4cCI6MTc1MzgyMjM3NCwiaWF0IjoxNzUzODE4Nzc0LCJqdGkiOiJiNjVkZWI1Mi1iZGViLTQ4NDItOTY2NC0xYjYxNjEyNmJjMzUifQ.lWAusScsFOoW13pWLylLe_pNk6W7YISk2vioxGuaDLTnLGNIiIxIn6Mq6QCIZaDOG0pOVX-t5i9Yn7PykXTLZ14op48uYHXG8mn4RQpv9w42tfggfr4c-YbiSmynEvcnCLTrWn3RsZA_myl3XZsd31pQbtxj7LVYkOKqYm7W2VCMJQ3o4oOF0O78DZKe-5WxuCjGo1s195FjYxHToOL2J3z4DXvjTTpKLEUT7CyIZMkcXTa2PDQIbro1C6ZBB0qAT_dLg-RM8tYQ66KfOB0ZEvHViJrU7qQbRvOOWZJK4-iaNbFDvxvpCNGW0XdP-Ttp_Num_IB0WrjMzcgeZaFQDA; _abck=3E067681BFFA618590FE066AD0AD904B~0~YAAQPfttaPi0r1WYAQAACqbJVw4+lNIh/Tq63sGSFstJk362ovVls1lDMnUPEy8Kyn9CMNM7Tx5hEW+ErjZajqrqBgf3/41WN4U95MCwdHN47o8I6Thdwr4m6A+HL+Bo3OWSkc8Ir7elu8DvpEA5hl6uGiKoBLnlmLvDfnj/27javOqziWPQJsnI2Rl4JTExL8bTcKEXOviqRNSFyxQtpw5AO4N3tSh6nIJCQSaesC56/rP0kV/eDF3/Dq7xcckh+1sXL6h62zBe7tJUiJ5xTPdLNdUfz95ZJJVENVAJFHnwHv1xEpAhnBG2OznqWZK9yUheN7j2LTFgWSXq+oqGoOFXMgShRxh+kbtlPCD5ST5OiUWd3fa/Sd3T/fhmbxLi5reZXo5c4np1UmKVsfUXIBSwQwiOwuN8kpkkinEAxXuQRcPCcRjv/qnuRZaKml3wDNQYwv3X2SqR65ufbn2t8WPIxlJOgCS0Kiu6K8ZkipKCV/dB0n0voiMwchOpWUp7NC0sZCo8//WrM6QZ304RvC5X1dbP3hkaB7bla8VTn6f9JI/ZaGJR/urLfl4/TNx1qwquVumJcbc/89DdOmIvYb6c81PsUdi6qV52emH0aisMNULn2ymvr9v8zzRtoXJ6+GrPyFLmZNDRKsmpBQyq8AJe7qROYwnwntTVdQqx542PHGGNasC856A97kzZvUHk1vjIZw44RcuGo3tX4qdNyW2RJuTA02I8gWmm~-1~-1~1753823075; BVBRANDID=645e135e-3898-4b0a-b90d-af9811ce9496; bm_mi=4A6084860583CFE87F248C7A2E1E55BB~YAAQPfttaNy4r1WYAQAAv/7KVxwCta5uxRi6pBaXij1gUVU+zkGCDmKSaTUEQD9Tz5D/3r4gLvhVIReniZdXJNOb9GfSbEKzgW6GmF36IU5XwhF2Z8ClRMhhWF02FD4JJxpqS2CBTCRtW6Y7EEqf106rJaMRWuQetS7LwLGquJlHPVFezW3gLyfiwfgpqhGLV78UPOPmIwSMSzWSbBfNyQaeOg3/bYFsqbUefCCDVHy1akFRP6EBD7eigeQk0wDOeYOH/DJbM1VUJ4Oh9E2CBRbg+AwbSDCpahnb4wKBIY8Gq0qxt87vOswul1lyl1Ffrbh6f1IdAF6qbFteDUv6eQk5SEbsB/oBd4WA41lu/MFmAlkOvG2eQ59EHblAxjR8PJ4C0KRpASmW/th9/YGhXGtD+pMENvc=~1; ak_bmsc=A2BB845ED95150F1387F486B5D51680F~000000000000000000000000000000~YAAQPfttaBK5r1WYAQAA8xbLVxx5gao/HBjbt19OIT7XWfR+p9ckl6l8ZatHXTUQDQaH7MYtqEL9bgZn63crFNIcREIi2stOUMkMQs2HBXpmSSBzU3G/tRKu6TLhPDDR4pTCJbODdJbvwyzH4yc9rXGe8FEUBCMjMBYFW5sIdfv5TEgZFnAY2q9sOQyAbppDQryLgZuMgOyL2QPDao41wrj/yqDzNUez7P9ZcYQClnDJ1FC7GdnQFu6Hci5hKWqWAN//qAlT/91iBVQS735dykRPax6X8tiwh5XDUSfeAZ0VRAjXP+Z17SsGbjZBsupuznAS4LU+ly5Pl4iMN+DbkErHx0NeahJzAzFcbX8Vuz6GWI6ic+QzsGBkRnFDcqlH1TpKTTyS6+EYlGKSIT1UYxelQ9we1o7r1lzqEZvQ4Dw8qz7OFjt0kZIpcZcSHTwnHXUTFtUf1E+e8PaVdS4VYg38cLOEgwcSzneFs5cqpTxReHmwBN1FdLdNuEuVxi1yOijSojRwQOPL4rMaaYSkHSH3GGlNgfeIkYBgpo6EFT4vsu0XrzCE2n4ZQm8D67k=; AMCV_A92B3BC75245B1030A490D4D%40AdobeOrg=179643557%7CMCIDTS%7C20299%7CMCMID%7C81339717232275361390196317311145638224%7CMCAAMLH-1754424392%7C6%7CMCAAMB-1754424392%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1753826792s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; bm_sz=893E6A88151FEE62503AA1012D84F041~YAAQTPttaO7D01SYAQAAUBHXVxysqUlYmvHtt2KOjHdJZ7kY6s3s9p+IDQqO6WlYLp7ccm7y3Lr7QVFDBfG5weMjIUNZpI2wEAUzvKSw6VLgNWqGgZZbQP/ZEZoJV/FkAaBojyu7hoKTb32r0K1KlWVL3tO5ytT1CAjyaccOziV2GSU1/nYxWP7ypGrYq7ngWd0FGwjYhnTdD+mT3CIrHWctW2Zak3Ct/4VNVRP9O990sWHFOUrSuk2Y0RaIMGGDTxo1dQvN6FbPXOxaf8Pljn8ZRHxi7tBTa7pRL+QtF8ajFTyUX8Da+ssRofoqAK2KqWtsPLM6oVK4Xx8LL/5i6JlSh2u6hFAaEHnVAL7yxrAM/COMbxFYZfHKKjrCIMkfT/F7MMOIMUZMgI4cKbZyyQWXORWTB98hjVPeed+q7HL6pON+ETt+y5BIpB3ErPMEVWDZbrfq2X9SJQg1WigNbsTR5Uj5T0LZ6uZyioH35I2GAjM2dVigFV4YCm8=~4273204~3290435; OptanonConsent=isGpcEnabled=0&datestamp=2025-07-29T20%3A19%3A32.185Z&version=202505.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=658f76fc-ac02-4d91-9e39-877a9c37228c&interactionCount=0&isAnonUser=1&landingPath=NotLandingPage&groups=TAB01%3A0%2CC0004%3A0%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CTAB02%3A1&AwaitingReconsent=false; lll_adobe_geo_country=united%20arab%20emirates; lll_adobe_geo_state=dubai; lll_adobe_geo_city=dubai; lll_adobe_geo_latitude=25.1019; lll_adobe_geo_longitude=55.1712; bm_sv=D395AD25BB3AB3E2B99DABDDAF0BE6E2~YAAQPfttaBT8r1WYAQAAcBX6Vxy8SaYTtv8lQ3EZBRRCHZYb+8PeDe3+MH/zK5GREVzajKXeaKQfgPG46kRBe2NtRzpCfppKXK94HESw/sLgW+EguDWLYZasTuvt9TclWW1orjn2F7aoIegFXVIsV7+uyXUvk1h0Y/QJBI9FSMEbvo7hcBGcOF13Uot1Gkr8cKzhXCk0W+S8serTcXpKku23DiLdI5EUNw/bUmZ49PIy9TofvZTWz7SSLz/ee+8kKHzQIw==~1; s_sq=llmnprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dcdp%25253Awomens-back-to-school%2526link%253DView%252520details%252520of%252520Nulu%252520Cropped%252520Short-Sleeve%252520Shirt%252520Retro%252520Remix%252520Set%2526region%253Dproduct-list%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dcdp%25253Awomens-back-to-school%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fshop.lululemon.com%25252Fp%25252Ftops-short-sleeve%25252FNulu-Cropped-Short-Sleeve-Shirt-Retro-Remix-Set%25252F_%25252Fpro%2526ot%253DA',
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
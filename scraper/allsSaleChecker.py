import requests

cookies = {
    'nt_page_init_referrer': 'NeotagEncrypt%3AU2FsdGVkX1%2BsJwiJkVZpz%2B%2Bbgy26OZ1VdMaIGEZ5G64%3D',
    'nt_page_init_referring_domain': 'NeotagEncrypt%3AU2FsdGVkX18z0G7ItqAY0GZere%2F5gC6IHvmoDdxwz%2Fc%3D',
    '_ga': 'GA1.1.1964284017.1751977271',
    '_tt_enable_cookie': '1',
    '_ttp': '01JZMZQ8178KYJ2S8ZNE1TC4EV_.tt.1',
    '_scid': 'F-dYMQitund0c-17xRDg3gr8FLD-1qh1',
    '_sctr': '1%7C1751918400000',
    'neo_sc': 'NeotagEncrypt%3AU2FsdGVkX1%2FSVMITZlMnRj1DpLfwRLEh4vJO3vgTAdw%3D',
    'nt_user_id': 'NeotagEncrypt%3AU2FsdGVkX1%2Bl1GenLaZa9YL7qkAgMD857ERl7m%2FKqlk%3D',
    'nt_trait': 'NeotagEncrypt%3AU2FsdGVkX19ONc%2FZtoEt%2FdheRbkyGQ2XVL%2FY4Fdx3cg%3D',
    'nt_group_id': 'NeotagEncrypt%3AU2FsdGVkX18%2B19WtTv9%2B4BT5wvQKOz1wKapi74J2yx0%3D',
    'nt_group_trait': 'NeotagEncrypt%3AU2FsdGVkX19A7iN%2FL5xMJ2H99UjnRFkcgXlC7v4I3JU%3D',
    'nt_anonymous_id': 'NeotagEncrypt%3AU2FsdGVkX19VnO6xUz4vy1MZLX0SGVccz92Qr5t6yG2hVBS9bxiz%2BlFd%2BJ5SdkrUlYyjq3evmYkQJ2Ybvc13kA%3D%3D',
    '_scid_r': 'FGdYMQitund0c-17xRDg3gr8FLD-1qh1gAj9Pw',
    '_ga_JCZ0JR3KPC': 'GS2.1.s1752143860$o6$g1$t1752144070$j60$l0$h644044425',
    'neo_session': 'NeotagEncrypt%3AU2FsdGVkX19msusgSkvean2%2F5tdsMTQAg8RjOmalFQPUFho5k5hJ3XrNwCbB7lmKTE2N8eZC2avEW5Ii42SXvZzKHN9K1bDnSuQXZ2GDAtf8SAzZkRAYETIvCvuDbvhg28tpbLvGd6gajIzIxC4Y%2FA%3D%3D',
    'ttcsid': '1752143732995::GvDKpVQEAsFuffv1TpkV.7.1752144233285',
    'ttcsid_CC1ON5JC77U4JJ3BHHHG': '1752143732994::Zef3YwuLXz7Nq0eIDojm.6.1752144234551',
    '_ga_RC54V0M6CC': 'GS2.1.s1752143731$o6$g1$t1752144252$j60$l0$h0',
    '_ga_083HX4D5KG': 'GS2.1.s1752143731$o1$g1$t1752144252$j41$l0$h1241084185',
    'rr_rcs': 'eF5jYSlN9kg2MzIySDE30E1LNDHSNUlJSdFNMjIw0zU3MTNNSzRPtUxONuPKLSvJTBEwMrA01TXUNQQAnasOlA',
    'ROUTE': '.api-784b947787-pxfl7',
    'ak_bmsc': 'EDDF690B3AA3ED06C3FDDB7646897152~000000000000000000000000000000~YAAQHucVAqaEm1yaAQAA8QiTbR06apIr6oZXCMI3wRP7CwN+OfvZX5XArE2HSzqgp0QZOCw6m6pw7FcIQIts1k2W+eiCqp9OzbyAgDv2pgUVcNxzX7DzkbfjolG868OHU0bzW1FH8GHfofaz+BLrV1/ceTOdnIzwokTLSKduN/PT1vxwasafv9ERmUSIVAH9f5P9G9aNWPgaSD2Q5hFbjX/7tmchvP8Pcl8VweX4pCcyl1VIuU0zy9cMBDw4OAzP6YULzOojS1BdAbRxhBYHWRzj5J6iHTaETpNGcg7M0JrbJlcqK/m7JichaROb3DUNUi74le6hdNT4mbg6tsLDhj/GmCTbeFl613DSBkBYtB7B5DEL+siYBBlG+bF7AJmzXeCNPVeyTWioZfA=',
    'bm_mi': 'D4185713AD39C5BB277AFC95EF9BCBE6~YAAQHucVAjCem1yaAQAAep+TbR2uUdQlq+zA2NDbif5iIDpP+Kb4xmkDh/UzrpMOH3Iz6cIUpCNM09SickcbU4NdgZV+TXQKKXM1iR8dSIL/h+QhfkMP0z+JikXgwsyjmgM3HQmeq8Puhg0nuYGAg/Dd1MzWDnn9p+/ua/0vVSnhUq3aLiPVOqqNhLKxWRkeHC7c1KrI7AhZ8m64Bz48omv4gCQoA1o34Q88PgilnAtlqMan4QGvB4OlJRvAzb1t3yxMpbVfTQ6Rw6+UMvk0dkBMCVSt0RY9xRW1YfaK3hrik5rgg2xkmPAvsTQDwTeMcT/cSU9GW9kyDcTlFps=~1',
    'bm_sv': 'CE09FE13B265D0D5DD3F40C5D240FFFA~YAAQHucVArSkm1yaAQAAfsWTbR2nTnTzgKZz6QEONHTAOPmB9XBFZ3Sw6pFjXXeJAUpt4K0dqJPOJO80UESblojiRRSrWk9xQDRWOnUxlRCyfYIng7kzHrnUA8jMZVReYMlFERkZkZ0bsBn7fPhq6Z/r222t2FN4mffXVzE3p8+aRS6qf32g6Rx8zWWO5mOxpMbzjfOUMoZz1F2/6t+YWnOxDOtsn82zHdIYcYjEo4ZHDt7Df77IDblTMk6LYLmKkelq~1',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.allsaints.me',
    'priority': 'u=1, i',
    'referer': 'https://www.allsaints.me/',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'x-anonymous-consents': '%5B%5D',
    # 'cookie': 'nt_page_init_referrer=NeotagEncrypt%3AU2FsdGVkX1%2BsJwiJkVZpz%2B%2Bbgy26OZ1VdMaIGEZ5G64%3D; nt_page_init_referring_domain=NeotagEncrypt%3AU2FsdGVkX18z0G7ItqAY0GZere%2F5gC6IHvmoDdxwz%2Fc%3D; _ga=GA1.1.1964284017.1751977271; _tt_enable_cookie=1; _ttp=01JZMZQ8178KYJ2S8ZNE1TC4EV_.tt.1; _scid=F-dYMQitund0c-17xRDg3gr8FLD-1qh1; _sctr=1%7C1751918400000; neo_sc=NeotagEncrypt%3AU2FsdGVkX1%2FSVMITZlMnRj1DpLfwRLEh4vJO3vgTAdw%3D; nt_user_id=NeotagEncrypt%3AU2FsdGVkX1%2Bl1GenLaZa9YL7qkAgMD857ERl7m%2FKqlk%3D; nt_trait=NeotagEncrypt%3AU2FsdGVkX19ONc%2FZtoEt%2FdheRbkyGQ2XVL%2FY4Fdx3cg%3D; nt_group_id=NeotagEncrypt%3AU2FsdGVkX18%2B19WtTv9%2B4BT5wvQKOz1wKapi74J2yx0%3D; nt_group_trait=NeotagEncrypt%3AU2FsdGVkX19A7iN%2FL5xMJ2H99UjnRFkcgXlC7v4I3JU%3D; nt_anonymous_id=NeotagEncrypt%3AU2FsdGVkX19VnO6xUz4vy1MZLX0SGVccz92Qr5t6yG2hVBS9bxiz%2BlFd%2BJ5SdkrUlYyjq3evmYkQJ2Ybvc13kA%3D%3D; _scid_r=FGdYMQitund0c-17xRDg3gr8FLD-1qh1gAj9Pw; _ga_JCZ0JR3KPC=GS2.1.s1752143860$o6$g1$t1752144070$j60$l0$h644044425; neo_session=NeotagEncrypt%3AU2FsdGVkX19msusgSkvean2%2F5tdsMTQAg8RjOmalFQPUFho5k5hJ3XrNwCbB7lmKTE2N8eZC2avEW5Ii42SXvZzKHN9K1bDnSuQXZ2GDAtf8SAzZkRAYETIvCvuDbvhg28tpbLvGd6gajIzIxC4Y%2FA%3D%3D; ttcsid=1752143732995::GvDKpVQEAsFuffv1TpkV.7.1752144233285; ttcsid_CC1ON5JC77U4JJ3BHHHG=1752143732994::Zef3YwuLXz7Nq0eIDojm.6.1752144234551; _ga_RC54V0M6CC=GS2.1.s1752143731$o6$g1$t1752144252$j60$l0$h0; _ga_083HX4D5KG=GS2.1.s1752143731$o1$g1$t1752144252$j41$l0$h1241084185; rr_rcs=eF5jYSlN9kg2MzIySDE30E1LNDHSNUlJSdFNMjIw0zU3MTNNSzRPtUxONuPKLSvJTBEwMrA01TXUNQQAnasOlA; ROUTE=.api-784b947787-pxfl7; ak_bmsc=EDDF690B3AA3ED06C3FDDB7646897152~000000000000000000000000000000~YAAQHucVAqaEm1yaAQAA8QiTbR06apIr6oZXCMI3wRP7CwN+OfvZX5XArE2HSzqgp0QZOCw6m6pw7FcIQIts1k2W+eiCqp9OzbyAgDv2pgUVcNxzX7DzkbfjolG868OHU0bzW1FH8GHfofaz+BLrV1/ceTOdnIzwokTLSKduN/PT1vxwasafv9ERmUSIVAH9f5P9G9aNWPgaSD2Q5hFbjX/7tmchvP8Pcl8VweX4pCcyl1VIuU0zy9cMBDw4OAzP6YULzOojS1BdAbRxhBYHWRzj5J6iHTaETpNGcg7M0JrbJlcqK/m7JichaROb3DUNUi74le6hdNT4mbg6tsLDhj/GmCTbeFl613DSBkBYtB7B5DEL+siYBBlG+bF7AJmzXeCNPVeyTWioZfA=; bm_mi=D4185713AD39C5BB277AFC95EF9BCBE6~YAAQHucVAjCem1yaAQAAep+TbR2uUdQlq+zA2NDbif5iIDpP+Kb4xmkDh/UzrpMOH3Iz6cIUpCNM09SickcbU4NdgZV+TXQKKXM1iR8dSIL/h+QhfkMP0z+JikXgwsyjmgM3HQmeq8Puhg0nuYGAg/Dd1MzWDnn9p+/ua/0vVSnhUq3aLiPVOqqNhLKxWRkeHC7c1KrI7AhZ8m64Bz48omv4gCQoA1o34Q88PgilnAtlqMan4QGvB4OlJRvAzb1t3yxMpbVfTQ6Rw6+UMvk0dkBMCVSt0RY9xRW1YfaK3hrik5rgg2xkmPAvsTQDwTeMcT/cSU9GW9kyDcTlFps=~1; bm_sv=CE09FE13B265D0D5DD3F40C5D240FFFA~YAAQHucVArSkm1yaAQAAfsWTbR2nTnTzgKZz6QEONHTAOPmB9XBFZ3Sw6pFjXXeJAUpt4K0dqJPOJO80UESblojiRRSrWk9xQDRWOnUxlRCyfYIng7kzHrnUA8jMZVReYMlFERkZkZ0bsBn7fPhq6Z/r222t2FN4mffXVzE3p8+aRS6qf32g6Rx8zWWO5mOxpMbzjfOUMoZz1F2/6t+YWnOxDOtsn82zHdIYcYjEo4ZHDt7Df77IDblTMk6LYLmKkelq~1',
}

response = requests.get(
    'https://api.allsaints.me/rest/v2/alls/products/search?fields=keywordRedirectUrl%2Cproducts(baseOptions(FULL)%2CbaseProduct%2Ccode%2CearnablePoints%2Csellable%2CmaxOrderQuantity%2Cname%2Csummary%2Cprice(FULL)%2Cbadges(code%2Cname)%2Cimages(DEFAULT)%2Cstock(FULL)%2CaverageRating%2CcrossedPrice(FULL)%2Ccategories(name%2Ccode%2Curl)%2CdiscountRate%2Cbreadcrumbs)%2Cfacets%2Cpagination(DEFAULT)%2Csorts(DEFAULT)%2CfreeTextSearch&query=%3Arelevance&currentPage=0&pageSize=9999&lang=en&curr=AED',
    cookies=cookies,
    headers=headers,
)

import json

# Check if the request was successful
if response.status_code == 200:
    # Save the response to a JSON file
    with open('allsSale.json', 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)
    print("Data has been successfully exported to 'products.json'.")
else:
    print("Failed to fetch data. Status code:", response.status_code)
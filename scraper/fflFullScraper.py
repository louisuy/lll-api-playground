import requests
import csv

cookies = {
    'NEXT_LOCALE': 'en-ae',
    'OptanonAlertBoxClosed': '2025-08-07T21:03:39.135Z',
    'bm_mi': 'BD690A0127E087A3A2C0FBB13EDC5CFE~YAAQF5fYF/dnCFeYAQAASm5ahhzOuqcBixs7DgdAUwoz3TOGZfWLOqs7IUK/dbS+lbXsZyCPVCdLydVChDSdQpZOs4XmxUtdFrhkD5Si1FuvI+AslAEBO1SSpu58kU08gsAJjQozwT4KIyRfhslQzj9capmi9IzhQILDhr5g3l//5wQx9TTzDd3FgNFAxc3DmTVtbwuohVKI5IUeZjTUUg8CLbj2rZLyDG8FdJ9ULIUbahI1VihYlo0Nyz4pL1wKD1UbCUZr3Z+zMtIqqk4qdHTveJC5TDc8CLb9JSbk6QLKDLa0S37Ij+VSOoXM9XBTC4lCpXrPIBDA4C53yKB/6GDxWDM6eTChtfnDQXm+ouWopLLk9SK+11g9vwU=~1',
    'bm_sv': '14CC790B2E4A48D468C14B9F86F3C748~YAAQF5fYFxpoCFeYAQAANnBahhzEV0m6c3p56HmCmC8oaRNwTNuRoSgZ17y7DsqE2XDDULcsvIfoOAqMszJZytVadRO/X8UpMiNwv9MYXhb7CcyN8aEPxiijYf/oKGKZnNmyGXDQQakDMVhU309Iqlq+uz6OmeWj5Ydyr3SOooGve8wEVKYHgzg6cTMsAJfYEj8eDR/ji2/4FsrGp0Ll8E4dQ+RTK4iC/QfN9KfujZ9gTZ4My2oFestiAuQ7NaOzUpLHy1TH~1',
    'ak_bmsc': '41FE5BD462014C8072AEE91290ABDB5F~000000000000000000000000000000~YAAQF5fYF2hwCFeYAQAA2ExbhhxySuIOkZ3sC4lWXkbviu2576PcmPUyXPlDeJt9d0X0n4ZMTlFuLC/QFxlLqpCeJQiEcKaCuKvg3FLyyux//8Q8beiSMqJzgg6iNZITtIQ5XIIXpM6tSdRwTvE0cP2bJIxEoKEmUfcmW/FHxczHrR2VKjqYUUxDNjnilU+8q7F/WeVxd6sh5/OVwtcLhOn5DxAwzSopztF7BWZhOBm+Ht0+OnAk30bEkVdFs6wGF2uS7pM+Ew6mwvYEinpvHuZeKCjSdUiX/zXh7xvX08BYfaDon7/rXPCqT1m8a45J4lgGlCJ1XeG+NQQy9R4qBBrfS80dsN+IPXZZuozrLLmWE76d0Eu5ukMUEsMQN+svawRHsEP71swfaos3E4i4JFk+ZyYXyBFJA406gbGjUS1mPYjmUnxwSQdOEVCi9QXXA9xIZ8Stm2UfZgIytxFs2vQNHl0RmJR4yCXkhRHtCL75hToH6KwbnQ==',
    'ROUTE': '.api-6756b5499c-9wsz2',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Aug+08+2025+01%3A12%3A56+GMT%2B0400+(Gulf+Standard+Time)&version=202403.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1&geolocation=%3B&AwaitingReconsent=false',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=1, i',
    'referer': 'https://www.fashion4less.me/en-ae/c/men?q=%3Arelevance%3AallCategories%3Amen',
    'sales-application': 'Web',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
    # 'cookie': 'NEXT_LOCALE=en-ae; OptanonAlertBoxClosed=2025-08-07T21:03:39.135Z; bm_mi=BD690A0127E087A3A2C0FBB13EDC5CFE~YAAQF5fYF/dnCFeYAQAASm5ahhzOuqcBixs7DgdAUwoz3TOGZfWLOqs7IUK/dbS+lbXsZyCPVCdLydVChDSdQpZOs4XmxUtdFrhkD5Si1FuvI+AslAEBO1SSpu58kU08gsAJjQozwT4KIyRfhslQzj9capmi9IzhQILDhr5g3l//5wQx9TTzDd3FgNFAxc3DmTVtbwuohVKI5IUeZjTUUg8CLbj2rZLyDG8FdJ9ULIUbahI1VihYlo0Nyz4pL1wKD1UbCUZr3Z+zMtIqqk4qdHTveJC5TDc8CLb9JSbk6QLKDLa0S37Ij+VSOoXM9XBTC4lCpXrPIBDA4C53yKB/6GDxWDM6eTChtfnDQXm+ouWopLLk9SK+11g9vwU=~1; bm_sv=14CC790B2E4A48D468C14B9F86F3C748~YAAQF5fYFxpoCFeYAQAANnBahhzEV0m6c3p56HmCmC8oaRNwTNuRoSgZ17y7DsqE2XDDULcsvIfoOAqMszJZytVadRO/X8UpMiNwv9MYXhb7CcyN8aEPxiijYf/oKGKZnNmyGXDQQakDMVhU309Iqlq+uz6OmeWj5Ydyr3SOooGve8wEVKYHgzg6cTMsAJfYEj8eDR/ji2/4FsrGp0Ll8E4dQ+RTK4iC/QfN9KfujZ9gTZ4My2oFestiAuQ7NaOzUpLHy1TH~1; ak_bmsc=41FE5BD462014C8072AEE91290ABDB5F~000000000000000000000000000000~YAAQF5fYF2hwCFeYAQAA2ExbhhxySuIOkZ3sC4lWXkbviu2576PcmPUyXPlDeJt9d0X0n4ZMTlFuLC/QFxlLqpCeJQiEcKaCuKvg3FLyyux//8Q8beiSMqJzgg6iNZITtIQ5XIIXpM6tSdRwTvE0cP2bJIxEoKEmUfcmW/FHxczHrR2VKjqYUUxDNjnilU+8q7F/WeVxd6sh5/OVwtcLhOn5DxAwzSopztF7BWZhOBm+Ht0+OnAk30bEkVdFs6wGF2uS7pM+Ew6mwvYEinpvHuZeKCjSdUiX/zXh7xvX08BYfaDon7/rXPCqT1m8a45J4lgGlCJ1XeG+NQQy9R4qBBrfS80dsN+IPXZZuozrLLmWE76d0Eu5ukMUEsMQN+svawRHsEP71swfaos3E4i4JFk+ZyYXyBFJA406gbGjUS1mPYjmUnxwSQdOEVCi9QXXA9xIZ8Stm2UfZgIytxFs2vQNHl0RmJR4yCXkhRHtCL75hToH6KwbnQ==; ROUTE=.api-6756b5499c-9wsz2; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Aug+08+2025+01%3A12%3A56+GMT%2B0400+(Gulf+Standard+Time)&version=202403.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1&geolocation=%3B&AwaitingReconsent=false',
}

params = {
    'endpoint': 'https://api.fashion4less.me/rest/v2/ffl/products/search?fields=FULL&query=:relevance&currentPage=0&pageSize=2000',
}

# Make the API request
response = requests.get('https://www.fashion4less.me/api', params=params, cookies=cookies, headers=headers)

# Parse the JSON response
data = response.json()

# Extract products from the response
products = data.get("products", [])

# Write products data to a CSV file
with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["baseProduct", "brandName", "code", "crossedPrice", "name", "price", "priceToCrossedPrice"])
    writer.writeheader()

    # Write each product's relevant data to the CSV
    for product in products:
        crossed_price = product.get("crossedPrice", {}).get("value", 0)
        price = product.get("price", {}).get("value", 0)
        
        # Calculate the price-to-crossedPrice ratio (avoid division by zero)
        price_to_crossed_price = 1 - price / crossed_price if crossed_price > 0 else 0
        mafl_price = price * 0.6
        mafl_discount = 1 - mafl_price / crossed_price if crossed_price > 0 else 0.4     

        writer.writerow({
            "baseProduct": product.get("baseProduct"),
            "brandName": product.get("brandName"),
            "code": product.get("code"),
            "crossedPrice": crossed_price,
            "name": product.get("name"),
            "price": price,
            "mafl_price": mafl_price,
            "mafl_discount": mafl_discount,
            "priceToCrossedPrice": price_to_crossed_price
        })

print("CSV file with price-to-crossed-price ratio created successfully!")
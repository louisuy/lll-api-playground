# batchProductScraper.py
import csv
import json
import re
import sys
import time
import random
from pathlib import Path
from typing import Iterable, List

import requests

# =========================
# Config / Paths
# =========================
SCRIPT_DIR = Path(__file__).resolve().parent
# Pass an input CSV path as first CLI arg, otherwise default to "falledit.csv" next to this script
INPUT_CSV  = Path(sys.argv[1]) if len(sys.argv) > 1 else (SCRIPT_DIR / "falledit.csv")
OUTPUT_CSV = SCRIPT_DIR / "pdp_output_batch.csv"
FAIL_CSV   = SCRIPT_DIR / "pdp_failed_codes.csv"

SLEEP_BETWEEN_CALLS = 1.1   # seconds between products (go slower if you get 403s)
MAX_RETRIES = 2             # number of retries (in addition to the first attempt)

# =========================
# PLACEHOLDER COOKIES / HEADERS
# Replace with real values from an active browser session
# =========================
BROWSER_COOKIES = {
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
    'pers_seg': 'eyJnZW5kZXJBZmZpbml0eSI6IndvbWVuIn0=',
    'tfc-l': '%7B%22k%22%3A%7B%22v%22%3A%22idap4hda1kcsh55m486ug1sph9%22%2C%22e%22%3A1815027743%7D%2C%22a%22%3A%7B%22v%22%3A%22e834e722-1ae3-4423-8462-beb5cf955776%22%2C%22e%22%3A1753181187%7D%2C%22c%22%3A%7B%22v%22%3A%22adult%22%2C%22e%22%3A1815027743%7D%7D',
    'Prg5BMu0': 'A5V7TXqYAQAAjUEQTLZjmz8a6VA_ZxWD0rYp_8ZPSH-TPF1ZHEz3dua0d_u5AV7L1u2uchxGwH8AAEB3AAAAAA|1|1|e7aea4d618cbf530d8ef3c8e9374c6701864d5cf',
    'lll_oidc_token': 'eyJraWQiOiJfd2dUU1ZQTFdwdUd1OXh0U1AzbkhhbDQwVUY4bnFDUnVsZnRFNzZ5bURRIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULmVyQm0tSElsVk9lTTh5NS0wQ1NxbklwUnVFS0NkeGhnU19kV3BIUkthVFUub2FyMzh6MmFsNUFjVzhUMVg0eDciLCJpc3MiOiJodHRwczovL2lkZW50aXR5Lmx1bHVsZW1vbi5jb20vb2F1dGgyL2F1c2FvczlkMldqM2d3NmtyNHg2IiwiYXVkIjoiZ3Vlc3RzIiwiaWF0IjoxNzU1MDc3MzAwLCJleHAiOjE3NTUwODQ1MDAsImNpZCI6IjBvYWFvcnVxNG9Gc2g1TzNlNHg2IiwidWlkIjoiMDB1c25vcmY3b081TjBZQjk0eDciLCJzY3AiOlsib2ZmbGluZV9hY2Nlc3MiLCJwaWkiLCJlbWFpbCIsIm9wZW5pZCJdLCJhdXRoX3RpbWUiOjE3NTQzOTg2MTgsInN1YiI6ImFudGhvbnkubG91aXNAbWFmLmFlIn0.V7mgB0X_4fZEJj_1uysQa5XEnRP7eZ368xumUiQEH5b8iLLQrIYSVgffHTjO6BKqfl_PM3P23ECXhv67ttT9dETbyPdVJr-iN5m16z_0lj3MRUJdKo9h8FIsYnZEJ2MDQxr2srGl7OxQw0dzgUrZ-hKkuwNo0YAqVQXejwdg5S0OOv_SGSzc4epEDLg1pQ889xWd535RWWK7_Q5vlYyWal0w9Va2ox8ZUFcHc5W7L9NHXr9r9S7Jixtt0AZ-Htwy-rk1drHjLiiNRRYPhMK6G0KdnHg-XJEdLI62uStEbv8h_EjWJidqSMSrRU9MiEOhQP0XgqT5bN7Kel0XxJ53UQ',
    'ak_bmsc': '943B6D6CB7B09AC21D18E416C3423456~000000000000000000000000000000~YAAQres/F59fxJ6YAQAArmbCohzHczawyl49qxxvgn2JovTeLJkYEfkcbyy4DizclczqSTLZIh1gb+6MHzPSGqBxTdVAl6s/aXCDcTQz31ieBwVdZFsZ6/8CkC4gLmNmCYf5y8cGF5vw74qq4lJCbCDWUaw/cPqZ/aOk5GrOldVhM5x7Fd7ZXErZAVetFAzgTCKPKYM9N16bxk0+xhlYnj7dC/pvTeO47b0XSrBxRNMO/F+a6W4joJwrV5c/7zQAkrMkpU9ZMbwZmZE1QyNFo+1F/yV0IkB8270gi9X50hYxg4AXZ3GuGIotP9VOY66aIW9lruTxrSYujjiECZga3SvN6T2QDJpVB1n8DsQ2+1YQ4y1g24avUiqwhmXfN/QlSJY4Sey82zoDmkf/anR5oTry',
    'lll_refresh_token': 'true',
    '_abck': '59D7DD48E6A90EEB131BA027556B192D~0~YAAQres/FyOCxZ6YAQAAGiflog64p5Z6HDojP4/uit9TeerzLDQUgXV8KPD5ldDQd6ozh1Nl7SBc9rePkq/G3qvN6Np0ixUC5ZJRZJF8aTdR7I5c7C4SAKxvLdc7YCIzyTRy4GxGuU+sbb9/1hBRb75wr6bNh/kpaqPZ0m/6HVVT8J3KNtewwDgVVCxUueN9gqBj28jlrXarOXHNG687Fesh2ElLKfvTw6Lyovg3OsRn3p1Y2m19tF4n+F5fUu/a7foVGWLTe2f+BDOL2JloiTZt5C5xBhkP9jd4vJzv5RwjJfA3lTD+Dj8h+KOIe/+GKLiLfKZnZgnq93/TkF4/Z7u/OUHRuJJKRAJSsDhN+oJzXmgeOsE53h5s5KMsBrWFE1c5XFKbWULatQxdT9/ENdCRvn55tOvyGZSRxxnPOpqjJghGa8Nf4V+69bsNGXmKt3XCXg0C0sKTjle3OfYiY1hwbtt6OqQ3eF8hU3C+al/TqyY4/DN3iCGlNlgX8RFfV7oJZZJ7NQOqe+WM1jFjloEiLnw/WH4fYbHIf+FdZmd7GDMmB7pplQT/T/fIJ/CZrIpjKAXzoA5/3+rlqyA+fOA2JsQesjjqHMjKWoXuoh56NgOCwJGUAiSKz1C+uEMjCxpqn1Xv4UAsDES5Y9g1Lpzu/3OeXNTSPe4jj3GK3KfztlQ/+iucJjkITjLwRasKqE49SS54vkGMc/57N7sw8Sn227iy2Qhbe5TeWkB/VnwIesnY80gZqBL3WeFjEoTjog5/2/wuvbJ4DidNkj7X+E7XDGM6TKWxzcKCxbriBq0KTyZ/Zk+uSHsirK8187CribDwG6dqicwNgJLa1zqXlgrUFw5ziPbdqXzH7m1WY9JcDlfNdx4K95RLD5V5syEJrs56vMpKdFh5lAiFI//AkgCDuwPSxgRLjPHEY6lTUebo9AyZMywL8g==~-1~-1~1755080637',
    'bm_mi': '1D9E5C5A9BFF89E00389AE91630E2363~YAAQzus/Fw0ex5+YAQAAXQXnohzjEgLcNDmmarpXk+N3ojsxDU0RUO+FnC3NPwabY00OHCzc2ZuTMYXLVKWTpgsUOg6shVKno8z6VdAIS7pd7TqqZCr9DCv6BTRqq22fXtK8a99wLvlZm5UBYrXDTjXzkNPZVtmgTpi2VDJ+/pf4/qMwSdvq2mqA2vfmxbCfuEGHThLAKFC2nlLF0SUGOOGKcUUHHMhUUiRDLkiRq4/0ITnDXomMGC+nQTZQg/HJ/j785zvn7eAGG5kNL9iiLb+kIuHEjdA6fmfaBKs5+bNH/zd9hOZA+2FR4i73+Hi/YSqTIWDQQev9B/IQgj7Wp/2S0SlrvzskxJEFDeflX7EDaJ8fMLUOR4t0K6cZWk0QDseIZOTcal6xsQ==~1',
    'bm_sz': 'A49F6DF10EC9D549032FCF542D21C4FA~YAAQzus/Fw8ex5+YAQAAXQXnohzNprHyMQ9PSpVewkx1paVeThRvFT0hhwThCeIdRolpz/sUlwHmkw40Gpxu1sFuMUyIaerFPfXLtqEp81A3MVmcijOyBMMOMnuRLiPInNXZqJf6yJ3pwiFA7coMhw94C7ULX+33Hajj83ytc+pt+9Nm+14D41Rl3ihXoJumDCHOadODHD/whWrAu4BAm2FWD6w9yOQNMSPNRnDCbUlO/264rvePkoPvGmVbIPLpbO2ac/EcXpZ/MY932JIF9Lu68JOA8qnf7QSKvLgtCLUEUZ8Q0fzzWa4tGu7PxGCQlnrpSQXEotMkwpHgtlePP0XuoG5p15ndDMK8BipOTC5VbXjrdbS+LovxdWqHb02vGMjHjAJYFzKmlyOIJTa2pFkl1b/XT+6zQWpP3QuZ69BgsRrnMYyhtrHVeF5k20inZzKLBXxgohnRly3ofxY3fBm8JJGmGkPc+5VzmA7v95fYgiDGJJ0ZvqU=~4600118~3687729',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=2025-08-13T10%3A08%3A29.311Z&version=202507.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=62bc537c-d2bd-4c0f-b103-826359a79cf2&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=TAB01%3A1%2CC0004%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CTAB02%3A1&AwaitingReconsent=false',
    'bm_sv': '05685581F29E73B3495C75B616D54BCB~YAAQzus/Fygfx5+YAQAArR7nohxqJbfqz75p9IPXZUDzoQWzKjLkMb3sFFNkZzZKYw3MGRiQ5Fyo5gw+ulQMXATcaGwf31BgktZK0NqO/2t8Ax6Ddey5Rgsn6EILVcRiP6tR08JTknEZKrWR9EzF01ap1quRXBNJIP8w1pWr+DMifJcIGxMCZv3EcgY9juF2lN19ESNwJb+bl9EQODLsw3bnGIUyL1KieZZ5a2N6G24O9JO62nMiR45sPg2sA8y2ZIzPCg==~1',
}

# A single requests.Session for the whole run
session = requests.Session()
session.headers.update({
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
    'sentry-trace': 'dc756b12f628435f94589bd57318928f',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
    'x-lll-client': 'product-sdk',
    'x-lll-ecom-correlation-id': 'E60ED0CA-AAA1-0899-A0BE-1B597DB6AE47',
    'x-lll-referrer': 'Channel=Web,Page=pdp',
    'x-lll-request-correlation-id': '1cf18d8e-4b05-4f69-957b-54dda0d98ded',
    # 'cookie': '_ga_14J17NW0K4=GS2.2.s1751890298$o1$g0$t1751890300$j58$l0$h0; _lfa=LF1.1.cabc1bb242347854.1751890302222; _ga_V1VQCPSY6V=GS2.1.s1751957660$o2$g0$t1751957660$j60$l0$h0; _ga_GQP33VCV1E=GS2.1.s1751957660$o2$g0$t1751957660$j60$l0$h0; sat_track=true; kameleoonVisitorCode=4i8ulubslwypslau; UsrLocale=en_US; sl=US; ajs_anonymous_id=86da3fa5-7393-413c-977b-cf3ca069ebda; _ttp=28-waHDKO7tGyHsemr-0l5PGtY_; _scid=LwPoAZXzLO1BoqC6hLyDRwnxAZfy8aYX; _fbp=fb.1.1752127612468.307145000; _ga=GA1.1.1260579579.1751890297; __pdst=3ec3fcb533cc4ac2a5e2cd0f87b4ab59; kampyle_userid=d104-008b-d31a-7d46-5eaa-17fd-3241-a450; _pin_unauth=dWlkPVl6TTJNelV6WlRRdE5XVXpOUzAwT1RFeExXRmlNemt0TTJaaE56aGhZemc0T0RRdw; digitalData.page.a1Token=$2a$10$tNGLzxgFy.YH1jVIvc.LIOY4ORTw.fW7fXfpWyGQgsH.ZWRjuyyyi; _evga_8f06={%22uuid%22:%229ec5c2631c240b31%22}; _sfid_cc29={%22anonymousId%22:%229ec5c2631c240b31%22%2C%22consents%22:[{%22consent%22:{%22provider%22:%22Consent%20Provider%22%2C%22purpose%22:%22Personalization%22%2C%22status%22:%22Opt%20In%22}%2C%22lastUpdateTime%22:%222025-07-10T06:06:55.435Z%22%2C%22lastSentTime%22:%222025-07-10T06:06:55.439Z%22}]}; _ttp=28-waHDKO7tGyHsemr-0l5PGtY_.tt.1; _tt_enable_cookie=1; _fbp=fb.1.1752127612468.307145000; _gcl_au=1.1.1388619635.1752127616; a1ashgd=4b8j6vwzg3p000004b8j6vwzg3p00000; _sctr=1%7C1752091200000; bttnsessionid=sess-H2qHL643wyETBr7pgU3Yx41xHW4NF5kZHtFJZd49IbUw_; QuantumMetricUserID=86831e065cf43c36ac4b56fde3222bff; _rdt_uuid=1752127613494.a76d7d73-f628-4de0-88ff-078d5535cfba; kampyleUserSession=1752129062551; kampyleUserSessionsCount=3; kampyleUserPercentile=14.551039287714485; kampyleSessionPageCounter=1; _scid=I3Km-6s9xltlYS7dc8AysCMHYnqqbMxjPrhP8A; ttcsid_C65BFLPR48GN82KJE2E0=1752127616136::25526VBqZoBaTt-QbCai.1.1752129063135; _ga_4ZRJ21056F=GS2.1.s1752131300$o2$g0$t1752131300$j60$l0$h0; _ga_CCD7VVYPZ7=GS2.1.s1752131300$o2$g0$t1752131300$j60$l0$h0; intlOTConsent=C0004:1,C0001:1,C0003:1,C0002:1; NoCookie=true; __cq_uuid=2ab6ce80-5d6c-11f0-8bb0-47509f0499fd; alaPPN=pdp:prod11680106; _scid_r=JXKm-6s9xltlYS7dc8AysCMHYnqqbMxjPrhP8g; _ga_BXZE3SJMWL=GS2.1.sD84drOFtA18hFH51RDTXopGOmFqnQ69vpXc%3D$o1$g1$t1752137983$j37$l0$h0; a1ashgd=cqlz5hkklui00000cqlz5hkklui00000; _uetvid=13c9c8605d5411f0a0fdaf8fca2d1181|jjcgek|1752129063687|4|1|bat.bing.com/p/insights/c/e; ttcsid_CNK2R5JC77U8IUSPJBFG=1752137960452::GtBuI1LXA4A6tL5T5oTU.1.1752137983701; ttcsid=1752137960454::xDW5y-BLQEYmZznaYhtD.2.1752137983701; AMCV_A92B3BC75245B1030A490D4D%40AdobeOrg=179643557%7CMCIDTS%7C20306%7CMCMID%7C52375525777371028292491689370830964215%7CMCAAMLH-1752732403%7C6%7CMCAAMB-1754377189%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1754384390s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; mbox=PC#bdf3d85951b14ca48c0c2159000bc260.37_0#1817621992|session#7f13025d373846b9b6ae5c3c2bc5fb3f#1754379052; cf_clearance=hwpudf0t3DVW8tPz29QLJfXpTeDkJ9cnCdbEfkOm3DM-1754383476-1.2.1.1-hBmsU0JPbNLY7QresnIPgaC92QEu3e5RWr4zx8URdOH.zaxvE.b.1QYxjvyyEqNeXuJV71JIjXTvp_K._L2fiEW6B3JO0jqe7OWDA2ME7Zo7yzkxHjwBDDEPwVoepiIfC0ANCD6mW_xzCYJt72pPRORDRC4F.J6i0hnPeM.i6em5A11LcHrLf81lrAmPJ3FCG_asH3rYoiweia.WuoNeBkpxOUGkrfmpV3CO1EK9IRc; lll-ix-wl=true; lll-ix-dash=true; lll_digital_id=52375525777371028292491689370830964215; lll_edge_geo_data=city=DUBAI&state=&zip=&country=AE&lat=25.25&long=55.28; lll-ecom-correlation-id=E60ED0CA-AAA1-0899-A0BE-1B597DB6AE47; akaalb_Shop_ALB_instance1=~op=shop_upperfunnel_static:shop-upperfunnel-1|shop_mwa_shared:mwa-shared-usw-2|~rv=34~m=shop-upperfunnel-1:0|mwa-shared-usw-2:0|~os=3ad3acca926c302b084e12bf3b209756~id=0367cd63924f633d33ba14ee23da8b40; ek8_guest=true; pers_seg=eyJnZW5kZXJBZmZpbml0eSI6IndvbWVuIn0=; tfc-l=%7B%22k%22%3A%7B%22v%22%3A%22idap4hda1kcsh55m486ug1sph9%22%2C%22e%22%3A1815027743%7D%2C%22a%22%3A%7B%22v%22%3A%22e834e722-1ae3-4423-8462-beb5cf955776%22%2C%22e%22%3A1753181187%7D%2C%22c%22%3A%7B%22v%22%3A%22adult%22%2C%22e%22%3A1815027743%7D%7D; Prg5BMu0=A5V7TXqYAQAAjUEQTLZjmz8a6VA_ZxWD0rYp_8ZPSH-TPF1ZHEz3dua0d_u5AV7L1u2uchxGwH8AAEB3AAAAAA|1|1|e7aea4d618cbf530d8ef3c8e9374c6701864d5cf; lll_oidc_token=eyJraWQiOiJfd2dUU1ZQTFdwdUd1OXh0U1AzbkhhbDQwVUY4bnFDUnVsZnRFNzZ5bURRIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULmVyQm0tSElsVk9lTTh5NS0wQ1NxbklwUnVFS0NkeGhnU19kV3BIUkthVFUub2FyMzh6MmFsNUFjVzhUMVg0eDciLCJpc3MiOiJodHRwczovL2lkZW50aXR5Lmx1bHVsZW1vbi5jb20vb2F1dGgyL2F1c2FvczlkMldqM2d3NmtyNHg2IiwiYXVkIjoiZ3Vlc3RzIiwiaWF0IjoxNzU1MDc3MzAwLCJleHAiOjE3NTUwODQ1MDAsImNpZCI6IjBvYWFvcnVxNG9Gc2g1TzNlNHg2IiwidWlkIjoiMDB1c25vcmY3b081TjBZQjk0eDciLCJzY3AiOlsib2ZmbGluZV9hY2Nlc3MiLCJwaWkiLCJlbWFpbCIsIm9wZW5pZCJdLCJhdXRoX3RpbWUiOjE3NTQzOTg2MTgsInN1YiI6ImFudGhvbnkubG91aXNAbWFmLmFlIn0.V7mgB0X_4fZEJj_1uysQa5XEnRP7eZ368xumUiQEH5b8iLLQrIYSVgffHTjO6BKqfl_PM3P23ECXhv67ttT9dETbyPdVJr-iN5m16z_0lj3MRUJdKo9h8FIsYnZEJ2MDQxr2srGl7OxQw0dzgUrZ-hKkuwNo0YAqVQXejwdg5S0OOv_SGSzc4epEDLg1pQ889xWd535RWWK7_Q5vlYyWal0w9Va2ox8ZUFcHc5W7L9NHXr9r9S7Jixtt0AZ-Htwy-rk1drHjLiiNRRYPhMK6G0KdnHg-XJEdLI62uStEbv8h_EjWJidqSMSrRU9MiEOhQP0XgqT5bN7Kel0XxJ53UQ; ak_bmsc=943B6D6CB7B09AC21D18E416C3423456~000000000000000000000000000000~YAAQres/F59fxJ6YAQAArmbCohzHczawyl49qxxvgn2JovTeLJkYEfkcbyy4DizclczqSTLZIh1gb+6MHzPSGqBxTdVAl6s/aXCDcTQz31ieBwVdZFsZ6/8CkC4gLmNmCYf5y8cGF5vw74qq4lJCbCDWUaw/cPqZ/aOk5GrOldVhM5x7Fd7ZXErZAVetFAzgTCKPKYM9N16bxk0+xhlYnj7dC/pvTeO47b0XSrBxRNMO/F+a6W4joJwrV5c/7zQAkrMkpU9ZMbwZmZE1QyNFo+1F/yV0IkB8270gi9X50hYxg4AXZ3GuGIotP9VOY66aIW9lruTxrSYujjiECZga3SvN6T2QDJpVB1n8DsQ2+1YQ4y1g24avUiqwhmXfN/QlSJY4Sey82zoDmkf/anR5oTry; lll_refresh_token=true; _abck=59D7DD48E6A90EEB131BA027556B192D~0~YAAQres/FyOCxZ6YAQAAGiflog64p5Z6HDojP4/uit9TeerzLDQUgXV8KPD5ldDQd6ozh1Nl7SBc9rePkq/G3qvN6Np0ixUC5ZJRZJF8aTdR7I5c7C4SAKxvLdc7YCIzyTRy4GxGuU+sbb9/1hBRb75wr6bNh/kpaqPZ0m/6HVVT8J3KNtewwDgVVCxUueN9gqBj28jlrXarOXHNG687Fesh2ElLKfvTw6Lyovg3OsRn3p1Y2m19tF4n+F5fUu/a7foVGWLTe2f+BDOL2JloiTZt5C5xBhkP9jd4vJzv5RwjJfA3lTD+Dj8h+KOIe/+GKLiLfKZnZgnq93/TkF4/Z7u/OUHRuJJKRAJSsDhN+oJzXmgeOsE53h5s5KMsBrWFE1c5XFKbWULatQxdT9/ENdCRvn55tOvyGZSRxxnPOpqjJghGa8Nf4V+69bsNGXmKt3XCXg0C0sKTjle3OfYiY1hwbtt6OqQ3eF8hU3C+al/TqyY4/DN3iCGlNlgX8RFfV7oJZZJ7NQOqe+WM1jFjloEiLnw/WH4fYbHIf+FdZmd7GDMmB7pplQT/T/fIJ/CZrIpjKAXzoA5/3+rlqyA+fOA2JsQesjjqHMjKWoXuoh56NgOCwJGUAiSKz1C+uEMjCxpqn1Xv4UAsDES5Y9g1Lpzu/3OeXNTSPe4jj3GK3KfztlQ/+iucJjkITjLwRasKqE49SS54vkGMc/57N7sw8Sn227iy2Qhbe5TeWkB/VnwIesnY80gZqBL3WeFjEoTjog5/2/wuvbJ4DidNkj7X+E7XDGM6TKWxzcKCxbriBq0KTyZ/Zk+uSHsirK8187CribDwG6dqicwNgJLa1zqXlgrUFw5ziPbdqXzH7m1WY9JcDlfNdx4K95RLD5V5syEJrs56vMpKdFh5lAiFI//AkgCDuwPSxgRLjPHEY6lTUebo9AyZMywL8g==~-1~-1~1755080637; bm_mi=1D9E5C5A9BFF89E00389AE91630E2363~YAAQzus/Fw0ex5+YAQAAXQXnohzjEgLcNDmmarpXk+N3ojsxDU0RUO+FnC3NPwabY00OHCzc2ZuTMYXLVKWTpgsUOg6shVKno8z6VdAIS7pd7TqqZCr9DCv6BTRqq22fXtK8a99wLvlZm5UBYrXDTjXzkNPZVtmgTpi2VDJ+/pf4/qMwSdvq2mqA2vfmxbCfuEGHThLAKFC2nlLF0SUGOOGKcUUHHMhUUiRDLkiRq4/0ITnDXomMGC+nQTZQg/HJ/j785zvn7eAGG5kNL9iiLb+kIuHEjdA6fmfaBKs5+bNH/zd9hOZA+2FR4i73+Hi/YSqTIWDQQev9B/IQgj7Wp/2S0SlrvzskxJEFDeflX7EDaJ8fMLUOR4t0K6cZWk0QDseIZOTcal6xsQ==~1; bm_sz=A49F6DF10EC9D549032FCF542D21C4FA~YAAQzus/Fw8ex5+YAQAAXQXnohzNprHyMQ9PSpVewkx1paVeThRvFT0hhwThCeIdRolpz/sUlwHmkw40Gpxu1sFuMUyIaerFPfXLtqEp81A3MVmcijOyBMMOMnuRLiPInNXZqJf6yJ3pwiFA7coMhw94C7ULX+33Hajj83ytc+pt+9Nm+14D41Rl3ihXoJumDCHOadODHD/whWrAu4BAm2FWD6w9yOQNMSPNRnDCbUlO/264rvePkoPvGmVbIPLpbO2ac/EcXpZ/MY932JIF9Lu68JOA8qnf7QSKvLgtCLUEUZ8Q0fzzWa4tGu7PxGCQlnrpSQXEotMkwpHgtlePP0XuoG5p15ndDMK8BipOTC5VbXjrdbS+LovxdWqHb02vGMjHjAJYFzKmlyOIJTa2pFkl1b/XT+6zQWpP3QuZ69BgsRrnMYyhtrHVeF5k20inZzKLBXxgohnRly3ofxY3fBm8JJGmGkPc+5VzmA7v95fYgiDGJJ0ZvqU=~4600118~3687729; OptanonConsent=isGpcEnabled=0&datestamp=2025-08-13T10%3A08%3A29.311Z&version=202507.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=62bc537c-d2bd-4c0f-b103-826359a79cf2&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=TAB01%3A1%2CC0004%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CTAB02%3A1&AwaitingReconsent=false; bm_sv=05685581F29E73B3495C75B616D54BCB~YAAQzus/Fygfx5+YAQAArR7nohxqJbfqz75p9IPXZUDzoQWzKjLkMb3sFFNkZzZKYw3MGRiQ5Fyo5gw+ulQMXATcaGwf31BgktZK0NqO/2t8Ax6Ddey5Rgsn6EILVcRiP6tR08JTknEZKrWR9EzF01ap1quRXBNJIP8w1pWr+DMifJcIGxMCZv3EcgY9juF2lN19ESNwJb+bl9EQODLsw3bnGIUyL1KieZZ5a2N6G24O9JO62nMiR45sPg2sA8y2ZIzPCg==~1',
})

# =========================
# GraphQL Query
# =========================
GRAPHQL_QUERY = '''
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
'''

# =========================
# Helpers
# =========================
def extract_prod(code_raw: str) -> str:
    """
    Extract 'prod########' from a raw string, ignoring case and suffixes like _LULU.
    """
    m = re.search(r'(prod\d+)', code_raw, re.IGNORECASE)
    if not m:
        raise ValueError("Could not extract a valid product code")
    return m.group(1).lower()

def read_codes(path: Path) -> List[str]:
    """
    Reads codes from a CSV. Accepts:
      - Single-column CSV (no header)
      - CSV with headers: 'code' or 'product_code' (case-insensitive)
    """
    if not path.exists():
        raise FileNotFoundError(f"CSV not found: {path}")

    codes: List[str] = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        sample = f.read(2048)
        f.seek(0)
        try:
            has_header = csv.Sniffer().has_header(sample)
            dialect = csv.Sniffer().sniff(sample) if sample else csv.excel
        except Exception:
            has_header = False
            dialect = csv.excel

        reader = csv.reader(f, dialect)
        if has_header:
            header = next(reader, [])
            header_lower = [h.strip().lower() for h in header]
            try:
                idx = header_lower.index("code")
            except ValueError:
                try:
                    idx = header_lower.index("product_code")
                except ValueError:
                    idx = 0
            for row in reader:
                if row and len(row) > idx:
                    codes.append(row[idx].strip())
        else:
            for row in reader:
                if row:
                    codes.append(row[0].strip())
    return codes

def combine_unique(*lists: Iterable[str]) -> List[str]:
    """
    Combine multiple iterables into a list of unique strings,
    case-insensitive uniqueness while preserving first-seen casing.
    """
    seen = set()
    out: List[str] = []
    for lst in lists:
        if not lst:
            continue
        for item in lst:
            s = (item or "").strip()
            key = s.lower()
            if s and key not in seen:
                seen.add(key)
                out.append(s)
    return out

def session_warmup():
    """Seed server-set cookies (some bot/CDN cookies only come after a GET)."""
    try:
        r = session.get("https://shop.lululemon.com/", timeout=15)
        print(f"Warmup GET: {r.status_code}")
    except Exception as e:
        print(f"Warmup failed: {e}")

def init_session():
    """Load browser cookies and warm up the session."""
    if BROWSER_COOKIES:
        jar = requests.cookies.RequestsCookieJar()
        for k, v in BROWSER_COOKIES.items():
            jar.set(k, v, domain=".lululemon.com", path="/")
        session.cookies.update(jar)
    session_warmup()

def post_graphql(payload: dict, attempt: int = 1, prod_code: str = "") -> requests.Response:
    """
    POST the GraphQL payload. Adds Origin/Referer. Prints status per product.
    Applies small backoff/jitter on non-200.
    """
    headers = {
        "Origin": "https://shop.lululemon.com",
        "Referer": "https://shop.lululemon.com/",
    }
    r = session.post(
        "https://shop.lululemon.com/cne/graphql",
        json=payload,
        headers=headers,
        timeout=25,
    )
    print(f"Status: {r.status_code} for {prod_code}")

    if r.status_code == 200:
        return r

    # Print a short preview of the body to see bot/blocked pages
    try:
        snippet = r.text[:300].replace("\n", " ")
        if snippet:
            print(f"Non-200 body (first 300 chars): {snippet}")
    except Exception:
        pass

    # Backoff for common block statuses
    if r.status_code in (401, 403, 429):
        time.sleep(min(6, 0.8 * attempt + random.uniform(0, 0.5)))
    else:
        time.sleep(0.5)

    r.raise_for_status()
    return r

def fetch_summary(prod_code: str) -> dict:
    variables = {
        "id": prod_code,
        "category": "",
        "unifiedId": "",
        "locale": "en-us",
    }
    payload = {"query": GRAPHQL_QUERY, "variables": variables}

    for attempt in range(1, MAX_RETRIES + 2):
        try:
            r = post_graphql(payload, attempt=attempt, prod_code=prod_code)
            data = r.json()
            if "errors" in data and data["errors"]:
                # GraphQL error payload
                raise RuntimeError(data["errors"])
            return (data.get("data", {})
                        .get("productDetailPage", {})
                        .get("productSummary", {}) or {})
        except requests.HTTPError:
            if attempt >= (MAX_RETRIES + 1):
                raise
            time.sleep(0.5 * attempt + random.uniform(0, 0.4))

    return {}

# =========================
# Main
# =========================
def main():
    print(f"Working dir : {Path.cwd()}")
    print(f"Script dir  : {SCRIPT_DIR}")
    print(f"Input CSV   : {INPUT_CSV}")
    print(f"Output CSV  : {OUTPUT_CSV}")
    print(f"Failures CSV: {FAIL_CSV}")

    codes_raw = read_codes(INPUT_CSV)
    print(f"Found {len(codes_raw)} codes")

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as out_f, \
         open(FAIL_CSV, "w", newline="", encoding="utf-8") as fail_f:

        out_writer = csv.writer(out_f, quoting=csv.QUOTE_ALL)  # QUOTE_ALL avoids delimiter issues
        out_writer.writerow(["productId", "displayName", "tags"])

        fail_writer = csv.writer(fail_f, quoting=csv.QUOTE_ALL)
        fail_writer.writerow(["input_code", "reason"])

        ok, failed = 0, 0

        for raw in codes_raw:
            # Slow down between products; add slight jitter
            time.sleep(SLEEP_BETWEEN_CALLS + random.uniform(0, 0.25))

            # Normalise product code
            try:
                prod_code = extract_prod(raw)
            except Exception as e:
                failed += 1
                fail_writer.writerow([raw, f"Normalize error: {e}"])
                continue

            # Fetch summary
            try:
                summary = fetch_summary(prod_code)
                if not summary:
                    failed += 1
                    fail_writer.writerow([raw, "No summary in response"])
                    continue

                product_id = ((summary.get("productId") or "").upper()) + "_LULU"
                display_name = summary.get("displayName", "") or ""

                tags_list = combine_unique(
                    summary.get("activity"),
                    summary.get("gender"),
                    summary.get("productCategory"),
                )
                tags = ", ".join(tags_list)

                out_writer.writerow([product_id, display_name, tags])
                ok += 1

            except Exception as e:
                failed += 1
                fail_writer.writerow([raw, f"Request/parse error: {e}"])

    print(f"Done. OK: {ok}, Failed: {failed}")
    print(f"Output written to : {OUTPUT_CSV}")
    print(f"Failures written to: {FAIL_CSV}")

if __name__ == "__main__":
    init_session()
    main()

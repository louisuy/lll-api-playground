import requests
import csv
import time
from datetime import datetime
from typing import Optional

try:
    from zoneinfo import ZoneInfo  # Python 3.9+
except ImportError:
    ZoneInfo = None

# ============================
# CONFIG: FILL THESE IN
# ============================
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
    'AKA_A2': 'A',
    'ak_bmsc': '9E6865ACEFCC54963058D7A285F2E1E5~000000000000000000000000000000~YAAQHucVAldLWF2aAQAAQsFYdB0pvmD6w7K5NZUpt2kIoQZS4uJlVN+FS/3Z9yGRsNdJ2/5AyFo2A8XVMy93pXFe3RGoi4M4yvRM8nfxYJN/M7hM28JlsAwlOUgkofN18NYcPAEAzA2csp1lMYFNBrE4naVsosYdyZhNwPMgYc0xs8Jyi35QDX+I1BIUTRGfgwO+6aRRdRySiyZ2I5ww74wrodj6Khrtx82jbylZtqZpEwzEiSDSE65Ait6EJWSoQejkrbYCKZpby5MrnrfK9IdBxJBSW3CVCBOG9B9Q/HJu4Ks+c+Uff0XsYCERZz2N85Qn6n13RKIo/BjDWAwICNeJrsTc3IQnfq07vSMZzxqDVHRWMqtcuEqvWEs1ILt+E8RM7kT122LR2WqxDgUE',
    'bm_mi': 'E127FE28D9126B0E61DAD9E071831C81~YAAQHucVAilSWF2aAQAAbwdZdB0JSfJvU/DfbG4qz6bdFde26ncZDk16F8JcPpF/NYPys147SsYu+qPnovh7J9QfXedFTd/f3ffduuZtx/7UQZJhn4Yfc4TTDjG8dFtJpnys72F6MZQpD8FVSDEOe2nQcgDVCZ3be9fzfd3GV6Clp6TJ9ReeZYR0MgPP22hxoWxmicNX4EUKi5kH/9RhDMF7E5S+jsAlazSbDZU6iak1KrsTngz4P9LEhY2tvN4a4ueFoTXjhiJDOjNub042BzYZG9ul7d+KaqI1kisXUEGPN8bDty4+K4F+B1ox68SH2VeK7Q==~1',
    'bm_sv': '9AFA58024A4DC16DAFAF4A9F0680C94C~YAAQHucVAlpUWF2aAQAAbClZdB1K1XtSXLJTSmq7vtiYWDvCQitrVgZHgD+h74QBRNu/JktAeYHrF1joV5Yu9SWYmqAF2qqu5v2Q7pHtqOFNkyFlZ1YVhavYposdkDFUM0sRmxP2r7D7n0n+RwKm+eLriRMN7kqoXDAg5LxhEBKoBfR9BhVyZGiW1I6RmLpAGiDuLfBRcBiCy9aRS0OYv24Dz3LEytmJaAEUqnxIthQaAuQngRxXziSqk0sEqmC6xpLV~1',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6UXpRekpFTlVNeE16aEdOemcwUlRjeVF6VXdRVEkyTWpoRlJEZEROVE0xTVVNM1F6TTJPUSJ9.eyJodHRwczovL21hZi5ncmF2dHkuYXV0aC9kZXYvYXBpL21lbWJlcklkIjoiOTQ3ODQwMDA1NjA0MjMwOCIsImh0dHBzOi8vbWFmLmdyYXZ0eS5hdXRoL2Rldi9hcGkvdm94TWVtYmVySWQiOiJTSEFSRUs0V0JONzREREIiLCJodHRwczovL21hZi5ncmF2dHkuYXV0aC9kZXYvYXBpL3ZveENhcmROdW1iZXIiOiI5NDc4NDAwMDU2MDQyMzA4IiwiaHR0cHM6Ly9tYWYuZ3JhdnR5LmF1dGgvZGV2L2FwaS9lbWFpbCI6ImFudGhvbnkubG91aXNAbWFmLmFlIiwiaHR0cHM6Ly9tYWYuZ3JhdnR5LmF1dGgvZGV2L2FwaS91dWlkIjoiODAxY2VlODAtNjI1NC0xMWYwLWI0NmYtNTE1NmRlOWYyZGIyIiwiaHR0cHM6Ly9tYWYuaWRlbnRpdHkuYXV0aC9kZXYvYXBpL3V1aWQiOiI4MDFjZWU4MC02MjU0LTExZjAtYjQ2Zi01MTU2ZGU5ZjJkYjIiLCJodHRwczovL21hZi5pZGVudGl0eS5hdXRoL2Rldi9hcGkvZW1haWxfdmVyaWZpZWQiOnRydWUsImh0dHBzOi8vbWFmLmlkZW50aXR5LmF1dGgvZGV2L2FwaS9lbWFpbCI6ImFudGhvbnkubG91aXNAbWFmLmFlIiwiaHR0cHM6Ly9tYWYuaWRlbnRpdHkuYXV0aC9kZXYvYXBpL3JpZCI6ImZkZWI3ODE4LWZhZmItNGMzZS04N2U1LTdlMjhkY2JmNGMxNiIsImh0dHBzOi8vbWFmLmlkZW50aXR5LmF1dGgvZGV2L2FwaS9taXJha2xfc2hvcF9pZCI6bnVsbCwiaHR0cHM6Ly9tYWYuaWRlbnRpdHkuYXV0aC9kZXYvYXBpL3RpbWUiOiIyMDI1LTExLTExVDE5OjE2OjA3LjYzOVoiLCJpc3MiOiJodHRwczovL2lkZW50aXR5Lm1hamlkYWxmdXR0YWltLmNvbS8iLCJzdWIiOiJhdXRoMHw2ODY0ZjM5NTdhOTg1ZDhlODJhMmExMGUiLCJhdWQiOlsibWFmaWQiLCJodHRwczovL3Byb2R1Y3Rpb24ubWFmLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3NjI4ODg1NjcsImV4cCI6MTc2Mjg5MDM2Nywic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBvZmZsaW5lX2FjY2VzcyIsImF6cCI6Imtmd1BNdUNWYnhOUHZQcGZES2l5dmdWdkhXbVRoWGM4In0.lPBalW5z2HI3rLFMCkeAcrcDTLVYQMhAa3Di0I9NOXrI-ZhGF-EyuXua-QFYHHX-3T5qUl-Re0IpcP4SK3kC7V_unNv77AZ2umSU8EubzMG0Z5ZB-Yy4zpHkWP_3j-2CO5nbi2nHa-k_VJbl_mAQVzS8798CbME26ele06G2IgF71Fj-Uh2AWS98R2hA1ISe_Z5Hcnv0pmgF58cPQ1Uj5IFReUyHquYO8IGgMsWu_CCu7QkyWEXPLoEFUImHYWVj2C9CX1_6oF-rAui2HfIw2tJD3C120_SZ3NTTxQrXug0WmKj6qxTQRd6hvNSoEp6zfNOJZSeegx18CBtICki6Vw',
    'content-type': 'application/json',
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
    # 'cookie': 'nt_page_init_referrer=NeotagEncrypt%3AU2FsdGVkX1%2BsJwiJkVZpz%2B%2Bbgy26OZ1VdMaIGEZ5G64%3D; nt_page_init_referring_domain=NeotagEncrypt%3AU2FsdGVkX18z0G7ItqAY0GZere%2F5gC6IHvmoDdxwz%2Fc%3D; _ga=GA1.1.1964284017.1751977271; _tt_enable_cookie=1; _ttp=01JZMZQ8178KYJ2S8ZNE1TC4EV_.tt.1; _scid=F-dYMQitund0c-17xRDg3gr8FLD-1qh1; _sctr=1%7C1751918400000; neo_sc=NeotagEncrypt%3AU2FsdGVkX1%2FSVMITZlMnRj1DpLfwRLEh4vJO3vgTAdw%3D; nt_user_id=NeotagEncrypt%3AU2FsdGVkX1%2Bl1GenLaZa9YL7qkAgMD857ERl7m%2FKqlk%3D; nt_trait=NeotagEncrypt%3AU2FsdGVkX19ONc%2FZtoEt%2FdheRbkyGQ2XVL%2FY4Fdx3cg%3D; nt_group_id=NeotagEncrypt%3AU2FsdGVkX18%2B19WtTv9%2B4BT5wvQKOz1wKapi74J2yx0%3D; nt_group_trait=NeotagEncrypt%3AU2FsdGVkX19A7iN%2FL5xMJ2H99UjnRFkcgXlC7v4I3JU%3D; nt_anonymous_id=NeotagEncrypt%3AU2FsdGVkX19VnO6xUz4vy1MZLX0SGVccz92Qr5t6yG2hVBS9bxiz%2BlFd%2BJ5SdkrUlYyjq3evmYkQJ2Ybvc13kA%3D%3D; _scid_r=FGdYMQitund0c-17xRDg3gr8FLD-1qh1gAj9Pw; _ga_JCZ0JR3KPC=GS2.1.s1752143860$o6$g1$t1752144070$j60$l0$h644044425; neo_session=NeotagEncrypt%3AU2FsdGVkX19msusgSkvean2%2F5tdsMTQAg8RjOmalFQPUFho5k5hJ3XrNwCbB7lmKTE2N8eZC2avEW5Ii42SXvZzKHN9K1bDnSuQXZ2GDAtf8SAzZkRAYETIvCvuDbvhg28tpbLvGd6gajIzIxC4Y%2FA%3D%3D; ttcsid=1752143732995::GvDKpVQEAsFuffv1TpkV.7.1752144233285; ttcsid_CC1ON5JC77U4JJ3BHHHG=1752143732994::Zef3YwuLXz7Nq0eIDojm.6.1752144234551; _ga_RC54V0M6CC=GS2.1.s1752143731$o6$g1$t1752144252$j60$l0$h0; _ga_083HX4D5KG=GS2.1.s1752143731$o1$g1$t1752144252$j41$l0$h1241084185; rr_rcs=eF5jYSlN9kg2MzIySDE30E1LNDHSNUlJSdFNMjIw0zU3MTNNSzRPtUxONuPKLSvJTBEwMrA01TXUNQQAnasOlA; ROUTE=.api-784b947787-pxfl7; AKA_A2=A; ak_bmsc=9E6865ACEFCC54963058D7A285F2E1E5~000000000000000000000000000000~YAAQHucVAldLWF2aAQAAQsFYdB0pvmD6w7K5NZUpt2kIoQZS4uJlVN+FS/3Z9yGRsNdJ2/5AyFo2A8XVMy93pXFe3RGoi4M4yvRM8nfxYJN/M7hM28JlsAwlOUgkofN18NYcPAEAzA2csp1lMYFNBrE4naVsosYdyZhNwPMgYc0xs8Jyi35QDX+I1BIUTRGfgwO+6aRRdRySiyZ2I5ww74wrodj6Khrtx82jbylZtqZpEwzEiSDSE65Ait6EJWSoQejkrbYCKZpby5MrnrfK9IdBxJBSW3CVCBOG9B9Q/HJu4Ks+c+Uff0XsYCERZz2N85Qn6n13RKIo/BjDWAwICNeJrsTc3IQnfq07vSMZzxqDVHRWMqtcuEqvWEs1ILt+E8RM7kT122LR2WqxDgUE; bm_mi=E127FE28D9126B0E61DAD9E071831C81~YAAQHucVAilSWF2aAQAAbwdZdB0JSfJvU/DfbG4qz6bdFde26ncZDk16F8JcPpF/NYPys147SsYu+qPnovh7J9QfXedFTd/f3ffduuZtx/7UQZJhn4Yfc4TTDjG8dFtJpnys72F6MZQpD8FVSDEOe2nQcgDVCZ3be9fzfd3GV6Clp6TJ9ReeZYR0MgPP22hxoWxmicNX4EUKi5kH/9RhDMF7E5S+jsAlazSbDZU6iak1KrsTngz4P9LEhY2tvN4a4ueFoTXjhiJDOjNub042BzYZG9ul7d+KaqI1kisXUEGPN8bDty4+K4F+B1ox68SH2VeK7Q==~1; bm_sv=9AFA58024A4DC16DAFAF4A9F0680C94C~YAAQHucVAlpUWF2aAQAAbClZdB1K1XtSXLJTSmq7vtiYWDvCQitrVgZHgD+h74QBRNu/JktAeYHrF1joV5Yu9SWYmqAF2qqu5v2Q7pHtqOFNkyFlZ1YVhavYposdkDFUM0sRmxP2r7D7n0n+RwKm+eLriRMN7kqoXDAg5LxhEBKoBfR9BhVyZGiW1I6RmLpAGiDuLfBRcBiCy9aRS0OYv24Dz3LEytmJaAEUqnxIthQaAuQngRxXziSqk0sEqmC6xpLV~1',
}

# Search config
BASE_URL = "https://api.allsaints.me/rest/v2/alls/products/search"
QUERY = ":relevance"  # keep ":relevance" for no filters; use ":relevance:allCategories:on-sale" for sale only
PAGE_SIZE = 9999
CURRENCY = "AED"
LANG = "en"

# Loudness controls
PRINT_EVERY_PRODUCT = True   # Print a line for each product processed
SLEEP_BETWEEN_REQUESTS = 0.15  # seconds, helpful to be polite to the API

# Retry config
MAX_RETRIES = 3
RETRY_BACKOFF = 1.0  # seconds


def timestamp_str() -> str:
    if ZoneInfo:
        now = datetime.now(ZoneInfo("Asia/Dubai"))
    else:
        now = datetime.now()
    return now.strftime("%Y%m%d_%H%M%S")


def safe_price(obj: Optional[dict]) -> Optional[float]:
    """Return numeric value from {'value': ...} or None."""
    if not isinstance(obj, dict):
        return None
    v = obj.get("value")
    try:
        return float(v) if v is not None else None
    except (TypeError, ValueError):
        return None


def get_page(page: int, params: dict) -> dict:
    """GET with basic retries and loud prints."""
    attempt = 0
    while True:
        attempt += 1
        print(f"[HTTP] Requesting page {page} (attempt {attempt}) ...", flush=True)
        try:
            resp = requests.get(
                BASE_URL, cookies=cookies, headers=headers, params={**params, "currentPage": page}, timeout=30
            )
            print(f"[HTTP] Status: {resp.status_code}", flush=True)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            print(f"[HTTP] Error on page {page}: {e}", flush=True)
            if attempt >= MAX_RETRIES:
                print("[HTTP] Max retries reached. Aborting.", flush=True)
                raise
            sleep_for = RETRY_BACKOFF * attempt
            print(f"[HTTP] Retrying in {sleep_for:.1f}s ...", flush=True)
            time.sleep(sleep_for)


def main():
    print("=== ALLSAINTS PRODUCTS EXTRACTOR (LOUD MODE) ===", flush=True)
    print(f"[SETUP] Base URL: {BASE_URL}", flush=True)
    print(f"[SETUP] Query: {QUERY}", flush=True)
    print(f"[SETUP] Page size: {PAGE_SIZE}, Lang: {LANG}, Currency: {CURRENCY}", flush=True)

    params = {
        "fields": (
            "keywordRedirectUrl,"
            "products(baseOptions(FULL),baseProduct,code,earnablePoints,sellable,maxOrderQuantity,name,summary,"
            "price(FULL),badges(code,name),images(DEFAULT),stock(FULL),averageRating,crossedPrice(FULL),"
            "categories(name,code,url),discountRate,breadcrumbs),"
            "facets,pagination(DEFAULT),sorts(DEFAULT),freeTextSearch"
        ),
        "query": QUERY,
        "pageSize": PAGE_SIZE,
        "lang": LANG,
        "curr": CURRENCY,
    }

    stamp = timestamp_str()
    outfile = f"alls_products_{stamp}.csv"
    print(f"[IO] Output file will be: {outfile}", flush=True)

    rows = []
    page = 0
    total_pages_known = None
    total_seen = 0

    while True:
        print(f"\n[STEP] Fetching page {page}", flush=True)
        data = get_page(page, params)

        # Discover total pages on first pass
        pag = data.get("pagination") or {}
        if total_pages_known is None:
            total_pages_known = pag.get("totalPages")
            total_results = pag.get("totalResults")
            print(f"[PAGINATION] totalPages: {total_pages_known}, totalResults: {total_results}", flush=True)

        products = data.get("products") or []
        print(f"[STEP] Page {page} returned {len(products)} products", flush=True)

        for idx, prod in enumerate(products, start=1):
            base_product = prod.get("baseProduct") or ""
            name = prod.get("name") or ""
            crossed_val = safe_price(prod.get("crossedPrice"))
            price_val = safe_price(prod.get("price"))

            discount_pct = ""
            if (crossed_val is not None) and (price_val is not None) and crossed_val > 0 and price_val <= crossed_val:
                pct = round((crossed_val - price_val) / crossed_val * 100)
                discount_pct = f"{pct}%"

            row = {
                "baseProduct": base_product,
                "name": name,
                "crossedPrice_value": crossed_val if crossed_val is not None else "",
                "price_value": price_val if price_val is not None else "",
                "discount": discount_pct,
            }
            rows.append(row)
            total_seen += 1

            if PRINT_EVERY_PRODUCT:
                print(
                    f"[PRODUCT] {total_seen:04d} | baseProduct={base_product!s} | "
                    f"name={name!s} | crossed={crossed_val!s} | price={price_val!s} | discount={discount_pct}",
                    flush=True,
                )

        # Decide next page
        if total_pages_known is None:
            # Safety fallback
            if not products:
                print("[PAGINATION] No products; stopping.", flush=True)
                break
        else:
            if page >= (total_pages_known - 1):
                print("[PAGINATION] Last page reached.", flush=True)
                break

        page += 1
        if SLEEP_BETWEEN_REQUESTS:
            print(f"[SLEEP] Sleeping {SLEEP_BETWEEN_REQUESTS:.2f}s before next page ...", flush=True)
            time.sleep(SLEEP_BETWEEN_REQUESTS)

    print(f"\n[IO] Writing CSV with {len(rows)} rows -> {outfile}", flush=True)
    with open(outfile, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["baseProduct", "name", "crossedPrice_value", "price_value", "discount"],
        )
        writer.writeheader()
        writer.writerows(rows)

    print("[DONE] CSV write complete.", flush=True)
    print(f"[SUMMARY] Total products processed: {total_seen}", flush=True)
    print(f"[SUMMARY] Output file: {outfile}", flush=True)
    print("=== FINISHED ===", flush=True)


if __name__ == "__main__":
    main()

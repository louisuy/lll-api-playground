#!/usr/bin/env python3
import json
import csv
from pathlib import Path

VAR = "lululemonME_2025-11-24_180710" #"lululemonME_2025-10-20_165449.json"
INPUT_JSON = VAR+".json"   # put your JSON file here
OUTPUT_CSV = VAR+".csv"   # will be created/overwritten

def join_list(vals):
    """Join a list of strings with commas, safely."""
    return ", ".join([str(v) for v in vals if v is not None])

def extract_qualifiers(quals):
    """Turn variantOptionQualifiers into a simple dict."""
    qmap = {}
    for q in quals or []:
        qual = q.get("qualifier")
        if not qual:
            continue
        # store both a 'value' and (when present) a 'name' (e.g., color)
        qmap[qual] = q.get("value")
        if "name" in q:
            qmap[f"{qual}_name"] = q.get("name")
    return qmap

def main():
    data = json.loads(Path(INPUT_JSON).read_text(encoding="utf-8"))
    products = data.get("products", [])

    rows = []

    for p in products:
        # --- Product-level fields ---
        product_name = p.get("name")
        base_product = p.get("baseProduct")

        # price (product-level)
        pprice = p.get("price") or {}
        product_price_currency = pprice.get("currencyIso")
        product_price_formatted = pprice.get("formattedValue")
        product_price_type = pprice.get("priceType")
        product_price_value = pprice.get("value")

        # badges and categories
        badges_list = [b.get("name") for b in (p.get("badges") or []) if b.get("name")]
        categories_list = [c.get("name") for c in (p.get("categories") or []) if c.get("name")]
        category_codes_list = [c.get("code") for c in (p.get("categories") or []) if c.get("code")]

        # --- Options (each becomes a row) ---
        for base_opt in p.get("baseOptions") or []:
            for opt in base_opt.get("options") or []:
                # option-level fields
                option_code = opt.get("code")
                option_product_name = opt.get("productName")
                option_sellable = opt.get("sellable")

                # option price
                oprice = opt.get("priceData") or {}
                option_price_value = oprice.get("value")

                # option stock
                stock = opt.get("stock") or {}
                option_stock_status = stock.get("stockLevelStatus")

                # qualifiers (e.g., color, size)
                qmap = extract_qualifiers(opt.get("variantOptionQualifiers") or [])
                color_value = qmap.get("color")
                color_name = qmap.get("color_name") or qmap.get("color_name")  # safe default
                size_value = qmap.get("size")

                row = {
                    # product-level (repeated)
                    "product_name": product_name,
                    "baseProduct": base_product,
                    "product_price_currency": product_price_currency,
                    "product_price_formatted": product_price_formatted,
                    "product_price_type": product_price_type,
                    "product_price_value": product_price_value,
                    "badges": join_list(badges_list),
                    "categories": join_list(categories_list),
                    "category_codes": join_list(category_codes_list),
                    # option-level
                    "option_code": option_code,
                    "option_productName": option_product_name,
                    "option_sellable": option_sellable,
                    "option_stock_status": option_stock_status,
                    "option_price_value": option_price_value,
                    "color_name": color_name,
                    "color_value": color_value,
                    "size": size_value,
                }
                rows.append(row)

    # Fixed column order for clean CSVs
    fieldnames = [
        "product_name",
        "baseProduct",
        "product_price_currency",
        "product_price_formatted",
        "product_price_type",
        "product_price_value",
        "badges",
        "categories",
        "category_codes",
        "option_code",
        "option_productName",
        "option_sellable",
        "option_stock_status",
        "option_price_value",
        "color_name",
        "color_value",
        "size",
    ]

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()

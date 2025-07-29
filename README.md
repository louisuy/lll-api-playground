# LLL GraphQL Scraper

A lightweight Python tool to extract product IDs from [LLL](https://shop.lululemon.com)'s GraphQL API using a user-supplied category URL and browser session data (cookies and headers).

---

## ✨ Features

- 🧠 Automatically extracts `category` and `cdpHash` from any LLL category URL  
- 📋 Accepts cookies and headers copied from browser cURL (via [curlconverter.com](https://curlconverter.com))  
- 🗂️ Exports product IDs into a CSV file  
- ⚙️ Simple, dependency-light structure for developers

---

## 🛠️ Setup

### 1. Clone the repo

### 2. Install dependencies

```bash
pip install pandas requests
```

---

## 🚀 Usage

1. Go to any LLL category page (e.g. [Men's Casual](https://shop.lululemon.com/c/men-casual-clothes/n1oxc7zyk1r))
2. Open DevTools → Network tab → Copy a GraphQL `fetch` or `XHR` request as **cURL (bash)**
3. Paste it into [curlconverter.com](https://curlconverter.com) and copy the **Python `requests`** output
4. Replace the `cookies = {}` and `headers = {}` placeholders in `main.py` with the converted data
5. Run the script.
6. Enter the full LLL category URL when prompted
7. Output: `your-category_product_ids.csv`

---

## 🧾 Example Output

```csv
productId
LW3DNLS
LW2EQMS
LM123ABC
...
```

---

## 📁 Output File

* Filename: `{category}_product_ids.csv`
* Example: `men-casual-clothes_product_ids.csv`

---

## 📌 Notes

* This script relies on **your browser session's cookies** to access category data.
* LLL's API may change — this is meant for educational and research purposes only.
* You must respect LLL’s [Terms of Service](https://shop.lululemon.com/legal/terms-of-use).

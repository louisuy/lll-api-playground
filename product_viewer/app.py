from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load product codes from Excel
df = pd.read_excel("product_codes.xlsx")
codes = df.iloc[:, 0].dropna().tolist()

# Build product URLs
urls = [f"https://www.lululemon.me/en-ae/product/_/{code}" for code in codes]

@app.route("/")
def index():
    return render_template("index.html", total=len(urls))

@app.route("/get_product", methods=["POST"])
def get_product():
    index = int(request.json.get("index", 0))
    if 0 <= index < len(urls):
        return jsonify({
            "index": index,
            "url": urls[index]
        })
    return jsonify({"error": "Out of range"})

if __name__ == "__main__":
    app.run(debug=True)

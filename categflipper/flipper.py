import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pandas as pd
import requests
from io import BytesIO
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ProductFlipper:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Image Flipper")
        self.root.geometry("800x600")

        # UI Elements
        self.label = tk.Label(root, text="Load an Excel file with product codes", font=("Arial", 14))
        self.label.pack(pady=10)

        self.load_button = tk.Button(root, text="Load Excel", command=self.load_excel)
        self.load_button.pack(pady=5)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=20, expand=True)

        self.nav_frame = tk.Frame(root)
        self.nav_frame.pack(pady=10)

        self.prev_button = tk.Button(self.nav_frame, text="⬅ Previous", command=self.prev_image, state="disabled")
        self.prev_button.grid(row=0, column=0, padx=10)

        self.next_button = tk.Button(self.nav_frame, text="Next ➡", command=self.next_image, state="disabled")
        self.next_button.grid(row=0, column=1, padx=10)

        # State
        self.codes = []
        self.current_index = 0
        self.driver = None

    def load_excel(self):
        filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if not filepath:
            return

        try:
            df = pd.read_excel(filepath)
            self.codes = df.iloc[:, 0].dropna().tolist()
            if not self.codes:
                raise ValueError("No product codes found in first column")

            # Setup Selenium
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")  # don’t open a visible browser
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

            self.current_index = 0
            self.show_image()

            self.next_button.config(state="normal")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def fetch_image_url(self, code):
        url = f"https://www.lululemon.me/en-ae/product/_/{code}"
        self.driver.get(url)
        time.sleep(3)
        try:
            img = self.driver.find_element(By.XPATH, '//*[@id="swiper-zoom"]/div[2]/div/div[1]/div/picture/img')
            return img.get_attribute("src")
        except:
            return None

    def show_image(self):
        code = self.codes[self.current_index]
        self.label.config(text=f"Code: {code}")

        img_url = self.fetch_image_url(code)
        if img_url:
            try:
                response = requests.get(img_url, timeout=10)
                image = Image.open(BytesIO(response.content))
                image = image.resize((500, 500), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)

                self.image_label.config(image=photo)
                self.image_label.image = photo
            except:
                self.image_label.config(text="Could not load image", image="")
        else:
            self.image_label.config(text="Image not found", image="")

        # Enable/disable buttons
        self.prev_button.config(state="normal" if self.current_index > 0 else "disabled")
        self.next_button.config(state="normal" if self.current_index < len(self.codes) - 1 else "disabled")

    def next_image(self):
        if self.current_index < len(self.codes) - 1:
            self.current_index += 1
            self.show_image()

    def prev_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_image()


if __name__ == "__main__":
    root = tk.Tk()
    app = ProductFlipper(root)
    root.mainloop()

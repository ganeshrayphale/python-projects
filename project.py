import os
import cv2
import requests
import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import platform

# ---------------- CONFIGURATION ----------------
CORRECT_PASSWORD = "asepg3"
EMAIL_ADDRESS = "ganray112@gmail.com"
EMAIL_PASSWORD = "lbfb sift sgmu urzt"
RECEIVER_EMAIL = "ganeshrayphale123@gmail.com"
IMAGE_PATH = "intruder.jpg"
BACKGROUND_IMAGE = "image.png"  # <-- Replace with your Windows-like background image path

# ---------------- LOCATION MODULE ----------------
def get_location():
    try:
        res = requests.get('https://ipinfo.io')
        data = res.json()
        location = data.get('loc', 'Unknown location')
        city = data.get('city', 'Unknown city')
        region = data.get('region', 'Unknown region')
        return f"Location: {location}\nCity: {city}\nRegion: {region}"
    except Exception as e:
        return f"Location tracking failed: {e}"

# ---------------- CAMERA MODULE ----------------
def capture_image(filename=IMAGE_PATH):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        cv2.imwrite(filename, frame)
    cam.release()

# ---------------- EMAIL MODULE ----------------
def send_email(subject, body, image_path=None):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECEIVER_EMAIL

        if image_path and os.path.exists(image_path):
            with open(image_path, 'rb') as img:
                msg.add_attachment(img.read(), maintype='image', subtype='jpeg', filename='intruder.jpg')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print("Email sent successfully.")
    except Exception as e:
        print(f"Email failed: {e}")

# ---------------- UI AND LOGIC ----------------
class LockScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows Lock Screen")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.failed_attempts = 0

        # Set background image to simulate Windows lock screen
        self.bg_image = Image.open(BACKGROUND_IMAGE)
        self.bg_image = self.bg_image.resize((600, 400), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.photo, anchor="nw")

        # Overlay lock screen components
        self.label = tk.Label(root, text="Enter Password", fg="white", bg="black", font=("Segoe UI", 14, "bold"))
        self.label_window = self.canvas.create_window(300, 200, window=self.label)

        self.password_entry = tk.Entry(root, show="*", width=25, font=("Segoe UI", 12))
        self.entry_window = self.canvas.create_window(300, 240, window=self.password_entry)
        self.password_entry.focus()

        self.submit_button = tk.Button(root, text="Unlock", command=self.check_password, font=("Segoe UI", 10))
        self.button_window = self.canvas.create_window(300, 280, window=self.submit_button)

    def check_password(self):
        entered_password = self.password_entry.get()
        if entered_password == CORRECT_PASSWORD:
            messagebox.showinfo("Access Granted", "Welcome!")
            self.root.destroy()
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                self.handle_intruder()
                messagebox.showwarning("Access Denied", "Too many failed attempts. Alert sent!")
                self.root.destroy()
            else:
                messagebox.showerror("Access Denied", f"Incorrect password. Attempt {self.failed_attempts}/3")

    def handle_intruder(self):
        capture_image()
        location_info = get_location()
        send_email(
            subject="⚠ Intrusion Detected - Unauthorized Access Attempt",
            body=f"Three failed login attempts detected.\n\n{location_info}",
            image_path=IMAGE_PATH
        )

# ---------------- MAIN ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = LockScreen(root)
    root.mainloop()

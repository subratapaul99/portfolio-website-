"""
Subrata Paul — Portfolio Backend
Flask server with contact form email API
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import re

# Load .env from the SAME folder as server.py — fixes "not found" issue
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Debug — confirms values loaded (you can remove these lines after it works)
print(f"DEBUG EMAIL_ADDRESS = {os.getenv('EMAIL_ADDRESS')}")
print(f"DEBUG EMAIL_PASSWORD = {'SET ✓' if os.getenv('EMAIL_PASSWORD') else 'NOT SET ✗'}")

app = Flask(__name__)
CORS(app, origins="*")


def is_valid_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return bool(re.match(pattern, email))


def send_email(sender_name: str, sender_email: str, message: str) -> bool:
    your_email    = os.getenv("EMAIL_ADDRESS")
    your_password = os.getenv("EMAIL_PASSWORD")

    if not your_email or not your_password:
        print("ERROR: EMAIL_ADDRESS or EMAIL_PASSWORD not set in .env")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Portfolio Contact — {sender_name}"
    msg["From"]    = your_email
    msg["To"]      = your_email

    text_body = f"""
New message from your portfolio contact form:

Name:    {sender_name}
Email:   {sender_email}
Message:
{message}
    """.strip()

    html_body = f"""
    <div style="font-family:sans-serif;max-width:520px;margin:0 auto;padding:32px 24px;background:#f7f5f0;border-radius:8px;">
      <h2 style="margin:0 0 24px;font-size:1.4rem;color:#0d0d0b;">New message from your portfolio</h2>
      <table style="width:100%;font-size:0.9rem;color:#444;">
        <tr><td style="padding:8px 0;color:#888;width:80px;">Name</td><td style="padding:8px 0;font-weight:600;color:#0d0d0b;">{sender_name}</td></tr>
        <tr><td style="padding:8px 0;color:#888;">Email</td><td style="padding:8px 0;"><a href="mailto:{sender_email}" style="color:#e8430a;">{sender_email}</a></td></tr>
      </table>
      <div style="margin-top:20px;padding:20px;background:#fff;border-radius:6px;border-left:3px solid #e8430a;">
        <p style="margin:0;font-size:0.9rem;line-height:1.7;color:#333;white-space:pre-wrap;">{message}</p>
      </div>
    </div>
    """

    msg.attach(MIMEText(text_body, "plain"))
    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(your_email, your_password)
            server.sendmail(your_email, your_email, msg.as_string())
        print("Email sent successfully!")
        return True
    except smtplib.SMTPAuthenticationError:
        print("ERROR: Gmail authentication failed. Check your App Password.")
        return False
    except Exception as e:
        print(f"ERROR sending email: {e}")
        return False


@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "Portfolio backend is running."})


@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"success": False, "message": "No data received."}), 400

    name    = data.get("name", "").strip()
    email   = data.get("email", "").strip()
    message = data.get("message", "").strip()

    if not name:
        return jsonify({"success": False, "message": "Name is required."}), 400
    if not email or not is_valid_email(email):
        return jsonify({"success": False, "message": "A valid email is required."}), 400
    if not message or len(message) < 10:
        return jsonify({"success": False, "message": "Message must be at least 10 characters."}), 400
    if len(message) > 2000:
        return jsonify({"success": False, "message": "Message is too long (max 2000 chars)."}), 400

    sent = send_email(name, email, message)

    if sent:
        return jsonify({"success": True, "message": "Message sent! I'll get back to you soon."}), 200
    else:
        return jsonify({"success": False, "message": "Server error — please email me directly."}), 500


if __name__ == "__main__":
    print("\n🚀  Portfolio backend running at http://localhost:5000")
    print("📬  POST /contact  to send a message\n")
    app.run(debug=True, port=5000)

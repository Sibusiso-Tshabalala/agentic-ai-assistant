# 📄 pages/8_📤_Export_Trip.py
import streamlit as st
from fpdf import FPDF
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from components import navbar, footer
import os

st.set_page_config(page_title="Export Trip", layout="wide")
navbar.render()

st.title("📤 Export Your Trip")

trip_data_file = "trip_data.txt"

if os.path.exists(trip_data_file):
    with open(trip_data_file, "r") as f:
        trip_text = f.read()
else:
    st.warning("No saved trip data found.")
    trip_text = ""

# Export as PDF
if st.button("📄 Export as PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in trip_text.splitlines():
        pdf.multi_cell(0, 10, line)
    pdf_path = "exported_trip.pdf"
    pdf.output(pdf_path)
    with open(pdf_path, "rb") as f:
        st.download_button("⬇️ Download PDF", f, file_name="trip.pdf")

# Email
st.subheader("📧 Email Trip Plan")
recipient = st.text_input("Recipient Email")
sender = st.text_input("Your Email")
password = st.text_input("Email App Password", type="password")

if st.button("Send Email"):
    if recipient and sender and password:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = "Your Trip Plan"

        body = MIMEText("Here is your planned trip.", 'plain')
        msg.attach(body)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in trip_text.splitlines():
            pdf.multi_cell(0, 10, line)
        pdf_path = "trip_email.pdf"
        pdf.output(pdf_path)

        with open(pdf_path, "rb") as f:
            part = MIMEApplication(f.read(), Name="TripPlan.pdf")
            part['Content-Disposition'] = 'attachment; filename="TripPlan.pdf"'
            msg.attach(part)

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(sender, password)
                server.send_message(msg)
            st.success("Email sent successfully!")
        except Exception as e:
            st.error(f"Failed to send email: {e}")
    else:
        st.warning("Please fill in all fields.")

footer.render()

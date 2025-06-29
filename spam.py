import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "minendra2062@gmail.com"
APP_PASSWORD="fsak ataf ltkb bwxc"
RECIPIENT_EMAIL = "satkritikhadka2061@gmail.com"

msg=EmailMessage()
msg['subject']="🤑 You Just Won $10,000 in the International Lotto Draw!"
msg['From']=SENDER_EMAIL
msg['To']=RECIPIENT_EMAIL
msg.set_content("Congratulations!Your email address was selected in the INTERNATIONAL ONLINE LOTTERY. You have won $500,000 USD!To claim your prize, contact our agent immediately:")

try:
    with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp:
        smtp.login(SENDER_EMAIL,APP_PASSWORD)
        smtp.send_message(msg)
    print("Email sent sucessfully")

except Exception as e:
    print("Could not send email.Check your credentials and settings")
    print("Error:{e}")
    print("\nNOTE: This is expected if you haven't replaced the placeholder credentials")

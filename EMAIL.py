import smtplib
from email.message import EmailMessage

SENDER_EMAIL = 'minendra2062@gmail.com'
APP_PASSWORD='sdpr pqtn lgfp ctls'
RECIPIENT_EMAIL='mahatrakesh77@gmail.com'

msg=EmailMessage()
msg['Subject']= 'An Automated Email From Python!'
msg['From']=SENDER_EMAIL
msg['To']=RECIPIENT_EMAIL
msg.set_content("Hello,\n\nThis is a test email sent from a python script. \n\nBest, \nYour Automation Bot")

try:
    with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

    print("Email Sent Successfully!!")

except Exception as e:
    print("Could not send email. Check your credentials and settings.")
    print(f"Error: {e}")
    print("\nNOTE: This is expected if you haven't replaced the placeholder credentials.")

import smtplib
from email.message import EmailMessage
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

# Create a FastAPI instance
app = FastAPI()

# Logging configuration for debugging purposes
logging.basicConfig(level=logging.INFO)

# Pydantic model for request data
class EmailData(BaseModel):
    recipient_email: str
    subject: str
    body: str


# Endpoint to send the email
@app.post("/send-email/")
async def send_email(data: EmailData):
    
    sender_email= 'minendra2062@gmail.com'
    app_password= 'fsak ataf ltkb bwxc'
    msg = EmailMessage()
    msg['Subject'] = data.subject
    msg['From'] = sender_email
    msg['To'] = data.recipient_email
    msg.set_content(data.body)
    

    try:
        # Connect to Gmail's SMTP server and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)

        logging.info("Email sent successfully.")
        return {"message": "Email sent successfully!"}

    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=f"Could not send email. Error: {e}")


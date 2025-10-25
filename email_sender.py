"""
Email Sender Script using Flask and SMTP
Sends assignment submission email with attachments
"""

from flask import Flask
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import json

app = Flask(__name__)

def load_email_config():
    """Load email configuration"""
    # You'll need to create email_config.json with your email credentials
    with open('email_config.json', 'r') as f:
        return json.load(f)

def create_email_body(name, availability="Yes, I am available to work full time (10 am to 7 pm) for the next 3-6 months"):
    """Create the email body"""
    
    body = f"""
Dear Hiring Team,

Please find attached my submission for the Python (Selenium) Assignment.

Submission includes:
1. Screenshot of the form filled via code
2. Source code (GitHub repository link below)
3. Brief documentation of approach (in README)
4. Resume
5. Links to past projects/work samples (see below)
6. Availability confirmation

GitHub Repository: https://github.com/Mustansir101/

Availability Confirmation:
{availability}

Best regards,
{name}
"""
    return body

def attach_file(msg, filepath):
    """Attach a file to the email"""
    try:
        with open(filepath, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        
        filename = os.path.basename(filepath)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename= {filename}'
        )
        
        msg.attach(part)
        print(f"Attached: {filename}")
        return True
    except Exception as e:
        print(f"Error attaching {filepath}: {str(e)}")
        return False

def send_email(
    sender_email,
    sender_password,
    recipient_email,
    cc_email,
    subject,
    body,
    attachments
):
    """Send email with attachments using SMTP"""
    
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Cc'] = cc_email
        msg['Subject'] = subject
        
        # Attach body
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach files
        for filepath in attachments:
            if os.path.exists(filepath):
                attach_file(msg, filepath)
            else:
                print(f"Warning: File not found - {filepath}")
        
        # Create SMTP session
        # For Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Login
        server.login(sender_email, sender_password)
        
        # Send email
        text = msg.as_string()
        recipients = [recipient_email, cc_email]
        server.sendmail(sender_email, recipients, text)
        
        server.quit()
        
        print("Email sent successfully!")
        return True
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False

@app.route('/send-submission', methods=['GET'])
def send_submission():
    """Flask route to trigger email sending"""
    
    # Load configuration
    config = load_email_config()
    
    # Email details
    sender_email = config['sender_email']
    sender_password = config['sender_password']  # App-specific password for Gmail
    your_name = config['your_name']
    
    recipient_email = "tech@themedius.ai"
    cc_email = "hr@themedius.ai"
    subject = f"Python (Selenium) Assignment - {your_name}"
    
    # Create email body
    body = create_email_body(your_name)
    
    # Attachments
    attachments = [
        'screenshots/confirmation.png',
        'resume.pdf',
        # Add more attachments as needed
    ]
    
    # Send email
    success = send_email(
        sender_email,
        sender_password,
        recipient_email,
        cc_email,
        subject,
        body,
        attachments
    )
    
    if success:
        return "Email sent successfully!", 200
    else:
        return "Failed to send email", 500

def send_email_direct():
    """Direct function to send email without Flask route (simpler approach)"""
    
    print("Loading email configuration...")
    config = load_email_config()
    
    # Email details
    sender_email = config['sender_email']
    sender_password = config['sender_password']
    your_name = config['your_name']
    
    recipient_email = "tech@themedius.ai"
    cc_email = "hr@themedius.ai"
    subject = f"Python (Selenium) Assignment - {your_name}"
    
    print(f"Preparing email to: {recipient_email}")
    print(f"CC: {cc_email}")
    
    # Create email body
    body = create_email_body(your_name)
    
    # Attachments
    attachments = [
        'screenshots/confirmation.png',
        'resume.pdf',
    ]
    
    print("Sending email...")
    success = send_email(
        sender_email,
        sender_password,
        recipient_email,
        cc_email,
        subject,
        body,
        attachments
    )
    
    return success

if __name__ == "__main__":
    # Direct execution (simpler)
    send_email_direct()
    
    # Or run Flask app (uncomment below)
    # app.run(debug=True, port=5000)
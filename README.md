# Google Form Automation & Email Submission

Automated solution for filling Google Forms and sending submission emails programmatically.

## 🎯 Project Overview

This project automates:

1. Filling a Google Form using Selenium WebDriver
2. Capturing confirmation screenshot
3. Sending submission email with attachments using Flask/SMTP

## 📋 Prerequisites

- Python 3.8+
- Google Chrome browser
- Gmail account (for sending emails)

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd selenium-form-automation
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Your Details

**config.json** - Your personal information for the form:

```json
{
  "full_name": "Your Full Name",
  "contact_number": "9876543210",
  "email": "your.email@example.com",
  "address": "Your Full Address",
  "pin_code": "411001",
  "dob": "1995-01-15",
  "gender": "Male",
  "captcha_code": "GNFPYC"
}
```

**email_config.json** - Your email credentials:

```json
{
  "sender_email": "your.email@gmail.com",
  "sender_password": "your-app-specific-password",
  "your_name": "Your Full Name"
}
```

### 4. Get Gmail App Password

For Gmail security:

1. Go to Google Account Settings
2. Security → 2-Step Verification
3. App Passwords → Generate new password
4. Use this password in `email_config.json`

### 5. Add Your Files

- Place your resume as `resume.pdf` in project root
- Update GitHub and project links in `email_sender.py`

## 🏃 Running the Scripts

### Step 1: Fill the Form

```bash
python form_filler.py
```

This will:

- Open Chrome browser
- Fill the Google Form
- Submit the form
- Capture screenshot → `screenshots/confirmation.png`

### Step 2: Send Submission Email

```bash
python email_sender.py
```

This will:

- Send email to tech@themedius.ai
- CC hr@themedius.ai
- Attach screenshot and resume

## 📁 Project Structure

```
selenium-form-automation/
├── form_filler.py          # Selenium automation script
├── email_sender.py         # Email sending script
├── config.json             # Form data configuration
├── email_config.json       # Email credentials
├── requirements.txt        # Python dependencies
├── screenshots/            # Output directory
│   └── confirmation.png
├── resume.pdf             # Your resume
├── README.md              # This file
└── .gitignore
```

## 🔧 Technical Approach

### Form Automation (Selenium)

- Uses Selenium WebDriver with Chrome
- Implements explicit waits for dynamic content
- Locates form fields using XPath
- Handles date picker and radio buttons
- Captures screenshot of confirmation page

### Email Automation (Flask/SMTP)

- Uses Flask framework for web service structure
- SMTP protocol for sending emails
- Supports multiple attachments
- Implements proper error handling

### Key Features

- Configurable data via JSON files
- Screenshot capture for verification
- Automated email with CC
- Error handling and logging

## ⚠️ Important Notes

1. **Chrome Driver**: Selenium will auto-download ChromeDriver
2. **Gmail Security**: Use app-specific password, not your regular password
3. **Form Selectors**: May need adjustment if form structure changes
4. **Files**: Ensure all attachments exist before sending email

## 🐛 Troubleshooting

**Issue**: Chrome driver not found

- Solution: Run `pip install webdriver-manager`

**Issue**: Email not sending

- Check Gmail app password is correct
- Ensure "Less secure app access" is enabled (if needed)

**Issue**: Form fields not filling

- Run in non-headless mode to see what's happening
- Check XPath selectors match current form structure

## 📝 Assignment Submission Checklist

- [x] Screenshot of filled form
- [x] Source code with documentation
- [x] Brief approach documentation
- [ ] Resume attached
- [ ] Past project links in email
- [ ] Availability confirmation in email

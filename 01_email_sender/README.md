# Email Assistant

A simple Python application that generates and sends emails using predefined templates.

## Features

- Choose from three email templates:
  - Thank You
  - Birthday Wishes
  - Job Application
- Personalize emails with recipient details.
- Preview the generated email before sending.
- Confirm or cancel email delivery.
- Send emails using Gmail SMTP with SSL.
- Store email credentials securely using environment variables.

## Technologies

- Python
- SMTP (`smtplib`)
- `email.message`
- `python-dotenv`
- SSL

## Project Structure

```text
01_email_sender/
├── main.py
├── .env
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd python-practice-projects
```

3. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

4. Install the required dependency:

```bash
pip install python-dotenv
```

## Configuration

Create a `.env` file inside the `01_email_sender` directory:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

Use a Google App Password instead of your regular Gmail password.

**Important:** Never upload your `.env` file or share your email credentials. The file is excluded from Git using `.gitignore`.

## Usage

Run the application:

```bash
python 01_email_sender/main.py
```

Follow the instructions in the terminal to select a template, enter recipient details, preview the email, and confirm sending.

## Purpose

This project was created as part of my Python learning journey to practice functions, conditional statements, loops, environment variables, exception handling, and email automation using SMTP.
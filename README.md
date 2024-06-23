# Health Bot

<img src="https://github.com/sankalpsaoji98/Health-Bot/assets/26198596/c8f36d1f-35a4-4dd7-8828-f27330ebfc40" alt="Health Bot" width="50%">

## Introduction

Health Bot is a versatile application designed to interact with users via WhatsApp, collect their personal information, and export it in various formats. This application uses the Flask framework for handling HTTP requests, the Twilio API for messaging, and Pandas for data management. 

## Features

- **User Interaction**: Communicates with users through WhatsApp.
- **Data Collection**: Collects personal information from users.
- **Data Export**: Exports collected data in structured formats like CSV.
- **Security**: Implements data encryption for secure information handling.

## Architecture

### Flask Framework
- **Role**: Manages web server operations and handles HTTP requests.
- **Functionality**: Hosts the application's endpoints and processes incoming and outgoing messages.

### Twilio API
- **Role**: Handles communication between the application and WhatsApp users.
- **Functionality**: Sends and receives WhatsApp messages, managing user interactions through predefined flows.

### Pandas Library
- **Role**: Manages and exports data.
- **Functionality**: Converts user data into structured formats for easy storage and retrieval.

### Cryptography Library
- **Role**: Provides tools for secure data encryption.
- **Functionality**: Generates a secure key for encrypting data, ensuring data integrity and security.

### Base64
- **Role**: Safe transmission of binary data over text-based environments.
- **Functionality**: Encodes binary data to be safely transmitted over environments that handle text data.

## Setup Guide

### Prerequisites
- **Python**: Ensure Python is installed on your system.
- **pip**: Python’s package installer.
- **ngrok**: A tool that exposes local servers behind NATs and firewalls to the public internet over secure tunnels.

### Step-by-Step Guide

1. **Set Up Your Python Environment**
   ```bash
   python -m venv bot-env
   source bot-env/bin/activate  # On Windows use `bot-env\Scripts\activate`
   pip install Flask twilio pandas cryptography

### 2. **Configure Twilio for WhatsApp**

1. Sign up for Twilio and set up your WhatsApp sandbox.
2. Note your Account SID and Auth Token from the Twilio dashboard.

### 3. **Implement the Flask Application**

1. Write your Flask application with the necessary route and logic to handle incoming WhatsApp messages.
2. Set environment variables:
    ```bash
    export TWILIO_ACCOUNT_SID='your_account_sid'
    export TWILIO_AUTH_TOKEN='your_auth_token'
    ```

### 4. **Run the Application Locally**

1. Start your Flask application:
    ```bash
    python app.py
    ```
2. Expose your local server using ngrok:
    ```bash
    ngrok http 5000
    ```
3. Copy the https forwarding address provided by ngrok.

### 5. **Configure Webhook in Twilio**

1. Set the webhook URL in the Twilio Console to your ngrok URL followed by `/webhook`.

### 6. **Test Your Bot**

1. Interact with your WhatsApp bot by sending a message to your Twilio WhatsApp number.

### 7. **Deployment and Further Development**

1. Deploy your Flask application to a cloud service like AWS, Heroku, or Google Cloud for better stability and performance.
2. Enhance security measures and implement additional features like data export to Google Sheets and Excel.

### Future Considerations and Security

- **Scalability**: Consider deploying the application in a cloud environment to handle increased traffic.
- **Security**: Implement full encryption for data in transit and at rest, and strengthen authentication and access controls.

### Conclusion

Health Bot provides a scalable and secure framework suitable for various use cases in data management and customer interaction, leveraging WhatsApp for data collection.

### Files Included

- `app.py`: The main Flask application file.
- `Setup_Guide.docx`: Detailed setup guide for deploying the bot.
- `Application_Documentation.docx`: Comprehensive documentation of the application architecture and functionalities.
- `Health Bot.mp4`: A video demonstrating the functionality of the bot.
- `patient_data.numbers`: Sample data collected by the bot.
- `image.jpg`: An image of the Health Bot.

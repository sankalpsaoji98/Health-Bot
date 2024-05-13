from flask import Flask, request, jsonify
from twilio.rest import Client
import pandas as pd
from cryptography.fernet import Fernet
import base64
import os

# Generate a random 32-byte key
key = os.urandom(32)

# Encode the key to base64
encoded_key = base64.urlsafe_b64encode(key)

print("Generated Fernet Key:", encoded_key)

# Use the encoded key to initialize the Fernet cipher
cipher = Fernet(encoded_key)

# Twilio configuration
ACCOUNT_SID = 'hiding the key for security purposes'
AUTH_TOKEN = 'hiding the key for security purposes'
FROM_WHATSAPP = 'hiding the key for security purposes'  # Twilio WhatsApp number
TO_WHATSAPP = 'hiding the key for security purposess'  # Your personal WhatsApp number

app = Flask(__name__)
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Secure data storage
patient_data = []

# Conversation states
conversation_states = {
    'start': 'Full Name',
    'ask_dob': 'Date of Birth',
    'ask_gender': 'Gender',
    'ask_address': 'Address',
    'ask_medical_history': 'Medical History',
    'ask_medications': 'Current Medications',
    'export': 'Export Options'
}

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').strip()
    from_number = request.values.get('From', '')

    # Find or create a session for the user
    session = next((item for item in patient_data if item['from'] == from_number), None)
    if not session:
        session = {'from': from_number, 'state': 'start', 'data': {}}
        patient_data.append(session)
        reply = f"Welcome to the Health Bot. Please enter your {conversation_states[session['state']]}."
    else:
        if session['state'] == 'export':
            if incoming_msg.lower() == 'csv':
                export_data(session['data'], 'csv')
                reply = "Your data has been exported as CSV. Thank you!"
                patient_data.remove(session)
            elif incoming_msg.lower() == 'google sheets':
                # Export to Google Sheets
                # Implement this part using Google Sheets API
                reply = "Exporting to Google Sheets is not implemented yet. Please choose another option."
            elif incoming_msg.lower() == 'excel':
                # Export to Excel
                # Implement this part
                reply = "Exporting to Excel is not implemented yet. Please choose another option."
            else:
                reply = "Invalid option. Please choose CSV, Google Sheets, or Excel."
        elif session['state'] == 'start':
            session['data']['name'] = incoming_msg
            session['state'] = 'ask_dob'
            reply = f"Thanks, {session['data']['name']}! Now, please send your {conversation_states[session['state']]} in YYYY-MM-DD format."
        else:
            key = session['state'].replace('ask_', '')
            session['data'][key] = incoming_msg
            next_state = get_next_state(session['state'])
            if next_state:
                session['state'] = next_state
                reply = f"Got it. What is your {conversation_states[session['state']]}?"
            else:
                export_data(session['data'], 'csv')
                reply = "Your data has been exported as CSV. Thank you!"
                patient_data.remove(session)

    client.messages.create(
        from_=FROM_WHATSAPP,
        body=reply,
        to=from_number
    )

    return jsonify(success=True), 200

def get_next_state(current_state):
    states = list(conversation_states.keys())
    current_index = states.index(current_state)
    if current_index < len(states) - 1:
        return states[current_index + 1]
    return None

def format_data(data):
    formatted_data = ''
    for key, value in data.items():
        formatted_data += f"{conversation_states[key]}: {value}\n"
    return formatted_data

def export_data(data, format):
    df = pd.DataFrame(data, index=[0])
    if format == 'csv':
        if not os.path.isfile('patient_data.csv'):
            df.to_csv('patient_data.csv', index=False)
        else:
            df.to_csv('patient_data.csv', mode='a', header=False, index=False)
    # Implement other export formats

if __name__ == '__main__':
    app.run(debug=True)

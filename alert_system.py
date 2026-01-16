from twilio.rest import Client

# --- TWILIO CONFIG (Get these from Twilio Console) ---
SID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # Replace with your SID
AUTH = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # Replace with your Token
FROM_NUM = '+1234567890' # Replace with Twilio Number
TO_NUM = '+919999999999' # Replace with Your Number

def send_sms_alert(message_body):
    try:
        client = Client(SID, AUTH)
        message = client.messages.create(
            body=message_body,
            from_=FROM_NUM,
            to=TO_NUM
        )
        return True
    except Exception as e:
        print(f"SMS Failed (Check Credentials): {e}")
        return False

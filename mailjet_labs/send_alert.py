import json
import os
import subprocess


def send_alert(subject, message):
    data = {"subject": subject, "message": message}
    with open('system_alert_email.json', 'w') as fw:
        json.dump(data, fw)
        
    try:
        user_auth_email = os.getenv('SYSTEM_EMAIL')
        user_auth_pass = os.getenv('SYSTEM_EMAIL_PASSWORD')
        
        file_path = os.path.join(os.getcwd(), 'node', 'mailer.js')
        output = subprocess.run(
            ['node', file_path, user_auth_email, user_auth_pass],
            capture_output=True,
            text=True,
            env={**os.environ}  # Ensures Python passes the environment to Node.js
        )
        
        if output.stdout:
            print('Email sent successfully')
        elif output.stderr:
            print(output.stderr)
        
    except Exception as e:
        print(f'Error occured while sending the alert! -> {e}')
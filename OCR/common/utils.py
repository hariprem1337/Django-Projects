import requests
import json

def sendTextMessage(message, contactno):
    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = "sender_id=TXTIND&message="+message+"&route=v3&numbers="+contactno
    headers = {
        'authorization': "con9LNvGeVAZmCXRDW1pQ3tshb865TrHJx0SIUKOPalgE4fdzMHl6oVEPGtKxMq7N3Qa1r0SuvFCmUkX ",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    data = json.loads(response.text)
    return data['return']

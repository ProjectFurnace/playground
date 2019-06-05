from urllib import request, parse
import json
import base64
import time, datetime
import os

webhook_url = os.environ("SLACK_WEBHOOK_URL")

def send_message_to_slack(payload):
     
    try:
        json_data = json.dumps(payload)
        req = request.Request(webhook_url,
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))
 

def create_payload(event, status):
        
    d = datetime.datetime.now()
    
    alert = {
        "attachments": [
            {
                "fallback": "GCP Build Action detected",
                "color": "#2eb886",
                "pretext": "GCP Build Action detected - BuildID: *{}*".format(event["build_id"]),
                "author_name": "Furnace Alerts",
                "author_link": "http://furnace.org",
                "author_icon": "https://furnace.org/favicon.ico",
                "title": "Furnace Deployment {}".format(status),
                "title_link": "https://console.cloud.google.com/cloud-build/builds/{}".format(event["build_id"]),
                "text": "Deployment {}, logs can be found at https://console.cloud.google.com/cloud-build/builds/{}".format(status, event["build_id"]),
                "fields": [
                    {
                        "title": "Log Level",
                        "value": "Info",
                        "short": False
                    }
                ],
                "footer": "Project Furnace",
                "footer_icon": "https://furnace.org/favicon.ico",
                "ts": time.mktime(d.timetuple())
            }
        ]
    } 

    return alert



async def processEvent(event):
    print(event)
    if "starting build" in event["message"]:
        payload = create_payload(event, "started")
        send_message_to_slack(payload)
    elif "Deployment failed." in event["message"]:
        payload = create_payload(event, "failed")
        send_message_to_slack(payload)
    elif "Deplyoment successful." in event["message"]:
        payload = create_payload(event, "successful")
        send_message_to_slack(payload)

    return event

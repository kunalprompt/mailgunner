from os import environ
import requests
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('tracking_and_return_policy_template.html')
msg = template.render(customer='CustName', order='OD304170123', tracking_id='track-kart-123a123b890')


def send_simple_message():
    return requests.post(
        environ["MAILGUN-URL"],
        auth=("api", environ["API-KEY"]),
        data={"from": "{} {}".format("Your Name", environ["MAILGUN@SANDBOXID.MAILGUN.ORG"]),
              "to": [environ["EMAIL-TO"]],
              "subject": "Hello",
              "text": "Testing Mailgun awesomeness!"})

def send_complex_message():
    return requests.post(
    	environ["MAILGUN-URL"],
    	auth=("api", environ["API-KEY"]),
        files=[("inline", open("templates/logo.gif")),
        		("attachment", open("return_policy.txt"))],
        data={"from": "{} {}".format("Your Name", environ["MAILGUN@SANDBOXID.MAILGUN.ORG"]),
              "to": environ["EMAIL-TO"],
              # "cc": "xyzzzzzzzz@gmail.com",
              # "bcc": "xyzzzzzzzz@gmail.com",
              "subject": "With Love from --- India Pvt. Ltd.",
              "html": msg})

# resp = send_simple_message()
# print resp

resp = send_complex_message()
print resp

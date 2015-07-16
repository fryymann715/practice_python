__author__ = 'ideans'

from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC808ba086eed75be6e0133cf8309164e5"
auth_token  = "d36fd36178e5c0359b5a3073fd62194f"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="It worked!",
    to="+19518160486",    # Replace with your phone number
    from_="+16168277922") # Replace with your Twilio number
print message.sid
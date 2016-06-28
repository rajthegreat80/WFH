#!/usr/bin/python2.7

Subject = "WFH"
Message = "I am having fever so i wont be able to come to office today. But i will be working on given project from home only."





import os
import sys
import httplib2
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes



SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = '<Application Name>'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials	
def CreateMessage(Subject,Message,To_email):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(Message)
  message['to'] = To_email
  message['from'] = "me"
  message['subject'] = Subject
  return {'raw': base64.urlsafe_b64encode(message.as_string())}

def SendMessage(Subject,Message,To_email):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.

  """
  credentials = get_credentials()
  http = credentials.authorize(httplib2.Http())
  service = discovery.build('gmail', 'v1', http=http)
  message = CreateMessage(Subject,Message,To_email)
  
  message = (service.users().messages().send(userId="me", body=message).execute())
  print ('Message Id: %s' % message['id'])
  return message

def manager():
	fileHandle = open("manager.txt")
	emailid= fileHandle.read().splitlines()
	SendMessage(Subject,Message,emailid[0])

	

def everyone():
	fileHandle = open("peer.txt")
	emailid = fileHandle.read().splitlines()
	fileHandle =open("manager.txt")
	emailid.extend(fileHandle.read().splitlines())
	for email in emailid:
		SendMessage(Subject,Message,email)


def main():
	if len(sys.argv) == 1:
		everyone()
	else:
		if sys.argv[1]=="manager":
			manager()
		else:
			everyone()	

if __name__ == "__main__":
	main()

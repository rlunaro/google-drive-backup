'''
service_gmail.py - class for manage email sending with gmail

@author: rluna
'''

import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build


class ServiceGmail(object):
    '''
    sends emails through gmail
    '''


    def __init__(self, credentials):
        self._gmail_service = build('gmail', 'v1', credentials=credentials)

    def sendSimpleEmail(self,
                        emailFrom, 
                        emailTo,
                        emailSubject, 
                        emailBody ):
        if isinstance( emailTo, str ) : 
            emailTo = [emailTo]
        
        for address in emailTo :  
            message = MIMEText(emailBody)
            message['from'] = emailFrom
            message['to'] = address
            message['subject'] = emailSubject
            encoded_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode('ascii')}
            self._gmail_service.users().messages().send(userId=emailFrom, body=encoded_message).execute()


        



'''
service_gmail.py - class for manage email sending with gmail

Copyright 2019 superman_ha_muerto@yahoo.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

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


        



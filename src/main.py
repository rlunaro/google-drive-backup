'''
main.py

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
import sys
import getopt
import os.path
import pickle
import json 
import datetime
import logging
import logging.config

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from email_template import EmailTemplate
from service_gmail import ServiceGmail
from service_google_drive import ServiceGoogleDrive
from backup_policy import BackupPolicy
from real_verify_strategy import RealVerifyStrategy
from on_memory_reporting_strategy import OnMemoryReportingStrategy

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata',
          'https://www.googleapis.com/auth/drive.file',
          'https://www.googleapis.com/auth/gmail.send']

def loadOrValidateCredentials( token_file: str, 
                               credentials_file: str, 
                               scopes_list : list ):
    creds = None
    log.debug(f"loading credentials from token file {token_file}")
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time
    if os.path.exists(token_file) : 
        with open(token_file, 'rb') as token : 
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file, scopes_list)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)
    return creds

def deleteAndCreateFolder( googleDrive, dirName, parentFolderId = None ):
    googleDrive.folderDelete( dirName, parentFolderId )
    folderId =  googleDrive.folderCreate( dirName, parentFolderId )
    return folderId 

def doDailyPolicy( config: dict, googleDrive, backupPolicy, backupFolderId: str ):
    dailyPolicyFolder = config["dailyPolicyFolder"]
    dailyPolicyFolderId = googleDrive.getOrCreateFolder( dailyPolicyFolder, 
                                                         backupFolderId )
    currentDestinationOfCopiesId = deleteAndCreateFolder( googleDrive, 
                                                          backupPolicy.getDailyDir(), 
                                                          dailyPolicyFolderId )
    doBackup( config, googleDrive, currentDestinationOfCopiesId )

        
def doMonthlyPolicy( config: dict, googleDrive, backupPolicy, backupFolderId: str ):
    monthlyPolicyFolder = config["monthlyPolicyFolder"]
    monthlyPolicyFolderId = googleDrive.getOrCreateFolder( monthlyPolicyFolder, 
                                                         backupFolderId )
    currentDestinationOfCopiesId = deleteAndCreateFolder( googleDrive,
                                                          backupPolicy.getMonthlyDir(), 
                                                          monthlyPolicyFolderId )
    doBackup( config, googleDrive, currentDestinationOfCopiesId )


def doYearlyPolicy( config: dict, googleDrive, backupPolicy, backupFolderId: str ):
    yearlyPolicyFolder = config["yearlyPolicyFolder"]
    yearlyPolicyFolderId = googleDrive.getOrCreateFolder( yearlyPolicyFolder, 
                                                         backupFolderId )
    currentDestinationOfCopiesId = deleteAndCreateFolder( googleDrive,
                                                          backupPolicy.getYearlyDir(), 
                                                          yearlyPolicyFolderId )
    doBackup( config, googleDrive, currentDestinationOfCopiesId )

def doBackup( config:dict, googleDrive, destinationOfCopiesId ):
    for resource in config["resourcesToBackup"] :
        googleDrive.uploadResource( resource, 
                                    os.path.basename( resource ), 
                                    destinationOfCopiesId )
        
        
def parseArguments( argumentList : list ):
    unixArgs = "t:c:l:d:"
    gnuArgs = ["token=", "config=", "logging=", "today="]
    # default values
    token_file = 'token.pickle'
    config_file = 'config.json'
    logging_file = 'logging.json'
    today_value = datetime.datetime.today()
    try : 
        args, values = getopt.getopt( argumentList, 
                                      unixArgs, 
                                      gnuArgs )
        for currentArgument, currentValue in args: 
            if currentArgument in ["--token", "t" ] : 
                token_file = currentValue
            if currentArgument in ["--config", "c"] : 
                config_file = currentValue
            if currentArgument in ["--logging", "l"] :
                logging_file = currentValue
            if currentArgument in ["--today", "d"] :
                today_value = datetime.datetime.strptime(currentValue, '%Y-%m-%d')
    except getopt.error as err:
        print( str(err) )
        sys.exit(2)
    return (token_file, config_file, logging_file, today_value)

def loadConfigContents( config_file : str ):
    log.debug(f'loading config contents from file {config_file}')
    with open(config_file, "rt", encoding='utf-8') as config_file : 
        config = json.load( config_file )       
    return config

def sendSuccessEmail( googleDrive, backupPolicy, creds, today_value, config ):
    log.info("Sending success email....")
    service_gmail = ServiceGmail( credentials=creds )
    placeholders = { "day" : today_value.strftime("%d/%m"), 
                     "hour" : datetime.datetime.now().strftime("%H:%M"),
                     "report" : googleDrive.getReporter().getMessagesAsString(),
                     "backupPolicyExplanation": backupPolicy.explain() }
    successTemplate = EmailTemplate( config["emailSuccess"],
                                     placeholders )
    service_gmail.sendSimpleEmail( emailFrom=config["emailFrom"],
                                   emailTo=config["emailTo"],
                                   emailSubject=successTemplate.getSubject(),
                                   emailBody=successTemplate.getBody() )
    log.info("sent")

def recoverErrorInfo( excInfo ):
    try:
        errorLineNumber = excInfo[2].tb_lineno
        errorDesc1 = excInfo[1]
        errorDesc0 = excInfo[0]
    except: 
        errorLineNumber = 0 
        errorDesc1 = 'Not available'
        errorDesc0 = 'Not available'
    return (errorLineNumber, errorDesc1, errorDesc0)

def sendFailureEmail( creds,  errorLine, errorDesc1, errorDesc0 ):
    try:
        service_gmail = ServiceGmail( credentials=creds )
        placeholders = { "day" : today_value.strftime("%d/%m"), 
                         "hour" : datetime.datetime.now().strftime("%H:%M"),
                         "error_description" : f"{errorLine}:{errorDesc1} ({errorDesc0})" }
        failureTemplate = EmailTemplate( config["emailFailure"],
                                         placeholders )
        service_gmail.sendSimpleEmail( emailFrom=config["emailFrom"],
                                       emailTo=config["emailTo"],
                                       emailSubject=failureTemplate.getSubject(),
                                       emailBody=failureTemplate.getBody() )
    except: 
        print( f"     To: {config['emailTo']}" )
        print( f"Subject: {failureTemplate.getSubject()}" )
        print( f"{failureTemplate.getBody()}" )


def setupLogger( logging_file : str ):
        with open( logging_file, 'rt', encoding='utf-8') as log_file_json: 
            loggingConfig = json.load( log_file_json )
        logging.config.dictConfig( loggingConfig )
        return logging.getLogger()

if __name__ == '__main__':
    print("google-drive-backup")
    
    try:

        (token_file, 
         config_file,
         logging_file, 
         today_value ) = parseArguments( sys.argv[1:] )
    
        log = setupLogger( logging_file )
        log.debug( "google-drive-backup: start of execution" )
    
        config = loadConfigContents( config_file )
            
        creds = loadOrValidateCredentials( token_file, config_file, SCOPES )
    
        reporter = OnMemoryReportingStrategy()
        log.debug( "Loading Service Google Drive" )
        googleDrive = ServiceGoogleDrive( credentials = creds, 
                                          verificationStrategy= RealVerifyStrategy( config["verifyUploadedFiles"] == "true" ),
                                          reporter= reporter ) 
        log.debug( "done" )
        backupFolderId = googleDrive.getOrCreateFolder("backup") 
        
        backupPolicy = BackupPolicy( today = today_value )
        
        if backupPolicy.isDailyPolicy() :
            reporter.info( "--->>> DAILY COPY START <<<------------------")
            reporter.info( f"backup/{config['dailyPolicyFolder']}/{backupPolicy.getDailyDir()}")
            doDailyPolicy( config, googleDrive, backupPolicy, backupFolderId )
            reporter.info( "--->>> DAILY COPY ENDS <<<------------------")
            log.info( "Performed daily copy" )
            
        if backupPolicy.isMonthlyPolicy() : 
            reporter.info( "--->>> MONTHLY COPY START <<<------------------")
            reporter.info( f"backup/{config['monthlyPolicyFolder']}/{backupPolicy.getMonthlyDir()}")
            doMonthlyPolicy( config, googleDrive, backupPolicy, backupFolderId )
            reporter.info( "--->>> MONTHLY COPY ENDS <<<------------------")
            log.info( "Performed monthly copy" )
            
        if backupPolicy.isYearlyPolicy() : 
            reporter.info( "--->>> YEARLY COPY START <<<------------------")
            reporter.info( f"backup/{config['yearlyPolicyFolder']}/{backupPolicy.getYearlyDir()}")
            doYearlyPolicy( config, googleDrive, backupPolicy, backupFolderId )
            reporter.info( "--->>> YEARLY COPY ENDS <<<------------------")
            log.info( "Performed yearly copy" )
        
        sendSuccessEmail( googleDrive, 
                          backupPolicy, 
                          creds, 
                          today_value, 
                          config )
          
        log.info("Finished")
        print( "Success" )

        
    except: 
        (errorLine, errorDesc1, errorDesc0) = recoverErrorInfo( sys.exc_info() )
        sendFailureEmail( creds, errorLine, errorDesc1, errorDesc0 ) 
        print(f"ERROR in line {errorLine}:{errorDesc1} ({errorDesc0})")
        sys.exit(3)   


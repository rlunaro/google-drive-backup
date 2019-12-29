'''
service_google_drive.py

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
import os
import os.path

from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from verify_stragegy import VerifyStrategy
from on_memory_reporting_strategy import OnMemoryReportingStrategy

class ServiceGoogleDrive(object):
    '''
    Google drive service functions
    '''

    def __init__(self, credentials, 
                 verificationStrategy = VerifyStrategy(), 
                 reporter = OnMemoryReportingStrategy() ):
        self._drive_service = build('drive', 'v3', credentials=credentials)
        self._verificationStrategy = verificationStrategy
        self._reporter = reporter
        
    def getReporter(self):
        return self._reporter
    
    def getOrCreateFolder(self, folderName, parentFolderId = None ):
        folderId = self.folderExists( folderName, parentFolderId ) 
        if not folderId : 
            folderId = self.folderCreate( folderName, parentFolderId )
        return folderId 
    
    def folderExists(self, folderName, parentFolderId = None ):
        '''
        if the folder exists, return the id, otherwise return none
        '''
        if parentFolderId : 
            queryString = f"mimeType='application/vnd.google-apps.folder' "\
                        + f"and name = '{folderName}' and trashed = false "\
                        + f"and '{parentFolderId}' in parents"
        else :
            queryString = f"mimeType='application/vnd.google-apps.folder' "\
                        + f"and name = '{folderName}' and trashed = false "
        response = self._drive_service.files().list( q=queryString, 
                              spaces='drive',
                              fields='files(id,name,trashed)').execute()
        folder_list = response.get('files',[])
        if len(folder_list) == 0 : 
            return None
        if len(folder_list) == 1 : 
            return folder_list[0]['id']
        else:
            raise Exception( f'More than one folder named {folderName}' )

    def folderCreate(self, folderName: str, parentFolderId = None ):
        if parentFolderId : 
            file_metadata = { 'name' : folderName, 
                         'mimeType': 'application/vnd.google-apps.folder',
                         'parents' : [ parentFolderId ] }
        else :
            file_metadata = { 'name' : 'backup', 
                         'mimeType': 'application/vnd.google-apps.folder' }
        file = self._drive_service.files().create(body=file_metadata,
                                        fields='id').execute()
        return file.get("id")

    def folderDelete(self, folderName: str, parentFolderId = None ):
        '''
        delete a folder given the name and the parent folder if it exists
        '''
        folderId = self.folderExists( folderName, parentFolderId )
        if folderId : 
            file = self._drive_service.files().delete(fileId=folderId).execute()
        return None

    def uploadFile(self, localFilePath: str, 
                            remoteDirId: str = None, 
                            remoteFileName: str = None ):
        '''
        uploads a file given by path and the remote dir id and returns the remote file id
        '''
        if not remoteFileName : 
            remoteFileName = os.path.basename( localFilePath )
        if not remoteDirId : 
            file_metadata = {'name' : remoteFileName }
        else:
            file_metadata = {'name' : remoteFileName,
                             'parents': [remoteDirId] }
        media = MediaFileUpload(localFilePath, resumable=True)
        # fields='id'
        file = self._drive_service.files().create( body=file_metadata, 
                                       media_body=media, 
                                       fields='id,md5Checksum').execute()
        return file

    

    def _uploadFileWithVerificationAndReporting(self, resource : str,
                                                destinationFolderId : str ):
        fileData = self.uploadFile( resource, destinationFolderId )
        if self._verificationStrategy.isVerificationAvailable() : 
            if self._verificationStrategy.verify( resource, 
                                               fileData.get('md5Checksum')) :
                self._reporter.info( f"{resource} OK+")
            else : 
                self._reporter.error( f"{resource} FAIL: checksum")
        else: 
            self._reporter.info( f"{resource} OK" )
        return fileData

    def uploadResource(self, localFullPath, localBasename, destinationFolderId ):
        '''
        Upload a localFullPath (file or directory) to google drive
        '''
        if os.path.isfile( localFullPath ) : 
            self._uploadFileWithVerificationAndReporting( localFullPath, destinationFolderId )
        else:
            # it's a directory
            self._reporter.info( f"entering directory: {localFullPath}")
            remoteDirId = self.folderCreate( localBasename, destinationFolderId )
            for element in os.listdir( localFullPath ) : 
                self.uploadResource( os.path.join( localFullPath, element), 
                                     element, 
                                     remoteDirId )
    
    

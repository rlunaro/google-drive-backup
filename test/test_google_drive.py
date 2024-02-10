'''
Copyright 2024 superman_ha_muerto@yahoo.com

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
import unittest
import pickle
import os.path

from service_google_drive import ServiceGoogleDrive
from real_verify_strategy import RealVerifyStrategy
from on_memory_reporting_strategy import OnMemoryReportingStrategy


class TestGoogleDrive(unittest.TestCase):


    def setUp(self):
        with open(os.path.join("..","token.pickle"), "rb") as token:
            creds = pickle.load(token)
        reporter = OnMemoryReportingStrategy()
        self.googleDrive = ServiceGoogleDrive( credentials = creds, 
                                          verificationStrategy= RealVerifyStrategy( True ),
                                          reporter= reporter ) 


    def tearDown(self):
        pass


    def testCreateFolder(self):
        backupFolderId = self.googleDrive.getOrCreateFolder( "my_backup_folder" )
        self.assertTrue( True )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
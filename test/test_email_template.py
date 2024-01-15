'''
Created on Dec 25, 2019

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
import datetime
import unittest

from main import loadConfigContents
from email_template import EmailTemplate

class TestEmailTemplate(unittest.TestCase):


    def testOne(self):
        self.config = loadConfigContents( "test_config.yaml" )
        today = datetime.datetime.fromisoformat("2024-01-01 08:30:00")
        placeholders = { "day" : today.strftime("%d/%m"), 
                     "hour" : today.strftime("%H:%M"),
                     "report" : "this is the result of the backup",
                     "backupPolicyExplanation": "this is the explanation of the backup policy" }
        template = EmailTemplate( self.config["reportEmail"]["emailSuccess"], 
                                   placeholders )
        print( template.getBody() )
        self.assertTrue( template.getBody() == 
"""
Hola caraguapa: 
El 01/01, a las 08:30 se ha realizado con éxito la copia de seguridad. 
this is the result of the backup
this is the explanation of the backup policy
Saludos, El robot más caraguapa del mundo
""" )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
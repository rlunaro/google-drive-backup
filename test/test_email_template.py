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
import os.path
import unittest

from email_template import EmailTemplate

class TestEmailTemplate(unittest.TestCase):


    def testOne(self):
        template = EmailTemplate( os.path.join("..","email_failure_template.txt"), 
                                   {"day" : "2019-12-25" } )
        print( template.getBody() )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
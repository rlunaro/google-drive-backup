'''
test_logging.py

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
import unittest

import logging
import logging.config
import json 

class TestLogging(unittest.TestCase):


    def setUp(self):
        with open( 'logging.json', 'rt', encoding='utf-8') as log_file_json: 
            self.loggingConfig = json.load( log_file_json )
        logging.config.dictConfig( self.loggingConfig )
        log = logging.getLogger()
        log.debug("loging debug")
        log.critical("logging critical")
        self.logger = logging.getLogger()


    def tearDown(self):
        pass


    def test1(self):
        self.logger.info("this is an info message")
        # self.logger.critical("hello, this is a CRITICAL message")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
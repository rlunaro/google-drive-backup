'''
Created on Dec 26, 2019

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
import datetime

from backup_policy import BackupPolicy

class TestBackupPolciy(unittest.TestCase):

    def setUp(self):
        self._backupPolicy = BackupPolicy()

    def tearDown(self):
        pass

    def testBackupPolicy1(self):
        backup = BackupPolicy( datetime.datetime(2019, 2, 5) )
        self.assertTrue( backup.isDailyPolicy() )
        self.assertFalse( backup.isMonthlyPolicy() )
        self.assertFalse( backup.isYearlyPolicy() )
        self.assertTrue( backup.getDailyDir() == '5' )
        self.assertTrue( backup.getMonthlyDir() == '02' )
        self.assertTrue( backup.getYearlyDir() == '9' )
        
        backup = BackupPolicy( datetime.datetime(2020, 2, 1) )
        self.assertTrue( backup.isDailyPolicy() )
        self.assertTrue( backup.isMonthlyPolicy() )
        self.assertFalse( backup.isYearlyPolicy() )
        self.assertTrue( backup.getDailyDir() == '1' )
        self.assertTrue( backup.getMonthlyDir() == '02' )
        self.assertTrue( backup.getYearlyDir() == '0' )

        backup = BackupPolicy( datetime.datetime(2020, 12, 30) )
        self.assertTrue( backup.isDailyPolicy() )
        self.assertFalse( backup.isMonthlyPolicy() )
        self.assertTrue( backup.isYearlyPolicy() )
        self.assertTrue( backup.getDailyDir() == '0' )
        self.assertTrue( backup.getMonthlyDir() == '12' )
        self.assertTrue( backup.getYearlyDir() == '0' )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
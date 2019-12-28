'''
Created on Dec 26, 2019

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
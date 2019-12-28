'''
Created on Dec 25, 2019

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
'''
Created on Dec 26, 2019

@author: rluna
'''

class VerifyStrategy(object):
    '''
    if verification should be done or not by comparing 
    the md5 sum of the files 
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def isVerificationAvailable(self):
        return False
    
    def verify(self, localResource, remoteMd5 ):
        return None
    

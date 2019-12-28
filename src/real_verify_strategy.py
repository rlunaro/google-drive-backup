'''
real_verify_strategy.py

@author: rluna
'''
import hashlib 

class RealVerifyStrategy(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def isVerificationAvailable(self):
        return True
    
    def verify(self, localResource, remoteMd5 ):
        localMd5Sum = hashlib.md5(open(localResource, 'rb').read()).hexdigest()
        return localMd5Sum == remoteMd5
    
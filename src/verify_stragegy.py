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
    

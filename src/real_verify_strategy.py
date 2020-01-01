'''
real_verify_strategy.py

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
import hashlib 

class RealVerifyStrategy(object):
    

    def __init__(self, configAvailable : bool ):
        self._configAvailable = configAvailable
        self._chunkSize = 8192
    
    def isVerificationAvailable(self):
        return self._configAvailable
    
    def verify(self, localResource, remoteMd5 ):
        return self._calculateMd5AsHex(localResource) == remoteMd5
    
    def _calculateMd5AsHex(self, filename ): 
        with open(filename, 'rb') as fileContents:
            file_hash = hashlib.md5()
            chunk = fileContents.read( self._chunkSize )
            while len(chunk) > 0 :
                file_hash.update( chunk )
                chunk = fileContents.read( self._chunkSize )
            return file_hash.hexdigest()
        
    
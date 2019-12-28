'''
email_template.py

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

class EmailTemplate(object):

    def __init__(self, filePath: str, placeHoldersDict : dict):
        self._placeHolders = placeHoldersDict
        with open( filePath, "rt", encoding="utf-8" ) as file_template : 
            lines = file_template.readlines()
            self._subject = lines[0]
            self._body = self._getBody( lines ) 
            
    def getSubject(self):
        return self._applyPlaceholders( self._subject )
    
    def getBody(self):
        return self._applyPlaceholders( self._body )
    
    def _getBody(self, lines ):
        body = ""
        for line in lines[1:]:
            body = body + line
            
        return body 
    
    def _applyPlaceholders(self, input : str ):
        placeHoldersKeys = self._placeHolders.keys()
        for key in placeHoldersKeys :
            input = input.replace(f"{{{key}}}", self._placeHolders[key])
        return input
            
            
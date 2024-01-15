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

    def __init__(self, config: dict, placeHoldersDict : dict):
        self._placeHolders = placeHoldersDict
        self._subject = config["subject"]
        self._body = config["body"]
            
    def getSubject(self):
        return self._subject.format( **self._placeHolders )
    
    def getBody(self):
        return self._body.format( **self._placeHolders )

            
            
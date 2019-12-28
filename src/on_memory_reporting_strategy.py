'''
on_memory_reporting_strategy

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

from reporting_strategy import ReportingStrategy

class OnMemoryReportingStrategy( ReportingStrategy ):
    '''
    classdocs
    '''



    def __init__(self):
        self._messages = []
        
    def getMessages(self):
        return self._messages
    
    def getMessagesAsString(self):
        output = ""
        for message in self._messages : 
            output = output + "\n{type}: {msg}".format(**message)
        return output
    
    def error(self, message ):
        self._messages.append( {'type' : 'error', 'msg' : message} )
    
    def warning(self, message ): 
        self._messages.append( {'type' : 'warning', 'msg' : message} )
    
    def info(self, message):
        self._messages.append( {'type' : 'info', 'msg' : message} )



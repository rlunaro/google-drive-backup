'''
on_memory_reporting_strategy

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



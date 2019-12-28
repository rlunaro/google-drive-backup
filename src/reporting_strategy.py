'''
reporting_strategy.py

@author: rluna
'''

class ReportingStrategy(object):
    '''
    strategy to inform the user about events ocurred during the execution of the program
    '''


    def __init__(self):
        pass
        
    def getMessages(self):
        return []
    
    def getMessagesAsString(self):
        return ""

    def error(self, message ):
        pass
    
    def warning(self, message ): 
        pass 
    
    def info(self, message):
        pass


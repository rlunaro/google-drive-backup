'''
email_template.py

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
            
            
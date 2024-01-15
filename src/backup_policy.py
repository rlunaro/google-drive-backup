'''
backup_policy.py

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

import datetime

class BackupPolicy(object):
    '''
    determine the backup policy to apply
    '''
    DAILY_TEXT = """La carpeta {folder}, contiene las copias diarias que se 
    hacen. Sólo se hacen {retention}: una de las carpetas contiene la 
    más reciente y el resto contienen las de días anteriores: el sistema
    va rotando para mantener sólo ése número de copias."""
    MONTLY_TEXT = """La segunda carpeta, {folder}, contiene las copias que se hacen 
    los días 1 de cada mes. Sólo se hacen {retention}: una de las carpetas contiene la 
    más reciente y el resto contienen las de meses anteriores: el sistema
    va rotando para mantener sólo ése número de copias."""
    YEARLY_TEXT = """La tercera carpeta, {folder}, contiene las copias que se hacen los
    días 30/12 (el penúltimo día del año). Se retienen sólamente {retention} copias, por
    el mismo algoritmo que en los casos anteriores: el programa va buscando qué carpeta
    toca y deja ahí la copia del año, de forma que sólo tendrás {retention} copias anuales."""

    DEFAULT_RETENTIONS = { "daily" : 10, 
                           "monthly" : 13, 
                           "yearly" : 10 }

    def __init__(self, 
                 backupPolicy: dict, 
                 today = datetime.datetime.today() ):
        self._backupPolicy = backupPolicy
        self._today = today
        
    def explain(self):
        policy_explanation = '''
Una breve nota sobre la política de respaldo: 

En la carpeta "{destinationFolder}" encontrarás {numberOfFolders} 
directorios: {foldersAsList}. 

{dailyExplanationIfNeeded}

{monthlyExplanationIfNeeded}

{yearlyExplanationIfNeeded}
'''
        return policy_explanation.format(
                destinationFolder = self._backupPolicy["destinationFolder"],
                numberOfFolders = self._numberOfFolders(), 
                foldersAsList = self._foldersAsList(), 
                dailyExplanationIfNeeded = self._explanationOrNothing( "daily", self.DAILY_TEXT ), 
                monthlyExplanationIfNeeded = self._explanationOrNothing( "monthly", self.MONTLY_TEXT ),
                yearlyExplanationIfNeeded = self._explanationOrNothing( "yearly", self.YEARLY_TEXT ) )
    
    def _numberOfFolders(self):
        folders = 0
        for key in ["daily", "monthly", "yearly"]: 
            if key in self._backupPolicy.keys() and self._backupPolicy[key]:
                folders += 1
        return folders
    
    def _foldersAsList(self):
        folders = ""
        for key in ["daily", "monthly", "yearly"]: 
            if key in self._backupPolicy.keys() and self._backupPolicy[key]:
                if folders != "": 
                    folders += ", "
                folders += self._backupPolicy[key]["folder"]
        return folders

    def _explanationOrNothing(self, key : str, text : str):
        if key in self._backupPolicy.keys():
            folder = self._backupPolicy[key].get("folder", "")
            retention = self._backupPolicy[key].get("retention", self.DEFAULT_RETENTIONS[key])
            explanation = text.format(
                folder = folder,
                retention = retention )
            return explanation
        return ""

    def isDailyPolicy(self):
        '''
        the daily policy is enforceable everytime the 
        program is invoked given that is configured
        '''
        return self._backupPolicy.get("daily", False)
    
    def isMonthlyPolicy(self):
        '''
        the montly policy is enforceable the day 1 of each month
        given that is configured 
        '''
        return (self._backupPolicy.get("monthly", False) 
                and self._today.day == 1) 
    
    def isYearlyPolicy(self):
        '''
        the yearly policy is enforceable the day 12/30 of each year
        (we will avoid to use the 12/31 date)
        given that is configured
        '''
        return (self._backupPolicy.get("yearly", False) 
                and self._today.month == 12 
                and self._today.day == 30)
    
    def getDailyPolicyFolder(self):
        return self._backupPolicy["daily"]["folder"]
    
    def getDailyDir(self):
        '''
        for each day, return the modulus 10 of the day, 
        11 -> '1' 
        1 -> '1'
        '''
        try:
            daily_retention = self._backupPolicy["daily"]["retention"]
        except:
            daily_retention = self.DEFAULT_RETENTIONS["daily"]
        return '{:01d}'.format( self._today.day % daily_retention )
    
    def getMonthlyPolicyFolder(self):
        return self._backupPolicy["monthly"]["folder"]
    
    def getMonthlyDir(self):
        try:
            monthly_retention = self._backupPolicy["monthly"]["retention"]
        except: 
            monthly_retention = self.DEFAULT_RETENTIONS["monthly"]
        return '{:02d}'.format( self._today.month % monthly_retention )
    
    def getYearlyPolicyFolder(self):
        return self._backupPolicy["yearly"]["folder"]

    def getYearlyDir(self):
        '''
        2019 -> '9'
        2020 -> '0'
        '''
        try: 
            yearly_retention = self._backupPolicy["yearly"]["retention"]
        except: 
            yearly_retention = self.DEFAULT_RETENTIONS["yearly"]
        return '{:01d}'.format( self._today.year % yearly_retention)

    

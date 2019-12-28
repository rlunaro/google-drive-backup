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
from http.cookiejar import EPOCH_YEAR

class BackupPolicy(object):
    '''
    determine the backup policy to apply
    '''


    def __init__(self, today = datetime.datetime.today() ):
        self._today = today
        
    def explain(self):
        return '''
Una breve nota sobre la política de respaldo: 

En la carpeta "backup" encontrarás tres directorios: 01_diarios, 
02_mensuales, 03_anuales. 

La primera carpeta, 01_diarios, contiene las copias diarias que se 
hacen. Solo se hacen 10, coincidiendo con el último dígito del día. 
Por ejemplo, si hoy es día 25, las copias que se hayan hecho en la 
noche del 24 al 25 (que es día 25), irán a la carpeta "5". 

La segunda carpeta, 02_menusales, contiene las copias que se hacen 
los días 1 de cada mes. Van por meses; es decir en la 05 encontrarás
la copia que se hizo el 01/05, es decir, la de primeros de Mayo.

La tercera carpeta, 03_anuales, contiene las copias que se hacen los
días 30/12 (el penúltimo día del año). Van por el último dígito del 
año. Es decir, para el año 2019 la copia irá al 03_anuales/9. Para el 
año 2020, la copia irá al 03_anuales/0. 
'''

    def isDailyPolicy(self):
        '''
        the daily policy is enforceable everytime the 
        program is invoked
        '''
        return True
    
    def isMonthlyPolicy(self):
        '''
        the montly policy is enforceable the day 1 of each month
        '''
        return self._today.day == 1 
    
    def isYearlyPolicy(self):
        '''
        the yearly policy is enforceable the day 12/30 of each year
        (we will avoid to use the 12/31 date)
        '''
        return (self._today.month == 12 and self._today.day == 30)
    
    def getDailyDir(self):
        '''
        for each day, return the modulus 10 of the day, 
        11 -> '1' 
        1 -> '1'
        '''
        return '{:01d}'.format( self._today.day % 10 )
    
    def getMonthlyDir(self):
        return '{:02d}'.format(  self._today.month )
    
    def getYearlyDir(self):
        '''
        2019 -> '9'
        2020 -> '0'
        '''
        return '{:01d}'.format( self._today.year % 10)

    

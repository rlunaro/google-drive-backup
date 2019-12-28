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
import unittest
import os
import os.path

def traverseDir( path ):
    if os.path.isfile( path ) : 
        print( path ) 
    else : 
        print("entering dir: " +  path )
        for element in os.listdir( path ) :
            traverseDir( os.path.join( path, element ) )

class TestWalk(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testListDir(self):
        traverseDir( os.path.join( "..", "data" ) )

    def testWalkDirectory(self):
        for (dir, subdirs, files) in os.walk( os.path.join('..','data') ):
            print(f"directory: {dir}")
            print(f"contains the following files: ")
            for file in files : 
                print( file )
    
    def testWalkFile(self):
        for (dir, subdirs, files) in os.walk( os.path.join('..','data','IMG_20190505_183622.jpg') ):
            print(f"directory: {dir}")
            print(f"contains the following files: ")
            for file in files : 
                print( file )
        print("saliendo del test")
    
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
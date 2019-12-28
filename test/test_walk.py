'''
Created on Dec 26, 2019

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
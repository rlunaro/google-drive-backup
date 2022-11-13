#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
deploy.py - for deploy the program as easy as it can be

@author: rluna
'''


import os
import zipfile 
import datetime

lib_dir='/home/rluna/python/google-drive-backup-env/lib/python3.6/site-packages'
deployment_filename = 'drive-backup.zip'

def add_file_dir( zipfile:object, file_path:str, archive_name:str ) -> None :
    #print(f"Adding file {file_path}")
    if os.path.isfile( file_path ) : 
        print(f'Adding {file_path}, {archive_name} )')
        zipfile.write( file_path, archive_name )
    else : 
        (root, dirs, files) = next( os.walk(file_path) )
        print( f'root: {root}' )
        print( f'dirs: {dirs}')
        for dir in dirs : 
            add_file_dir( zipfile, 
                          os.path.join( root, dir ), 
                          os.path.join( archive_name, dir ) )
        for file in files : 
            add_file_dir( zipfile, 
                          os.path.join( root, file ), 
                          os.path.join( archive_name, file ) )
    return

if __name__ == '__main__' : 
    print('deploy.py - create a deploy file')
    
    # read VERSION file contents
    try: 
        with open('VERSION', 'rt', encoding='utf-8' ) as version_file : 
            versionAsTxt = version_file.read().strip()
        deployment_filename = deployment_filename.replace('.zip', f'_{versionAsTxt}.zip')
    except: 
        # do nothing, this error can be safely ignored
        pass

    with zipfile.ZipFile(deployment_filename, 'w', zipfile.ZIP_DEFLATED) as deployment : 

        add_file_dir( deployment, 'src/backup_policy.py', 'backup_policy.py' )
        add_file_dir( deployment, 'src/email_template.py', 'email_template.py' )
        add_file_dir( deployment, 'src/main.py', 'main.py' )
        add_file_dir( deployment, 'src/on_memory_reporting_strategy.py', 'on_memory_reporting_strategy.py' )
        add_file_dir( deployment, 'src/real_verify_strategy.py', 'real_verify_strategy.py' )
        add_file_dir( deployment, 'src/reporting_strategy.py', 'reporting_strategy.py' )
        add_file_dir( deployment, 'src/service_gmail.py', 'service_gmail.py' )
        add_file_dir( deployment, 'src/service_google_drive.py', 'service_google_drive.py' )
        add_file_dir( deployment, 'src/verify_stragegy.py', 'verify_stragegy.py' )

        add_file_dir( deployment, 'email_failure_template.txt', 'email_failure_template.txt' )
        add_file_dir( deployment, 'email_success_template.txt', 'email_success_template.txt' )
        add_file_dir( deployment, 'example-config.json', 'example-config.json' )
        add_file_dir( deployment, 'logging.json', 'logging.json' )
        
        add_file_dir( deployment, 'drive-backup.cmd', 'drive-backup.cmd' )
        add_file_dir( deployment, 'drive-backup.sh', 'drive-backup.sh' )
        
    print(f'Deployed file {deployment_filename} on {datetime.datetime.now()}')   

    

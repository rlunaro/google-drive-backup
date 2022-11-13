#!/bin/bash
#
# drive_backup.sh
#
#

PYTHONIOENCODING=UTF-8

if [ -z "$drive_backup_home" ] 
then  
    drive_backup_home="PUT-HERE-THE-HOME-OF-YOUR-APPLICATION"
    PYTHONPATH="$drive_backup_home;$drive_backup_home/src"
    PYTHON_HOME="$drive_backup_home"
    PATH="$PYTHON_HOME/bin:$PATH"
    PYTHON_EXE="$PYTHON_HOME/bin/python"
fi

"$PYTHON_EXE" -u "$drive_backup_home/main.py" \
--config="config.json" \
--logging="logging.json" \
$1 $2 $3 $4 $5



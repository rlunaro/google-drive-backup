#!/bin/bash
#
# google_drive_backup.sh
#
#

PYTHONIOENCODING=UTF-8

if [ -z "$google_drive_backup_home" ] 
then  
    google_drive_backup_home="PUT-HERE-THE-HOME-OF-YOUR-APPLICATION"
    PYTHONPATH="$google_drive_backup_home;$google_drive_backup_home/src"
    PYTHON_HOME="$google_drive_backup_home"
    PATH="$PYTHON_HOME/bin:$PATH"
    PYTHON_EXE="$PYTHON_HOME/bin/python"
fi

"$PYTHON_EXE" -u "$google_drive_backup_home/main.py" \
--config="config.yaml" \
--logging="logging.json" \
$1 $2 $3 $4 $5



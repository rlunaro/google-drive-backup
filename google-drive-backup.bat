rem 
rem google_drive_backup.cmd
rem

set PYTHONIOENCODING=UTF-8

if "%google_drive_backup_home%" == "" goto do_init

goto skip_init

:do_init
set google_drive_backup_home=CONFIGURE HERE 
set PYTHONPATH=%google_drive_backup_home%;%google_drive_backup_home%\src
set PYTHON_HOME=%google_drive_backup_home%
set PATH=%PYTHON_HOME%\Scripts\;%PATH%
set PYTHON_EXE=%PYTHON_HOME%\Scripts\python.exe

:skip_init

"%PYTHON_EXE%" -u %google_drive_backup_home%\main.py ^
--config="config.yaml" ^
--logging="logging.json" ^
%1 %2 %3 %4 %5




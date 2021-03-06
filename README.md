
# ![google-drive-backup logo](docs/app-logo.png) Make backup copies to google drive

google-drive-backup is a python script that allows you to make a copy of
a single file or directory to google drive. 

google-drive-backup keeps a yearly, monthly and daily different copies 
of your data, so it will be difficult to lose a file even if you realize
the lose time after. 

## Installation procedure

To install google-drive-backup, follow this steps: 

1. First of all, you have to request permission from google to use their API's. For instructions, 
[clic here](docs/request_permission_from_google.md)
1. In the machine you want to run it, a working installation of python must be 
in place. You can download it from https://www.python.org/
2. Install the needed google libraries by running: 
`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib  oauth2client file_cache`
If you want to create a virtual environment using `virtualenv`, feel free to do so
3. Create a directory (for instance, google-drive-backup) and uncompress the 
file "google-drive-backup-1.0.0.zip" into it
3. Configure the file config.json (you can start by renaming the file example-config.json)
(you don't need to modify the fifth section)
4. Configure the file google-drive-backup.bat if needed (specific instructions for users of virtualenv)
5. Run the bat file "google-drive-backup.bat" to test if everything works properly
6. Program in the task scheduler (or cron job) the corresponding execution of the batch file
	



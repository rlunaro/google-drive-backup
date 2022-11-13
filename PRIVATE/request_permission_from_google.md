

# ![google-drive-backup logo](app-logo.png) Request permission from google to use their API

One of the first things you have to do in order to use the google API's is effectively, 
ask for permission. API usage can be billed. Said that, I have never got billed for 
the use of this program *so far today*. The use is not really intensive and normally 
this does not imply charges for that, but things can change and I must warn about this. 

## Step 1: Create a new google cloud project

Open the google console: [https://console.cloud.google.com/](https://console.cloud.google.com/). 
You will be asked for your gmail account and password.

Create a new project by selecting the project selector and then click on "New project": 

![create new project](img/request01.png)

## Step 2: Fulfill the project information form

You will be asked for a name for your project (drive-backup could be a good name, 
but you can use whatever you want; it's yours). When you have finished, click on create. 

![create new project](img/request02.png)

## Step 3: Select your newly created project

Back in the main window, you will have to select your new project: 

![create new project](img/request03.png)

## Step 4: Now it's the time to enable the use of google drive and gmail

Now, you have to press the button "Enable apis and services": 

![create new project](img/request04.png)

 - Search for "gmail", click on the element that appears, and click on the "enable" button: 
 you just have enabled your project the use of the gmail API
 - Search again for "google drive", click on the element that appears, and click on 
 the "enable" for this API
 
## Step 5: Configure the OAuth consent screen

The oauth consent screen is a configuration screen that appears when your program runs the 
first time, requesting the real google account (gmail account) that will held the google drive
and the gmail. 

So, click again on the menu -> APIs & Services -> OAuth consent screen: 

![create new project](img/request08.png)

In the user type, select "external" and then click on Create:

![create new project](img/request09.png)

By now, in the application name, put a name (drive-backup could be as good as any) and then 
click on "Save". 


## Step 6: Now, create a credentials for the program 

The credentials are the user and password the program (in this case, google-drive-backup) can 
use to use these API's enabled by you. 

To create a new credentials (you can revoke whenever you want), just click on "google cloud
platform" and then on "api's and services" again: 

![create new project](img/request05.png)

And follow the steps:

![create new project](img/request06.png)

![create new project](img/request07.png)

![create new project](img/request10.png)

And finally, click on the download button: 

![create new project](img/request11.png)

The downloaded content will be a JSON file like this (after formatting): 

	{"installed":
	    {"client_id":"SOME-VALUE-HERE",
	    "project_id":"OTHER-VALUE-HERE",
	    "auth_uri":"https://accounts.google.com/o/oauth2/auth",
	    "token_uri":"https://oauth2.googleapis.com/token",
	    "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
	    "client_secret":"ANOTHER-VALUE-HERE",
	    "redirect_uris":[
	        "urn:ietf:wg:oauth:2.0:oob",
	        "http://localhost"
	    ]
	}
	}

**You have to copy the "installed" object and substitute it in the config.json file.**
It's very important to make the program work. 




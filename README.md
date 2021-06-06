# Python task reminder:

## How to setup
```
1. Create/Select a gmail account you want to use.
2. Enable less secure apps for it with this link:
    https://myaccount.google.com/lesssecureapps
3. Edit the config.py file
    You can also find examples in the example folder
4. Upload all the files on where you want to host it and keep the app running
    Currently the main file has to be run only once a day and preferably in the morning
5. Install all requirements by running "pip install -r requirements.txt" 
6. Create the tasks.txt file
    It has to be in a specific format, see below
    You can also find examples in the example folder
```

## File format
```
The file format consists out of 2 parts

The first part is the date in the crontab format:
    You can check it out here: https://crontab.guru/
    The only thing that is not implemented is the @yearly, @monthly, etc

The second part is the content:
    The only limitation is that they can only consist out of one line

All lines starting with a '#' are considered comments and thus ignored
```

## Verifying the file
```
If you're not sure wheather the tasks.txt file is valid you can verify it
You can do it by running "python verify.py"

In case you don't verify the email and tasks.txt is not valid you will get notified through the email
```
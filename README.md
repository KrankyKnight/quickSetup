# quickSetup

Quickly open commonly used chrome windows on mac with a quick script

## setup

1. install 'python' on your device (this is setup with python 3)
2. install 'pyyaml' for parsing the config file  
  ```pip install pyyaml```
  or
  ```pip3 install pyyaml```

That should do it!

## using

1. generate the executable  
-run ```npm run build```  
-This will create the file "openwin.sh"  
-You can place this wherever you'd like. (I keep mine in my cli ~ directory)  

2. add windows you want to open to the config.yaml file  

The below example will open a new window named Media with two tabs. One on youtube's homepage and the other on spotify's homepage.

```
Media Window:
  - Media
  - https://www.youtube.com/
  - https://open.spotify.com/
```

3. Done!  
Run the "openwin.sh" using ```bash openwin.sh``` whenever you want to quickly open all of these windows!  
(make sure to navigate the cli to the directory you stored this "openwin.sh" in)

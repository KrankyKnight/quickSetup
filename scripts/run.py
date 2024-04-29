import subprocess
import sys
import os
import yaml
with open('config.yaml') as file:
  windows = yaml.safe_load(file)

shellPath = os.path.dirname(os.path.abspath(__file__)) + '/openNewWindow.sh'
baseScript = ['sh', shellPath]

def partialSetup():
  
  processQueue = []
  
  for key in windows:
    userInput = input('Open ' + key + '(y/N)')
    if(userInput.lower() == 'y'): processQueue.append(key)

  processQueue.reverse()

  for page in processQueue:
    cliCommand = baseScript.copy()
    cliCommand.extend(windows[page])
    subprocess.call(cliCommand)

def fullSetup():
  for page in windows:
    cliCommand = baseScript.copy()
    cliCommand.extend(windows[page])
    subprocess.call(cliCommand)

if(len(sys.argv) > 1 and sys.argv[1] == '--select'): partialSetup()
else: fullSetup()


#!/bin/sh
# this file runs AppleScript for MacOS and instructs the "Google Chrome" application to open a new window, name it, and open new tabs to specific urls

osascript \
  -e 'on run(theUrls)' \
  -e '  tell application "Google Chrome"' \
  -e '  log item 1 of theUrls' \
  -e '	  set newWindow to make new window with properties {given name:item 1 of theUrls}' \
  -e '    repeat with num from 2 to length of theUrls' \
  -e '      tell newWindow to make new tab with properties {URL:item num of theUrls}' \
  -e '    end repeat' \
  -e '    set firstTab to first tab of newWindow' \
  -e '    tell firstTab to close' \
  -e '  end tell' \
  -e 'end run' \
  $@
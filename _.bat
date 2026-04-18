@echo off
set "msg=Update: %date:~0,10% %time:~0,5%"
git add .
git commit -m "%msg%"
git push
echo Done!
timeout /t 3
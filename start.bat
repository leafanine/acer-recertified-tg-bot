@echo off
title Bot-scrapper
echo Automating the scrapper for the Bot lets go!
start cmd.exe /k "python bot.py"
:a
python scrapper.py
start cmd.exe /k "python bot.py"
timeout /t 10
goto a
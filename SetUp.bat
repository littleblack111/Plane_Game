@echo off
echo python3 is required 
python get-pip.py
pip install pgzero
pip install pgame
pip install pgzgame
pip install time 
pip install os
pip install random
pip install pynput
pip install mouse
pip install keyboard
pip install pygame
echo @echo off > Game.Play.bat
echo pgzrun "Plane_Game2D.py" >> Game.Play.bat
echo pause >> Game.Play.bat
echo echo press any key to restart the game, press X to close the game >> Game.Play.bat
echo pause >> Game.Play.bat
echo start Game.Play.bat >> Game.Play.bat
echo pause >> Game.Play.bat
echo SetUp have successfully complete
echo press any key to start the game, press X to close this windows and start the game with Game.Play.bat, hope you have fun!
pause
start Game.Play.bat
pause
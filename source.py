import requests , time , os

open('PROXIES.txt', 'a')

d = 0

PLIST = []

os.remove('PROXIES.txt')

PAPI = ['https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all','https://www.proxy-list.download/api/v1/get?type=http','https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt','https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt','https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt','https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt','https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt','https://raw.githubusercontent.com/xcodl/proxy-list/main/proxies/http.txt','https://raw.githubusercontent.com/xcodl/proxy-list/main/proxies_anonymous/http.txt','https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt','https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt','https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt']
def SCRAP():
    try:
        for REQURL in PAPI:
            REQ = requests.get(REQURL).text
            PLIST.append(REQ)
            print(f'\r[ + ] Geting Proxies Please Wait',end="")
            time.sleep(0.2)
            print(f'\r[ + ] Geting Proxies Please Wait .',end="")
            time.sleep(0.2)
            print(f'\r[ + ] Geting Proxies Please Wait ..',end="")
            time.sleep(0.2)
            print(f'\r[ + ] Geting Proxies Please Wait ...',end="")
            time.sleep(0.2)
            with open('PROXIES.txt','a') as R:
                R.write(REQ)
        print('\n[ + ] Done Get All Proxies')
        R.close()
    except Exception as PP:
        print('[ - ] Sorry Error Found !')
        input('[ - ] You Must Open Vpn !')
        print(f'{str(PP)}')
SCRAP()
for SSS in open('PROXIES.txt','r').read().splitlines():
    d+=1
input(f'[ + ] All Proxies = {d}')







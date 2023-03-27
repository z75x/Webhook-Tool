import requests, colorama, time, os


def _exit():
    time.sleep(5)
    exit()


def check_hook(hook):
    info = requests.get(hook).text
    if "\"message\": \"Unknown Webhook\"" in info:
        return False
    return True


def main(webhook, name, delay, amount, message, hookDeleter):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        try:
            data = requests.post(webhook, json={"content": str(message), "name": str(name), "avatar_url": "https://upload.wikimedia.org/wikipedia/fr/thumb/4/4f/Discord_Logo_sans_texte.svg/106px-Discord_Logo_sans_texte.svg.png?20210527094128"})
            if data.status_code == 204:
                print(f"{colorama.Back.MAGENTA} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
            else:
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Fail{colorama.Back.RESET}")
        except:
            print()
        time.sleep(float(delay))
        counter += 1
    if hookDeleter.lower() == "y":
        requests.delete(webhook)
        print(f'{colorama.Fore.MAGENTA}webhook deleted')
    print(f'{colorama.Fore.YELLOW}done...')


def initialize():
    print(f"""{colorama.Fore.GREEN}


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@(//////(@@@@@@@@@@@@@@@@@@@///////(@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@&/////(@@@@@@@((///////////////((@@@@@@@/////(@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@/////%@@%//////////////////////////////////(&@@#////(@@@@@@@@@@@@@
@@@@@@@@@@@@////@(/////////////////////////////////////////////(@///#@@@@@@@@@@@
@@@@@@@@@@@//////////////////////////////////////////////////////////(@@@@@@@@@@
@@@@@@@@@@/////////////////////////////////////////////////(//////////(@@@@@@@@@
@@@@@@@@@/////////////////////////////////////////////(@@@@/%@/////////(@@@@@@@@
@@@@@@@@/////////////////////////////////////////////(@@////@@//////////(@@@@@@@
@@@@@@@///////////////////////////////////////////////(@//@@@////////////%@@@@@@
@@@@@@@/////////////////////////////////////////////////@@////////////////@@@@@@
@@@@@@/////////////////////////////////***////////////////////////////////(@@@@@
@@@@@@/////////////////(@@@@@@@@@@@//////////%@@@@@@@@@@@//////////////////@@@@@
@@@@@///////////////////@@@@@@@@@@@//////////(@@@@@@@@@@@//////////////////(@@@@
@@@@@////////////////////@@@@@@@@@////////////(@@@@@@@@@////////////////////@@@@
@@@@////////////////////////(#(///////////////////(#(///////////////////////#@@@
@@@@////////////////////////////////////////////////////////////////////////(@@@
@@@@///////////@////////////////////////////////////////////////(&//////////(@@@
@@@@@////////////(@@@///////////////////////////////////////@@@/////////////@@@@
@@@@@@@//////////////(@@@@@%/////////////////////////&@@@@@(/////////////#@@@@@@
@@@@@@@@@@@///////////////(@@@@@@@@@@@@@@@@@@@@@@@@@@@(//////////////(@@@@@@@@@@
@@@@@@@@@@@@@@@@@/////////(@@@@@@@@@@@@@@@@@@@@@@@@@@@/////////(@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                           
                         Webhook Tool By tokyo ;)
     """)
    
    webhook = input("l'url du webhook > ")
    name = input("le nom > ")
    message = input("le message qu'il envoye > ")
    delay = input("le delai ? > ")
    amount = input("Combien de message ? > ")
    hookDeleter = input("Veut tu supprimé le webhook après avoir spam ?  [Y/N] > ")
    
    try:
        delay = float(delay)
    except ValueError:
        _exit()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (hookDeleter.lower() != "y" and hookDeleter.lower() != "n"):
        _exit()
    else:
        main(webhook, name, delay, amount, message, hookDeleter)
        _exit()

if __name__ == '__main__':
    os.system('cls')
    os.system('')
    colorama.init()
    initialize()

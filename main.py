import time
import httpx
import random

from constants import XSUPER
from hcapbypass import bypass





def proxy():
    with open("proxies.txt", "r") as f:
        proxy = random.choice(f.readlines()).strip().split(":")
    
    return {
        "http://": f"http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}",
        "https://": f"http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}"
        }



class discord:
    def __init__(self, invite) -> None:

        self.invite = invite
        self.proxy = proxy()
        
        self.client = httpx.Client(proxies=self.proxy, timeout=10)

        self.step = "init"

        while True:

            if self.step == "init":
                print("Initializing task")
                try:
                    self.getInit()
                except:
                    print("Error initializing task")
                    time.sleep(5)
                else:
                    self.step = "fingerprint"
            
            elif self.step == "fingerprint":
                print("Fetching fingerprint")
                try:
                    self.fingerprint = self.getFingerprint()
                except:
                    print("Error fetching fingerprint")
                    time.sleep(5)
                else:
                    self.step = "captcha"

            elif self.step == "captcha":
                print("Bypassing captcha")
                try:
                    self.captcha = bypass("4c672d35-0701-42b2-88c3-78380b0db560", "discord.com", self.proxy)
                except:
                    print("Error solving captcha")
                    time.sleep(5)
                else:
                    self.step = "register"
            
            elif self.step == "register":
                print("Registring account")
                try:
                    self.token = self.register()
                except:
                    print("Registring account")
                    time.sleep(5)
                else:
                    break
            
        print(f"Token: {self.token} ")

        with open("tokens.txt", "a") as f:
            f.write(self.token)

        return
        
        


    
    def getInit(self):
        headers = {
            'authority': 'discord.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'if-modified-since': 'Thu, 15 Sep 2022 19:04:42 GMT',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
        
        r = self.client.get(f"https://discord.com/invite/{self.invite}", headers=headers)

        if r.status_code > 201:
            raise Exception(f"Bad response ::: {r.status_code}")
        
        return

    
    def getFingerprint(self):

        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
            #'x-context-properties': 'eyJsb2NhdGlvbiI6IkFjY2VwdCBJbnZpdGUgUGFnZSJ9',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-super-properties': XSUPER,
        }
        
        r = self.client.get("https://discord.com/api/v9/experiments?with_guild_experiments=true", timeout=10)

        if r.status_code > 201:
            raise Exception(f"Bad response ::: {r.status_code}")

        try:
            fingerprint = r.json()['fingerprint']
        except:
            raise Exception("Failed to get fingerprint")
        else:
            return fingerprint
        
    
    def register(self):
        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-fingerprint': self.fingerprint,
            'x-super-properties': XSUPER,
        }

        data = {
            'fingerprint': self.fingerprint,
            'username': f'NewAlt{str(random.randint(100,999))}',
            'invite': self.invite,
            'consent': True,
            'gift_code_sku_id': None,
            'captcha_key': self.captcha,
        }

        r = self.client.post("https://discord.com/api/v9/auth/register",headers=headers,json=data)

        if r.status_code > 201:
            raise Exception(f"Bad response ::: {r.status_code}")

        return r.json()['token']
        

if __name__ =="__main__":
    discord("deals")
    

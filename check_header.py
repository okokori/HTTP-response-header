#!/usr/bin/env python3

import requests
from colorama import Fore, Style
import time

print(Fore.RED + """ 

                    ,----,       ,----,                                                                                                  ,----,                                                                                                  
        ,--,      ,/   .`|     ,/   .`|,-.----.                                                                                        ,/   .`|                                  ,--,                                                            
      ,--.'|    ,`   .'  :   ,`   .'  :\    /  \                   .--.--.       ,---,.  ,----..               ,-.----.     ,---,    ,`   .'  :                                ,--.'|    ,---,.   ,---,           ,---,        ,---,.,-.----.    
   ,--,  | :  ;    ;     / ;    ;     /|   :    \                 /  /    '.   ,'  .' | /   /   \         ,--, \    /  \ ,`--.' |  ;    ;     /      ,---,                  ,--,  | :  ,'  .' |  '  .' \        .'  .' `\    ,'  .' |\    /  \   
,---.'|  : '.'___,/    ,'.'___,/    ,' |   |  .\ :               |  :  /`. / ,---.'   ||   :     :      ,'_ /| ;   :    \|   :  :.'___,/    ,'      /_ ./|               ,---.'|  : ',---.'   | /  ;    '.    ,---.'     \ ,---.'   |;   :    \  
|   | : _' ||    :     | |    :     |  .   :  |: |               ;  |  |--`  |   |   .'.   |  ;. / .--. |  | : |   | .\ ::   |  '|    :     | ,---, |  ' :               |   | : _' ||   |   .':  :       \   |   |  .`\  ||   |   .'|   | .\ :  
:   : |.'  |;    |.';  ; ;    |.';  ;  |   |   \ :               |  :  ;_    :   :  |-,.   ; /--`,'_ /| :  . | .   : |: ||   :  |;    |.';  ;/___/ \.  : |               :   : |.'  |:   :  |-,:  |   /\   \  :   : |  '  |:   :  |-,.   : |: |  
|   ' '  ; :`----'  |  | `----'  |  |  |   : .   /                \  \    `. :   |  ;/|;   | ;   |  ' | |  . . |   |  \ :'   '  ;`----'  |  | .  \  \ ,' '               |   ' '  ; ::   |  ;/||  :  ' ;.   : |   ' '  ;  ::   |  ;/||   |  \ :  
'   |  .'. |    '   :  ;     '   :  ;  ;   | |`-'                  `----.   \|   :   .'|   : |   |  | ' |  | | |   : .  /|   |  |    '   :  ;  \  ;  `  ,'               '   |  .'. ||   :   .'|  |  ;/  \   \'   | ;  .  ||   :   .'|   : .  /  
|   | :  | '    |   |  '     |   |  '  |   | ;                     __ \  \  ||   |  |-,.   | '___:  | | :  ' ; ;   | |  \'   :  ;    |   |  '   \  \    '                |   | :  | '|   |  |-,'  :  | \  \ ,'|   | :  |  '|   |  |-,;   | |  \  
'   : |  : ;    '   :  |     '   :  |  :   ' |                    /  /`--'  /'   :  ;/|'   ; : .'|  ; ' |  | ' |   | ;\  \   |  '    '   :  |    '  \   |                '   : |  : ;'   :  ;/||  |  '  '--'  '   : | /  ; '   :  ;/||   | ;\  \ 
|   | '  ,/     ;   |.'      ;   |.'   :   : :                   '--'.     / |   |    \'   | '/  :  | : ;  ; | :   ' | \.'   :  |    ;   |.'      \  ;  ;                |   | '  ,/ |   |    \|  :  :        |   | '` ,/  |   |    \:   ' | \.' 
;   : ;--'      '---'        '---'     |   | :                     `--'---'  |   :   .'|   :    /'  :  `--'   \:   : :-' ;   |.'     '---'         :  \  \               ;   : ;--'  |   :   .'|  | ,'        ;   :  .'    |   :   .':   : :-'   
|   ,/                                 `---'.|                               |   | ,'   \   \ .' :  ,      .-./|   |.'   '---'                      \  ' ;               |   ,/      |   | ,'  `--''          |   ,.'      |   | ,'  |   |.'     
'---'                                    `---`                               `----'      `---`    `--`----'    `---'                                 `--`                '---'       `----'                   '---'        `----'    `---'       
                                                                                                                                                                                                                                                 
                                                                                                                                                                                                        Developed by x3chs  """ + Style.RESET_ALL) 

def get_http_headers(url):
    try:
        # Kullanıcının girdiği URL'den HTTP başlıklarını alın
        response = requests.head(url)

        # HTTP Yanıt Başlıkları
        headers = response.headers
        print(Fore.RED + "\nHTTP Yanıt Başlıkları:" + Style.RESET_ALL)
        for i, (key, value) in enumerate(headers.items(), start=1):
            print(Fore.CYAN + f"{i}. {key}" + Fore.RESET, )

    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Hata:" + Style.RESET_ALL, )

def check_custom_headers(url):
    custom_headers = input("Kontrol etmek istediğiniz HTTP başlıklarını virgülle ayırarak girin (örnek: 1,2,3): ").split(',')
    try:
        # Kullanıcının girdiği URL'den belirlediği başlıkları alın
        response = requests.head(url)

        # Belirtilen başlıkları yazdırın
        
        print(Fore.BLUE + "\nBelirtilen HTTP Başlıkları:" + Style.RESET_ALL)
        for header_num in custom_headers:
            header_num = int(header_num.strip()) - 1  # Kullanıcıdan gelen numarayı düzeltin
            headers = response.headers.items()
            header_list = list(headers)
            if header_num >= 0 and header_num < len(header_list):
                key, value = header_list[header_num]
                print(Fore.CYAN + f"{header_num + 1}. {key}:" + Fore.RESET, value)
            else:
                print(Fore.YELLOW + f"{header_num + 1}: Geçersiz başlık numarası." + Fore.RESET)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Hata:" + Style.RESET_ALL, e)


def custom_headers(url, custom_headers=None):
    try:
        # HTTP GET isteği gönderin ve yanıtı alın
        response = requests.get(url)

        # Belirtilen başlıkları kontrol edin
        required_headers = [
            "Content-Security-Policy",
            "Cross-Origin-Embedder-Policy",
            "Cross-Origin-Opener-Policy",
            "Cross-Origin-Resource-Policy",
            "Origin-Agent-Cluster",
            "Referrer-Policy",
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-DNS-Prefetch-Control",
            "X-Download-Options",
            "X-Frame-Options",
            "X-Powered-By",
            "X-XSS-PROTECTION",
            "Public-Key-Pins",
            "Expect-CT",
        ]
        
        print(Fore.RED + "\nHTTP Yanıt Başlıkları:" + Style.RESET_ALL)
        for i, (key, value) in enumerate(response.headers.items(), start=1):
            print(Fore.CYAN + f"{i}. {key}:" + Fore.RESET, value)

        if custom_headers:
            print(Fore.BLUE + "\nBelirtilen HTTP Başlıkları:" + Style.RESET_ALL)
            for header_num in custom_headers:
                header_num = int(header_num.strip()) - 1  # Kullanıcıdan gelen numarayı düzeltin
                headers = response.headers.items()
                header_list = list(headers)
                if header_num >= 0 and header_num < len(header_list):
                    key, value = header_list[header_num]
                    print(Fore.CYAN + f"{header_num + 1}. {key}:" + Fore.RESET, value)
                else:
                    print(Fore.YELLOW + f"{header_num + 1}: Geçersiz başlık numarası." + Fore.RESET)

        print("\nDefault Başlıklar:")
        missing_headers = []
        for header in required_headers:
            value = response.headers.get(header)
            if value:
                print(f"{header}: {value}")
            else:
                missing_headers.append(header)
                print(f"{header}: Başlık bulunamadı.")

        if missing_headers:
            print(Fore.RED + "\nAşağıdaki başlıklar eksik:")
            for header in missing_headers:
                print(Fore.YELLOW + "(!) " + Style.RESET_ALL + header)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Hata:" + Style.RESET_ALL, e)

if __name__ == "__main__":
    while True:
        print("""
Seçenekler:
          
1. HTTP Başlıklarını Listele
2. Kullanıcı Belirlediği HTTP Response Headers Başlıkları Kontrol Et
3. Belirli bir URL'nin HTTP Yanıt Başlıklarını ve Default Başlıkları Göster
4. Çıkış
              """)

        choice = input("Seçenek numarasını girin: ")

        if choice == "1":
            user_url = input("Lütfen URL'yi girin: ")
            time.sleep(1)
            get_http_headers(user_url)
             
        elif choice == "2":
            user_url = input("Lütfen URL'yi girin: ")
            time.sleep(1)
            check_custom_headers(user_url)

        elif choice == "3":
            user_url = input("Lütfen URL'yi girin: ")
            time.sleep(1)
            custom_headers(user_url)
             
        elif choice == "4":
            time.sleep(1)
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçenek! Lütfen 1, 2, 3 veya 4 girin.")
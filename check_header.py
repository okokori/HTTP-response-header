#!/usr/bin/env python3

import requests
from colorama import Fore, Style
import time
import re

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

# HTTP başlıkları hakkında bilgiyi bir sözlükte saklayın
HEADER_INFO = {
    "Content-Security-Policy":  "1.XSS Saldırıları (Cross-Site Scripting): XSS saldırılarını önlemek için, güvensiz kaynakları etkinleştirmeyen ve 'unsafe-inline' ve 'unsafe-eval' gibi riskli işlemleri engelleyen bir CSP politikası kullanılmalıdır. Örnek bir politika şu şekilde olabilir:"
                                "\n\033[93mContent-Security-Policy: default-src 'self'; script-src 'self' 'nonce-RANDOM_NONCE_VALUE'\033[0m\n"
                                "nonce (tek kullanımlık izin kodu) kullanarak yalnızca belirli kaynakların betiklerini yüklemek, XSS saldırılarına karşı daha fazla koruma sağlar.\n" 
                                "\n2.Kaynak Kısıtlamaları İhlali: Politikaların, uygulamanızın gereksinimlerini karşıladığından emin olun. Gereksiz kaynakları engellemeyin ve sadece güvendiğiniz kaynaklara izin verin:"
                                "\n\033[93mContent-Security-Policy: default-src 'self' trusted-source.com; script-src 'self' 'unsafe-inline' 'unsafe-eval' trusted-source.com\033[0m\n"
                                "\n3.Raporlama Sorunları: Raporlama özelliğini düzgün yapılandırmak, güvenlik ihlallerini izlemek için önemlidir:"
                                "\n\033[93mContent-Security-Policy: default-src 'self'; report-uri /csp-report-endpoint;\033[0m\n"
                                "Bu politika, tarayıcıların güvenlik ihlallerini belirtilen bir raporlama URL'sine göndermesine izin verir.\n"
                                "\n4.İçerik Sorunları: Sayfanızın işlevselliğini engellememek için politikaları dikkatlice belirleyin. Gereksinimlerinizi ve kaynaklarınızı tanımlayan bir politika oluşturun:"
                                "\n\033[93mContent-Security-Policy: default-src 'self' trusted-source.com; img-src 'self' img-source.com;\033[0m\n"
                                "\n5.Güncel Olmayan Politikalar: CSP politikalarını düzenli olarak güncellemek ve güvenlik ihtiyaçlarına uygun hale getirmek önemlidir. Politikaların düzenli olarak gözden geçirilmesi ve gerektiğinde güncellenmesi gerekmektedir.\n"
                                "\n6.Test Eksikliği: CSP politikalarının uygulamada etkili olduğunu doğrulamak için test senaryoları oluşturmalısınız. Farklı tarayıcı sürümlerinde ve senaryolarda test yaparak politikalarınızın işlevselliğini kontrol edin.\n"
                                "\n7.Güvensiz Konfigürasyonlar: Güvensiz kaynaklara veya kötü amaçlı sitelere erişime izin vermemek için politikaları doğru bir şekilde yapılandırın ve güvenilir kaynaklara sınırlar koyun:"
                                "\n\033[93mContent-Security-Policy: default-src 'self' trusted-source.com; frame-src 'self' trusted-source.com;\033[0m\n",

    "X-XSS-Protection":         "1.Eski ve Uyumsuz Tarayıcılar İçin Geçerli Değil: Bu zafiyeti ele almak için, X-XSS-Protection'i etkinleştirmek yerine modern tarayıcılarda desteklenen bir CSP politikası kullanabilirsiniz. CSP, daha geniş bir tarayıcı yelpazesi tarafından desteklenir. Örnek bir CSP politikası:"
                                "\n\033[93mContent-Security-Policy: default-src 'self';\033[0m\n"
                                "\n2.Kapatılabilir: Kullanıcıların X-XSS-Protection'ı devre dışı bırakmalarını engellemek için, CSP'yi kullanarak CSP politikası zorunlu hale getirebilirsiniz. Aynı zamanda tarayıcıların bu politikayı devre dışı bırakmasına izin vermezsiniz. Örnek:"
                                "\n\033[93mContent-Security-Policy: default-src 'self'; x-xss-protection '1; mode=block';\033[0m\n"
                                "\n3.Sınırlı Koruma Sağlar: XSS saldırılarına karşı daha güçlü bir koruma sağlamak için, CSP'nin 'script-src' veya 'default-src' bölümlerini sıkılaştırabilirsiniz. Örneğin, yalnızca güvenilir kaynaklardan betiklerin yüklenmesine izin vermek için:"
                                "\n\033[93mContent-Security-Policy: default-src 'self'; script-src 'self' trusted-scripts.com;\033[0m\n"
                                "\n4.Etki Alanı Kontrolü Yok: CSP politikaları, diğer güvenlik gereksinimlerini (örneğin, içerik güvenliği politikaları) belirtmek için kullanılabilir. Birden fazla güvenlik başlığı kullanarak eksiksiz bir güvenlik politikası oluşturun:"    
                                "\n\033[93mContent-Security-Policy: default-src 'self'; frame-src 'self' trusted-frames.com;\033[0m\n"
                                "\n5.Koruma Seviyesi Sorunları: X-XSS-Protection başlığından daha hassas bir koruma seviyesi sağlamak için, CSP politikasını sıkılaştırabilirsiniz. Örneğin, 'mode=block' benzeri bir etki sağlayabilirsiniz:"   
                                "\n\033[93mContent-Security-Policy: default-src 'self'; script-src 'self' 'nonce-RANDOM_NONCE_VALUE';\033[0m\n"
                                "\n6.Koruma Yanlış Pozitifleri: CSP politikalarını belirlerken, işlevselliği engellemeden istenmeyen betikleri engellememek için dikkatli olmalısınız. Doğru kaynaklara izin veren bir politika oluşturarak bu sorunu aşabilirsiniz:"  
                                "\n\033[93mContent-Security-Policy: default-src 'self' trusted-sources.com; script-src 'self' 'unsafe-inline' 'unsafe-eval' trusted-sources.com;\033[0m\n",

    "X-Content-Type-Options":   "1.MIME Türü Eksik veya Yanlış Ayarlandığında Güvenlik Sorunları:Bu zafiyeti ele almak için, 'nosniff' (MIME türünü değiştirmeyi reddet) özelliğini kullanarak tarayıcılara içeriğin MIME türünü değiştirme veya yorumlama girişimlerini engelleyebilirsiniz. İşte bir örnek politika:"
                                "\n\033[93mX-Content-Type-Options: nosniff;\033[0m\n"
                                "\n2.Dosya İndirme Güvenliği Sorunları: Kullanıcıların dosyaları yanlış MIME türleriyle açmasını önlemek için yine 'nosniff' özelliğini kullanabilirsiniz:"
                                "\n\033[93mX-Content-Type-Options: nosniff;\033[0m\n"
                                "\n3.IE (Internet Explorer) Uyumlu Tarayıcılarda Etkin Olmama Sorunu: Bu başlığın IE gibi eski tarayıcılarda etkili olabilmesi için, modern tarayıcılarda desteklenen bir CSP (Content-Security-Policy) politikası oluşturabilirsiniz ve tarayıcınızın uyumsuz eski sürümlerini hedeflemekten kaçınabilirsiniz:"
                                "\n\033[93mContent-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline';\033[0m\n"
                                "\n4.Tarayıcı Uyumluluğu Sorunları: Tarayıcı uyumluluğu sorunlarına karşı savunmak için 'nosniff' özelliğiyle birlikte bir CSP politikası kullanabilirsiniz. Bu, tarayıcı uyumluluğunu artırabilir ve güvenlik açıklarını en aza indirebilir."
                                "\n\033[93mX-Content-Type-Options: nosniff; Content-Security-Policy: default-src 'self';\033[0m\n"
                                "\n5.Güvenlik Eksikliği ve Yanlış Pozitifler: Yanlış pozitiflerden kaçınmak için, X-Content-Type-Options başlığını kullanırken içerik türlerinizi doğru bir şekilde belirlemeniz önemlidir. Tarayıcıların içeriği yanlış yorumlamasını önlemek için en uygun MIME türünü belirleyin ve bu başlığı etkinleştirin:"
                                "\n\033[93mX-Content-Type-Options: nosniff;\033[0m\n",

    "X-Frame-Options":          "1.Clickjacking Saldırıları: Clickjacking saldırılarını engellemek için X-Frame-Options başlığını kullanabilirsiniz. Bu başlık, sayfanızın başka bir çerçevede görüntülenmesini engelleyebilir. En güvenli politika, tüm çerçeveleri reddeden 'DENY' ayarını kullanmaktır: Bu, sayfanızın herhangi bir çerçevede görüntülenmesini engeller."
                                "\n\033[93mX-Frame-Options: DENY;\033[0m\n"
                                "\n2.UI Kullanıcı Deneyimi Sorunları: X-Frame-Options başlığını kullanarak sayfanızın başka çerçevelerde görüntülenmesini engellediğinizde, bu tür sorunları önleyebilirsiniz. Yine 'DENY' ayarı kullanılabilir."
                                "\n\033[93mX-Frame-Options: DENY;\033[0m\n"
                                "\n3.Güvenlik Sorunları: X-Frame-Options başlığı, sayfanızın başka bir çerçevede görüntülenmesini engellediğinde, potansiyel güvenlik açıklarını önleyebilir. DENY' ayarı bu tür sorunları en aza indirir:"
                                "\n\033[93mX-Frame-Options: DENY;\033[0m\n"
                                "\n4.Tarayıcı Uyumluluğu Sorunları: X-Frame-Options başlığının 'DENY' veya 'SAMEORIGIN' gibi uygun bir ayarla kullanılması, tarayıcı uyumluluğu sorunlarını minimize eder:"
                                "\n\033[93mX-Frame-Options: DENY;\033[0m veya \033[93mX-Frame-Options: SAMEORIGIN;\033[0m\n"
                                "'SAMEORIGIN' seçeneği, sayfanızın sadece aynı kökenli (origin) web siteleri içinde çerçevelerde görüntülenmesine izin verir.\n"
                                "\n5.Başka Web Siteleriyle Entegrasyon Sorunları: X-Frame-Options başlığını kullanarak başka web siteleriyle entegrasyonu kontrol edebilirsiniz. Örneğin, 'SAMEORIGIN' ayarı, yalnızca aynı kökenli web sitelerinin sayfanızı çerçevede görmesine izin verir:"
                                "\n\033[93mX-Frame-Options: SAMEORIGIN;\033[0m\n",

"Strict-Transport-Security":    "1.Başlangıçta Eksik veya Yanlış Yapılandırılmış HSTS: HSTS başlığını kullanmanın ilk adımı, web sunucusunun yanıtına HSTS politikasını eklemektir. En basit HSTS politikası, tüm alt alanlarda ve maksimum bir yıl boyunca HTTPS kullanımını zorunlu kılar:"
                                "\n\033[93mStrict-Transport-Security: max-age=31536000; includeSubDomains;\033[0m\n"
                                "Bu, tüm alt alanlarda (includeSubDomains) bir yıl (31536000 saniye) boyunca HSTS'nin etkin olduğu anlamına gelir.\n"
                                "\n2.Ulaşılabilirlik Sorunları: HSTS politikasını başlatırken, kullanıcıların sorun yaşamaması için dikkatli olmalısınız. İlk HSTS politikası oluştururken, önbellek sorunlarından kaçınmak için kısa bir 'max-age' süresi kullanabilirsiniz:"
                                "\n\033[93mStrict-Transport-Security: max-age=300; includeSubDomains;\033[0m\n"
                                "Daha sonra bu süreyi daha uzun bir süreyle değiştirebilirsiniz.\n"
                                "\n3.Tarayıcı Uyumsuzluğu: Tarayıcı uyumsuzluğunu en aza indirmek için, HSTS politikasını yayınlamadan önce tarayıcıların bu özelliği desteklediğinden emin olmalısınız. Tarayıcı uyumluluğunu kontrol etmek için tarayıcıların belgelerini veya kaynaklarını kontrol edebilirsiniz.\n"
                                "\n4.Bağlantı Kurma Süreçlerinde Sorunlar: HSTS politikasını başlattığınızda, kullanıcıların web sitesine erişiminde sorun yaşamamaları için sunucunuzun HTTPS'yi desteklemesi gerekmektedir. Ayrıca, web sitesi sahipleri, HSTS ile ilişkilendirilen alt alanlarda da HTTPS'yi zorunlu kılmak için 'includeSubDomains' kullanabilirler.\n"
                                "\n5.Sertifika Sorunları: HSTS kullanımı, geçerli ve güvenilir bir SSL/TLS sertifikasına sahip olmayı gerektirir. Sertifika süresinin dolmasını veya geçerliliğini yitirmesini önlemek için sertifikanızı düzenli olarak güncellemelisiniz.\n",

    "Referrer-Policy":          "1.Referans Bilgisinin Sızdırılması: Referrer bilgisini tamamen devre dışı bırakmak isterseniz, 'no-referrer' politikasını kullanabilirsiniz. Bu, referrer bilgisini hiçbir istekle iletmeyecektir:"
                                "\n\033[93mReferrer-Policy: no-referrer;\033[0m\n"
                                "\n2.Güvenilmez Web Sitelerine Veri Sızdırma: Referrer bilgisini sadece aynı originli (aynı kökendeki) sitelere iletmek için 'same-origin' politikasını kullanabilirsiniz. Bu, referrer bilgisinin yalnızca aynı kökenli web sitelerine gönderilmesini sağlar:"
                                "\n\033[93mReferrer-Policy: same-origin;\033[0m\n"
                                "\n3.Üçüncü Taraf Web Sitelerinin Takibi: Üçüncü taraf web sitelerinin referrer bilgisini almasını önlemek için 'no-referrer-when-downgrade' politikasını kullanabilirsiniz. Bu politika, HTTPS'den HTTP'ye geçişlerde referrer bilgisini sızdırmaz, ancak aynı originli isteklerde sızdırır:"
                                "\n\033[93mReferrer-Policy: no-referrer-when-downgrade;\033[0m\n"
                                "\n4.Gizlilik Sorunları: Kullanıcıların gizliliğini daha fazla korumak için 'origin' politikasını kullanabilirsiniz. Bu, referrer bilgisini yalnızca origin bilgisiyle gönderir:"
                                "\n\033[93mReferrer-Policy: origin;\033[0m\n"
                                "\n5.Sosyal Mühendislik Saldırıları:Sosyal mühendislik saldırılarına karşı daha fazla koruma sağlamak için yine 'origin' politikasını kullanabilirsiniz:"
                                "\n\033[93mReferrer-Policy: origin;\033[0m\n"
                                "\n6.Web Uygulamalarının Güvenliği: Web uygulamalarının güvenliğini artırmak için, referrer bilgisini sadece aynı originli isteklerde göndermek için 'same-origin' politikasını kullanabilirsiniz:"
                                "\n\033[93mReferrer-Policy: same-origin;\033[0m\n"

}

# HTTP başlıkları için gerekli olanları bir listede saklayın
REQUIRED_HEADERS = [
    "Content-Security-Policy",
    "X-XSS-Protection",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "Referrer-Policy",
]

def bilgi_blogu(header_name):
    if header_name in HEADER_INFO:
        return f"\033[91m{header_name} Başlığı Hakkında Bilgi:\033[0m\n{HEADER_INFO[header_name]}"
    else:
        return f"\033[91m{header_name} Başlığı Hakkında Bilgi: Bilgi mevcut değil.\033[0m"

def get_http_headers(input_value):
    try:
        response = requests.head(input_value)
        headers = response.headers
        return headers
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Hata:" + Style.RESET_ALL, e)
        return None

def list_http_headers(url):
    headers = get_http_headers(url)
    if headers:
        print(Fore.RED + "\nHTTP Yanıt Başlıkları:" + Style.RESET_ALL)
        for i, (key, value) in enumerate(headers.items(), start=1):
            print(Fore.CYAN + f"{i}. {key}" + Fore.RESET, value)

def check_custom_headers(url):
    headers = get_http_headers(url)
    if headers:
        custom_headers = input("Kontrol etmek istediğiniz HTTP başlıklarını virgülle ayırarak girin (örnek: 1,2,3): ").split(',')
        try:
            print(Fore.RED + "\nBelirtilen HTTP Başlıkları:" + Style.RESET_ALL)
            for header_num in custom_headers:
                header_num = int(header_num.strip()) - 1
                header_list = list(headers.items())
                if 0 <= header_num < len(header_list):
                    key, value = header_list[header_num]
                    print(Fore.CYAN + f"{header_num + 1}. {key}:" + Fore.RESET, value)
                else:
                    print(Fore.YELLOW + f"{header_num + 1}: Geçersiz başlık numarası." + Fore.RESET)
        except ValueError:
            print(Fore.RED + "Hata: Geçersiz giriş." + Style.RESET_ALL)

def custom_headers(url):
    headers = get_http_headers(url)
    if headers:
        print(Fore.RED + "\nHTTP Yanıt Başlıkları:" + Style.RESET_ALL)
        for i, (key, value) in enumerate(headers.items(), start=1):
            print(Fore.CYAN + f"{i}. {key}:" + Fore.RESET, value)

        print("\nHTTP Security Headers:")
        missing_headers = [header for header in REQUIRED_HEADERS if not headers.get(header)]
        for header in missing_headers:
            print(bilgi_blogu(header))
        if missing_headers:
            print(Fore.RED + "\nMissing Headings:" + Style.RESET_ALL)
            for header in missing_headers:
                print(Fore.YELLOW + "(!) " + Style.RESET_ALL + header)

if __name__ == "__main__":
    while True:
        print("\033[92m" + """
        Seçenekler:
        1. HTTP Başlıklarını Listele
        2. Kullanıcı Belirlediği HTTP Response Headers Başlıkları Kontrol Et
        3. Belirli bir URL'nin HTTP Yanıt Başlıklarını ve Default Başlıkları Göster
        4. Çıkış
        """ + "\033[0m")

        choice = input("Seçenek numarasını girin: ")
        if choice == "1":
            user_input = input("Lütfen URL veya IP adresini girin: ")
            time.sleep(4)
            url = f"http://{user_input}" if not re.match(r'^(https?://)', user_input) else user_input
            list_http_headers(url)
        elif choice == "2":
            user_input = input("Lütfen URL veya IP adresini girin: ")
            time.sleep(4)
            url = f"http://{user_input}" if not re.match(r'^(https?://)', user_input) else user_input
            check_custom_headers(url)
        elif choice == "3":
            user_input = input("Lütfen URL veya IP adresini girin: ")
            time.sleep(4)
            url = f"http://{user_input}" if not re.match(r'^(https?://)', user_input) else user_input
            custom_headers(url)
        elif choice == "4":
            time.sleep(4)
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçenek! Lütfen 1, 2, 3 veya 4 girin.")
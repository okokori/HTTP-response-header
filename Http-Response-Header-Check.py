#!/usr/bin/env python3

import requests
from colorama import Fore, Back, Style, init
import time
import re
import argparse 
from tabulate import tabulate
from prettytable import PrettyTable



print(Fore.MAGENTA + """ 

  _    _ _______ _______ _____    _____  ______  _____ _____   ____  _   _  _____ ______   _    _ ______          _____  ______ _____     _____ _    _ ______ _____ _  __
 | |  | |__   __|__   __|  __ \  |  __ \|  ____|/ ____|  __ \ / __ \| \ | |/ ____|  ____| | |  | |  ____|   /\   |  __ \|  ____|  __ \   / ____| |  | |  ____/ ____| |/ /
 | |__| |  | |     | |  | |__) | | |__) | |__  | (___ | |__) | |  | |  \| | (___ | |__    | |__| | |__     /  \  | |  | | |__  | |__) | | |    | |__| | |__ | |    | ' / 
 |  __  |  | |     | |  |  ___/  |  _  /|  __|  \___ \|  ___/| |  | | . ` |\___ \|  __|   |  __  |  __|   / /\ \ | |  | |  __| |  _  /  | |    |  __  |  __|| |    |  <  
 | |  | |  | |     | |  | |      | | \ \| |____ ____) | |    | |__| | |\  |____) | |____  | |  | | |____ / ____ \| |__| | |____| | \ \  | |____| |  | | |___| |____| . \ 
 |_|  |_|  |_|     |_|  |_|      |_|  \_\______|_____/|_|     \____/|_| \_|_____/|______| |_|  |_|______/_/    \_\_____/|______|_|  \_\  \_____|_|  |_|______\_____|_|\_|
                                                                                                                                                                         
                                                                                                                                                        Developed by x3chs  """ + Style.RESET_ALL)

# Store information about HTTP headers in a dictionary
HEADER_INFO = {
    "Content-Security-Policy": "1. Cross-Site Scripting (XSS) Attacks: To prevent XSS attacks, use a CSP policy that does not enable insecure sources and blocks risky operations like 'unsafe-inline' and 'unsafe-eval'. An example policy could be:"
                               "\n\033[93mContent-Security-Policy: default-src 'self'; script-src 'self' 'nonce-RANDOM_NONCE_VALUE'\033[0m\n"
                               "Using a nonce (a one-time use permission code) to load only scripts from specific sources provides additional protection against XSS attacks.\n"
                               "\n2. Violation of Resource Restrictions: Make sure that your policies meet the requirements of your application. Do not block necessary resources and only allow trusted sources:"
                               "\n\033[93mContent-Security-Policy: default-src 'self' trusted-source.com; script-src 'self' 'unsafe-inline' 'unsafe-eval' trusted-source.com\033[0m\n"
                               "\n3. Reporting Issues: Properly configuring reporting feature is important to monitor security breaches:"
                               "\n\033[93mContent-Security-Policy: default-src 'self'; report-uri /csp-report-endpoint;\033[0m\n"
                               "This policy allows browsers to send security breaches to a specified reporting URL.\n"
                               "\n4. Content Issues: Carefully define policies to not hinder the functionality of your page. Create a policy that identifies your requirements and resources:"
                               "\n\033[93mContent-Security-Policy: default-src 'self' trusted-source.com; img-src 'self' img-source.com;\033[0m\n"
                               "\n5. Outdated Policies: It is important to regularly update and align CSP policies with security needs. Policies should be reviewed periodically and updated as needed.\n"
                               "\n6. Lack of Testing: Create test scenarios to verify the effectiveness of CSP policies. Test your policies in different browser versions and scenarios to ensure their functionality.\n"
                               "\n7. Insecure Configurations: Configure policies correctly and limit access to insecure sources or malicious websites:"
                               "\n\033[93mContent-Security-Policy: default-src 'self' trusted-source.com; frame-src 'self' trusted-source.com;\033[0m\n",
    
    "X-XSS-Protection":     "1. Not Valid for Old and Incompatible Browsers: To address this vulnerability, you can use a CSP policy supported by modern browsers instead of enabling X-XSS-Protection. CSP is supported by a wider range of browsers. An example CSP policy could be:"
                            "\n\033[93mContent-Security-Policy: default-src 'self';\033[0m\n"
                            "\n2. Can Be Disabled: To prevent users from disabling X-XSS-Protection, you can make CSP mandatory by using CSP policy. It also prevents browsers from disabling this policy. Example:"
                            "\n\033[93mContent-Security-Policy: default-src 'self'; x-xss-protection '1; mode=block';\033[0m\n"
                            "\n3. Provides Limited Protection: To provide stronger protection against XSS attacks, you can tighten the 'script-src' or 'default-src' sections of CSP. For example, allowing scripts only from trusted sources:"
                            "\n\033[93mContent-Security-Policy: default-src 'self'; script-src 'self' trusted-scripts.com;\033[0m\n"
                            "\n4. Lack of Domain Control: CSP policies can be used to specify other security requirements (e.g., content security policies). Create a comprehensive security policy using multiple security headers:"
                            "\n\033[93mContent-Security-Policy: default-src 'self'; frame-src 'self' trusted-frames.com;\033[0m\n"
                            "\n5. Level of Protection Issues: To provide a more sensitive level of protection than X-XSS-Protection, you can tighten the CSP policy. For example, you can achieve a similar effect as 'mode=block':"
                            "\n\033[93mContent-Security-Policy: default-src 'self'; script-src 'self' 'nonce-RANDOM_NONCE_VALUE';\033[0m\n"
                            "\n6. Protection False Positives: Be careful when defining CSP policies to not block unwanted scripts without hindering functionality. Create a policy that allows the correct sources by:"
                            "\n\033[93mContent-Security-Policy: default-src 'self' trusted-sources.com; script-src 'self' 'unsafe-inline' 'unsafe-eval' trusted-sources.com;\033[0m\n",
    
    "X-Content-Type-Options": "1. Security Issues When MIME Type is Missing or Misconfigured: To address this vulnerability, you can use the 'nosniff' (refuse to change MIME type) feature to prevent browsers from changing or interpreting the content. Here's an example policy:"
                              "\n\033[93mX-Content-Type-Options: nosniff;\033[0m\n"
                              "\n2. File Download Security Issues: You can use the 'nosniff' feature to prevent users from opening files with incorrect MIME types:"
                              "\n\033[93mX-Content-Type-Options: nosniff;\033[0m\n"
                              "\n3. Not Effective in IE (Internet Explorer) Compatible Browsers: To make this header effective in older browsers like IE, you can create a CSP (Content-Security-Policy) policy supported by modern browsers and avoid targeting incompatible older versions of browsers:"
                              "\n\033[93mContent-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline';\033[0m\n"
                              "\n4. Browser Compatibility Issues: You can use a CSP policy along with the 'nosniff' feature to increase browser compatibility and minimize security vulnerabilities."
                              "\n\033[93mX-Content-Type-Options: nosniff; Content-Security-Policy: default-src 'self';\033[0m\n"
                              "\n5. Security Gaps and False Positives: When using the X-Content-Type-Options header, it is important to correctly specify your content types to avoid false positives. Determine the appropriate MIME type to prevent browsers from misinterpreting the content and enable this header:"
                              "\n\033[93mX-Content-Type-Options: nosniff;\033[0m\n",
    
    "X-Frame-Options": "1. Clickjacking Attacks: You can use the X-Frame-Options header to prevent clickjacking attacks. This header can prevent your page from being displayed in another frame. The most secure policy is to deny all frames: This prevents your page from being displayed in any frame."
                       "\n\033[93mX-Frame-Options: DENY;\033[0m\n"
                       "\n2. UI User Experience Issues: By using the X-Frame-Options header to prevent your page from being displayed in other frames, you can prevent such issues. Again, the 'DENY' setting can be used."
                       "\n\033[93mX-Frame-Options: DENY;\033[0m\n"
                       "\n3. Security Issues: The X-Frame-Options header can prevent potential security vulnerabilities when your page is displayed in another frame. The 'DENY' setting minimizes such issues:"
                       "\n\033[93mX-Frame-Options: DENY;\033[0m\n"
                       "\n4. Browser Compatibility Issues: Using the 'DENY' or 'SAMEORIGIN' setting with the X-Frame-Options header minimizes browser compatibility issues:"
                       "\n\033[93mX-Frame-Options: DENY;\033[0m or \033[93mX-Frame-Options: SAMEORIGIN;\033[0m\n"
                       "The 'SAMEORIGIN' option allows your page to be displayed in frames only within the same origin.\n"
                       "\n5. Integration Issues with Other Websites: You can control integration with other websites using the X-Frame-Options header. For example, the 'SAMEORIGIN' setting allows your page to be displayed in frames only within the same origin:"
                       "\n\033[93mX-Frame-Options: SAMEORIGIN;\033[0m\n",
    
    "Strict-Transport-Security": "1. Missing or Misconfigured HSTS at the Beginning: The first step to using HSTS is adding the HSTS policy to the web server's response. The simplest HSTS policy enforces the use of HTTPS on all subdomains for a maximum of one year:"
                                 "\n\033[93mStrict-Transport-Security: max-age=31536000; includeSubDomains;\033[0m\n"
                                 "This means that HSTS is active for all subdomains (includeSubDomains) for one year (31536000 seconds).\n"
                                 "\n2. Accessibility Issues: When initiating HSTS, you should be careful to avoid issues for users. When creating the first HSTS policy, you can use a short 'max-age' period to avoid caching issues:"
                                 "\n\033[93mStrict-Transport-Security: max-age=300; includeSubDomains;\033[0m\n"
                                 "Later, you can change this period to a longer duration.\n"
                                 "\n3. Browser Incompatibility: To minimize browser incompatibility, ensure that browsers support this feature before publishing the HSTS policy. You can check browser documentation or resources to verify browser compatibility."
                                 "\n\033[93mStrict-Transport-Security: max-age=31536000; includeSubDomains; preload;\033[0m\n"
                                 "The 'preload' option allows you to submit your domain to the HSTS preload list maintained by browser vendors.\n"
                                 "\n4. Issues in Connection Establishment: When initiating the HSTS policy, your server must support HTTPS for users to access your website. Additionally, website owners can use 'includeSubDomains' to enforce HTTPS on subdomains associated with HSTS."
                                 "\n\033[93mStrict-Transport-Security: max-age=31536000; includeSubDomains;\033[0m\n"
                                 "\n5. Certificate Issues: HSTS usage requires a valid and trusted SSL/TLS certificate. Regularly update your certificate to prevent expiration or invalidation of the certificate.\n",
    
    "Referrer-Policy": "1. Referrer Information Leakage: If you want to completely disable the referrer information, you can use the 'no-referrer' policy. This will not send the referrer information with any requests:"
                       "\n\033[93mReferrer-Policy: no-referrer;\033[0m\n"
                       "\n2. Data Leakage to Untrusted Websites: To only send the referrer information to same-origin sites, you can use the 'same-origin' policy. This allows the referrer information to be sent only to same-origin websites:"
                       "\n\033[93mReferrer-Policy: same-origin;\033[0m\n"
                       "\n3. Tracking by Third-Party Websites: To prevent third-party websites from receiving the referrer information, you can use the 'no-referrer-when-downgrade' policy. This policy does not leak the referrer information in transitions from HTTPS to HTTP, but leaks it in same-origin requests:"
                       "\n\033[93mReferrer-Policy: no-referrer-when-downgrade;\033[0m\n"
                       "\n4. Privacy Issues: To further protect user privacy, you can use the 'origin' policy. This sends the referrer information only with the origin information:"
                       "\n\033[93mReferrer-Policy: origin;\033[0m\n"
                       "\n5. Social Engineering Attacks: To provide additional protection against social engineering attacks, you can also use the 'origin' policy:"
                       "\n\033[93mReferrer-Policy: origin;\033[0m\n"
                       "\n6. Web Application Security: To enhance the security of web applications, you can use the 'same-origin' policy to send the referrer information only in same-origin requests:"
                       "\n\033[93mReferrer-Policy: same-origin;\033[0m\n"
}

# Store the required HTTP headers in a list
REQUIRED_HEADERS = ["Content-Security-Policy", "Strict-Transport-Security", "X-Content-Type-Options",
                    "X-Frame-Options", "X-XSS-Protection"]

def info_blog(header_name):
    if header_name in HEADER_INFO:
        return [header_name, HEADER_INFO[header_name]]
    else:
        return [header_name, "Information not available."]

def get_http_headers(input_value):
    try:
        response = requests.head(input_value)
        headers = response.headers
        return headers
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Error:" + Style.RESET_ALL, e)
        return None

def list_http_headers(url): # Option 1
    headers = get_http_headers(url)
    if headers:
        print(Fore.RED + "\nHTTP Response Headers:" + Style.RESET_ALL)
        header_table = PrettyTable()
        header_table.field_names = [Fore.CYAN + "Header" + Style.RESET_ALL]
        header_table.padding_width = 1
        header_table.align[Fore.CYAN + "Header" + Style.RESET_ALL] = "l"
        header_table.horizontal_char = "─"  # Horizontal line character
        header_table.vertical_char = "│"  # Vertical line character
        header_table.junction_char = "┼"  # Junction line character
        for i, (key, _) in enumerate(headers.items(), start=1):
            header_table.add_row([f"{i}. {key}"])
        print(header_table)

def check_custom_headers(url): # Option 2
    headers = get_http_headers(url)
    if headers:
        custom_headers = input("Enter the HTTP headers you want to check, separated by commas (e.g., 1,2,3): ").split(',')
        try:
            print(Fore.RED + "\nSpecified HTTP Headers:" + Style.RESET_ALL)
            header_table = PrettyTable()
            header_table.field_names = [Fore.CYAN + "Header" + Style.RESET_ALL, Fore.CYAN + "Value" + Style.RESET_ALL]
            header_table.padding_width = 1
            header_table.align[Fore.CYAN + "Header" + Style.RESET_ALL] = "l"
            header_table.align[Fore.CYAN + "Value" + Style.RESET_ALL] = "l"
            header_table.horizontal_char = "─"  # Horizontal line character
            header_table.vertical_char = "│"  # Vertical line character
            header_table.junction_char = "┼"  # Junction line character
            for header_num in custom_headers:
                header_num = int(header_num.strip()) - 1
                header_list = list(headers.items())
                if 0 <= header_num < len(header_list):
                    key, value = header_list[header_num]
                    header_table.add_row([f"{header_num + 1}. {key}", value])
                else:
                    print(Fore.YELLOW + f"{header_num + 1}: Invalid header number." + Fore.RESET)
            print(header_table)
        except ValueError:
            print(Fore.RED + "Error: Invalid input." + Style.RESET_ALL)

def main():
    url = input("Enter the URL you want to check the headers for: ")
    list_http_headers(url)
    check_custom_headers(url)
    custom_headers(url)

def custom_headers(url): # Option 3
    headers = get_http_headers(url)
    if headers:
        print(Fore.CYAN + "\nHTTP Response Headers:" + Style.RESET_ALL)
        header_table = PrettyTable()
        header_table.field_names = [Fore.CYAN + "Header" + Style.RESET_ALL, Fore.CYAN + "Value" + Style.RESET_ALL]
        header_table.padding_width = 1
        header_table.align[Fore.CYAN + "Header" + Style.RESET_ALL] = "l"
        header_table.align[Fore.CYAN + "Value" + Style.RESET_ALL] = "l"
        header_table.horizontal_char = "─"  # Horizontal line character
        header_table.vertical_char = "│"  # Vertical line character
        header_table.junction_char = "┼"  # Junction line character
        for i, (key, value) in enumerate(headers.items(), start=1):
            header_table.add_row([f"{i}. {key}", value])
        print(header_table)

        print(Fore.RED +"\nHTTP Security Headers:"+ Style.RESET_ALL)
        missing_headers = [header for header in REQUIRED_HEADERS if not headers.get(header)]
        missing_header_table = PrettyTable()
        missing_header_table.field_names = [Fore.CYAN + "Header" + Style.RESET_ALL, Fore.CYAN + "Info" + Style.RESET_ALL]
        missing_header_table.padding_width = 1
        missing_header_table.align[Fore.CYAN + "Header" + Style.RESET_ALL] = "l"
        missing_header_table.align[Fore.CYAN + "Info" + Style.RESET_ALL] = "l"
        missing_header_table.horizontal_char = "─"  # Horizontal line character
        missing_header_table.vertical_char = "│"  # Vertical line character
        missing_header_table.junction_char = "┼"  # Junction line character
        for header in missing_headers:
            missing_header_table.add_row(info_blog(header))
        missing_header_table.max_width = 140
        print(missing_header_table)

        if missing_headers:
            print(Fore.RED + "\nMissing Headers:" + Style.RESET_ALL)
            missing_header_table = PrettyTable()
            missing_header_table.field_names = [Fore.CYAN + "Header" + Style.RESET_ALL]
            missing_header_table.padding_width = 1
            missing_header_table.align[Fore.CYAN + "Header" + Style.RESET_ALL] = "l"
            missing_header_table.horizontal_char = "─"  # Horizontal line character
            missing_header_table.vertical_char = "│"  # Vertical line character
            missing_header_table.junction_char = "┼"  # Junction line character
            for header in missing_headers:
                missing_header_table.add_row([f"{header}"])
            missing_header_table.max_width = 140
            print(missing_header_table)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-g","--guide", action="store_true", help="Show help page")
    args = parser.parse_args()
    if args.guide:
        print("""
            Project Guide
        This Python script is designed to check the security status of websites by examining HTTP headers.
        The script can perform the following operations by targeting a specific URL and checking the relevant HTTP headers:
        1. List HTTP Headers: This option lists the response headers of a specific URL.
        2. Check User-Defined HTTP Response Headers: This option checks user-defined HTTP response headers.
        3. Show HTTP Response Headers and Default Headers of a Specific URL: This option shows the HTTP response headers of a specific URL and the security-related headers.
        4. Exit: Exits the script.
        While using the script, you can follow these options and check the security headers of websites. 
        The script can be a useful tool to enhance the security of your web applications and identify potential security vulnerabilities.
        """)
    while True:
        print("\033[92m" + """
        Options:
        1. List HTTP Headers
        2. Check User-Defined HTTP Response Headers
        3. Show HTTP Response Headers and Default Headers of a Specific URL
        4. Exit
        """ + "\033[0m")
        choice = input("Enter the option number: ")
        if choice == "1":
            user_input = input("Please enter the URL or IP address: ")
            time.sleep(3)
            url = f"http://{user_input}" if not re.match(r'^(https?://)', user_input) else user_input
            list_http_headers(url)
        elif choice == "2":
            user_input = input("Please enter the URL or IP address: ")
            time.sleep(3)
            url = f"http://{user_input}" if not re.match(r'^(https?://)', user_input) else user_input
            check_custom_headers(url)
        elif choice == "3":
            user_input = input("Please enter the URL or IP address: ")
            time.sleep(3)
            url = f"http://{user_input}" if not re.match(r'^(https?://)', user_input) else user_input
            custom_headers(url)
        elif choice == "4":
            time.sleep(3)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
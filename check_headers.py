import requests

def check_headers(headers):
    missing_headers = []
    highlighted_headers = []
    for header in ['X-Frame-Options', 'X-XSS-Protection', 'Content-Security-Policy']:
        if header not in headers:
            missing_headers.append(header)
        else:
            highlighted_headers.append(header)
    return missing_headers, highlighted_headers

def suggest_solutions(missing_headers):
    solutions = {}
    red_color = "\033[91m"
    reset_color = "\033[0m"
    for header in missing_headers:
        if header == 'X-Frame-Options':
            solutions[header] = f"{red_color}X-Frame-Options headerını ekleyin ve değeri 'DENY' olarak ayarlayın.{reset_color}"
        elif header == 'X-XSS-Protection':
            solutions[header] = f"{red_color}X-XSS-Protection headerını ekleyin ve değeri '1; mode=block' olarak ayarlayın.{reset_color}"
        elif header == 'Content-Security-Policy':
            solutions[header] = f"{red_color}Content-Security-Policy headerını ekleyin ve gerekli politikaları belirleyin.{reset_color}"
    return solutions

def show_results(headers, solutions, highlighted_headers):
    print("Header Kontrol Sonuçları:\n")
    for header, value in headers.items():
        if header in highlighted_headers:
            print(f"\033[93m{header}: {value}\033[0m")
        else:
            print(f"{header}: {value}")
    print("\nÇözüm Önerileri:\n")
    for header, solution in solutions.items():
        print(f"{header} için çözüm önerisi: {solution}")

def main():
    target = input("Hedef domain veya IP adresini girin: ")
    response = requests.get(target)
    headers = response.headers
    missing_headers, highlighted_headers = check_headers(headers)
    solutions = suggest_solutions(missing_headers)
    show_results(headers, solutions, highlighted_headers)

if __name__ == "__main__":
    main()
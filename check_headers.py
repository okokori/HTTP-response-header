import requests

def check_headers(headers):
    missing_headers = []
    for header in ['X-Frame-Options', 'X-XSS-Protection', 'Content-Security-Policy']:
        if header not in headers:
            missing_headers.append(header)
    return missing_headers

def suggest_solutions(missing_headers):
    solutions = {}
    for header in missing_headers:
        if header == 'X-Frame-Options':
            solutions[header] = "X-Frame-Options headerını ekleyin ve değeri 'DENY' olarak ayarlayın."
        elif header == 'X-XSS-Protection':
            solutions[header] = "X-XSS-Protection headerını ekleyin ve değeri '1; mode=block' olarak ayarlayın."
        elif header == 'Content-Security-Policy':
            solutions[header] = "Content-Security-Policy headerını ekleyin ve gerekli politikaları belirleyin."
    return solutions

def show_results(headers, solutions):
    print("Header Kontrol Sonuçları:\n")
    for header, value in headers.items():
        print(f"{header}: {value}")
    print("\nÇözüm Önerileri:\n")
    for header, solution in solutions.items():
        print(f"{header} için çözüm önerisi: {solution}")

def main():
    target = input("Hedef domain veya IP adresini girin: ")
    response = requests.get(target)
    headers = response.headers
    headers['HTTP Durumu'] = response.status_code
    missing_headers = check_headers(headers)
    solutions = suggest_solutions(missing_headers)
    show_results(headers, solutions)

if __name__ == "__main__":
    main()
import requests

# Function to check various HTTP headers
def check_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        results = []

        # Check X-Frame-Options header
        xfo_header = headers.get('X-Frame-Options', None)
        if xfo_header is None:
            results.append({
                'header': 'X-Frame-Options',
                'issue': 'Header is missing',
                'solution': 'Add an X-Frame-Options header with the value "DENY" or "SAMEORIGIN" to prevent clickjacking attacks.'
            })

        # Check Content-Security-Policy header
        csp_header = headers.get('Content-Security-Policy', None)
        if csp_header is None:
            results.append({
                'header': 'Content-Security-Policy',
                'issue': 'Header is missing',
                'solution': 'Add a Content-Security-Policy header to define a security policy for your site.'
            })

        # Check Strict-Transport-Security header
        hsts_header = headers.get('Strict-Transport-Security', None)
        if hsts_header is None:
            results.append({
                'header': 'Strict-Transport-Security',
                'issue': 'Header is missing',
                'solution': 'Add a Strict-Transport-Security header to enforce secure HTTPS connections.'
            })

        # Check X-Content-Type-Options header
        xcto_header = headers.get('X-Content-Type-Options', None)
        if xcto_header is None:
            results.append({
                'header': 'X-Content-Type-Options',
                'issue': 'Header is missing',
                'solution': 'Add an X-Content-Type-Options header with the value "nosniff" to prevent MIME-type sniffing.'
            })

        # Check X-XSS-Protection header
        xss_header = headers.get('X-XSS-Protection', None)
        if xss_header is None:
            results.append({
                'header': 'X-XSS-Protection',
                'issue': 'Header is missing',
                'solution': 'Add an X-XSS-Protection header with the value "1; mode=block" to enable XSS protection.'
            })

        # Check Cache-Control header
        cache_header = headers.get('Cache-Control', None)
        if cache_header is None:
            results.append({
                'header': 'Cache-Control',
                'issue': 'Header is missing',
                'solution': 'Add a Cache-Control header to control caching behavior.'
            })

        # Check Server header
        server_header = headers.get('Server', None)
        if server_header is not None:
            results.append({
                'header': 'Server',
                'issue': 'Server information disclosed',
                'solution': 'Consider removing or obfuscating the Server header for security through obscurity.'
            })

        # Check X-Powered-By header
        powered_by_header = headers.get('X-Powered-By', None)
        if powered_by_header is not None:
            results.append({
                'header': 'X-Powered-By',
                'issue': 'Server technology disclosed',
                'solution': 'Consider removing or obfuscating the X-Powered-By header for security through obscurity.'
            })

        return results
    except Exception as e:
        return [{'error': str(e)}]

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    header_results = check_headers(target_url)

    if 'error' in header_results[0]:
        print(f"Error occurred while checking headers: {header_results[0]['error']}")
    else:
        print("\nSecurity Check Results:")
        for result in header_results:
            print(f"Header: {result['header']}")
            print(f"Issue: {result['issue']}")
            print(f"Solution: {result['solution']}\n")
            
import pyshorteners

def main():
    print("=" * 50)
    print("URL SHORTENER")
    print("=" * 50)
    
    # Get URL from user
    url = input("Enter URL to shorten: ").strip()
    
    # Add protocol if missing
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        # Shorten using is.gd
        s = pyshorteners.Shortener()
        short_url = s.isgd.short(url)
        
        print("\n" + "=" * 50)
        print("RESULTS")
        print("=" * 50)
        print(f"Original: {url}")
        print(f"Shortened: {short_url}")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    # Install required package: pip install pyshorteners
    main()
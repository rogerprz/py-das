import urllib.request

def main():
    web_url = urllib.request.urlopen("http://www.google.com")
    print("result code: " + str(web_url.getcode()))
    data = web_url.read()
    print(data)
if __name__ == "__main__":
    main()

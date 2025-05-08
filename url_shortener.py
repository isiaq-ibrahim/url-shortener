import pyshorteners

url = input("Enter URL to shorten:\n")
shortener = pyshorteners.Shortener()
print("New URL:", shortener.tinyurl.short(url))
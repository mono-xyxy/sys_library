import requests

print("URL Shortener CLI")

url = input("Enter long url :")

api_url =  f"http://tinyurl.com/api-create.php?url={url}"


response = requests.get(api_url)

if response.status_code == 200:
    print("\nShortened URL:")
    print(response.text)

else:
    print("\nShortened URL:")
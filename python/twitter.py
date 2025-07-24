import re
url=input("URL: ").strip()
if matches:=re.search(r"^https?://(?:www\.)?twitter\.(?:com|org)/([a-z0-9_]+)", url,re.IGNORECASE):
  print(f"Username:",matches.group(1))
#(?: ) to not capture
#username=re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)          #substitute,? makes s optional


#username=url.replace("https://twitter.com/","")

#username=url.removeprefix("https://twitter.com/")
#print(f"Username: {username}")

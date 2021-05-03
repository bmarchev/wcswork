import requests


wordlist = 'C:\\Users\\MARCH\\Desktop\\wcswork\\your_wordlist.txt'


with open(wordlist) as wl:
   line = wl.readline()
   cnt = 1
   for line in wordlist:
       line = wl.readline()
       cnt += 1
       payload = "https://target_website/{}".format(line)
       r = requests.head(payload)
       result = r.status_code
       if result == 200:
           print("{}{}DOES EXIST".format("/", line,))
       elif result == 301:
           print("{}{}REDIRECTED".format("/", line,))
       else:
           print("{}{}DOES NOT EXIST".format("/", line,))

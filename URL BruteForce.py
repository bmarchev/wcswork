import requests


wordlist = 'C:\\Users\\MARCH\\Desktop\\wcswork\\loltest.txt'


with open(wordlist) as wl:
   line = wl.readline()
   cnt = 1
   for line in wordlist:
       line = wl.readline()
       cnt += 1
       payload = "https://stefanys-creations.com/{}".format(line)
       r = requests.head(payload)
       result = r.status_code
       if result == 200:
           print("{}{}DOES EXIST OR REDIRECTED".format("/", line,))
       elif result == 301:
           print("{}{}REDIRECTED".format("/", line,))
       else:
           print("{}{}DOES NOT EXIST".format("/", line,))

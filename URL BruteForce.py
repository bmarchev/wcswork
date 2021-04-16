import requests
import optparse


wordlist = 'C:\\Users\\MARCH\\Desktop\\bruteforce\\wordlist\\test.txt'
url = "https://s2d-entreprise.fr/"

exploit = open ('C:\\Users\\MARCH\\Desktop\\bruteforce\\wordlist\\test.txt')

for words in exploit:
    r =  requests.get(url, params={wordlist})
    r.status_code


    if r ==200:
        print(r + "DOES exist")

    if r ==404:
        print (r + "DOES NOT exist")



"""
       if b'Mot de passe invalide' in content:
           print("Mauvais mot de passe", password)

       else:
           print(password)
           break
"""

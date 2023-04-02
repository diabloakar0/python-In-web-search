import requests
import time
import os

os.system('cls')

filename = "urllist.txt"
output_file = "output.txt"
aranacak_yazi = "wp-submit"

with open(filename, 'r') as file, open(output_file, 'w') as out:
    lines = file.readlines()
    for line in lines:
        url = line.strip()
        try: # YANLIIIIIIIIIIIIIIIŞ
            r = requests.get(url+"/wp-login.php")
            if r.status_code == 200:
            
                if aranacak_yazi in r.content.decode('latin-1'):
                    out.write("{}\n".format(url.split("wp")[0])) # SİLMEEEEEEEEEEEZ
                    print("Belirtilen yazı {} adresinde mevcut: {}".format(url, aranacak_yazi))
                else:
                    print("Belirtilen yazı {} adresinde mevcut değil: {}".format(url, aranacak_yazi))
            else:
                print("URL {} ziyaret edilemedi".format(url))
        except:
            print("Can't Connect The Server !")
creds

kali / kali

```sh
setxkbmap fr

sudo apt-get update

sudo apt install seclists

ffuf -h
```

## ffuf

    ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt:FUZZ -u https://meedz.io/FUZZ -fs 0

match status code 200

    

    ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt:FUZZ1 -w /usr/share/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ2 -u https://meedz.io/FUZZ1FUZZ2 -fs 0 -mc 200

    ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u https://FUZZ.meedz.io/ 
    
    ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u https://meedz.io/ -H "Host: FUZZ.meedz.io"
    
    ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u https://www.spirkop.com/ -H "Host: FUZZ.spirkop.com" -mc 200


## SecLists

https://github.com/danielmiessler/SecLists


└─$ find /usr/share/seclists -name *french*                             
/usr/share/seclists/Passwords/richelieu-french-top5000.txt
/usr/share/seclists/Passwords/richelieu-french-top20000.txt
/usr/share/seclists/Discovery/Web-Content/common-and-french.txt
/usr/share/seclists/Miscellaneous/lang-french-small.txt
/usr/share/seclists/Miscellaneous/Moby-Project/Moby-Language-II/french.txt
/usr/share/seclists/Miscellaneous/lang-french-full.txt


└─$ find /usr/share/seclists -name *french* -exec du -h {} +
40K     /usr/share/seclists/Passwords/richelieu-french-top5000.txt
152K    /usr/share/seclists/Passwords/richelieu-french-top20000.txt
40K     /usr/share/seclists/Discovery/Web-Content/common-and-french.txt
4.0K    /usr/share/seclists/Miscellaneous/lang-french-small.txt
1.6M    /usr/share/seclists/Miscellaneous/Moby-Project/Moby-Language-II/french.txt
3.8M    /usr/share/seclists/Miscellaneous/lang-french-full.txt
                                                                

## test with meedz

    ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/common-and-french.txt:FUZZ -u https://meedz.io/FUZZ -fs 0 -mc 200


[Status: 200, Size: 185, Words: 10, Lines: 12, Duration: 4274ms]
    * FUZZ: wp-links-opml

[Status: 200, Size: 67, Words: 4, Lines: 4, Duration: 8191ms]
    * FUZZ: robots.txt

User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
    

    ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt:FUZZ -u https://meedz.io/wp-admin/FUZZ.php -fs 0 -mc 200


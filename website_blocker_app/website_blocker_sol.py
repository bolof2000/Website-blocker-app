# adding host file path
import time
from datetime import datetime as dt

host_path = r"\Volumes\Macintosh HD\etc\hosts"
host_temp = "hosts"
redirect = "127.0.0.1"
host_mac = "/etc/hosts"
# websites to block define as array of elements
website_list = ["www.facebook.com","facebook.com","google.com","www.google.com"]
# the goal: the scripts adds and deletes contents from the host file base on the specify periods defined

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):

        print("working hour")
        # adding file handling methods to interact with the host files
        with open(host_temp,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(host_temp,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("fun hour")
        time.sleep(5)

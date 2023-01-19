import requests
from termcolor import colored
import time

def check_proxy(proxy):
    proxy_url = f"http://{proxy['user']}:{proxy['password']}@{proxy['host']}:{proxy['port']}"
    try:
        start_time = time.time()
        # Make a request to a website that returns a 200 status code
        # for success to check if the proxy is working
        response = requests.get("http://www.example.com", proxies={"http": proxy_url, "https": proxy_url}, timeout=3)
        end_time = time.time()
        if response.status_code == 200:
            print(colored(f"{proxy['host']}:{proxy['port']} is working. Time taken: {end_time - start_time:.3f}s", "green"))
        else:
            print(colored(f"{proxy['host']}:{proxy['port']} is not working. Time taken: {end_time - start_time:.3f}s", "red"))
    except:
        end_time = time.time()
        print(colored(f"{proxy['host']}:{proxy['port']} is not working. Time taken: {end_time - start_time:.3f}s", "red"))



#-----Start of execution------
print(colored(f"\n\n--------------------------------------", "yellow"))
print(colored(f"        Proxy list checker", "yellow"))
print(colored(f"---------------polgs------------------\n", "yellow"))
print(colored(f"Tests all proxies in file proxies.txt\n", "yellow"))
print(colored(f"Starting Checks:\n", "yellow"))

# Read the file containing the proxies
with open("proxies.txt", "r") as f:
    proxies = f.readlines()

# Check each proxy
for proxy in proxies:
    proxy_list = proxy.strip().split(":")
    check_proxy({"host":proxy_list[0], "port":proxy_list[1], "user":proxy_list[2], "password":proxy_list[3]})

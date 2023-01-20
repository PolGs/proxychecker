import boto3
import requests
from termcolor import colored
import time

#-----Start of execution------
print(colored(f"\n\n--------------------------------------------------", "blue"))
print(colored(f"            Proxy Manager by polgs             ", "blue"))
print(colored(f"--------------------------------------------------\n", "blue"))
print(colored(f"Gets proxy list and tests all proxies (proxies.txt)\n", "blue"))

#--Get Server List ----

# configure boto3 client for EC2
client = boto3.client('ec2', aws_access_key_id='------keyhere----', aws_secret_access_key='------keyhere----', region_name="eu-central-1")

# retrieve all instances in the account
instances = client.describe_instances()

# loop through instances and print IP addresses
print(colored(f"[*]Searching for proxies\n", "yellow"))
with open("proxies.txt", "w") as file:
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            outs = str(instance.get('PublicIpAddress'))
            if outs != "None":
                outs += ":PORT:USER:PASS\n"
                print(colored(outs, "blue"))
                file.write(outs)
# close the file
file.close()

#--- Test Proxies---

def check_proxy(proxy, site):
    proxy_url = f"http://{proxy['user']}:{proxy['password']}@{proxy['host']}:{proxy['port']}"
    try:
        start_time = time.time()
        # Make a request to a website that returns a 200 status code
        # for success to check if the proxy is working
        response = requests.get(site, proxies={"http": proxy_url, "https": proxy_url}, timeout=3)
        end_time = time.time()
        if response.status_code == 200:
            print(colored(f"{proxy['host']}:{proxy['port']} is working. Time taken: {end_time - start_time:.3f}s", "green"))
        else:
            print(colored(f"{proxy['host']}:{proxy['port']} is not working. Time taken: {end_time - start_time:.3f}s", "red"))
    except:
        end_time = time.time()
        print(colored(f"{proxy['host']}:{proxy['port']} is not working. Time taken: {end_time - start_time:.3f}s", "red"))

print(colored(f"[*]Starting Checks at example.com:", "yellow"))

# Read the file containing the proxies
with open("proxies.txt", "r") as f:
    proxies = f.readlines()

# Check each proxy sitea
for proxy in proxies:
    proxy_list = proxy.strip().split(":")
    check_proxy({"host":proxy_list[0], "port":proxy_list[1], "user":proxy_list[2], "password":proxy_list[3]}, "http://www.example.com")

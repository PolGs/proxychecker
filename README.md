# Proxy Manager
### AWSProxyManager.py
This script is used to manage a list of proxies. The script uses the boto3 library to interact with Amazon Web Services (AWS) and the requests library to test the proxies.
![image](https://user-images.githubusercontent.com/19478700/213590663-ffee2af3-0ace-4e89-a362-cd3580e54687.png)

## How it works
Run the script using python
The script starts by printing some information about the script and its purpose.
Then it uses the boto3 client to connect to the EC2 service and retrieves a list of all instances in the account.
It then loops through the instances and prints the public IP addresses of each instance, if they have any. It also writes the IP addresses to a file called "proxies.txt"
After that, the script defines a function called "check_proxy" which takes in a proxy and a site as parameters, it then constructs a proxy URL using the proxy's host, port, user, and password, it then attempts to make a request to the specified site using the proxy URL and a timeout of 3 seconds.
If the request is successful, it prints that the proxy is working and the time taken to complete the request, otherwise, it prints that the proxy is not working and the time taken to complete the request.
Finally, the script opens the "proxies.txt" file and reads all the proxies, it then calls the "check_proxy" function with each proxy and a test site "http://www.example.com"
The script uses the termcolor library to add color to the output text for better readability. It also uses the time library to measure the time taken to complete the requests.

Note: You need to replace the aws_access_key_id and aws_secret_access_key with your own keys.

# Under Development
A web interface is currently under development to make the use of this script more user-friendly and easily accessible. The web interface will allow users to perform all the functionalities of this script through a web browser, without the need to run the script locally. The web interface will also include additional features such as the ability to save and manage multiple lists of proxies, and to customize the test site.


This is a web application that allows users to check a list of proxies for their validity. The user can paste a list of proxies into a form on the website, and the application will check each proxy against the Google homepage, returning a list of valid and invalid proxies. The application is built using the Flask framework and Python's built-in http.server module. 


![image](https://user-images.githubusercontent.com/19478700/213341350-a57a1685-2ff3-4e87-9bd7-21ed3c4c5dc8.png)
![image](https://user-images.githubusercontent.com/19478700/213341373-5aed4450-e6f2-4db0-8d03-6812f30600b3.png)

# proxychecker_wm.py
Tests all proxies in file proxies.txt (same directory)

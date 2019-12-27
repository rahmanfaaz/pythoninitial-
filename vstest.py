import math
import os
import sys

import requests

name = input (" Your name ?")
print ("hello," , name)
    
r = requests.get("https://google.com")
print(r.status_code)
print(r.ok)
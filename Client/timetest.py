import re

response = "bobos as been defeated"

if re.search("defeated",response):  
    if re.search("bobos", response):
        print("bobos a perdu")
    else:
        print("quelqun dautre")
        
else:
    print(response)
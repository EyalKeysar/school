import os
resource = "/css/doremon.css"
for root, dirs, files in os.walk(r'C:\Networks\school\cyber\homework\send_http\webroot'):
            for name in files:
                print(name)
                if name == resource:
                    print("found")
                    found = True

a = input()
import os, platform
from pyfiglet import figlet_format

print("Enter the password if the machine asks !!!")

os_type = platform.system().lower()

if os_type == "darwin" or os_type == "linux" or os_type == "unix":
    os.system("sudo rm -rf world_data.json vn_data.json")
else:
    os.system("del /f world_data.json vn_data.json")

print(figlet_format("SUCCESSFULLY"))

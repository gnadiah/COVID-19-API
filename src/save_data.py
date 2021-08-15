from app import save_vn_data, save_world_data
from pyfiglet import figlet_format

print("Enter the password if the machine asks !!")

save_vn_data()
save_world_data()

print(figlet_format("SUCCESSFULLY"))

import subprocess
import json

class TermuxMenu:
    def __init__(self):
        self.menu_options = {
            '1': 'Get Battery Status',
            '2': 'Get Device Info',
            '3': 'Take a Photo',
            '4': 'Set Screen Brightness',
            '5': 'List Call Log',
            '6': 'List Contacts',
            '7': 'Get GPS Location',
            '8': 'Exit'
        }

    def display_menu(self):
        print("Termux API Menu:")
        for key, value in self.menu_options.items():
            print(f"{key}: {value}")

    def get_battery_status(self):
        command = "termux-battery-status"
        result = subprocess.run([command], capture_output=True, text=True)
        if result.returncode == 0:
            battery_info = json.loads(result.stdout)
            print("Battery Level:", battery_info.get("percentage"))
        else:
            print("Failed to get battery status.")

    def get_device_info(self):
        command = "termux-info"
        result = subprocess.run([command], capture_output=True, text=True)
        if result.returncode == 0:
            device_info = json.loads(result.stdout)
            print("Device Info:")
            for key, value in device_info.items():
                print(f"{key}: {value}")
        else:
            print("Failed to get device info.")

    def take_photo(self):
        command = "termux-camera-photo test.jpg"
        subprocess.run([command], shell=True)
        print("Photo taken and saved as 'test.jpg'")

    def set_brightness(self):
        brightness = input("Enter screen brightness (0-255): ")
        command = f"termux-brightness {brightness}"
        subprocess.run([command], shell=True)
        print(f"Screen brightness set to {brightness}")

    def list_call_log(self):
        command = "termux-call-log"
        result = subprocess.run([command], capture_output=True, text=True)
        if result.returncode == 0:
            call_log = result.stdout
            print("Call Log:")
            print(call_log)
        else:
            print("Failed to list call log.")

    def list_contacts(self):
        command = "termux-contact-list"
        result = subprocess.run([command], capture_output=True, text=True)
        if result.returncode == 0:
            contacts = json.loads(result.stdout)
            print("Contacts:")
            for contact in contacts:
                print(contact.get("name"), "-", contact.get("number"))
        else:
            print("Failed to list contacts.")

    def get_gps_location(self):
        command = "termux-location"
        result = subprocess.run([command], capture_output=True, text=True)
        if result.returncode == 0:
            location_info = json.loads(result.stdout)
            latitude = location_info.get("latitude")
            longitude = location_info.get("longitude")
            print(f"GPS Location: Latitude={latitude}, Longitude={longitude}")
        else:
            print("Failed to get GPS location.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.get_battery_status()
            elif choice == '2':
                self.get_device_info()
            elif choice == '3':
                self.take_photo()
            elif choice == '4':
                self.set_brightness()
            elif choice == '5':
                self.list_call_log()
            elif choice == '6':
                self.list_contacts()
            elif choice == '7':
                self.get_gps_location()
            elif choice == '8':
                print("Exiting the menu.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    termux_menu = TermuxMenu()
    termux_menu.run()


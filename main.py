import subprocess
import platform
import time
from colorama import init, Fore, Style


init(autoreset=True)

def ping(target):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ['ping', param, '4', target]
    output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if output.returncode != 0:
        print(Fore.RED + f"Error: Unable to ping {target}")
        print(output.stderr)
        return
    
    time_values = []
    lost_packets = None

    lines = output.stdout.splitlines()

    for line in lines:
        if "time=" in line.lower():
            time_value = line.split("time=")[-1].split()[0]
            time_values.append(time_value)
        
        if "lost" in line.lower():
            lost_packets = line.strip()

    if time_values:
        print(Fore.GREEN + f"Ping times: {', '.join(time_values)}")
    if lost_packets:
        print(Fore.GREEN + f"Packet loss: {lost_packets}")

if __name__ == "__main__":
    try:
        while True:
            ip = input("Enter the IP address or domain to ping: ")
            ping(ip)
            
            choice = input('Do you want to test another IP/domain? (Y/N): ').strip().lower()
            if choice != 'y':
                print(Fore.RED + "Exiting the program...")
                time.sleep(1)
                break
    except KeyboardInterrupt:
        print("\n" + Fore.RED + "Exiting the program...")
        time.sleep(1)

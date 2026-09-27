# Libraries Installed
import socket
import argparse
from datetime import datetime
import pyfiglet
import threading
from tqdm import tqdm


portsOpen = []
lock = threading.Lock()  

def checkPort(ip, port, pbar):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            with lock:
                portsOpen.append(port)
        sock.close()
    except:
        pass
    finally:
        pbar.update(1)

def scanPort(ip):
    threads = []

    pbar = tqdm(total=65535, desc="Scanning Ports", ncols=80)

    for port in range(1, 65535):
        thread = threading.Thread(target=checkPort, args=(ip, port, pbar))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    pbar.close()
    return portsOpen


def portOpenDisplay(port):
    print(f"[+] Port {port} is OPEN")

def main():
    ascii_banner = pyfiglet.figlet_format("Port Scanner By Arron Patter")
    print(ascii_banner)
    print("Available at https://gitlab.com/arronveerpatter-group/PortScanner/-/blob/main/portScannerApp.py?ref_type=heads")

    parser = argparse.ArgumentParser(description="Python Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP address or hostname")
    args = parser.parse_args()

    target = args.target

    try:
        ipAddress = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[!] Could not resolve hostname: {target}")
        return

    print("-" * 60)
    print(f"Scanning Target: {target} ({ipAddress})")
    print("Scan started:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-" * 60)

    result = scanPort(ipAddress)

    print("-" * 60)
    if not result:
        print("No open ports found.")
    else:
        print("Scanning Completed")
        for port in result:
            portOpenDisplay(port)
    print("-" * 60)

if __name__ == "__main__":
    main()

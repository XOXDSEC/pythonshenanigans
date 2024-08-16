import socket
import threading
from tqdm import tqdm

def scan_port(target, port, open_ports, progress_bar):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        progress_bar.update(1)
    except Exception as e:
        print(f"Error on port {port}: {e}")
    finally:
        sock.close()

def port_scan(target, num_threads):
    print(f"Scanning target: {target}")
    open_ports = []
    threads = []

    with tqdm(total=65536, desc="Scanning Ports", unit="port") as progress_bar:
        for port in range(0, 65536):
            thread = threading.Thread(target=scan_port, args=(target, port, open_ports, progress_bar))
            threads.append(thread)
            thread.start()

            if len(threads) >= num_threads:
                for thread in threads:
                    thread.join()
                threads = []

        for thread in threads:
            thread.join()

    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    target = input("Enter the target IP or hostname: ")
    num_threads = int(input("Enter the number of threads: "))
    port_scan(target, num_threads)

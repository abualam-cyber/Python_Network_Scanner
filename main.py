
import socket
import ipaddress

def scan_ip(ip, ports): ## Scans an IP address for open ports
    open_ports = []
    closed_ports = []

    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
                else:
                    closed_ports.append(port)
        except socket.error:
            closed_ports.append(port)
    return open_ports, closed_ports


def scan_network(network, ports): # Scans a network for open ports on all IPs.
    network_ip = ipaddress.IPv4Network(network)

    for ip in network_ip:
        open_ports, closed_ports = scan_ip(str(ip), ports)
        if open_ports or closed_ports:
            print(f"IP: {ip}")
            if open_ports:
                for i in open_ports:
                    print(f" Open Ports: ")
                    print(f"              {i}\n")
            else:
                print(f"No ports open in IP {ip}")
            if closed_ports:
                for i in closed_ports:
                    print(f" Closed Ports: ")
                    print(f"              {i}\n")
            else:
                print(f"No ports closed in IP {ip}")


if __name__ == "__main__":
    target_network = input("Enter the network to scan (e.g. 192.168.1.0/24): ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    ports = range(start_port, end_port + 1)
    scan_network(target_network, ports)

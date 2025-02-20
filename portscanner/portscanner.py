import socket

def scanner(host, port_start, port_end):
    for port in range(port_start, port_end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) 
        try:
            test = s.connect_ex((host, port))
            if test == 0:
                print(f"TCP {port} open")
            else:
                #print(f"TCP {port} closed")
                continue
        except:
            print(f"TCP {port} unreachable")
        finally:
            s.close()

host = input("What is the target IPv4? ")
port_start = int(input("Define port range, start: "))
port_end = int(input("Define port range, end: "))

scanner(host, port_start, port_end)

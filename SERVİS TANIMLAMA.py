

import socket 

def banner_yakala(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.cennect((ip, port))
        
        banner = s.recv(1024).decode().strip()
        print(f"[+] Port {port} üzerinden gelen bilgi: {banner}")
        
    except Exception as e:
        print(f"[-] Port {port} bilgisi alınamadı: {e}")
        
    finally:
        s.close()

hedef_ip = "***.***.*.***"
banner_yakala(hedef_ip, 80)
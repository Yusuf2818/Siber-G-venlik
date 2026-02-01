# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 01:38:52 2026

@author: yusuf
"""
import socket
from datetime import datetime

def port_taraması(hedef_ip):
    print("-" * 50)
    print(f"Hedef taranıyor: {hedef_ip}")
    print(f"Tarama başlangıcı: {str(datetime.now())}")
    print("-" * 50)
    
    portlar = [21, 22, 23, 25, 53, 80, 110, 443]
    
    try:
        for port in portlar:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            sonuc = s.connect_ex((hedef_ip, port))
            
            if sonuc == 0:
                print(f"[+] Port {port}: AÇIK")
            else: 
                print(f"[-] Port {port}: KAPALI")
            
            s.close()
            
    except KeyboardInterrupt:
        print("\nkullanıcı tarafından durduruldu.")
    except socket.gaierror:
        print("\nHostname çözülemedi.")
    except socket.error:
        print("\nSunucuya bağlanılamadı.")
        
hedef = "192.168.1.107"
port_taraması(hedef)
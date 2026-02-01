import socket 

def keşif_yap(hedef_ip, port_listesi):
    print(f"\n--- {hedef_ip} Üzerinde Analiz Başlatıldı ---\n")
    
    for port in port_listesi:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.5)
            
            sonuc = s.connect_ex((hedef_ip, port))
            
            if sonuc == 0:
                print(f"[+] Port {port}: Açık")
                
                try:
                    banner = s.recv(1024).decode().strip()
                    if banner: 
                        print(f"     --- Servis Bilgisi: {banner}")
                    else:
                        print(f"     --- Servis Bilgisi: Yanıt alınamadı (Filtreli olabilir)")
                except:
                    print(f"      --- Servis Bilgisi: Banner çekilemedi.")
                    
            s.close()
        
        except socket.error:
            print(f"[!] {port} numaralı port ulaşılamadı")


hedef = "***.***.*.***"
portlar = [21, 22, 80, 443, 8080]

keşif_yap(hedef, portlar)
                        
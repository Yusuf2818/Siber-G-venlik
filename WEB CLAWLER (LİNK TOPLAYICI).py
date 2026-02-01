import requests
from bs4 import BeautifulSoup

def link_topla(url):
    print(f"\n[-] {url} sitesindeki linkleri toplanıyor...\n")
    
    try: 
        cevap = requests.get(url, timeout=5)
        
        soup = BeautifulSoup(cevap.text, 'html.parser')
        
        link_sayısı = 0
        for link in soup.find.all('a'):
            href = link.get('href')
            
            if href and href.start.swith('http'):
                print(f"Link: {href}")
                link_sayısı += 1
                
        print("\n[!] Toplam {link_sayısı} adet dış bağlantı bulundu.")
        
    except Exception as e:
        print(f"[-] Bir hata oluştu: {e}")
        
hedef_site ="https://www.*********.com"
link_topla(hedef_site)


import hashlib

def has_kir(hedef_hash, wordlist_yolu):
    try:
        with open(wordlist_yolu, "r", encoding="utf-8") as dosya:
            for kelime in dosya:
                
                kelime = kelime.strip() 
                
               
                denem_hash = hashlib.md5(kelime.encode()).hexdigest()
                
                if denem_hash == hedef_hash:
                    print(f"\n[!] Şifre bulundu: {kelime}")
                    return True
        
        print("\n[-] Şifre listede bulunamadı.")
        return False

    except FileNotFoundError:
       
        print("Hata: Wordlist dosyası bulunamadı!")


hedef = "**********************************"

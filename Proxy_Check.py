import requests
import os

def get_proxy_list_filename():
    """Kullanıcıdan proxy listesi dosyasının adını alır."""
    while True:
        file_name = input("Dosya Adını Gir: ")
        if os.path.exists(file_name):
            return file_name
        else:
            print("Belirtilen dosya bulunamadı. Lütfen geçerli bir dosya adı ve yolunu girin.")

# Test edilecek URL
TEST_URL = "https://www.google.com"

def test_proxy(proxy):
    """Verilen proxy'nin çalışıp çalışmadığını kontrol eder."""
    try:
        response = requests.get(TEST_URL, proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

def main():
    print('''
    ╦ ╦┌─┐╔═╗╦╔═┌─┐╔╦╗  ╔╗ ┬ ┬  ╔═╗┌─┐╔═╗┌─┐╔═╗┬ ┬╔═╗
    ╠═╣├─┤║  ╠╩╗├┤  ║║  ╠╩╗└┬┘  ╠═╝├┤ ║ ╦├─┤╚═╗│ │╚═╗
    ╩ ╩┴ ┴╚═╝╩ ╩└─┘═╩╝  ╚═╝ ┴   ╩  └─┘╚═╝┴ ┴╚═╝└─┘╚═╝
    ''')

    print('Proxy Listesi İndiriliyor...')

    # Proxy listesi dosyasının adı ve yolu
    PROXY_LIST_FILE = get_proxy_list_filename()

    with open(PROXY_LIST_FILE) as f:
        proxies = f.readlines()
    
    working_proxies = []
    for proxy in proxies:
        proxy = proxy.strip()
        if test_proxy(proxy):
            working_proxies.append(proxy)
            print(f"{proxy} çalışıyor.")
        else:
            print(f"{proxy} çalışmıyor.")
    
    print(f"\nToplam {len(working_proxies)} adet proxy çalışıyor, {len(proxies)} adet proxy test edildi. https://about.me/pegasus")

    with open("pegasus.txt", "w") as f:
        f.write("\n".join(working_proxies))

if __name__ == "__main__":
    main()

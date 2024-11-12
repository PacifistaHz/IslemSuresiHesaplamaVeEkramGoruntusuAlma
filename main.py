import time
import pyautogui

def ekranGoruntusuAl():
    baslangic=time.time()
    goruntu=pyautogui.screenshot()
    dosyaAdi="EkranGoruntusu_"+str(time.time_ns())+".jpg"
    goruntu.save(dosyaAdi)
    bitis=time.time()
    print(bitis-baslangic)
ekranGoruntusuAl()
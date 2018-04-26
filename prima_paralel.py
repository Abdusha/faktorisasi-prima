import os, re, threading
import time


class prima_check(threading.Thread):
    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.ip = ip
        self.hasil = 0

    def run(self):
        hitung = 0
        for j in range(1, self.ip + 1):
            div = self.ip % j
            if (div == 0):
                hitung = hitung + 1
                if (hitung == 3):
                    break
        if (hitung == 2):
            # print(i)
            self.hasil = 1
        return self.hasil

    def status(self):
        if self.hasil == 1:
            return "Bilangan Prima"
        else:
            return "Bukan Bilangan Prima"


class faktor_prima(threading.Thread):
    def __init__(self, ip, primas):
        threading.Thread.__init__(self)
        self.ip = ip
        self.primas = primas
        self.faktor = []

    def run(self):
        tem = self.ip
        while (tem!=1):
            for k in self.primas:
                if (tem % k == 0):
                    self.faktor.append(k)
                    tem = tem / k
                    break
        return self.faktor

start = time.time()
check_results = []
primas = []
prima_results = []
c = 0

for i in range(1, 10000):
    ip = i;
    current = prima_check(ip)
    check_results.append(current)
    current.start()

for el in check_results:
    el.join()
    if (el.run() == 1):
        primas.append(el.ip)
        # print(('Status from ', el.ip, 'is', el.status()))
    pr = faktor_prima(el.ip, primas)
    prima_results.append(pr)
    en = prima_results[c]
    pr.start()
    en.join()
    print(('Angka ', en.ip, ' adalah ',el.status(),' dengan faktor faktornya : ', en.faktor))
    c = c+1

# for en in prima_results:
#     en.join()
#     print(('Factor from ', en.ip, 'are', en.faktor))

end = time.time()
print((end - start))



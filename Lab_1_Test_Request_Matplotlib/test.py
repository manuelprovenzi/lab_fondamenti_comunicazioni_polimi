import requests
import matplotlib.pyplot as plt #per grafici

"""
sito = 'http://www.google.com'
r = requests.get(sito)
print(r.status_code)


tempo di risposta del server
for _ in range(10): #non interessa l'indice del ciclo
    #r = requests.get(sito)
    #print('Tempo di Risposta: ', r.elapsed.microseconds/1000, 'ms')
    
    

#--media,max,min--
tempi_ms = []
num_ciclo = 10

for _ in range(num_ciclo):
    r = requests.get(sito)
    tempi_ms.append(r.elapsed.microseconds/1000)

print('Tempo minimo MIN', min(tempi_ms), 'ms')
print('Tempo medio AVG', sum(tempi_ms)/len(tempi_ms), 'ms')
print('Tempo massimo MAX', max(tempi_ms), 'ms')


#--grafici--
plt.figure() #spazio predefinito del grafico
plt.plot(tempi_ms, label=f'{sito}', linestyle='-.') #aggiunge lista dei tempi_ms al grafico e li distribuisce, con titolo e tipo di linea modificato
plt.ylim([0,1.1*max(tempi_ms)]) #per vedere chiaro tutto quanto partendo da un valore y di 0 anzichè del minimo dei miei valori
plt.xlabel('ID richiesta') #titolo asse x
plt.ylabel('[ms]') #titolo asse y
plt.title(f'Test {sito}') # titolo di tutto, con format del testo in cui la variabile sito è inserita
plt.legend() #mostra la legenda
plt.grid() #griglia
plt.show() #mostra il grafico
"""
#--server multiptli--

num_ciclo = 10
siti = ['https://www.gazzetta.it', 'https://www.netflix.com', 'https://www.facebook.com']
tempi_tutti = []

for url in siti:
    print(f'{url}:\r\n')
    tempi = []
    for _ in range(num_ciclo):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'}
        r = requests.get(url, headers=headers)
        tempi.append(r.elapsed.microseconds/1000)
        tempi_tutti.append(r.elapsed.microseconds/1000)
        
        
    print('Tempo minimo MIN', min(tempi), 'ms')
    print('Tempo medio AVG', sum(tempi)/len(tempi), 'ms')
    print('Tempo massimo MAX', max(tempi), 'ms')

print('Tempo massimo MAX', max(tempi_tutti), 'ms')

#altro modo
#for ID_url,url in enumerate(siti):
    #print(url)
    #print(ID_url)
    #...
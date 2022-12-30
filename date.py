import datetime
import time
from os import system


now = datetime.datetime.now()

print(now)

fecha_programada = str(now)[0:16]
fecha_programada_lista = fecha_programada[0:11] + '21:40'



for n in range(2000):
    time.sleep(20)
    print(n)




if str(now)[0:16] == fecha_programada_lista:
    system('shutdown -s -t 2000')


else:
    print(str(now)[0:16])
# system("shutdown -a")
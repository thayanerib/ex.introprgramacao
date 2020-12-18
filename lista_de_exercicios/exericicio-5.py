##programa que transforma segundos em horas, minutos e segundos

segundos = int(input(""))
horas = int(segundos /3600)
minutos = int(segundos%3600)/60
seg = int((segundos%3600)%60)/60
print(" %d h, %d minutos e %d s" % (horas, minutos, seg))

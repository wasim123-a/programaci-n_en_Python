segundos_totales = int(input("Ingresa la cantidad de segundos: "))
horas = segundos_totales // 3600
minutos = (segundos_totales % 3600) // 60
segundos = segundos_totales % 60
print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")

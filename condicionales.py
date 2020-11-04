import datetime 
#Inicio del programa hora
#Ingresar hora del día con string formato hh:mm

hora_dia = str(input("Ingrese la hora del día en formato de 24 horas (hh:mm): "))
while ((int(hora_dia[0:2])) >= 0 and (int(hora_dia[0:2])) < 24) and (int(hora_dia[3:6]) >= 0 and int(hora_dia[3:6]) < 60) == False:
    print("Hora equivocada")
    hora_dia = str(input("Ingrese la hora del día en formato de 24 horas (hh:mm): "))
    #(int(hora_dia[0:2])) >= 0 and (int(hora_dia[0:2])) < 24

#Convertidor de hora a segundos
#1 hora = 3600 segundos
#hh:mm

hora_convertido = int(hora_dia[0:2])*3600
hora_convertido = int(hora_dia[0:2])*3600
minutos_convertido = int(hora_dia[3:6])*60
print(hora_convertido)
print(minutos_convertido)
segundos_totales = hora_convertido + minutos_convertido
print("Han pasado ", segundos_totales, "segundos desde medianoche.")

'''
Emisión de saludo: 
“Mañana” si la hora es mayor a las 06:00 y  hasta las 12:00.
“Tarde” si la hora es mayor a 12:00 y hasta las 17:00.
“Atardecer” si la hora es mayor a 17:00 y hasta las 20:00.
“Noche” si la hora es mayor a 20:00 y hasta las 02:00.
“Madrugada” si la hora es mayor a 02:00 y hasta las 6:00
'''

if int(hora_dia[0:2]) >= 6 and int(hora_dia[0:2]) < 12:
    print("Es Mañana: BUENOS DÍAS!")
elif int(hora_dia[0:2]) >= 12 and int(hora_dia[0:2]) < 17:
    print("Es la tarde")
elif int(hora_dia[0:2]) >= 17 and int(hora_dia[0:2]) < 20:
    print("Es la atardecer")
elif (int(hora_dia[0:2]) >= 20 and int(hora_dia[0:2]) < 24) or (int(hora_dia[0:2]) >= 0 and int(hora_dia[0:2]) < 2):
    print("Es la noche")
elif int(hora_dia[0:2]) >= 2 and int(hora_dia[0:2]) < 6:
    print("Es la madrugada")

#Inicio de programa: estación del año.

fecha = str(input("Ingrese el día y mes del año en formato (dd-mm): "))

while (int(fecha[0:2]) > 0 and int(fecha[0:2]) <= 31) and (int(fecha[3:6]) > 0 and int(fecha[3:6]) <= 12) == False:
    print("Fecha equivocada")
    fecha = str(input("Ingrese el día y mes del año en formato (dd-mm): "))

hemisferio = str(input("Ingrese en que hemisferio se encuentra, norte o sur: "))
hemisferio = hemisferio.upper()
"""
Inicio	H. norte	H. sur
20-21 Marzo	Primavera	Otoño
21-22 Junio	Verano	Invierno
22-24 Septiembre	Otoño	Primavera
21-22 Diciembre	Invierno	Verano
"""

# date in yyyy/mm/dd format 
fecha_usuario = datetime.datetime(2020, int(fecha[3:6]), int(fecha[0:2]))
inicio_primavera_norte = datetime.datetime(2020, 3, 20)
inicio_otono_sur = datetime.datetime(2020, 3, 20)
inicio_verano_norte = datetime.datetime(2020, 6, 21)
inicio_invierno_sur = datetime.datetime(2020, 6, 21)
inicio_otono_norte = datetime.datetime(2020, 9, 22)
inicio_primavera_sur = datetime.datetime(2020, 9, 22)
inicio_invierno_norte = datetime.datetime(2020, 12, 21)
inicio_verano_sur = datetime.datetime(2020, 12, 21)

#print(fecha_usuario)

if hemisferio == "NORTE":
    if fecha_usuario >= inicio_primavera_norte and fecha_usuario < inicio_verano_norte:
        print("Es primavera")
    elif fecha_usuario >= inicio_verano_norte and fecha_usuario < inicio_otono_norte:
        print("Es verano")
    elif fecha_usuario >= inicio_otono_norte and fecha_usuario < inicio_invierno_norte:
        print("Es otoño")
    elif fecha_usuario >= inicio_invierno_norte and fecha_usuario < datetime.datetime(2020, 12, 31):
        print("Es verano")
    elif fecha_usuario >= datetime.datetime(2020, 1, 1) and fecha_usuario < inicio_primavera_norte:
        print("Es verano")
elif hemisferio == "SUR":
    if fecha_usuario >= inicio_primavera_sur and fecha_usuario < inicio_verano_sur:
        print("Es primavera")
    elif fecha_usuario >= inicio_verano_sur and fecha_usuario < datetime.datetime(2020, 12, 31):
        print("Es verano")
    elif fecha_usuario >= datetime.datetime(2020, 1, 1) and fecha_usuario < inicio_otono_sur:
        print("Es verano")
    elif fecha_usuario >= inicio_otono_sur and fecha_usuario < inicio_invierno_sur:
        print("Es otoño")
    elif fecha_usuario >= inicio_invierno_sur and fecha_usuario < inicio_primavera_sur:
        print("Es invierno")

papeletas = [100,200,500,1000]
option_bank = 0

def Proceso(monto):
    for papeleta in papeletas:
        #print(monto//b)
        if(monto/papeleta == 1):
            print('Se le ha dado 1 billete de {}'.format(papeleta))
            exit()

        if((monto//papeleta) != 0):
            devueltas.append([monto//papeleta,papeleta])
    
    devueltas_finales = sorted(devueltas)
    #Con esto se puede lograr pagar con las papeletas mayores, lo cual  puedo dar las de mayor valor que seria menos
    #fisicamente que es lo que se logra o persive buscar. (LOGICO MUCHO, FISICO POCO.)

    #print(devueltas_finales)

    for dev in devueltas_finales:
        print('Se le ha dado ',dev[0],' billetes de ',dev[1])
        monto = monto - (dev[0]*dev[1])
        #break (Para comprobar el monto o la valides de la operacion)
        if(monto >= 100):
            Proceso(monto)
        else:
            exit()

    print('MOnto total: {}'.format(monto))
    #FIN FUNCION

print('Cajero  Automatico.net')

monto_cuenta = int(input('Ingrese su monto a retirar: '))

print('(1) FDP Inversments(Bank) \n(2) Any Bank')
option_bank = int(input())


if(monto_cuenta == 0 or monto_cuenta < 100):
    print('Sea conciente, debe retirar 100 pesos en adelante.')
    exit()

if(option_bank == 1):
    if(monto_cuenta > 20000):
       print('Lo sentimos usted no puede solicitar mas de 20000 pesos.')
    else:
       devueltas = []
       Proceso(monto_cuenta)
else:
     if(monto_cuenta > 10000):
       print('Lo sentimos usted no puede solicitar mas de 10000 pesos.')
       print('El otro banco para la próxima, esta en desarrollo. (COMING SOON)')


#AUN NO COMPLETADO PERO ESTO HA SIDO UN TRABAJO DESDE LAS 1PM Y SON 11:13PM. :/
#PERO INTEGRANDO POCO A POCO LO QUE HE HECHO LO HE IDO SOLUCIONANDO POQUITO A POQUITO.

#Edwin Alberto ROMAN Seberino - 2020-10233
#https://github.com/Edwinroman30/Primer_Parcial_Python
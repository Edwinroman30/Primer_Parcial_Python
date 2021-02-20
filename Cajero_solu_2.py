papeletas = [100,200,500,1000]
monto = int(input('Ingrese su monto a retirar: '))

devueltas = []

def Proceso(monto):
    for papeleta in papeletas:
        #print(monto//b)
        if(monto/papeleta == 1):
            print('Usted puede pagar con 1 billete de {}'.format(papeleta))
            exit()

        if((monto//papeleta) != 0):
            devueltas.append([monto//papeleta,papeleta])
    
    devueltas_finales = sorted(devueltas)
    #Con esto se puede lograr pagar con las papeletas mayores, lo cual  puedo dar las de mayor valor que seria menos
    #fisicamente que es lo que se logra o persive buscar. (LOGICO MUCHO, FISICO POCO.)

    #print(devueltas_finales)

    for dev in devueltas_finales:
        print('Usted tiene que dar ',dev[0],' billetes de ',dev[1])
        monto = monto - (dev[0]*dev[1])
        #break (Para comprobar el monto o la valides de la operacion)
        if(monto > 0):
            Proceso(monto)
        else:
            exit()
            
    print('MOnto total: {}'.format(monto))


Proceso(monto)

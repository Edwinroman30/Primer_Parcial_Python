papeletas = [100,200,500,1000]
monto = 2000

devueltas = []

for papeleta in papeletas:
    #print(monto//b)
    if(monto/papeleta == 1):
        print('Usted puede pagar con 1 {}'.format(papeleta))
        break

    if((monto//papeleta) != 0):
        devueltas.append([monto//papeleta,papeleta])

devueltas_finales = sorted(devueltas)
#print(devueltas_finales)

for dev in devueltas_finales:
    print('Usted tiene que dar ',dev[0],' billetes de ',dev[1])
    #if(monto < 0):

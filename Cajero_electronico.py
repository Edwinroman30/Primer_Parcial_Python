option_bank = 0
monto_cuenta = 0

#-----------------------
miles = [18000, 18, 1000]
quinientos = [9500,19, 500]
docientos = [4600, 23, 200]
cien = [5000, 50, 100]
#-----------------------
#0| 1 | 2 | 3(Billetes  entregados de estos)

estado_monto = 1

print('Cajero  Automatico.net')
print('(1) FDP Bank \n(2) Any Bank')
option_bank = int(input())

monto_cuenta = int(input('Dígite el monto a solicitar: '))

if(monto_cuenta == 0 or monto_cuenta < 100):
    print('Sea conciente, debe retirar 50 en adelante.')
else:
    if(option_bank == 1):
        if(monto_cuenta > 20000):
            print('Lo sentimos usted no puede solicitar mas de 20000 pesos.')
        else:
            estado_monto = monto_cuenta
            while(estado_monto != 0):
                if((monto_cuenta%miles[2] == 0)  and miles[1] != 0 ):
                    #PROCEDER CON MIL               
                    estado_monto = monto_cuenta - (miles[2]*(monto_cuenta/miles[2]))
                    miles[0] = miles[0] - (miles[2]*(monto_cuenta/miles[2]))
                    miles[1] = miles[1] - (monto_cuenta/miles[2])
                else:
                    if(monto_cuenta%quinientos[2] == 0):
                        #PROCEDER CON 500
                        estado_monto = monto_cuenta - (quinientos[2]*(monto_cuenta/quinientos[2]))
                        quinientos[0] = quinientos[0] - (quinientos[2]*(monto_cuenta/quinientos[2]))
                        quinientos[1] = quinientos[1] - (monto_cuenta/quinientos[2])
                    elif(monto_cuenta%docientos[2] == 0):
                           #PROCEDER CON 200
                            estado_monto = monto_cuenta - (docientos[2]*(monto_cuenta/docientos[2]))
                            docientos[0] = docientos[0] - (docientos[2]*(monto_cuenta/docientos[2]))
                            docientos[1] = docientos[1] - (monto_cuenta/docientos[2])
                    else:
                             #PROCEDER CON 100
                             estado_monto = monto_cuenta - (cien[2]*(monto_cuenta/cien[2]))
                             cien[0] = cien[0] - (cien[2]*(monto_cuenta/cien[2]))
                             cien[1] = cien[1] - (monto_cuenta/cien[2])
    elif(option_bank == 2):
        print('Caso Any')
    else:
        print('No existe esta opción :(')

print('Estado monto {} '.format(estado_monto))
print('Billetes de miles {} '.format(miles[1]))
print('Billetes de quiniento {0} , {1} '.format(quinientos[1],quinientos[0]))
print('Billetes de dociento {} '.format(docientos[1]))
print('Billetes de cien {} '.format(cien[1]))
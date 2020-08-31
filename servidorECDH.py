import socket
import sys
from curvaEliptica.curvaEliptica import CurvaElipticaNSS
from curvaEliptica.curvaEliptica import CurvaElipticaSS
from curvaEliptica.clasePunto import Punto
from curvaEliptica.claseECDH import ECDH_NSS
from curvaEliptica.claseECDH import ECDH_SS

#-----------------------------------------------------------------------------------------------------
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.bind(server_address)

print('---------------------------------------------------')
print(' ** CRIPTOGRAFÍA DE CURVA ELÍPTICA ** ')
print('---------------------------------------------------')
print('La Criptografía de Curva Elíptica (del inglés: Elliptic curve cryptography, ECC) es una variante de la criptografía')
print('asimétrica o de clave pública basada en las matemáticas de las curvas elípticas. Sus autores argumentan que la CCE ')
print('puede ser más rápida y usar claves más cortas que los métodos antiguos —como RSA— al tiempo que proporcionan un ' )
print('nivel de seguridad equivalente.')

# Listen for incoming connections
sock.listen(1)
print('---------------------------------------------------')
print('Esperando conexión del lado del cliente...')
print('---------------------------------------------------')
connection, client_address = sock.accept()
print('Conexión desde', client_address)
print('---------------------------------------------------')
print('\n')


#-----------------------------------------------------------------------------------------------------


tipo_curva = 0

while tipo_curva !=1 and tipo_curva !=2:

    print('-------------------------------------------')
    print(' ** SELECCIONE TIPO DE CURVA ELÍPTICA CON LA QUE QUIERA TRABAJAR: ** ')
    print('-------------------------------------------')
    print('  1) "Curva Elíptica Non-Supersingular (y² + xy = x³ + ax² + b)".')
    print('  2) "Curva Elíptica Supersingular (y² + cy = x³ + ax + b)".')
    print('')
    print('---------------------------------------------------')
    tcurva = bytes(input('Introduzca el tipo de curva: \n'), 'utf-8')
    
#ENVIO DEL TIPO DE CURVA
#---------------------------------------------------------------------
    tipo_curva = int(tcurva)
    print('---------------------------------------------------')
    print('Curva elegida {!r}'.format(tcurva))
    print('---------------------------------------------------')
    connection.sendall(tcurva)
    print('-------------------------------------------')
    print('')

    #-------------------------------------------------------------------------------------------------------------------------------------
    # TIPO DE CURVA NSS
    #-------------------------------------------------------------------------------------------------------------------------------------
    
    if (tipo_curva == 1):

        print('TIPO DE CURVA Non-Supersingular (y² + xy = x³ + ax² + b) ')
        print('---------------------------------------------------------')
        print('Este tipo de curva se compone de tres campos, (A,B,C).')
        print('A y B seran los polinomios de la curva, representados como un entero.')
        print('C será otro polinomio, también representado como un entero, al que se denomina contexto.')
        print('Dichos campos serán representaremos como el ejemplo siguiente:')
        print('')
        print('Ejemplo de uso:')
        print('    2 = 10 = x')
        print('    3 = 11 = x + 1')
        print('    13 = 1101 = x³ + x² + 1')
        print('    35 = 100011 = x⁵ + x + 1')
        print('')
        print('---------------------------------------------------')
        print('')

        lista_curva = 0
        orden = None
        print('---------------------------------------------------')
        print('¿Que curva va a utilizar?')
        print('---------------------------------------------------')
        print('  1) "NIST CURVA B-163" ')
        print('  2) "NIST CURVA K-163" ')
        print('  3) "NIST CURVA B-233" ')
        print('  4) "NIST CURVA K-233" ')
        print('  5) "NIST CURVA B-283" ')
        print('  6) "NIST CURVA K-283" ')
        print('  7) "NIST CURVA B-409" ')
        print('  8) "NIST CURVA K-409" ')
        print('  9) "NIST CURVA B-571" ')
        print(' 10) "NIST CURVA K-571" ')
        print(' 11) "CURVA PROPIA B-19" ')
        print(' 12) "CURVA PROPIA" (Insercion de Parametros).')
        print('---------------------------------------------------')

        #ENVIO DE LA CURVA
        #---------------------------------------------------------------------
        lcurva = bytes(input('Introduzca la curva con la que va a trabajar: \n'), 'utf-8')
        lista_curva = int(lcurva)
        print('---------------------------------------------------')
        print('Curva elegida {!r}'.format(lcurva))
        print('---------------------------------------------------')
        connection.sendall(lcurva)
        print('-------------------------------------------')

        # Curva UNO
        #---------------------------------------------------------------------

        if lista_curva == 1:

            curva1 = CurvaElipticaNSS(
            1,
            2982236234343851336267446656627785008148015875581,
            11692013098647223345629478661730264157247460344009,
            )
            print('Su representacion es:') 
            print('-------------------------------------------')
            curva1.pinta_curvaNSS()
            print('')
            print('---------------------------------------------------')
            print('')
            print(' Uno de sus puntos pertenecientes es [Punto(x, y)] ')
            print('---------------------------------------------------')
            punto1 = Punto(
            5759917430716753942228907521556834309477856722486,
            1216722771297916786238928618659324865903148082417)

            punto1.pinta_punto()
            print('')
            orden = 5846006549323611672814742442876390689256843201587
            
        # Curva DOS
        #---------------------------------------------------------------------

        elif lista_curva == 2:

            curva1 = CurvaElipticaNSS(
            1,
            1,
            11692013098647223345629478661730264157247460344009,
            )
            print('Su representacion es:') 
            print('-------------------------------------------')
            curva1.pinta_curvaNSS()
            print('')
            print('---------------------------------------------------')
            print('')
            print(' Uno de sus puntos pertenecientes es [Punto(x, y)] ')
            print('---------------------------------------------------')
            punto1 = Punto(
            4373527398576640063579304354969275615843559206632,
            3705292482178961271312284701371585420180764402649)
            punto1.pinta_punto()
            print('')
            orden = 5846006549323611672814741753598448348329118574063
            
            
        # Curva TRES
        #---------------------------------------------------------------------
        
        elif lista_curva == 3:
            
            curva1 = CurvaElipticaNSS(
            1,
            2760497980029204187078845502377898520307707256259003964398570147123373,
            13803492693581127574869511724554050904902217944359662576256527028453377,
            )
            print('Su representacion es:') 
            print('-------------------------------------------')
            curva1.pinta_curvaNSS()
            print('')
            print('---------------------------------------------------')
            print('')
            print(' Uno de sus puntos pertenecientes es [Punto(x, y)] ')
            print('---------------------------------------------------')
            punto1 = Punto(
            6761246501583409083997096882159824046681246465812468867444643442021771,
            6912913004411390932094889411904587007871508723951293564567204383952978)
            punto1.pinta_punto()
            print('')
            orden = 6901746346790563787434755862277025555839812737345013555379383634485463
            
        # Curva CUATRO
        #---------------------------------------------------------------------

        elif lista_curva == 4:

            curva1 = CurvaElipticaNSS(
            0,
            1,
            13803492693581127574869511724554050904902217944359662576256527028453377,
            )
            print('Su representacion es:') 
            print('-------------------------------------------')
            curva1.pinta_curvaNSS()
            print('')
            print('---------------------------------------------------')
            print('')
            print(' Uno de sus puntos pertenecientes es [Punto(x, y)] ')
            print('---------------------------------------------------')
            punto1 = Punto(
            9980522611481012342443087688797002679043489582926858424680330554073382,
            12814767389816757102953168016268660157166792010263439198493421287958179)
            punto1.pinta_punto()
            print('')
            orden = 3450873173395281893717377931138512760570940988862252126328087024741343
                   
        
        # Curva CINCO
        #---------------------------------------------------------------------

        elif lista_curva == 5:

            curva1 = CurvaElipticaNSS(
            1,
            4821813576056072374006997780399081180312270030300601270120450341205914644378616963829,
            15541351137805832567355695254588151253139254712417116170014499277911234281641667989665,
            )
            print('Su representacion es:') 
            print('-------------------------------------------')
            curva1.pinta_curvaNSS()
            print('')
            print('---------------------------------------------------')
            print('')
            print(' Uno de sus puntos pertenecientes es [Punto(x, y)] ')
            print('---------------------------------------------------')
            punto1 = Punto(
            11604587487407003699882500449177537465719784002620028212980871291231978603047872962643,
            6612720053854191978412609357563545875491153188501906352980899759345275170452624446196)
            punto1.pinta_punto()
            print('')
            orden = 7770675568902916283677847627294075626569625924376904889109196526770044277787378692871
            

        # Curva SEIS
        #---------------------------------------------------------------------

        elif lista_curva == 6:

            curva1 = CurvaElipticaNSS(
            0,
            1,
            15541351137805832567355695254588151253139254712417116170014499277911234281641667989665,
            )
            print('Su representacion es:') 
            print('-------------------------------------------')
            curva1.pinta_curvaNSS()
            print('')
            print('---------------------------------------------------')
            print('')
            print(' Uno de sus puntos pertenecientes es [Punto(x, y)] ')
            print('---------------------------------------------------')
            punto1 = Punto(
            9737095673315832344313391497449387731784428326114441977662399932694280557468376967222,
            3497201781826516614681192670485202061196189998012192335594744939847890291586353668697)
            punto1.pinta_punto()
            print('')
            orden = 3885337784451458141838923813647037813284811733793061324295874997529815829704422603873
            
            
        # Curva SIETE
        #---------------------------------------------------------------------

        elif lista_curva == 7:

            curva1 = CurvaElipticaNSS(
            1,
            86886261634090707672817770640384425264505829479043641824438658614111870471004564988634410809058207142318571212147935892575,
            1322111937580497197903830616065542079656809365928562438569297590548811582472622691650378420879430724437687334722581078999041,
            )
            print('Su representacion es:') 
            print('-------------------------------------------')
            curva1.pinta_curvaNSS()
            print('')
            print('---------------------------------------------------')
            print('')
            print(' Uno de sus puntos pertenecientes es [Punto(x, y)] ')
            print('---------------------------------------------------')
            punto1 = Punto(
            901935279919555460519938020229627704409149556251441963587868715440518797594851300277260702073828731983206453567757135484583,
            252271804478663965520986398892908223486048997352743726687083769858460083134230324190507814191768191984593727083669152319238)
            punto1.pinta_punto()
            print('')
            orden = 661055968790248598951915308032771039828404682964281219284648798304157774827374805208143723762179110965979867288366567526771
            
        # Curva OCHO
        #---------------------------------------------------------------------

        elif lista_curva == 8:

            curva1 = CurvaElipticaNSS(
            0,
            1,
            1322111937580497197903830616065542079656809365928562438569297590548811582472622691650378420879430724437687334722581078999041,
            )
            print('Su representacion es:') 
            print('-------------------------------------------')
            curva1.pinta_curvaNSS()
            print('')
            print('---------------------------------------------------')
            print('')
            print(' Uno de sus puntos pertenecientes es [Punto(x, y)] ')
            print('---------------------------------------------------')
            punto1 = Punto(
            250320606379109783324043328573944955992891736106680352671677389786222910027088291741834878773922859231376787355260678190918,
            1248286015820357801871250692732381479576954307085883348044850800154576601694946857655762823838587314348501053191643883120747)
            punto1.pinta_punto()
            print('')
            orden = 330527984395124299475957654016385519914202341482140609642324395022880711289249191050673258457777458014096366590617731358671
            
            
        # Curva NUEVE
        #---------------------------------------------------------------------

        elif lista_curva == 9:

            curva1 = CurvaElipticaNSS(
            1,
            2853329245261343535560086964181551296889298776106832980891560850944180011701123307905326019642652653533003482753023669016842884108172514870944140611113679225347419720217210,
            7729075046034516689390703781863974688597854659412869997314470502903038284579120849072387533163845155924927232063004354354730157322085975311485817346934161497393961629647909,
            )
            print('Su representacion es:') 
            print('-------------------------------------------')
            curva1.pinta_curvaNSS()
            print('')
            print('---------------------------------------------------')
            print('')
            print(' Uno de sus puntos pertenecientes es [Punto(x, y)] ')
            print('---------------------------------------------------')
            punto1 = Punto(
            2909726711393360238997027325079981094903293083416277207163191533186952179846948691035435651273252692731060457249729605513129233502615507099213961913121214831097565254790425,
            3366174731810125753087813209708676894833150358595778752145226712858102783612277607950241452090192525005883890170639174605150394168627448707126811848455102037101825665712475)
            punto1.pinta_punto()
            print('')
            orden = 3864537523017258344695351890931987344298927329706434998657235251451519142289560424536143999389415773083133881121926944486246872462816813070234528288303332411393191105285703
            

        # Curva DIEZ
        #---------------------------------------------------------------------

        elif lista_curva == 10:

            curva1 = CurvaElipticaNSS(
            0,
            1,
            7729075046034516689390703781863974688597854659412869997314470502903038284579120849072387533163845155924927232063004354354730157322085975311485817346934161497393961629647909,
            )
            print('Su representacion es:') 
            print('-------------------------------------------')
            curva1.pinta_curvaNSS()
            print('')
            print('---------------------------------------------------')
            print('')
            print(' Uno de sus puntos pertenecientes es [Punto(x, y)] ')
            print('---------------------------------------------------')
            punto1 = Punto(
            2350112116304015523482377231684766626496228526415123964355167346023168453994712131915750801804327368697642410358740900984083649787136749901162917044657353481320802543241586,
            3177153047892284027955092820645594290840691892110463136294318330308675645046690871624329737215785097835850661950174873195667225591921644089615520604151251098277510177212323)
            punto1.pinta_punto()
            print('')
            orden = 1932268761508629172347675945465993672149463664853217499328617625725759571144780212268133978522706711834706712800825351461273674974066617311929682421617092503555733685276673
            
            
        # Curva ONCE
        #---------------------------------------------------------------------

        elif lista_curva == 11:

            curva1 = CurvaElipticaNSS(
            8,
            9,
            19,
            )
            print('Su representacion es:') 
            print('-------------------------------------------')
            curva1.pinta_curvaNSS()
            print('')
            print('---------------------------------------------------')
            print('')
            print(' Uno de sus puntos pertenecientes es [Punto(x, y)] ')
            print('---------------------------------------------------')
            punto1 = Punto(
            3,
            12)
            punto1.pinta_punto()
            print('')
            orden= 22
            
        # Curva DOCE
        #---------------------------------------------------------------------

        elif lista_curva == 12:

            # INTRUCCION DEL TERMINO A
            #--------------------------------------------------------------------
            termino_a = bytes(input('Introduzca el término A: \n '), 'utf-8')
            a = int(termino_a)
            print('Enviando Termino A {!r}'.format(termino_a))
            print('---------------------------------------------------')
            connection.sendall(termino_a)


            # INTRUCCION DEL TERMINO B
            #--------------------------------------------------------------------
            termino_b = bytes(input('Introduzca el término B: \n '), 'utf-8')
            b = int(termino_b)
            print('Enviando Termino B {!r}'.format(termino_b))
            print('---------------------------------------------------')
            connection.sendall(termino_b)

            # INTRUCCION DEL TERMINO C
            #--------------------------------------------------------------------
            termino_c= bytes(input('Introduzca el término C (contexto): \n '), 'utf-8')
            c = int(termino_c)
            print('Enviando Termino C {!r}'.format(termino_c))
            print('---------------------------------------------------')
            connection.sendall(termino_c)

            # PRESENTACION DE LA CURVA
            #--------------------------------------------------------------------
            print('')
            print('---------------------------------------------------')
            print('')
            curva1 = CurvaElipticaNSS(a, b, c)
            print('TU CURVA ELÍPTICA ES:') 
            print('-------------------------------------------')
            curva1.pinta_curvaNSS()

            #--------------------------------------------------------------------
            print('')
            print('---------------------------------------------------')
            print('')
            print(' PUNTO DE UNA CURVA ELÍPTICA [Punto(x, y)] ')
            print('---------------------------------------------------')

            # INTRUCCION DE LA COORDENADA X
            #--------------------------------------------------------------------
            x_p = bytes(input('Introduzca coordenada X:'), 'utf-8')
            x = int(x_p)
            print('Enviando coordenada {!r}'.format(x_p))
            print('---------------------------------------------------')
            connection.sendall(x_p)


            # INTRUCCION DE LA COORDENADA Y
            #--------------------------------------------------------------------
            y_p = bytes(input('Introduzca coordenada Y:'), 'utf-8')
            y = int(y_p)
            print('Enviando coordenada {!r}'.format(y_p))
            print('---------------------------------------------------')
            connection.sendall(y_p)

            #PRESENTACION DEL PUNTO DE LA CURVA
            #--------------------------------------------------------------------
            punto1 = Punto(x, y)
            print('')
            print('Tu punto es:') 
            print('-------------------------------------------')
            punto1.pinta_punto()
            print('')
            
            
            print('¿EL PUNTO PERTENECE AL TIPO DE CURVA "Non-Supersingular" ?:')
            print('-----------------------------------------------------------')
            

        else:
            print('Debe elegir una curva del listado. ')



        #----------------------------------------------------------------------------------------------
        # NSS   -   Caso del punto infinito
        #----------------------------------------------------------------------------------------------
        if(punto1.x == 0 and punto1.y == 0):
            punto1.pinta_punto()
            print('Este es el punto del infinito de la...')
            curva1.pinta_curvaNSS()
            print('')

            n_operacion = 0
            while n_operacion!=1 :
            
                print('SELECCIONE UNA OPERACIÓN:')
                print('---------------------------------------')
                print('    1) Algoritmo ECDH NSS')


                n_operacion = int(input('Marque el número correspondiente a la operación: \n'))

                #--------------------------------------------------
                #   OPERACION ECDH
                #--------------------------------------------------

                if n_operacion == 1:
                    print('-------------------------------------------')
                    print(' CALCULO DE LLAVES ECDH "Non-Supersingular"')
                    print('-------------------------------------------')
                    print(' Escriba el orden del punto de la curva ')
                    print('---------------------------------------------------')
                    orden = int(input('Introduzca el número:'))

                    mensaje2 = b'Se a seleccionado el algoritmo ECDH'

                    llaves_ecdh = ECDH_NSS(curva1, punto1, orden)
                    llaves_ecdh.pinta_llave_privada()
                    llaves_ecdh.pinta_llave_publica()

                else:
                    print('Opción inválida.')
                    mensaje2 = b'No se a seleccionado ningun algoritmo'

                #---------------------------------------------------------------------------------------------------------
                #   AQUI MANDAMOS EL TIPO DE ALGORITMO A USAR
                #---------------------------------------------------------------------------------------------------------

                print('---------------------------------------------------')
                print('Esperando conexión de la otra persona...')
                print('---------------------------------------------------')
                #connection, client_address = sock.accept()
                print('Conexión desde', client_address)
                print('---------------------------------------------------')
                print('\n')
                print('---------------------------------------------------')
                print('Curva elegida {!r}'.format(mensaje2))
                print('---------------------------------------------------')
                connection.sendall(mensaje2)

        #----------------------------------------------------------------------------------------------
        #   NSS    -   Otros puntos que pertenencen
        #----------------------------------------------------------------------------------------------
    
        elif (curva1.pertenece_a_NSS(punto1) == True):
            punto1.pinta_punto()
            print('PERTENECE  a la ')
            curva1.pinta_curvaNSS()
            print('')


            print(' Algoritmo ECDH NSS')
            print('---------------------------------------------------')
            print(' CALCULO DE LLAVES ECDH "Non-Supersingular" ')
            print('--------------------------------------------------')


            #INTRODUCCION DEL ORDEN DE LA CURVA
            #--------------------------------------------------
            if orden == None:

                orden_b = bytes(input('Introduzca el orden de la curva:'), 'utf-8')
                orden = int(orden_b)
                print('Enviando orden de la curva {!r}'.format(orden_b))
                print('---------------------------------------------------')
                connection.sendall(orden_b)

            #--------------------------------------------------

            persona1 = ECDH_NSS(curva1, punto1, orden)
            print('LLave privada Persona 1:')
            print(persona1.llave_privada)
            print('LLave publica Persona 1:')
            print(persona1.llave_publica.x)
            print(persona1.llave_publica.y)
            print('-----------------------------------------------------------------------------')
            print('Ahora debe mandar los puntos de su llave pública al otro usuario: ')
            print('-----------------------------------------------------------------------------')


            #----------------------------------------------------------------------
            # AQUI COMIENZA EL ENVIO Y RECEPCION DE LA LLAVE PUBLICA
            #----------------------------------------------------------------------
            coordX = bytes( input('Ingrese la coordenada X : '), 'utf-8')
            coordY = bytes( input('Ingrese la coordenada Y: '), 'utf-8')
            print('\n')
            dataX = connection.recv(1024)
            print ('Coordenada X recibida:  {!r}'.format(dataX))
            connection.sendall(coordX)

            dataY = connection.recv(1024)
            print ('Coordenada Y recibida:  {!r}'.format(dataY))
            connection.sendall(coordY)
            print('\n')
            #-------------------------------------------------------
                    
            x_coord = int(dataX)
            y_coord = int(dataY)
            otra_llave_publica = Punto(x_coord, y_coord)

            secreto_persona1 = persona1.calcula_secreto_compartido(otra_llave_publica)
            print('Secreto Compartido:')
            print(secreto_persona1.x)
            print(secreto_persona1.y)


        #----------------------------------------------------------------------------------------------
        #   NSS     -   Puntos que no pertenecen
        #----------------------------------------------------------------------------------------------
        else:
            print('El punto no pertenecen a la Curva descrita.')










    #-------------------------------------------------------------------------------------------------------------------------------------
    # TIPO DE CURVA SS
    #-------------------------------------------------------------------------------------------------------------------------------------
    elif (tipo_curva == 2):

        print('TIPO DE CURVA Supersingular (y² + cy = x³ + ax + b)')
        print('---------------------------------------------------------')
        print('Este tipo de curva se compone de 4 campos, (A,B,C,D).')
        print('A, B y C  seran los polinomios de la curva, representados como un entero.')
        print('D será otro polinomio, también representado como un entero, al que se denomina contexto.')
        print('Dichos campos serán representaremos como el ejemplo siguiente:')
        print('')
        print('Ejemplo de uso:')
        print('    2 = 10 = x')
        print('    3 = 11 = x + 1')
        print('    13 = 1101 = x³ + x² + 1')
        print('    35 = 100011 = x⁵ + x + 1')
        print('')
        print('---------------------------------------------------')
        print('')


        lista_curva = 0
        orden = None
        print('---------------------------------------------------')
        print('¿Que curva va a utilizar?')
        print('---------------------------------------------------')
        print(' 1) "CURVA B-4" ')
        print(' 2) "INSERTE SU PROPIA CURVA" ')

        print('---------------------------------------------------')

        #ENVIO DE LA CURVA
        #---------------------------------------------------------------------
        lcurva = bytes(input('Introduzca la curva con la que va a trabajar: \n'), 'utf-8')
        lista_curva = int(lcurva)
        print('---------------------------------------------------')
        print('Curva elegida {!r}'.format(lcurva))
        print('---------------------------------------------------')
        connection.sendall(lcurva)
        print('-------------------------------------------')

        if lista_curva == 1:
            print('Ha elegido la curva "CURVA PROPIA B-4" ')
            curva1 = CurvaElipticaSS(
            1,
            2,
            3,
            19,
            )
            print('Su representacion es:') 
            print('-------------------------------------------')
            curva1.pinta_curvaSS()
            print('')
            print('---------------------------------------------------')
            print('')
            print(' Uno de sus puntos pertenecientes es [Punto(x, y)] ')
            print('---------------------------------------------------')
            punto1 = Punto(
            5,
            5)
            punto1.pinta_punto()
            print('')
            orden = 32

        elif lista_curva == 2:

           # INTRUCCION DEL TERMINO A
            #--------------------------------------------------------------------
            termino_a = bytes(input('Introduzca el término A: \n '), 'utf-8')
            a = int(termino_a)
            print('Enviando Termino A {!r}'.format(termino_a))
            print('---------------------------------------------------')
            connection.sendall(termino_a)


            # INTRUCCION DEL TERMINO B
            #--------------------------------------------------------------------
            termino_b = bytes(input('Introduzca el término B: \n '), 'utf-8')
            b = int(termino_b)
            print('Enviando Termino B {!r}'.format(termino_b))
            print('---------------------------------------------------')
            connection.sendall(termino_b)

            # INTRUCCION DEL TERMINO C
            #--------------------------------------------------------------------
            termino_c= bytes(input('Introduzca el término C: \n '), 'utf-8')
            c = int(termino_c)
            print('Enviando Termino C {!r}'.format(termino_c))
            print('---------------------------------------------------')
            connection.sendall(termino_c)

            # INTRUCCION DEL TERMINO Contexto
            #--------------------------------------------------------------------
            termino_cont= bytes(input('Introduzca el término C (contexto): \n '), 'utf-8')
            cont = int(termino_cont)
            print('Enviando Termino C {!r}'.format(termino_cont))
            print('---------------------------------------------------')
            connection.sendall(termino_cont)

            # PRESENTACION DE LA CURVA
            #--------------------------------------------------------------------
            print('')
            print('---------------------------------------------------')
            print('')
            curva1 = CurvaElipticaSS(a, b, c, cont)
            print('TU CURVA ELÍPTICA ES:') 
            print('-------------------------------------------')
            curva1.pinta_curvaSS()

            #--------------------------------------------------------------------
            print('')
            print('---------------------------------------------------')
            print('')
            print(' PUNTO DE UNA CURVA ELÍPTICA [Punto(x, y)] ')
            print('---------------------------------------------------')

            # INTRUCCION DE LA COORDENADA X
            #--------------------------------------------------------------------
            x_p = bytes(input('Introduzca coordenada X:'), 'utf-8')
            x = int(x_p)
            print('Enviando coordenada {!r}'.format(x_p))
            print('---------------------------------------------------')
            connection.sendall(x_p)


            # INTRUCCION DE LA COORDENADA Y
            #--------------------------------------------------------------------
            y_p = bytes(input('Introduzca coordenada Y:'), 'utf-8')
            y = int(y_p)
            print('Enviando coordenada {!r}'.format(y_p))
            print('---------------------------------------------------')
            connection.sendall(y_p)

            #PRESENTACION DEL PUNTO DE LA CURVA
            #--------------------------------------------------------------------
            punto1 = Punto(x, y)
            print('')
            print('Tu punto es:') 
            print('-------------------------------------------')
            punto1.pinta_punto()
            print('')
            
            
            print('¿EL PUNTO PERTENECE AL TIPO DE CURVA "Non-Supersingular" ?:')
            print('-----------------------------------------------------------')

            
        else:
            print('Debe elegir una curva del listado. ')

#----------------------------------------------------------------------------------------------
# SS    -    Caso del punto infinito
#----------------------------------------------------------------------------------------------
        if(punto1.x == 0 and punto1.y == -1):
            punto1.pinta_punto()
            print('Este es el punto del infinito de la...')
            curva1.pinta_curvaSS()
            print('')

            
#----------------------------------------------------------------------------------------------
# SS    -    Otros puntos que pertenencen
#----------------------------------------------------------------------------------------------

        elif (curva1.pertenece_a_SS(punto1) == True):
            punto1.pinta_punto()
            print('PERTENECE  a la ')
            curva1.pinta_curvaSS()
            print('')

            print(' Algoritmo ECDH NSS')
            print('---------------------------------------------------')
            print(' CALCULO DE LLAVES ECDH "Non-Supersingular" ')
            print('--------------------------------------------------')


            #INTRODUCCION DEL ORDEN DE LA CURVA
            #--------------------------------------------------
            if orden == None:

                orden_b = bytes(input('Introduzca el orden de la curva:'), 'utf-8')
                orden = int(orden_b)
                print('Enviando orden de la curva {!r}'.format(orden_b))
                print('---------------------------------------------------')
                connection.sendall(orden_b)

            #--------------------------------------------------

            persona1 = ECDH_SS(curva1, punto1, orden)
            print('LLave privada Persona 1:')
            print(persona1.llave_privada)
            print('LLave publica Persona 1:')
            print(persona1.llave_publica.x)
            print(persona1.llave_publica.y)
            print('-----------------------------------------------------------------------------')
            print('Ahora debe mandar los puntos de su llave pública al otro usuario: ')
            print('-----------------------------------------------------------------------------')


            #----------------------------------------------------------------------
            # AQUI COMIENZA EL ENVIO Y RECEPCION DE LA LLAVE PUBLICA
            #----------------------------------------------------------------------
            coordX = bytes( input('Ingrese la coordenada X : '), 'utf-8')
            coordY = bytes( input('Ingrese la coordenada Y: '), 'utf-8')
            print('\n')
            dataX = connection.recv(1024)
            print ('Coordenada X recibida:  {!r}'.format(dataX))
            connection.sendall(coordX)

            dataY = connection.recv(1024)
            print ('Coordenada Y recibida:  {!r}'.format(dataY))
            connection.sendall(coordY)
            print('\n')
            #-------------------------------------------------------
                    
            x_coord = int(dataX)
            y_coord = int(dataY)
            otra_llave_publica = Punto(x_coord, y_coord)

            secreto_persona1 = persona1.calcula_secreto_compartido(otra_llave_publica)
            print('Secreto Compartido:')
            print(secreto_persona1.x)
            print(secreto_persona1.y)



            
#----------------------------------------------------------------------------------------------
# SS    -    Puntos que no pertenecen
#----------------------------------------------------------------------------------------------
        else:
            print('El punto no pertenecen a la Curva descrita.')

#----------------------------------------------------------------------------------------------------
    else:
        print('Recuerde, pulse 1 ó 2')

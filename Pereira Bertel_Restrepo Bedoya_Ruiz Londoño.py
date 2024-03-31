"""                           TALLER # 1:
-----------------------------INTEGRANTES-----------------------------------
CC.1000758420------- Christian Camilo Pereira Bertel
CC.1000872160------ Kevin Alejandro Restrepo Bedoya
CC.1017274121------ Emmanuel Ruiz Londoño
"""

import math
Estado_Menu=True
while Estado_Menu == True:
    print('================================================================')
    print('-------------------CUENTA DE USUARIO----------------------------')
    print('SELECCIONES EL PUNTO DEL TALLER QUE DESEA QUE SE EJECUTE')
    print(' 1. LISTA QUE ALAMACENE NUMEROS N......')
    print(' 2. FACTORIAL DE UN NUMERO......')
    print(' 3. SERIE DE RAMANUJAN......')
    print(' 4. DICCIONARIO DE USUARIOS......')
    try:
        Menu_Opcion = int(input('R/= '))
        if Menu_Opcion>=1 and Menu_Opcion<=4:
            if Menu_Opcion==1:
                EstadoWhile_1=True;
                while EstadoWhile_1==True:
                    try:
                        print('===============================================================')
                        A = int(input("INGRESE EL LIMITE DE SUCESION "))
                        if A>=0:
                            lista = [0, 1]
                            for i in range(0, A-1):
                                lista.append(lista[-1] + lista[-2])
                            print(lista)
                            print('===============================================================')
                            print(' DESEA CALCULAR OTRO LIMITE DE SUCESION? ')
                            print(' 1. SI  2. NO ')
                            Opcion_1=input(' R/= ')
                            if Opcion_1 =='2':
                                EstadoWhile_1=False
                            if Opcion_1 != '1' and Opcion_1!='2':
                                print('===============================================================')
                                print('NO INGRESO UN DATO COHERENTE A LA INSTRUCCION .')
                        else:
                            print('EL DATO NO PUEDE SER NEGATIVO')
                    except:
                        print('===============================================================')
                        print('INGRESO EL CAMPO DE FORMA ERRONEA ')
                        print('PORFAVOR INGRESE NUEVAMENTE EL DATO ')

            if Menu_Opcion==2:
                EstadoWhile_2=True
                while EstadoWhile_2==True:
                    print('===============================================================')
                    try:
                        n = int(input('INGRESE UN NUMERO PARA CALCULAR EL FACTORIAL: '))
                        if n >= 0:
                            x = 1
                            f = 1
                            while x <= n:
                                f = f * x
                                x += 1
                            print("EJ FACTORIAL DE ", n, " ES ", f)
                            print('===============================================================')
                            print('DESEA CALCULAR EL FACTORIAL DE OTRO NUMERO?  ')
                            print(' 1. SI  2. NO ')
                            Opcion_2=input(' R/= ')
                            if Opcion_2 == '2':
                                EstadoWhile_2 = False
                            if Opcion_2!='1' and Opcion_2!='2':
                                print('===============================================================')
                                print('NO INGRESO UN DATO COHERENTE A LA INSTRUCCION .')

                        else:
                            print('===============================================================')
                            print("NO SE PUEDE CALCULAR EL FACTORIAL")
                            print('PORFAVOR INGRESE NUEVAMENTE EL DATO ')
                    except:
                        print('===============================================================')
                        print('INGRESO EL CAMPO DE FORMA ERRONEA ')
                        print('PORFAVOR INGRESE NUEVAMENTE EL DATO ')

            if Menu_Opcion==3:
                N = 0
                ValidarSalida=True;
                Estado = True
                SumaTerminos = 0

                while Estado == True:

                    Formula_1 = (((math.factorial(4 * N)) * (1103 + (26390 * N))) / (
                                ((math.factorial(N)) ** 4) * ((4 * 99) ** (4 * N))))
                    SumaTerminos += Formula_1
                    Formula_2 = ((2 * math.sqrt(2)) / 9801)
                    Formula_1 = 0
                    Resultado = (Formula_2 * (SumaTerminos + Formula_1)) ** -1
                    print('===============================================================')
                    print('RESULTADO DE SERIE DE RAMANUJAN CUANDO N =', N, '    π = ', Resultado)
                    print('===============================================================')
                    ValidarSalida=True
                    while(ValidarSalida==True):
                        print(' DESEA SEGUIR INCREMENTANDO EL TERMINO? A N = ', N + 1)
                        print(' 1. SI  2. NO ')
                        Estado_While=input(' R/= ')
                        if Estado_While!='1' and  Estado_While!='2':
                            print('INGRESO ALGUN CAMPO DE FORMA ERRONEA ')
                            ValidarSalida=True
                        elif Estado_While=='2':
                            Estado = False
                            ValidarSalida=False
                        else:
                            N += 1
                            ValidarSalida= False

            if Menu_Opcion==4:
                Dic_Info_Basica = {'IDENTIFICACION': [], 'SEXO': [], 'EDAD': [], 'ESTATURA': [], 'PESO': []}
                NumeroHombres = 0
                NumeroMujeres = 0
                NumeroOtros = 0
                PromedioEdadHombres = 0
                PromedioEdadMujeres = 0
                PromedioEdadOtros = 0
                PromedioEstaturaHombres = 0
                PromedioEstaturaMujeres = 0
                PromedioEstaturaOtros = 0
                PromedioPesoHombres = 0
                PromedioPesoMujeres = 0
                PromedioPesoOtros = 0
                EstadoWhile = True

                while EstadoWhile == True:

                    try:
                        print('================================================================')
                        Usu_Identificacion = input('DIGITE LA IDENTIFICACION DEL USUARIO ')
                        print('1) HOMBRE '
                              '2) MUJER '
                              '3) OTRO')
                        Usu_Sexo = int(input(' '))
                        Usu_Edad = int(input('DIGITE EDAD DEL USUARIO '))
                        Usu_Estatura = int(input('DIGITE ESTATURA DEL USUARIO '))
                        Usu_Peso = float(input('DIGITE PESO DEL USUARIO '))
                        if len(Usu_Identificacion) == 0 or Usu_Edad < 0 or Usu_Estatura <= 0 or Usu_Peso <= 0 or Usu_Sexo < 1 or Usu_Sexo > 3:
                            print('======================================================================')
                            print('INGRESO ALGUN CAMPO DE FORMA ERRONEA ')
                            print('PORFAVOR INGRESE NUEVAMENTE LOS DATO ')
                        else:
                            Dic_Info_Basica['IDENTIFICACION'].append(Usu_Identificacion)
                            Dic_Info_Basica['EDAD'].append(Usu_Edad)
                            Dic_Info_Basica['ESTATURA'].append(Usu_Estatura)
                            Dic_Info_Basica['PESO'].append(Usu_Peso)
                            if Usu_Sexo == 1:
                                Genero = 'HOMBRE'
                            if Usu_Sexo == 2:
                                Genero = 'MUJER'
                            if Usu_Sexo == 3:
                                Genero = 'OTRO'

                            Dic_Info_Basica['SEXO'].append(Genero)
                            print('======================================================================')
                            print('DATOS GUARDADOS CON EXITO ')
                    except:
                        print('======================================================================')
                        print('INGRESO ALGUN CAMPO DE FORMA ERRONEA ')
                        print('PORFAVOR INGRESE NUEVAMENTE LOS DATO ')

                    print('DESEA INGRESAR LOS DATOS DE OTRO USUARIO? ')
                    if int(input('1) Si, 2) NO? ')) == 2:
                        EstadoWhile = False

                for Usuario in range(len(Dic_Info_Basica['IDENTIFICACION'])):
                    if Dic_Info_Basica['SEXO'][Usuario] == 'HOMBRE':
                        NumeroHombres += 1
                        PromedioEdadHombres += int(Dic_Info_Basica['EDAD'][Usuario])
                        PromedioEstaturaHombres += int(Dic_Info_Basica['ESTATURA'][Usuario])
                        PromedioPesoHombres += float(Dic_Info_Basica['PESO'][Usuario])
                    if Dic_Info_Basica['SEXO'][Usuario] == 'MUJER':
                        NumeroMujeres += 1
                        PromedioEdadMujeres += int(Dic_Info_Basica['EDAD'][Usuario])
                        PromedioEstaturaMujeres += float(Dic_Info_Basica['ESTATURA'][Usuario])
                        PromedioPesoMujeres += float(Dic_Info_Basica['PESO'][Usuario])
                    if Dic_Info_Basica['SEXO'][Usuario] == 'OTRO':
                        NumeroOtros += 1
                        PromedioEdadOtros += int(Dic_Info_Basica['EDAD'][Usuario])
                        PromedioEstaturaOtros += float(Dic_Info_Basica['ESTATURA'][Usuario])
                        PromedioPesoOtros += float(Dic_Info_Basica['PESO'][Usuario])

                if NumeroHombres != 0:
                    PromedioEdadHombres /= NumeroHombres
                    PromedioEstaturaHombres /= NumeroHombres
                    PromedioPesoHombres /= NumeroHombres
                if NumeroMujeres != 0:
                    PromedioEdadMujeres /= NumeroMujeres
                    PromedioEstaturaMujeres /= NumeroMujeres
                    PromedioPesoMujeres /= NumeroMujeres
                if NumeroOtros != 0:
                    PromedioEdadOtros /= NumeroOtros
                    PromedioEstaturaOtros /= NumeroOtros
                    PromedioPesoOtros /= NumeroOtros

                print('==============================================')
                print('NUMERO DE HOMBRES ', NumeroHombres)
                print('NUMERO DE MUJERES', NumeroMujeres)
                print('NUMERO DE OTROS', NumeroOtros)
                print('==============================================')
                print('PROMEDIOS DE EDAD SEGUN GENERO')
                print('PROMEDIO EDAD HOMBRES ', PromedioEdadHombres)
                print('PROMEDIO EDAD MUJERES ', PromedioEdadMujeres)
                print('PROMEDIO EDAD OTROS ', PromedioEdadOtros)
                print('==============================================')
                print('PROMEDIO ESTATURA HOMBRES', PromedioEstaturaHombres)
                print('PROMEDIO ESTATURA MUJERES', PromedioEstaturaMujeres)
                print('PROMEDIO ESTATURA OTROS', PromedioEstaturaOtros)
                print('==============================================')
                print('PROMEDIO PESO HOMBRES', PromedioPesoHombres)
                print('PROMEDIO PESO MUJERES', PromedioPesoMujeres)
                print('PROMEDIO PESO OTROS', PromedioPesoOtros)
                print('==============================================')
        else:
            print('NO INGRESO UN DATO COHERENTE A LA INSTRUCCION.')
            print('PORFAVOR INTENTE DENUEVO.')

        print('DESEA VOLVER AL AL MENU DE INCIO ?')
        print(' 1. Si  2. NO')

        Menu_Opcion_Inicio = int(input(' '))
        if Menu_Opcion_Inicio < 1 or Menu_Opcion_Inicio > 2:
            print('NO INGRESO UN DATO COHERENTE A LA INSTRUCCION')
        elif Menu_Opcion_Inicio == 2:
            Estado_Menu = False
            print('FIN DE SESION!!!')


    except:
        print('NO INGRESO UN DATO COHERENTE A LA INSTRUCCION')












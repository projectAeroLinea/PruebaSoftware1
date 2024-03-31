"""                           TALLER # 4:
-----------------------------INTEGRANTES-----------------------------------
CC.1000758420------- Christian Camilo Pereira Bertel
CC.1000872160------ Kevin Alejandro Restrepo Bedoya
CC.1017274121------ Emmanuel Ruiz Londoño

"""

import math
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------------------------------
class cls_Paciente:
    def __init__(self):
        self.__Identificacion=None,
        self.__Nombre=None,
        self.__Sexo = None,
        self.__Edad = None,
        self.__Peso = None,
        self.__Estatura = None,
        self.DataFramePacientes= pd.DataFrame()
        self.Error=None,
        self.__Paciente = {
            "IDENTIFICACION": [],
            "NOMBRE": [],
            "SEXO": [],
            "EDAD": [],
            "PESO": [],
            "ESTATURA": []
        }

    def Ingresar(self,numeropacientes):

        self.__Paciente['IDENTIFICACION'].append(self.__Identificacion)
        self.__Paciente['NOMBRE'].append(self.__Nombre)
        self.__Paciente['SEXO'].append(self.__Sexo)
        self.__Paciente['EDAD'].append(self.__Edad)
        self.__Paciente['PESO'].append(self.__Peso)
        self.__Paciente['ESTATURA'].append(self.__Estatura)
        if len(self.__Paciente['IDENTIFICACION']) == int(numeropacientes):

            if len(self.DataFramePacientes.columns)==0:

                self.DataFramePacientes = pd.DataFrame(self.__Paciente)

            else:
                DataFramePacientes_2 = pd.DataFrame(self.__Paciente)
                self.DataFramePacientes = pd.concat([self.DataFramePacientes, DataFramePacientes_2], ignore_index=True)


            self.__Paciente['IDENTIFICACION'] = []
            self.__Paciente['NOMBRE'] = []
            self.__Paciente['SEXO'] = []
            self.__Paciente['EDAD'] = []
            self.__Paciente['PESO'] = []
            self.__Paciente['ESTATURA'] = []

    def Consultar(self,Identificacion):

        DataFramePacientes_Identificacion =self.DataFramePacientes.loc[self.DataFramePacientes['IDENTIFICACION'] == Identificacion]
        print(DataFramePacientes_Identificacion)

    def FiltrarDataFrame(self,sexo):
        DataFramePacientes_Sexo = self.DataFramePacientes.loc[self.DataFramePacientes['SEXO'] == sexo]
        print(DataFramePacientes_Sexo)

    def RangosEtarios(self):
        DataFramePacientes_Sexo = {
            "H": [],
            "M": [],
            "O": []
        }
        for i in range (3):
            if (i == 0):
                sexo='H'
            if (i == 1):
                sexo = 'M'
            if (i == 2):
                sexo = 'O'

            DataFramePacientes_Sexo[sexo].append(len(self.DataFramePacientes.loc[((self.DataFramePacientes['EDAD'] >=0) & (self.DataFramePacientes['EDAD']<=9) & (self.DataFramePacientes['SEXO']==sexo))]))
            DataFramePacientes_Sexo[sexo].append(len(self.DataFramePacientes.loc[((self.DataFramePacientes['EDAD'] >=10) & (self.DataFramePacientes['EDAD']<=19)& (self.DataFramePacientes['SEXO']==sexo))]))
            DataFramePacientes_Sexo[sexo].append(len(self.DataFramePacientes.loc[((self.DataFramePacientes['EDAD'] >=20) & (self.DataFramePacientes['EDAD']<=29)& (self.DataFramePacientes['SEXO']==sexo))]))
            DataFramePacientes_Sexo[sexo].append(len(self.DataFramePacientes.loc[((self.DataFramePacientes['EDAD'] >=30) & (self.DataFramePacientes['EDAD']<=39)& (self.DataFramePacientes['SEXO']==sexo))]))
            DataFramePacientes_Sexo[sexo].append(len(self.DataFramePacientes.loc[((self.DataFramePacientes['EDAD'] >=40) & (self.DataFramePacientes['EDAD']<=49)& (self.DataFramePacientes['SEXO']==sexo))]))
            DataFramePacientes_Sexo[sexo].append(len(self.DataFramePacientes.loc[((self.DataFramePacientes['EDAD'] >=50) & (self.DataFramePacientes['EDAD']<=59)& (self.DataFramePacientes['SEXO']==sexo))]))
            DataFramePacientes_Sexo[sexo].append(len(self.DataFramePacientes.loc[((self.DataFramePacientes['EDAD'] >=60) & (self.DataFramePacientes['EDAD']<=69)& (self.DataFramePacientes['SEXO']==sexo))]))
            DataFramePacientes_Sexo[sexo].append(len(self.DataFramePacientes.loc[((self.DataFramePacientes['EDAD'] >=70) & (self.DataFramePacientes['EDAD']<=79)& (self.DataFramePacientes['SEXO']==sexo))]))
            DataFramePacientes_Sexo[sexo].append(len(self.DataFramePacientes.loc[((self.DataFramePacientes['EDAD'] >=80) & (self.DataFramePacientes['EDAD']<=89)& (self.DataFramePacientes['SEXO']==sexo))]))
            DataFramePacientes_Sexo[sexo].append(len(self.DataFramePacientes.loc[(self.DataFramePacientes['EDAD'] >=90) & (self.DataFramePacientes['SEXO']==sexo) ]))

        DataFramePacientes_Sexo = pd.DataFrame(DataFramePacientes_Sexo,
            index=["0-9", "10-19", "20-29", "30-39", "40,49","50,59","60,69","70,79","80,89","90 0 MAS"]
        )
        DataFramePacientes_Sexo.plot(kind="bar")
        plt.show()

    def __calcularIMC(self):


        self.DataFramePacientes['IMC'] = self.DataFramePacientes['PESO'] / ((self.DataFramePacientes['ESTATURA']) / 100) ** 2


    def evaluar(self):

        self.__calcularIMC()
        DataFramePacientes_IMC = {
            "H": [],
            "M": [],
            "O": []
        }
        for i in range(3):
            if (i == 0):
                sexo = 'H'
            if (i == 1):
                sexo = 'M'
            if (i == 2):
                sexo = 'O'

            DataFramePacientes_IMC[sexo].append(len(self.DataFramePacientes.loc[(self.DataFramePacientes['IMC'] < 18.49) & (self.DataFramePacientes['SEXO']==sexo)]))
            DataFramePacientes_IMC[sexo].append(len(self.DataFramePacientes.loc[(self.DataFramePacientes['IMC'] >= 18.50) & (self.DataFramePacientes['IMC'] <= 24.99) & (self.DataFramePacientes['SEXO']==sexo) ]))
            DataFramePacientes_IMC[sexo].append(len(self.DataFramePacientes.loc[(self.DataFramePacientes['IMC'] >= 25) & (self.DataFramePacientes['IMC'] <= 29.9) & (self.DataFramePacientes['SEXO']==sexo)]))
            DataFramePacientes_IMC[sexo].append(len(self.DataFramePacientes.loc[(self.DataFramePacientes['IMC'] >= 30) & (self.DataFramePacientes['IMC'] <= 39.99) & (self.DataFramePacientes['SEXO']==sexo)]))
            DataFramePacientes_IMC[sexo].append(len(self.DataFramePacientes.loc[(self.DataFramePacientes['IMC'] >= 40) & (self.DataFramePacientes['SEXO']==sexo)]))


        DataFramePacientes_IMC = pd.DataFrame(DataFramePacientes_IMC,
        index=["Peso bajo","peso normal","Sobrepeso","Obesidad","Obesidad extrema"]
                                               )
        DataFramePacientes_IMC.plot(kind="bar")
        plt.show()

    def Validar(self,Operacion,Valor=None):
        try:
            if Operacion=='NUMEROPACIENTES':
                numeropacientes=int(Valor)
                if numeropacientes<=0:
                    self.Error = 'EL NUMERO DE PACIENTES NO DEBE SER NI MENOR NI IGUAL A CERO'
                    return  False

            if Operacion=='IDENTIFICACION':
                Identificacion = int(Valor)
                self.__Identificacion= str(Identificacion)
            if Operacion == 'NOMBRE':
                if Valor == '':
                    self.Error = 'NO INGRESO EL NOMBRE DEL PACIENTE'
                    return False
                self.__Nombre=Valor
            if Operacion == 'EDAD':
                Edad = int(Valor)
                if Edad < 0:
                    self.Error = 'NO SE DIGITARON DATOS COHERENTES, LA EDAD DEL PACIENTE NO PUEDE SER MENOR A CERO'
                    return False
                self.__Edad = Edad
            if Operacion == 'PESO':
                Peso = float(Valor)
                if Peso <= 0:
                    self.Error = 'NO SE DIGITARON DATOS COHERENTES, EL PESO DEL PACIENTE NO PUEDE SER NI IGUAL NI MENOR A CERO'
                    return False
                self.__Peso = Peso
            if Operacion == 'SEXO':
                if Valor != 'H' and Valor != 'M' and Valor != 'O':
                    self.Error = 'NO SE DATOS COHERENTES CON RESPECTO AL SEXO DE PACIENTE'
                    return False
                self.__Sexo=Valor
            if Operacion == 'FILTRAR_SEXO':
                if Valor!='1' and Valor!='2':
                    self.Error = 'NO SE DIGITARON DATOS COHERENTES'
                    return True, False
                if Valor=='1':
                    return False,True
                else:
                    return False,False

            if Operacion == 'ESTATURA':
                Estatura = float(Valor)
                if Estatura <= 0:
                    self.Error = 'NO SE DIGITARON DATOS COHERENTES, LA ESTATURA DEL PACIENTE NO PUEDES SER NI IGUAL NI MENOR A CERO'
                    return False
                self.__Estatura = Estatura

            if Operacion == 'CONSULTAR_PACIENTE':
                if ~self.DataFramePacientes['IDENTIFICACION'].isin([Valor]).any():
                    self.Error = 'NO SE ENCUENTRA REGISTRO DE LA INDETIFICACION INGRESADA'
                    return False
            if Operacion == 'CONSULTAR_EXISTENCIAS_DATAFRAME':
                if len(self.DataFramePacientes.columns) == 0:
                    self.Error = 'NO EXISTE REGISTRO DE PACIENTES'
                    return False
            return True
        except:
            self.Error='NO SE DIGITARON DATOS COHERENTES A LA INSTRUCCION'
            return False




# CLASES PUNTO #2 -------------------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------------------------------

class Taller_4():
    def __init__(self):
        self.opcion = None
        self.Paciente = cls_Paciente()
        self.error = None

    def __punto_1(self):
            validarentrada = True
            while validarentrada:
                validarentrad_3 = True
                ValidarPaciente = True
                Posicion = 0
                print('===========================================================')
                while ValidarPaciente:
                    if Posicion == 0:
                        numeropacientes = input('¿CUANTOS PACIENTES DESEA INGRESAR? R/= ')
                    if self.Paciente.Validar('NUMEROPACIENTES', numeropacientes):
                        Posicion += 1
                        for contadorpacientes in range(int(numeropacientes)):
                            ValidarPaciente = True
                            while ValidarPaciente:
                                if Posicion == 1:

                                    print('====================== PACIENTE #', contadorpacientes + 1,
                                          ' ======================')
                                    print('===========================================================')
                                    print('INGRESE IDENTIFICACION DEL PACIENTE ', contadorpacientes + 1)
                                    Identificacion = input('R/= ')
                                    if self.Paciente.Validar('IDENTIFICACION', Identificacion):
                                        Posicion += 1
                                    else:
                                        print('===========================================================')
                                        print(self.Paciente.Error)
                                if Posicion == 2:
                                    print('===========================================================')
                                    print('INGRESE NOMBRE DEL PACIENTE ', contadorpacientes + 1)
                                    Nombre = input('R/= ')
                                    if self.Paciente.Validar('NOMBRE', Nombre):
                                        Posicion += 1
                                    else:
                                        print('===========================================================')
                                        print(self.Paciente.Error)
                                if Posicion == 3:
                                    print('===========================================================')
                                    print('INGRESE SEXO DEL PACIENTE ', contadorpacientes + 1)
                                    print('HOMBRE ----> H, MUJER ----> M, OTRO ----> O')
                                    sexo = input(' R/= ')
                                    if self.Paciente.Validar('SEXO', sexo):
                                        Posicion += 1
                                    else:
                                        print('===========================================================')
                                        print(self.Paciente.Error)
                                if Posicion == 4:
                                    print('===========================================================')
                                    print('INGRESE LA EDAD DEL PACIENTE ', contadorpacientes + 1)
                                    edad = input('R/= ')
                                    if self.Paciente.Validar('EDAD', edad):
                                        Posicion += 1
                                    else:
                                        print('===========================================================')
                                        print(self.Paciente.Error)
                                if Posicion == 5:
                                    print('===========================================================')
                                    print('INGRESE EL PESO DEL PACIENTE ', contadorpacientes + 1)
                                    peso = input('R/= ')
                                    if self.Paciente.Validar('PESO', peso):
                                        Posicion += 1
                                    else:
                                        print('===========================================================')
                                        print(self.Paciente.Error)
                                if Posicion == 6:
                                    print('===========================================================')
                                    print('INGRESE LA ESTATURA DEL PACIENTE ', contadorpacientes + 1)
                                    estatura = input('R/= ')
                                    if self.Paciente.Validar('ESTATURA', estatura):
                                        self.Paciente.Ingresar(numeropacientes)
                                        Posicion = 1
                                        ValidarPaciente = False
                                    else:
                                        print('===========================================================')
                                        print(self.Paciente.Error)
                    else:
                        print('===========================================================')
                        print(self.Paciente.Error)


                print('==================================================')
                if self.Paciente.Validar('CONSULTAR_EXISTENCIAS_DATAFRAME'):
                    while validarentrad_3:

                        print('==================================================')
                        print('DESEA FILTRAR POR SEXO?')
                        opcion = input('1. SI, 2. NO (R/= ')
                        validarentrad_3, opcion = self.Paciente.Validar('FILTRAR_SEXO', opcion)
                        if opcion:
                            print('¿QUE SEXO DESEA FILTRAR?')
                            print('HOMBRE ----> H, MUJER ----> M, OTRO ----> O')
                            sexo = input(' R/= ')
                            if self.Paciente.Validar('SEXO', sexo):
                                self.Paciente.FiltrarDataFrame(sexo)
                            else:
                                validarentrad_3 = True

                    self.Paciente.RangosEtarios()
                    self.Paciente.evaluar()

                else:
                    print('===========================================================')
                    print(self.Paciente.Error)


                validarentrad_3 = True
                while validarentrad_3:
                    print('==================================================')
                    print('PORFAVOR ELIJA UNA OPCION')
                    opcion = input('1. VOLVER A INGRESAR PACIENTE(S), 2. VOLVER AL MENU DE INICIO (R/= ')
                    if opcion == '1':
                        validarentrad_3 = False
                        validarentrada = True
                    if opcion == '2':
                        validarentrad_3 = False
                        validarentrada = False



    def __punto_2(self):
        validarentrada=True
        while validarentrada:
            validarentrad_3 = True
            if self.Paciente.Validar('CONSULTAR_EXISTENCIAS_DATAFRAME'):
                print('==================================================')
                print('INGRESE LA IDENTIFICACION DEL PACIENTE QUE DESEA CONSULTAR')
                Identificacion = input(' R/= ')
                if self.Paciente.Validar('IDENTIFICACION', Identificacion):
                    if self.Paciente.Validar('CONSULTAR_PACIENTE', Identificacion):
                        self.Paciente.Consultar(Identificacion)
                    else:
                        print('===========================================================')
                        print(self.Paciente.Error)
                else:
                    print('===========================================================')
                    print(self.Paciente.Error)
            else:
                print('===========================================================')
                print(self.Paciente.Error)
                validarentrada = False

            while validarentrad_3:
                print('==================================================')
                print('PORFAVOR ELIJA UNA OPCION')
                opcion = input('1. VOLVER A CONSULTAR UN PACIENTE, 2. VOLVER AL MENU DE INICIO (R/= ')
                if opcion == '1':
                    validarentrad_3 = False
                    validarentrada = True
                if opcion == '2':
                    validarentrad_3 = False
                    validarentrada = False



    def __recorrerpuntos(self):
        if self.opcion == '1':
            self.opcion = None
            self.__punto_1()
            self.opcion = None
            self.menu_inicio()
        if self.opcion == '2':
            self.opcion = None
            self.__punto_2()
            self.opcion = None
            self.menu_inicio()
        if self.opcion == '3':
            print('==================================================')
            print('            FIN DE SESION !!!!!')
            quit()

    def __Validar_datos_entrada(self):
        validarentrada = True
        if self.opcion == None:
            return False
        if self.opcion != '1' and self.opcion != '2' and self.opcion != '3':
            while validarentrada:
                print('NO SE DIGITARON DATOS COHERENTES A LA INSTRUCCION')
                print('DESEA VOLVER AL MENU DE INICIO ?')
                opcion = input('1. SI, 2. NO  (R/= ')
                if opcion == '1':
                    return False
                if opcion == '2':
                    return True

    def menu_inicio(self):
        while self.__Validar_datos_entrada() == False:
            print('======================MENU DE PACIENTES======================')
            print('SELECCIONE LA ACCION A REALIZAR ')
            print('1. INGRESAR PACIENTES')
            print('2. CONSULTAR PACIENTES')
            print('3. SALIR')
            self.opcion = input('R/= ')

        self.__recorrerpuntos()


Taller_4 = Taller_4()
Taller_4.menu_inicio()
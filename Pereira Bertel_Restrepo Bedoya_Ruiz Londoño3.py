"""                           TALLER # 2:
-----------------------------INTEGRANTES-----------------------------------
CC.1000758420------- Christian Camilo Pereira Bertel
CC.1000872160------ Kevin Alejandro Restrepo Bedoya
CC.1017274121------ Emmanuel Ruiz Londoño
"""

import math
import numpy as np
import matplotlib.pyplot as plt


#CLASES PUNTO #1 -------------------------------------------------------------------------------------------
class cls_EcuacionesGenericas:
    def __init__(self,valor_inicial_x,valor_final_x,numero_puntos):

        self.valor_inicial_x=valor_inicial_x
        self.valor_final_x = valor_final_x
        self.numero_puntos = numero_puntos
        self.y=[]
        self.Arreglo_x=None

    def ConvertirArreglo_x(self):
        self.Arreglo_x = np.linspace(self.valor_inicial_x,self.valor_final_x,num=self.numero_puntos)


    def formulacirculo(self,k,r,h):

        try:

            for i in range(len(self.Arreglo_x)):
                y_2=math.sqrt((r**2)-((self.Arreglo_x[i]-h)**2))+k
                self.y.append(y_2)
            self.y=np.array(self.y)
            radio = float(((self.Arreglo_x[self.numero_puntos-1] - h) ** 2) + ((y_2 - k) ** 2))

            return radio
        except:

             return None


    def formula_elipse(self,k,a,b,h):
        try:
            for i in range(len(self.Arreglo_x)):
               y_2=math.sqrt((b**2)-((b**2)*(((self.Arreglo_x[i]-h)**2)/a**2)))+k
               self.y.append(y_2)
            self.y = np.array(self.y)
            return float((((self.Arreglo_x[0] - h) ** 2) / a ** 2) + (((self.y[0] - k) ** 2) / b ** 2))

        except:
            return None

    def formulaparabola(self,k,a,h):
        try:
            for i in range(len(self.Arreglo_x)):
                y_2=a*((self.Arreglo_x[i]-h)**2)+k
                self.y.append(y_2)
            self.y = np.array(self.y)
            return self.y[0]
        except:
            return None


    def formulahiperbola(self,k,a,b,h):
        try:
            for i in range(len(self.Arreglo_x)):
                y_2=math.sqrt((b**2*(((self.Arreglo_x[i]-h)**2)/a**2))-b**2)+k
                self.y.append(y_2)
            self.y = np.array(self.y)
            return int((((self.Arreglo_x[0] - h) ** 2) / a ** 2) - (((self.y[0] - k) ** 2) / b ** 2))
        except:
            return None


class Circulo(cls_EcuacionesGenericas):
    def __init__(self,k,r,h):
        self.k=k
        self.r=r
        self.h=h

    def graficarplanocartesiano(self):

        plt.plot(self.Arreglo_x, self.y)
        plt.show()
    def calcular_Radio(self,valor_inicial_x,valor_final_x,numero_puntos):
        if self.validar_datos(valor_inicial_x,valor_final_x,numero_puntos):

            super().__init__(int(valor_inicial_x),int(valor_final_x),int(numero_puntos))
            super().ConvertirArreglo_x()
            if self.validarDominio(int(numero_puntos)):
                radio=super().formulacirculo(self.k,self.r,self.h)

                if round(radio) == self.r**2:

                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    def validarDominio(self,numero_puntos):

        for i in range(numero_puntos):

            validarDominio_Y = self.r ** 2 - (((self.Arreglo_x[i] - self.h)) ** 2)
            if validarDominio_Y < 0:
                print('===========================================================')
                print('LOS VALORES INGRESADOS VIOLAN EL DOMINIO DE LA FUNCION')
                return False
        return True

    def validar_datos(self,valor_inicial_x,valor_final_x,numero_puntos):
       try:

           valor_inicial_x=int(valor_inicial_x)
           valor_final_x = int(valor_final_x)
           numero_puntos=  int(numero_puntos)
           self.k= float(self.k)
           self.r= float(self.r)
           self.h= float(self.h)

           if numero_puntos<=0:
               print('LOS PUNTOS DEL ARREGLO NO PUEDEN SER NI IGUAL O MENOR A CERO')
               return False

           if self.r==0:
               print('EL VALOR DEL RADIO DEBE SER DIFERENTE DE CERO')
               return False

           return  True
       except:
           print('===========================================================')
           print('NO SE DIGITARON DATOS COHERENTES A LA INSTRUCCION ')
           return False



class Elipse(cls_EcuacionesGenericas):
    def __init__(self,k,a,b,h):
        self.h = h
        self.k = k
        self.a = a
        self.b = b
    def graficarplanocartesiano(self):

        plt.plot(self.Arreglo_x, self.y)
        plt.show()
    def calcular_Elipse(self,valor_inicial_x,valor_final_x,numero_puntos):
        if self.validardatos(valor_inicial_x,valor_final_x,numero_puntos):
            super().__init__(int(valor_inicial_x),int(valor_final_x),int(numero_puntos))
            super().ConvertirArreglo_x()
            if self.validarDominio(int(numero_puntos)):
                resultado=super().formula_elipse(self.k, self.a, self.b,self.h)
                if round(resultado) ==1:

                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def validardatos(self,valor_inicial_x,valor_final_x,numero_puntos):
        try:
            valor_inicial_x = int(valor_inicial_x)
            valor_final_x = int(valor_final_x)
            numero_puntos = int(numero_puntos)
            self.k = float(self.k)
            self.a = float(self.a)
            self.b = float(self.b)
            self.h = float(self.h)

            if numero_puntos <= 0:
                print('LOS PUNTOS DEL ARREGLO NO PUEDEN SER NI IGUAL O MENOR A CERO')
                return False

            if self.a != 0 and self.b != 0:
                if self.a > self.b:
                    pass

                else:
                    print('===========================================================')
                    print('LA LONGITUD A DEBE SER MAYOR A B')
                    return False

                return True
            else:
                print('===========================================================')
                print('LOS VALORES DE A Y B DEBEN SER DIFERENTES A CERO')
                return False

        except:
            print('===========================================================')
            print('NO SE DIGITARON DATOS COHERENTES A LA INSTRUCCION ')
            return False

    def validarDominio(self, numero_puntos):

        for i in range(numero_puntos):
            validarDominio_Y = (self.b ** 2) - ((self.b ** 2) * (((self.Arreglo_x[i] - self.h) ** 2) / self.a ** 2))
            if validarDominio_Y < 0:
                print('===========================================================')
                print('LOS VALORES INGRESADOS VIOLAN EL DOMINIO DE LA FUNCION')
                return False
        return True


class Parabola(cls_EcuacionesGenericas):
    def __init__(self,k,a,h):
        self.h = h
        self.k = k
        self.a = a
    def graficarplanocartesiano(self):

        plt.plot(self.Arreglo_x, self.y)
        plt.show()
    def calcular_Parabola(self,valor_inicial_x,valor_final_x,numero_puntos):
        if self.validardatos(valor_inicial_x,valor_final_x,numero_puntos):
            super().__init__(int(valor_inicial_x),int(valor_final_x),int(numero_puntos))
            super().ConvertirArreglo_x()

            resultado= super().formulaparabola(self.k, self.a,self.h)
            if resultado !=None:
                return True
            else:
                return False
        else:
            return False

    def validardatos(self,valor_inicial_x,valor_final_x,numero_puntos):
        try:
            valor_inicial_x = int(valor_inicial_x)
            valor_final_x = int(valor_final_x)
            numero_puntos = int(numero_puntos)
            self.k = float(self.k)
            self.a = float(self.a)
            self.h = float(self.h)
            if numero_puntos <= 0:
                print('LOS PUNTOS DEL ARREGLO NO PUEDEN SER NI IGUAL O MENOR A CERO')
                return False

            return  True
        except:
            print('===========================================================')
            print('NO SE DIGITARON DATOS COHERENTES A LA INSTRUCCION ')
            return False


class Hiperbola(cls_EcuacionesGenericas):
    def __init__(self,k,a,b,h):
        self.h = h
        self.k = k
        self.a = a
        self.b = b

    def graficarplanocartesiano(self):

        plt.plot(self.Arreglo_x, self.y)
        plt.show()

    def calcular_Hiperbola(self,valor_inicial_x,valor_final_x,numero_puntos):
        if self.validardatos(valor_inicial_x,valor_final_x,numero_puntos):
            super().__init__(int(valor_inicial_x), int(valor_final_x), int(numero_puntos))
            super().ConvertirArreglo_x()
            if self.validarDominio(int(numero_puntos)):
                resultado = super().formulahiperbola(self.k, self.a, self.b,self.h)
                if resultado == 1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    def validardatos(self,valor_inicial_x,valor_final_x,numero_puntos):
        try:
            valor_inicial_x = int(valor_inicial_x)
            valor_final_x = int(valor_final_x)
            numero_puntos = int(numero_puntos)
            self.h = float(self.h)
            self.k = float(self.k)
            self.a = float(self.a)
            self.b = float(self.b)


            if self.a!=0 and self.b!=0:
                if self.a > self.b:
                    pass

                else:
                    print('===========================================================')
                    print('LA LONGITUD A DEBE SER MAYOR A B')
                    return False


                return True
            else:
                print('===========================================================')
                print('LOS VALORES DE A Y B DEBEN SER DIFERENTES A CERO')
                return False



        except:
            print('===========================================================')
            print('NO SE DIGITARON DATOS COHERENTES A LA INSTRUCCION ')
            return False

    def validarDominio(self, numero_puntos):

        for i in range(numero_puntos):
            validarDominio_Y = ((self.b ** 2 * (((self.Arreglo_x[i] - self.h) ** 2) / self.a ** 2)) - self.b ** 2)
            if validarDominio_Y < 0:
                print('===========================================================')
                print('LOS VALORES INGRESADOS VIOLAN EL DOMINIO DE LA FUNCION')
                return False
        return True

#-----------------------------------------------------------------------------------------------------------
#CLASES PUNTO #2 -------------------------------------------------------------------------------------------
class clsTemperaturas:

    def __init__(self,t_inicial,t_final,t_resolucion):
        self.t_inicial=t_inicial
        self.t_final = t_final
        self.t_resolucion = t_resolucion

    def convertirTemperatura(self):
        if self.__validarTemperatura():
            temp_celsius = np.arange(self.t_inicial, self.t_final + 1, self.t_resolucion, dtype=float)
            temp_farenh = np.around((temp_celsius * (9 / 5)) + 32, decimals=1)
            arreglo = np.array([temp_celsius, temp_farenh], dtype=float)
            print('===========================================================')
            print('EL ARREGLO FINAL ES : ')
            print(arreglo)
            return True
        else:
            return False

    def __validarTemperatura(self):

        try:
            self.t_inicial = float(self.t_inicial)
            self.t_final = float(self.t_final)
            self.t_resolucion = float(self.t_resolucion)
            if self.t_inicial >= self.t_final:
                print('LA TEMPERATURA INICIAL EN °C NO PUEDE SER MAYOR NI IGUAL A LA LA TEMPERATURA FINAL EN °C  ')
                return False
            if self.t_resolucion <=0:
                print('EL INCREMENTO DE LA TEMPERATUARA NO PUEDE SER NI IGUAL NI MENOR A CERO')
                return False
            return True
        except:
            print('NO SE DIGITARON DATOS COHERENTES A LA INSTRUCCION')
            return False
#-----------------------------------------------------------------------------------------------------------
#CLASES PUNTO #3 -------------------------------------------------------------------------------------------
class clsSistemaEcuacionLineal_3X3:

    def __init__(self,a_11,a_12,a_13,a_21,a_22,a_23,a_31,a_32,a_33,b_1,b_2,b_3,X1=None,X2=None,X3=None):
        self.a_11=a_11
        self.a_12 = a_12
        self.a_13 = a_13
        self.a_21 = a_21
        self.a_22 = a_22
        self.a_23 = a_23
        self.a_31 = a_31
        self.a_32 = a_32
        self.a_33 = a_33
        self.b_1 = b_1
        self.b_2 = b_2
        self.b_3 = b_3
        self.X1 = X1
        self.X2 = X2
        self.X3 = X3
        self.Error = ""

    def Calcular_SistemaDeEcuacionesLineales3x3(self):
        if self.__ValidarDatos3x3():
            ArregloX1, ArregloX2,Arreglo_X3, Delta = self.__ConvertirArreglo()
            if self.__Calcular_X1_y_X_2_yX_3(ArregloX1, ArregloX2,Arreglo_X3, Delta):

                return True
            else:
                return False
        else:
            return False

    def __ConvertirArreglo(self):

        ArregloX1 = [[self.b_1, self.a_12,self.a_13], [self.b_2, self.a_22, self.a_23],[self.b_3, self.a_32, self.a_33]]
        ArregloX2 = [[self.a_11, self.b_1,self.a_13], [self.a_21, self.b_2,self.a_23], [self.a_31, self.b_3,self.a_33]]
        ArregloX3 = [[self.a_11, self.a_12,self.b_1], [self.a_21, self.a_22,self.b_2], [self.a_31, self.a_32,self.b_3]]
        Delta = [[self.a_11, self.a_12,self.a_13], [self.a_21, self.a_22,self.a_23], [self.a_31, self.a_32,self.a_33]]
        Arreglo_X1 = np.array(ArregloX1)
        Arreglo_X2 = np.array(ArregloX2)
        Arreglo_X3 = np.array(ArregloX3)
        Delta = np.array(Delta)
        return Arreglo_X1, Arreglo_X2, Arreglo_X3, Delta

    def __Calcular_X1_y_X_2_yX_3(self, ArregloX1, ArregloX2,Arreglo_X3, Delta):
        try:
            if (Delta[0, 0] * (Delta[1, 1] * Delta[2, 2] - Delta[1, 2] * Delta[2, 1]) - Delta[0, 1] * (Delta[1, 0] * Delta[2, 2] - Delta[1, 2] * Delta[2, 0]) + Delta[0, 2] * (Delta[1, 0] * Delta[2, 1] - Delta[1, 1] * Delta[2, 0] ))==0:
                print('EL DETERMINANTE DE LA MATRIZ ES CERO')
                print('ESTO DIGNIFICA QUE EL SISTEMA DE ECUACIONES LINEALES ES INCONSISTENTE O TIENE UN NUMERO DE SOLUCIONES ILIMITADO')
                print('===========================================================')
                return False

            self.X1 = (ArregloX1[0,0]*((ArregloX1[1,1]*ArregloX1[2,2])-(ArregloX1[1,2]*ArregloX1[2,1]))-ArregloX1[0,1]*((ArregloX1[1,0]*ArregloX1[2,2])-(ArregloX1[1,2]*ArregloX1[2,0]))+ArregloX1[0,2]*((ArregloX1[1,0]*ArregloX1[2,1])-(ArregloX1[1,1]*ArregloX1[2,0])))/ (
                  Delta[0, 0] * (Delta[1, 1] * Delta[2, 2] - Delta[1, 2] * Delta[2, 1]) - Delta[0, 1] * (Delta[1, 0] * Delta[2, 2] - Delta[1, 2] * Delta[2, 0]) + Delta[0, 2] * (Delta[1, 0] * Delta[2, 1] - Delta[1, 1] * Delta[2, 0] ))

            self.X2 = (ArregloX2[0,0]*((ArregloX2[1,1]*ArregloX2[2,2])-(ArregloX2[1,2]*ArregloX2[2,1]))-ArregloX2[0,1]*((ArregloX2[1,0]*ArregloX2[2,2])-(ArregloX2[1,2]*ArregloX2[2,0]))+ArregloX2[0,2]*((ArregloX2[1,0]*ArregloX2[2,1])-(ArregloX2[1,1]*ArregloX2[2,0])))/ (
                  Delta[0, 0] * (Delta[1, 1] * Delta[2, 2] - Delta[1, 2] * Delta[2, 1]) - Delta[0, 1] * (Delta[1, 0] * Delta[2, 2] - Delta[1, 2] * Delta[2, 0]) + Delta[0, 2] * (Delta[1, 0] * Delta[2, 1] - Delta[1, 1] * Delta[2, 0] ))

            self.X3 = (Arreglo_X3[0,0]*((Arreglo_X3[1,1]*Arreglo_X3[2,2])-(Arreglo_X3[1,2]*Arreglo_X3[2,1]))-Arreglo_X3[0,1]*((Arreglo_X3[1,0]*Arreglo_X3[2,2])-(Arreglo_X3[1,2]*Arreglo_X3[2,0]))+Arreglo_X3[0,2]*((Arreglo_X3[1,0]*Arreglo_X3[2,1])-(Arreglo_X3[1,1]*Arreglo_X3[2,0])))/ (
                  Delta[0, 0] * (Delta[1, 1] * Delta[2, 2] - Delta[1, 2] * Delta[2, 1]) - Delta[0, 1] * (Delta[1, 0] * Delta[2, 2] - Delta[1, 2] * Delta[2, 0]) + Delta[0, 2] * (Delta[1, 0] * Delta[2, 1] - Delta[1, 1] * Delta[2, 0] ))

            return True
        except:

            print('EL DETERMINANTE DE LA MATRIZ ES CERO')
            print('ESTO DIGNIFICA QUE EL SISTEMA DE ECUACIONES LINEALES ES INCONSISTENTE O TIENE UN NUMERO DE SOLUCIONES ILIMITADO')
            return False

    def __ValidarDatos3x3(self):

        try:
            self.a_11 = int(self.a_11)
            self.a_12 = int(self.a_12)
            self.a_13 = int(self.a_13)
            self.a_21 = int(self.a_21)
            self.a_22 = int(self.a_22)
            self.a_23 = int(self.a_23)
            self.a_31 = int(self.a_31)
            self.a_32 = int(self.a_32)
            self.a_33 = int(self.a_33)
            self.b_1 = int(self.b_1)
            self.b_2 = int(self.b_2)
            self.b_3 = int(self.b_3)
            return True
        except:
            print("NO SE INGRESARON VALORES COHERENTES A LA INSTRUCCION")
            return False

class clsSistemaEcuacionLineal_2X2:
    def __init__(self,a_11,a_12,b_1,b_2,a_21,a_22,X1=None,X2=None):
        self.a_11=a_11
        self.a_12=a_12
        self.b_1=b_1
        self.b_2=b_2
        self.a_21=a_21
        self.a_22=a_22
        self.X1=X1
        self.X2=X2
        self.Error=""
    def Calcular_SistemaDeEcuacionesLineales2x2(self):
        if self.__ValidarDatos2x2():
            ArregloX1, ArregloX2, Delta = self.__ConvertirArreglo()
            if self.__Calcular_X1_y_X_2(ArregloX1, ArregloX2, Delta):
                return True
            else:
                return False
        else:
            return False


    def __ConvertirArreglo(self):
        ArregloX1 = [[self.b_1, self.a_12], [self.b_2, self.a_22]]
        ArregloX2 = [[self.a_11, self.b_1], [self.a_21, self.b_2]]
        Delta= [[self.a_11, self.a_12], [self.a_21, self.a_22]]
        Arreglo_X1 = np.array(ArregloX1)
        Arreglo_X2 = np.array(ArregloX2)
        Delta=np.array(Delta)
        return Arreglo_X1,Arreglo_X2,Delta



    def __Calcular_X1_y_X_2(self,ArregloX1,ArregloX2,Delta):
        try:

            if (Delta[0,0]*Delta[1,1]-Delta[1,0]*Delta[0,1])==0:
                print('EL DETERMINANTE DE LA MATRIZ ES CERO')
                print('ESTO DIGNIFICA QUE EL SISTEMA DE ECUACIONES LINEALES ES INCONSISTENTE O TIENE UN NUMERO DE SOLUCIONES ILIMITADO')
                print('===========================================================')
                return False
            self.X1= (ArregloX1[0,0]*ArregloX1[1,1]-ArregloX1[1,0]*ArregloX1[0,1])/(Delta[0,0]*Delta[1,1]-Delta[1,0]*Delta[0,1])
            self.X2= (ArregloX2[0,0]*ArregloX2[1,1]-ArregloX2[1,0]*ArregloX2[0,1])/(Delta[0,0]*Delta[1,1]-Delta[1,0]*Delta[0,1])

            return  True
        except:
            print('EL DETERMINANTE DE LA MATRIZ ES CERO')
            print('ESTO DIGNIFICA QUE EL SISTEMA DE ECUACIONES LINEALES ES INCONSISTENTE O TIENE UN NUMERO DE SOLUCIONES ILIMITADO')
            return False

    def __ValidarDatos2x2(self):
        try:
            self.a_11=int(self.a_11)
            self.a_12 = int(self.a_12)
            self.b_1 = int(self.b_1)
            self.b_2 = int(self.b_2)
            self.a_21 = int(self.a_21)
            self.a_22 = int(self.a_22)
            return True
        except:

            print("NO SE INGRESARON VALORES COHERENTES A LA INSTRUCCION")
            return False


class clsReglasDeCramer(clsSistemaEcuacionLineal_2X2,clsSistemaEcuacionLineal_3X3):

    def __init__(self,NumeroIncognita,listaArgumentos):
        self.NumeroIncognita = NumeroIncognita
        self.listaArgumentos = listaArgumentos
        self.Error=""

    def CalcularEcuacionLineal(self):
        if self.__Validar_Datos():
            if self.NumeroIncognita ==2:
                EcuacionLineal_2X2= clsSistemaEcuacionLineal_2X2(self.listaArgumentos[0],self.listaArgumentos[1],self.listaArgumentos[2],self.listaArgumentos[3],self.listaArgumentos[4],self.listaArgumentos[5])
                if EcuacionLineal_2X2.Calcular_SistemaDeEcuacionesLineales2x2():
                    print("PARA EL SISTEMA INGRESADO LA SOLUCION ES: ", "X1 = ", EcuacionLineal_2X2.X1, "X2 = ", EcuacionLineal_2X2.X2)
                    return True
                return False
            if self.NumeroIncognita ==3:
                EcuacionLineal_3X3 = clsSistemaEcuacionLineal_3X3(self.listaArgumentos[0], self.listaArgumentos[1],  self.listaArgumentos[2], self.listaArgumentos[3], self.listaArgumentos[4], self.listaArgumentos[5],self.listaArgumentos[6], self.listaArgumentos[7],  self.listaArgumentos[8], self.listaArgumentos[9], self.listaArgumentos[10], self.listaArgumentos[11])
                if EcuacionLineal_3X3.Calcular_SistemaDeEcuacionesLineales3x3():
                    print("PARA EL SISTEMA INGRESADO LA SOLUCION ES: ","X1 = ", EcuacionLineal_3X3.X1,"X2 = ", EcuacionLineal_3X3.X2,"X3 = ", EcuacionLineal_3X3.X3)
                    return  True
                return False
        else:
            return False

    def __Validar_Datos(self):
        try:

            if self.NumeroIncognita != "2" and self.NumeroIncognita != "3":
                self.Error = "SE INGRESARON DATOS INCOHERENTES REFERENTES AL NUMERO DE INCOGNITAS"
                return False
            self.NumeroIncognita = int(self.NumeroIncognita)

            return True
        except:

            self.Error = "NO SE INGRESARON VALORES COHERENTES A LA INSTRUCCION"
            return False

#-----------------------------------------------------------------------------------------------------------
class Taller_3(Circulo,Elipse,Parabola,Hiperbola,clsTemperaturas,clsReglasDeCramer):
    def __init__(self):
        self.opcion=None
        self.error=None

    def __punto_1(self):
        validarentrada = True

        while validarentrada:
            validarentrad_2 = True
            validarentrad_3 = True
            print('===========================================================')
            print('SELECCIONE EL OBJETO AL CUAL DESEA DESEA OBTENER Y ')
            print('1. CIRCULO,  2. ELIPSE, 3. PARABOLA, 4. HIPERBOLA ')
            self.opcion = input('R/= ')
            if self.opcion != '1' and self.opcion != '2' and self.opcion != '3' and self.opcion != '4':
                while validarentrad_2:
                    print('===========================================================')
                    print('NO SE DIGITARON DATOS COHERENTES A LA INSTRUCCION')
                    print('PORFAVOR ELIJA UNA OPCION')
                    opcion = input('1. VOLVER A SELECCIONAR UN OBJETO, 2. VOLVER AL MENU DE INICIO (R/= ')
                    if opcion == '1':
                        validarentrad_2 = False
                    if opcion == '2':
                        validarentrad_2 = False
                        validarentrada = False
            else:
                if self.opcion == '1':
                    print('===========================================================')
                    valor_inicial_x= input('INGRESE EL VALOR INICIA DEL ARREGLO ------> X  R/= ')
                    valor_final_x = input('INGRESE EL VALOR FINAL DEL ARREGLO ------> X  R/= ')
                    numero_puntos = input('INGRESE EL NUMERO DE PUNTOS DEL ARREGLO ------> X  R/= ')
                    h = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> H  R/= ')
                    k = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> K  R/= ')
                    r = input('INGRESE EL VALOR DEL RADIO ------>   R/= ')
                    circulo = Circulo(k, r, h)
                    if(circulo.calcular_Radio(valor_inicial_x,valor_final_x,numero_puntos)):
                        for i in range (len(circulo.y)):
                            print('==================================================')
                            print('EL VALOR DE Y = ', circulo.y[i], ' PARA EL VALOR DE X = ', circulo.Arreglo_x[i])
                        circulo.graficarplanocartesiano()
                if self.opcion == '2':
                    print('==================================================')
                    valor_inicial_x = input('INGRESE EL VALOR INICIA DEL ARREGLO ------> X  R/= ')
                    valor_final_x = input('INGRESE EL VALOR FINAL DEL ARREGLO ------> X  R/= ')
                    numero_puntos = input('INGRESE EL NUMERO DE PUNTOS DEL ARREGLO ------> X  R/= ')
                    h = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> H  R/= ')
                    k = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> K  R/= ')
                    a = input('INGRESE EL VALOR DEL REFERENTE A LA LONGITUD ------> A  R/= ')
                    b = input('INGRESE EL VALOR DEL REFERENTE A LA LONGITUD ------> B  R/= ')
                    elipse = Elipse(k, a, b, h)
                    if elipse.calcular_Elipse(valor_inicial_x,valor_final_x,numero_puntos):
                        for i in range (len(elipse.y)):
                            print('==================================================')
                            print('EL VALOR DE Y = ', elipse.y[i], ' PARA EL VALOR DE X = ', elipse.Arreglo_x[i])
                        elipse.graficarplanocartesiano()

                if self.opcion == '3':
                    print('==================================================')
                    valor_inicial_x = input('INGRESE EL VALOR INICIA DEL ARREGLO ------> X  R/= ')
                    valor_final_x = input('INGRESE EL VALOR FINAL DEL ARREGLO ------> X  R/= ')
                    numero_puntos = input('INGRESE EL NUMERO DE PUNTOS DEL ARREGLO ------> X  R/= ')
                    h = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> H  R/= ')
                    k = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> K  R/= ')
                    a = input('INGRESE EL VALOR DEL REFERENTE A LA LONGITUD ------> A  R/= ')
                    parabola = Parabola(k, a, h)
                    if parabola.calcular_Parabola(valor_inicial_x,valor_final_x,numero_puntos):
                        for i in range(len(parabola.y)):
                            print('==================================================')
                            print('EL VALOR DE Y = ', parabola.y[i], ' PARA EL VALOR DE X = ', parabola.Arreglo_x[i])
                        parabola.graficarplanocartesiano()


                if self.opcion == '4':
                    print('==================================================')
                    valor_inicial_x = input('INGRESE EL VALOR INICIA DEL ARREGLO ------> X  R/= ')
                    valor_final_x = input('INGRESE EL VALOR FINAL DEL ARREGLO ------> X  R/= ')
                    numero_puntos = input('INGRESE EL NUMERO DE PUNTOS DEL ARREGLO ------> X  R/= ')
                    h = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> H  R/= ')
                    k = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> K  R/= ')
                    a = input('INGRESE EL VALOR DEL REFERENTE A LA LONGITUD ------> A  R/= ')
                    b = input('INGRESE EL VALOR DEL REFERENTE A LA LONGITUD ------> B  R/= ')
                    hiperbola = Hiperbola(k, a, b, h)
                    if hiperbola.calcular_Hiperbola(valor_inicial_x,valor_final_x,numero_puntos):
                        for i in range(len(hiperbola.y)):
                            print('==================================================')
                            print('EL VALOR DE Y = ', hiperbola.y[i], ' PARA EL VALOR DE X = ', hiperbola.Arreglo_x[i])
                        hiperbola.graficarplanocartesiano()
                while validarentrad_3:
                    print('==================================================')
                    print('PORFAVOR ELIJA UNA OPCION')
                    opcion = input('1. VOLVER A SELECCIONAR UN OBJETO, 2. VOLVER AL MENU DE INICIO (R/= ')
                    if opcion == '1':
                        validarentrad_3 = False
                        validarentrada = True
                    if opcion == '2':
                        validarentrad_3 = False
                        validarentrada = False


    def __punto_2(self):

        validarentrada = True
    
        while validarentrada:
            validarrentra_2 = True
            print('============ARREGLOS CONVERSION TEMPERATUTAS================================')
            t_inicial = input('INGRESE LA T INICIAL EN °C:')
            t_final = input('INGRESE LA T FINAL EN °C:')
            t_resolucion = input('INGRESE LA RESOLUCION EN °C:')
            temperaturas = clsTemperaturas(t_inicial,t_final,t_resolucion)
            if temperaturas.convertirTemperatura():
                print('===========================================================')
                print('PROCESOS FINALIZADO DE FORMA EXITOSA!!!!!!')

    
            while validarrentra_2:
                print('==================================================')
                print('PORFAVOR ELIJA UNA OPCION')
                opcion = input('1. VOLVER A CONVERTIR TEMPERATURA, 2. VOLVER AL MENU DE INICIO (R/= ')
                if opcion == '1':
                     validarrentra_2 = False
                     validarentrada = True
                if opcion == '2':
                    validarrentra_2 = False
                    validarentrada = False


    def __punto_3(self):
        validarentrada = True

        while validarentrada:
            validarentrad_2 = True
            validarentrad_3 = True
            print('===========================================================')
            print('INGRESE EL NUMERO DE INCOGNITAS DE LA ECUACION ')
            print('2 INCOGNITAS  Ó  3 INCOGNITAS ')
            self.opcion = input('R/= ')
            if self.opcion != '2' and self.opcion != '3':
                while validarentrad_2:
                    print('===========================================================')
                    print('NO SE DIGITARON DATOS COHERENTES A LA INSTRUCCION')
                    print('PORFAVOR ELIJA UNA OPCION')
                    opcion = input('1. VOLVER A INGRESAR NUMERO DE INCOGNITAS, 2. VOLVER AL MENU DE INICIO (R/= ')
                    if opcion == '1':
                        validarentrad_2 = False
                    if opcion == '2':
                        validarentrad_2 = False
                        validarentrada = False
            else:
                if self.opcion == '2':
                    listcramer2x2=[]
                    print('===========================================================')
                    listcramer2x2.append(input('INGRESE EL VALOR DE A_11 R/= '))
                    listcramer2x2.append(input('INGRESE EL VALOR DE A_12 R/= '))
                    listcramer2x2.append(input('INGRESE EL VALOR DE b_1 R/= '))
                    listcramer2x2.append(input('INGRESE EL VALOR DE b_2 R/= '))
                    listcramer2x2.append(input('INGRESE EL VALOR DE A_21 R/= '))
                    listcramer2x2.append(input('INGRESE EL VALOR DE A_22 R/= '))
                    print('===========================================================')
                    reglacramer = clsReglasDeCramer(self.opcion, listcramer2x2)
                    if reglacramer.CalcularEcuacionLineal():
                        print('===========================================================')
                        print('PROCESOS FINALIZADO DE FORMA EXITOSA!!!!!!')
                        print('===========================================================')


                if self.opcion == '3':
                    listcramer3x3=[]
                    print('===========================================================')
                    listcramer3x3.append(input('INGRESE EL VALOR DE A_11 R/= '))
                    listcramer3x3.append(input('INGRESE EL VALOR DE A_12 R/= '))
                    listcramer3x3.append(input('INGRESE EL VALOR DE A_13 R/= '))
                    listcramer3x3.append(input('INGRESE EL VALOR DE A_21 R/= '))
                    listcramer3x3.append(input('INGRESE EL VALOR DE A_22 R/= '))
                    listcramer3x3.append(input('INGRESE EL VALOR DE A_23 R/= '))
                    listcramer3x3.append(input('INGRESE EL VALOR DE A_31 R/= '))
                    listcramer3x3.append(input('INGRESE EL VALOR DE A_32 R/= '))
                    listcramer3x3.append(input('INGRESE EL VALOR DE A_33 R/= '))
                    listcramer3x3.append(input('INGRESE EL VALOR DE b_1 R/= '))
                    listcramer3x3.append(input('INGRESE EL VALOR DE b_2 R/= '))
                    listcramer3x3.append(input('INGRESE EL VALOR DE b_3 R/= '))
                    print('===========================================================')
                    reglacramer = clsReglasDeCramer(self.opcion, listcramer3x3)
                    if reglacramer.CalcularEcuacionLineal():
                        print('===========================================================')
                        print('PROCESOS FINALIZADO DE FORMA EXITOSA!!!!!!')
                        print('===========================================================')
                while validarentrad_3:

                    print('PORFAVOR ELIJA UNA OPCION')
                    opcion = input('1. VOLVER A INGRESAR NUMERO DE INCOGNITAS, 2. VOLVER AL MENU DE INICIO (R/= ')
                    if opcion == '1':
                        validarentrad_3 = False
                        validarentrada = True
                    if opcion == '2':
                        validarentrad_3 = False
                        validarentrada = False



    def __recorrerpuntos(self):
        if self.opcion == '1':
            self.opcion=None
            self.__punto_1()
            self.opcion = None
            self.menu_inicio()
        if self.opcion == '2':
            self.opcion = None
            self.__punto_2()
            self.opcion = None
            self.menu_inicio()
        if self.opcion == '3':
            self.opcion = None
            self.__punto_3()
            self.opcion = None
            self.menu_inicio()
        if self.opcion == '4':
            print('==================================================')
            print('            FIN DE SESION !!!!!')
            quit()

    def __Validar_datos_entrada(self):
         validarentrada=True
         if self.opcion ==None:
            return False
         if self.opcion != '1' and  self.opcion != '2' and self.opcion != '3' and self.opcion != '4':
            while validarentrada:
                print('NO SE DIGITARON DATOS COHERENTES A LA INSTRUCCION')
                print('DESEA VOLVER AL MENU DE INICIO ?')
                opcion= input('1. SI, 2. NO  (R/= ')
                if opcion=='1':
                    return False
                if opcion=='2':
                    return True


    def menu_inicio(self):
        while self.__Validar_datos_entrada()==False:
            print('======================MENU DE USUARIO======================')
            print('SELECCIONE EL PUNTO DEL TALLER # 3 QUE DESEA REVISAR ')
            print('1. SECCIONES CONICAS')
            print('2. ARREGLOS DE CONVERSION DE TEMPERATURA ')
            print('3. REGLA DE CRAMER')
            print('4. SALIR')
            self.opcion=input('R/= ')

        self.__recorrerpuntos()


Taller_3= Taller_3()
Taller_3.menu_inicio()
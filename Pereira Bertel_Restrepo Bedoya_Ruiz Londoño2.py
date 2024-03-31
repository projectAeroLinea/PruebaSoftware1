"""                           TALLER # 2:
-----------------------------INTEGRANTES-----------------------------------
CC.1000758420------- Christian Camilo Pereira Bertel
CC.1000872160------ Kevin Alejandro Restrepo Bedoya
CC.1017274121------ Emmanuel Ruiz Londoño
"""

import math



#-------------------------CLASES DEL PUNTO #1---------------------------------------

class cls_FormulaSeries:

    def __init__(self,n):
        self.n=n


    def validardatos(self):
        try:
            self.n = int(self.n)
            if self.n>=0:
                return True
            else:
                print('EL DATO NO PUEDE SER NEGATIVO')
        except:
            print('INGRESO DATOS  INCOHERENTES A LA INSTRUCCION')
            return False

    def fibonacci(self):
        if self.validardatos():
            lista = [0, 1]
            for i in range(0, self.n - 1):
                lista.append(lista[-1] + lista[-2])
            print(lista)
            return True
        else:
            print('OCURRIO UN PROBLEMA DURANTE EL CALCULO DE LA SERIE')
            return False

    def factorial(self):
        if self.validardatos():
            x = 1
            f = 1
            while x <= self.n:
                f = f * x
                x += 1
            return True,self.n,f

        else:
            return False

#-------------------------CLASES DEL PUNTO #2---------------------------------------
class cls_EcuacionesGenericas:
    def __init__(self,x=None,y=None):
        self.x=x
        self.y=y



    def formulacirculo(self,k,r,h):
        try:
            self.y= math.sqrt((r**2)-((self.x-h)**2))+k
            radio= float(((self.x - h) ** 2) + ((self.y - k) ** 2))

            return radio
        except:
            return None


    def formula_elipse(self,k,a,b,h):
        try:
           self.y=math.sqrt((b**2)-((b**2)*(((self.x-h)**2)/a**2)))+k
           return float((((self.x - h) ** 2) / a ** 2) + (((self.y - k) ** 2) / b ** 2))

        except:
            return None

    def formulaparabola(self,k,a,h):
        try:
            self.y=a*((self.x-h)**2)+k
            return self.y
        except:
            return None


    def formulahiperbola(self,k,a,b,h):
        try:

            self.y=math.sqrt((b**2*(((self.x-h)**2)/a**2))-b**2)+k
            return int((((self.x - h) ** 2) / a ** 2) - (((self.y - k) ** 2) / b ** 2))
        except:
            return None


class Circulo(cls_EcuacionesGenericas):
    def __init__(self,k,r,h):
        self.k=k
        self.r=r
        self.h=h


    def calcular_Radio(self,x):
        if self.validar_datos(x):

            super().__init__(float(x))
            radio=super().formulacirculo(self.k,self.r,self.h)

            if round(radio) == self.r**2:
                return True
            else:
                return False
        else:
            return False
    def validar_datos(self,x):
       try:
           x=float(x)
           self.k= float(self.k)
           self.r= float(self.r)
           self.h= float(self.h)
           if self.r!=0:
               validarDominio_Y= self.r**2-(((x-self.h))**2)
               if validarDominio_Y >=0:
                   return True
               else:
                   print('===========================================================')
                   print('LOS VALORES INGRESADOS VIOLAN EL DOMINIO DE LA FUNCION')
                   return False

           else:
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

    def calcular_Elipse(self,x):
        if self.validardatos(x):
            super().__init__(float(x))
            resultado=super().formula_elipse(self.k, self.a, self.b,self.h)
            if round(resultado) ==1:

                return True
            else:
                return False
        else:
            return False

    def validardatos(self,x):
        try:
            x = float(x)
            self.k = float(self.k)
            self.a = float(self.a)
            self.b = float(self.b)
            self.h = float(self.h)

            if self.a != 0 and self.b != 0:
                if self.a > self.b:
                    validarDominio_Y = (self.b**2)-((self.b**2)*(((x-self.h)**2)/self.a**2))
                    if validarDominio_Y >= 0:
                        return True
                    else:
                        print('===========================================================')
                        print('LOS VALORES INGRESADOS VIOLAN EL DOMINIO DE LA FUNCION')

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




class Parabola(cls_EcuacionesGenericas):
    def __init__(self,k,a,h):
        self.h = h
        self.k = k
        self.a = a

    def calcular_Parabola(self,x):
        if self.validardatos(x):
            super().__init__(float(x))
            resultado= super().formulaparabola(self.k, self.a,self.h)
            if resultado !=None:
                return True
            else:
                return False
        else:
            return False

    def validardatos(self,x):
        try:
            x = float(x)
            self.k = float(self.k)
            self.a = float(self.a)
            self.h = float(self.h)

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

    def calcular_Hiperbola(self,x):
        if self.validardatos(x):
            super().__init__(float(x))
            resultado = super().formulahiperbola(self.k, self.a, self.b,self.h)
            if resultado == 1:
                return True
            else:
                return False
        else:
            return False


    def validardatos(self,x):
        try:
            x = float(x)
            self.h = float(self.h)
            self.k = float(self.k)
            self.a = float(self.a)
            self.b = float(self.b)


            if self.a!=0 and self.b!=0:
                if self.a > self.b:
                    validarDominio_Y=  ((self.b**2*(((x-self.h)**2)/self.a**2))-self.b**2)
                    if validarDominio_Y>=0:
                        return True
                    else:
                        print('===========================================================')
                        print('LOS VALORES INGRESADOS VIOLAN EL DOMINIO DE LA FUNCION')

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


#-------------------------------------------------------------------------------------
#-------------------------CLASES DEL PUNTO #3---------------------------------------
class clsPaciente:
    def __init__(self,id,talla, peso, edad, sexo):
        self.identificacion = id
        self.talla = talla
        self.peso = peso
        self.edad = edad
        self.sexo = sexo
        self.__imc = None

    def validardatos(self):
        try:

            self.talla = float(self.talla)
            self.peso = float(self.peso)
            self.edad= int(self.edad)
            if self.talla<=0 or self.peso <=0 or self.edad <0:
                print('INGRESO DATOS  INCOHERENTES A LA INSTRUCCION')
                return False
            if self.identificacion=='':
                print('NO INGRESO NUMERO DE IDENTIFICACION')
                return False
            if self.sexo!='1' and self.sexo!='2':
                print('ERROR: EL SEXO DEBE DE SER MASCULINO O FEMENINO')
                return False
            elif self.sexo=='1':
                self.sexo='MASCULINO'
            else:
                self.sexo='FEMENINO'

            return True

        except:
            print('INGRESO DATOS  INCOHERENTES A LA INSTRUCCION')
            return  False

    def __calcularIMC(self):

        if self.validardatos():
            self.__imc= self.peso / ((self.talla)/100)**2
            return True
        else:
            return False




    def imprimir(self):
        print('IDENTIFICACION = ', self.identificacion)
        print('TALLA = ', self.talla)
        print('PESO = ', self.peso)
        print('EDAD = ', self.edad)
        print('SEXO', self.sexo)
        print('IMC = ', self.__imc)


    def evaluar(self):
        if self.__calcularIMC():
            if self.__imc < 18.49:
                estadopaciente="Peso bajo"

            elif self.__imc >= 18.50 and self.__imc <= 24.99:
                estadopaciente="peso normal"

            elif self.__imc >= 25 and self.__imc <= 29.9:
                estadopaciente="Sobrepeso"

            elif self.__imc >= 30 and self.__imc <= 39.99:
                estadopaciente="Obesidad"

            elif self.__imc >= 40:
                estadopaciente="Obesidad extrema"
            print(estadopaciente)
            if estadopaciente != "peso normal":
                self.__remitir()
            else:
                self.__daralta()
            return True
        else:
            return False







    def __remitir(self):
            print("Será remitido con un médico tratante")


    def __daralta(self):

            print(f"Su imc es igual a: {self.__imc}, por lo tanto será dado de alta")





#-------------------------------------------------------------------------------------
class Taller_2(Circulo,Elipse,Parabola,Hiperbola,cls_FormulaSeries,clsPaciente):
    def __init__(self):
        self.opcion=None
        self.error=None

    def __punto_1(self):
        validarentrada = True

        while validarentrada:
            validarentrad_2 = True
            validarentrad_3 = True
            print('===========================================================')
            print('SELECCIONE LA ACCION QUE DESEA REALIZAR DEL PUNTO # 1')
            print('1. SUCESION DE FIBONACCI ,  2.  FACTORIAL DE UN NUMERO ')
            self.opcion = input('R/= ')
            if self.opcion != '1' and self.opcion != '2':
                while validarentrad_2:
                    print('===========================================================')
                    print('NO SE DIGITARON DATOS COHERENTES A LA INSTRUCCION')
                    print('PORFAVOR ELIJA UNA OPCION')
                    opcion = input('1. VOLVER A SELECCIONAR UNA SERIE, 2. VOLVER AL MENU DE INICIO (R/= ')
                    if opcion == '1':
                        validarentrad_2 = False
                    if opcion == '2':
                        validarentrad_2 = False
                        validarentrada = False
            else:
                if self.opcion == '1':
                    print('===========================================================')
                    n = input('INGRESE EL LIMITE DE SUCESION  R/= ')
                    fibonnaci= cls_FormulaSeries(n)
                    if fibonnaci.fibonacci():
                        print('===========================================================')
                        print('SERIE CALCULADA CON EXITO !!!!')

                if self.opcion == '2':
                    print('===========================================================')
                    n = input('INGRESE UN NUMERO PARA CALCULAR EL FACTORIAL:   R/= ')
                    factorial = cls_FormulaSeries(n)
                    resultado=factorial.factorial()
                    if resultado[0]:
                        print('===========================================================')
                        print("EJ FACTORIAL DE ", resultado[1], " ES ", resultado[2])
                        print('SERIE CALCULADA CON EXITO !!!!')
                while validarentrad_3:
                    print('==================================================')
                    print('PORFAVOR ELIJA UNA OPCION')
                    opcion = input('1. VOLVER A SELECCIONAR UNA SERIE, 2. VOLVER AL MENU DE INICIO (R/= ')
                    if opcion == '1':
                        validarentrad_3 = False
                        validarentrada = True
                    if opcion == '2':
                        validarentrad_3 = False
                        validarentrada = False





    def __punto_2(self):
        validarentrada=True

        while validarentrada:
            validarentrad_2 = True
            validarentrad_3= True
            print('===========================================================')
            print('SELECCIONE EL OBJETO AL CUAL DESEA DESEA OBTENER Y ')
            print('1. CIRCULO,  2. ELIPSE, 3. PARABOLA, 4. HIPERBOLA ')
            self.opcion= input('R/= ')
            if self.opcion != '1' and  self.opcion != '2' and self.opcion != '3' and self.opcion != '4':
                while validarentrad_2:
                    print('===========================================================')
                    print('NO SE DIGITARON DATOS COHERENTES A LA INSTRUCCION')
                    print('PORFAVOR ELIJA UNA OPCION')
                    opcion = input('1. VOLVER A SELECCIONAR UN OBJETO, 2. VOLVER AL MENU DE INICIO (R/= ')
                    if opcion == '1':
                        validarentrad_2=False
                    if opcion == '2':
                        validarentrad_2 = False
                        validarentrada= False
            else:
                if self.opcion=='1':
                   print('===========================================================')
                   x = input('INGRESE EL VALOR DE ------> X  R/= ')
                   h = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> H  R/= ')
                   k = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> K  R/= ')
                   r = input('INGRESE EL VALOR DEL RADIO ------>   R/= ')
                   circulo= Circulo(k,r,h)
                   if circulo.calcular_Radio(x):
                       print('==================================================')
                       print('EL VALOR DE Y = ',circulo.y,' PARA EL VALOR DE X = ', circulo.x)


                if self.opcion=='2':
                    print('==================================================')
                    x = input('INGRESE EL VALOR DE ------> X  R/= ')
                    h = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> H  R/= ')
                    k = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> K  R/= ')
                    a = input('INGRESE EL VALOR DEL REFERENTE A LA LONGITUD ------> A  R/= ')
                    b = input('INGRESE EL VALOR DEL REFERENTE A LA LONGITUD ------> B  R/= ')
                    elipse=Elipse(k,a,b,h)
                    if elipse.calcular_Elipse(x):
                        print('==================================================')
                        print('EL VALOR DE Y = ', elipse.y, ' PARA EL VALOR DE X = ', elipse.x)
                        elipse=None



                if self.opcion == '3':
                    print('==================================================')
                    x = input('INGRESE EL VALOR DE ------> X  R/= ')
                    h = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> H  R/= ')
                    k = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> K  R/= ')
                    a = input('INGRESE EL VALOR DEL REFERENTE A LA LONGITUD ------> A  R/= ')
                    parabola=Parabola(k,a,h)
                    if parabola.calcular_Parabola(x):
                        print('==================================================')
                        print('EL VALOR DE Y = ', parabola.y, ' PARA EL VALOR DE X = ', parabola.x)


                if self.opcion == '4':
                    print('==================================================')
                    x = input('INGRESE EL VALOR DE ------> X  R/= ')
                    h = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> H  R/= ')
                    k = input('INGRESE EL VALOR DEL CENTRO REFERENTE AL VALOR ------> K  R/= ')
                    a = input('INGRESE EL VALOR DEL REFERENTE A LA LONGITUD ------> A  R/= ')
                    b = input('INGRESE EL VALOR DEL REFERENTE A LA LONGITUD ------> B  R/= ')
                    hiperbola = Hiperbola(k, a, b,h)
                    if hiperbola.calcular_Hiperbola(x):
                        print('==================================================')
                        print('EL VALOR DE Y = ', hiperbola.y, ' PARA EL VALOR DE X = ', hiperbola.x)
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


    def __punto_3(self):
        validarentrada = True

        while validarentrada:
            validarrentra_2 = True
            print('============INGRESO PACIENTE ================================')
            id = input('INGRESE LA IDENTIFICACION DEL PACICENTE  R/= ')
            talla = input('INGRESE LA TALLA DEL PACICENTE EN CM  R/= ')
            peso = input('INGRESE EL PESO DEL PACICENTE  R/= ')
            edad = input('INGRESE LA EDAD DEL PACICENTE  R/= ')
            print('INGRESE EL SEXO DEL PACICENTE  R/= ')
            sexo = input('1. MASCULINO, 2. FEMENINO R/= ')
            Paciente=clsPaciente(id,talla,peso,edad,sexo)
            print('==================================================')
            if Paciente.evaluar():

                print('=============DATOS PERSONALES DEL PACIENTE=============')
                Paciente.imprimir()

            while validarrentra_2:
                print('==================================================')
                print('PORFAVOR ELIJA UNA OPCION')
                opcion = input('1. VOLVER A INGRESAR UN PACIENTE, 2. VOLVER AL MENU DE INICIO (R/= ')
                if opcion == '1':
                    validarrentra_2 = False
                    validarentrada = True
                if opcion == '2':
                    validarrentra_2 = False
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
            print('SELECCIONE EL PUNTO DEL LABORATORIO 2 QUE DESEA REVISAR ')
            print('1. USO DE PROGRAMACION FUNCIONAL IMPLEMENTADA A LOS DOS PRIMEROS EJERCICIOS DEL TALLER_1')
            print('2. SECCIONES CONICAS ')
            print('3. OBJETOS TIPO PASCIENTE')
            print('4. SALIR')
            self.opcion=input('R/= ')

        self.__recorrerpuntos()


Taller_2= Taller_2()
Taller_2.menu_inicio()
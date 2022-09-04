from ctypes.wintypes import HLOCAL
from submenu import Menu
from Modulos.funcionesMatemáticas import *
from Paquete1.funcionesCadena import *
from Paquete1.funcionesNumericas import *
import time 
import os


sub = Menu()

lista1 = ["1) Print de un 'Hola Mundo'", "2) Tipos de variables en Python", "3) Conversión de tipos de variables","4) Operaciones con números", "5) Concatenación","6) Cadenas", "7) Tuplas","8) Listas","9) Diccionarios","10) Ingreso de Datos por teclado", "11) Usos del If y Else","12) Funciones","13) Operadores Lógicos", "14) Operador ternario", "15) Función Range","16) Bucle For","17) If in","18) Factorial de un número","19) Bucle While","20) Break, Continue y Pass","21) Generadores","23) Excepciones","24) Lanzamiento de excepciones","25) Módulos en Python","26) Paquetes en Python","27 Programación Orientada a Objetos","28) Constructores de clase","29) Encapsulamiento de variables","30) Encapsulamiento de métodos","31) Métodos Get y Set","32) Método de clase __str__","33) Herencia en Python", "34) Sobreescribir un método de clase", "35) Principio de sustición","36) Herencia múltiple","37) Polimorfismo","38) Relaciones entre clases"]

alternativa = ""
while alternativa !=37: 
    os.system("cls")
    alternativa = sub.menu(lista1, "Menú de Opciones")
    os.system("cls")

    if alternativa == "1":
        print("Este es un print clásico en el mundo de la programación")
        print("Hola Mundo")
        time.sleep(2)
        os.system("cls")

    elif alternativa == "2":
        print("A continuación se mostrarán los distintos tipos de datos")
        string = "Martín Vélez"
        int = 19
        boolean = True
        float = 247.9
        print(""*1)
        print(string,": Es una cadena de caracteres\n", int,": Se trata de un entero\n", boolean,": Un valor booleano\n", float, ": Un número conformado por decimales\n")
        time.sleep(4)
        os.system("cls")

    elif alternativa == "3":
        
        lista2 = ["1) Concatenar", "2) Sumar", "3) De un Float a Int", "4) De String a Float", "5) Obtener la longitud de una variable string", "6) Para salir"]
        opc = ""
        while opc != 6:
            os.system("cls")
            opc = sub.menu(lista2, "Opciones a usar con los tipos de variables")
            os.system("cls")

            if opc == "1":
                a = "Hola, "
                b = "soy Marco"
                print(a + b, ":Esto es una concatenación.")
                time.sleep(2)
                os.system("cls")

            elif opc == "2":
                sum = 5+8
                print("La suma de 5 + 8 es igual a = {}".format(sum))
                time.sleep(2)
                os.system("cls")

            elif opc == "3":
                num = 145.7
                print("Inicialmente, el número es: {}".format(num))
                print("Y convirtiendo al mismo en un entero, quedaría como: {}".format(int(num)))
                time.sleep(4)
                os.system("cls")

            elif opc == "4":
                var = "45.7"
                nuevoDat = float(var)
                print(nuevoDat, type(nuevoDat))
                time.sleep(3)
                os.system("cls")
            
            elif opc == "5":
                long = " 'Hola muy buenas' "
                print("La frase: ",long, "tiene una longitud de: ",len(long)," caracteres")
                time.sleep(3)
                os.system("cls")

    elif alternativa == "4":
        num = 8
        num2 = 9 
        print("De los números ",num,"y", num2,"tenemos las siguientes operaciones:")
        sum = num + num2
        print("La suma es: ",sum)

        res = num - num2
        print("La resta es: ",res)

        mul = num * num2
        print("La multiplicación es: ",mul)
        
        div = num / num2
        print("La división es: ",div)

        divex = num // num2
        print("La división exacta es: ",divex)
        
        pot = num ** num2 
        print("Teniendo como base ",num,"y", num2,"como exponente, tenemos: ", pot)
        time.sleep(10)
        os.system("cls")

    elif alternativa == "5":
        text1 = "Hola"
        text2 = "Mundo"
        textoFinal = text1 + " " + text2

        print(textoFinal)

        print("El saludo es: %s %s " % (text1,text2))

        saludoFinal = "Saludo: {} {}".format(text1,text2)
        print(saludoFinal)

        SaludoXpos = "Saludo {x} {y}".format(x=text1, y=text2)
        print(SaludoXpos)
        time.sleep(3)
    
    elif alternativa == "6":
        textExam = "IShowSpeed HOODIE"
        print("Del siguiente texto ",textExam,"se puede mostrar como:")

        print("Todo minúscula: ",textExam.lower())
        print("Todo mayúscula: ",textExam.upper())
        print("Título: ",textExam.title())
        print("La posición es: ",textExam.find("Sp"))
        print("La cantidad de veces que se encuentre la 'o' dentro de la frase es: ",textExam.count("o"))
        mostrar = textExam.replace("o","a")
        print("Reemplazando cosas en la frase: ",mostrar)
        print(textExam.isnumeric())
        arra = textExam.split(" ")
        print("El array de la oración es: ",arra)
        time.sleep(6)
        os.system("cls")

    elif alternativa == "7":
        tupl = (1,2,3)
        print("Una tupla normal es: ",tupl)
        tupl2 = (3, "Armando", True, 405.70, 16+7j)
        print("Y también puede contener valores especiales",tupl2)
        tupl3 = (1, 3, 2, 3, tupl2)
        print("Adicionalmente, también puede existir una tupla dentro de otra tupla",tupl3)
        print("Accediendo a la posición 1 de la nuestra segunda tupla, se devuelve: ",tupl2[1])
        print("El último valor de la tupla 2 es: ",tupl2[-1])
        print("Haciendo un recorrido de la posición 1 hasta la 4 se muestra: ",tupl2[0:4])
        tuplfinal = tupl2+tupl3
        print("Concatenando tuplas quedaría: ",tuplfinal)
        print("El número de coincidencias del número 3 en la tupla 3, es de: ", tupl3)
        time.sleep(15)
        os.system("cls")
    
    elif alternativa == "8":
        list1 = ["Oscar",325,54.7, True, "Salazar"]
        print(list1)
        print("La posición 2 de la lista es: ",list1)
        print("El último elemento de la fila es: ",list1[-1])
        new = list1[0:4]
        print("Una porción de la lista es: ",new)
        new1 = list1[3:]
        print("Desde la posición 3 hacia adelante, tenemos: ",new1)
        list1.append("HOLA MUNDO")
        print("También se pueden añadir valores a la lista, teniendo como nuevo resultado: ",list1)
        list1.insert(0,"Región")
        print("Insertando nuevos valores, la lista quedaría: ",list1)
        print(" ")
        list2=[1,2,3,4]
        list3=[5,6,7,8]
        list2.extend([5,6,7,8])
        print("Incluso se pueden extender las listas, teniendo como resultado: ",list2)
    
        print("La posición del nombre Oscar es: ",list1.index("Oscar"))
        newlis = list1.remove("Oscar")
        print("Eliminando el elmento Oscar de la lista, se tiene: ",list1)
        el = list1.pop
        print("Eliminando el último elemento de la lista con la función pop tenemos: ",el)

        nuevalist = list2+list3
        print(nuevalist)

        compr = "5" in list1
        print("¿El número 5 se encuentra en la primera lista?", compr)

        time.sleep(20)
        os.system("cls")
    
    elif alternativa == "9": 
        dic = {"Ecuador": "Quito", "Perú": "Lima", "Alemania":"Berlín"}
        print(" Diccionario |La capital del Ecuador es: ",dic["Ecuador"])
    
        print(" ")
        dic["Venezuela"]="Caracas"
        print(" Añadiendo un nuevo valor  |Se añadió un nuevo país junto con su capital: ",dic)

        print(" ")
        dic["Ecuador"] = "Colombia"
        print(" Cambio de valor |Reemplazando el valor perteneciente a la clave 'Ecuador', obtenemos el siguiente diccionario: ",dic)

        print(" ")
        del dic["Ecuador"]
        print(" Método 'del' |Eliminando la clave 'Ecuador', tenemos el siguiente diccionario: ",dic)
        
        print(" ")
        dic2 = {"Garcia": "Oscar", 25: True, "Sueldo": 150.80}
        print("Valor perteneciente a una clave | ",dic2[25])

        print(" ")
        llaves = ("España","Francia","Inglaterra")
        diccionParis = {llaves[0]: "Madrid", llaves[1]:"París" , llaves[2]: "Londres"}
        print(" Asignar valores a una clave mediante una tupla |",diccionParis)

        print(" ")
        datosPersonales = {"Ape":"Garcia", "Anios":{1:2019, 2:2020, 3:2021, 4:2022}}
        print(" Diccionario dentro de otro |",datosPersonales)

        print(" ")
        print ("Método get en un Diccionario |",datosPersonales.get("Ape","Oscar"))

        print(" ")
        print("Devuelve las claves de nuestro diccionario |",datosPersonales.keys())

        print(" ")
        print("Muestra los valores que hay en el diccionario |",datosPersonales.values())

        print(" ")
        valores = list(datosPersonales.values())
        print("Devuelve los valores dentro de una lista: ",valores)

        valores1 = tuple(datosPersonales.values())
        print("Devuelve los valores dentro de una tupla", valores1)
        time.sleep(12)
        os.system("cls")
    
    elif alternativa == "10":
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        sueldo = float(input("Ingrese su sueldo: "))

        os.system("cls")
        print("Hola, "+nombre)
        edadFutura = edad + 20
        print("Y tu edad es: ",edad, "y tu edad dentro de 20 años es: ",edadFutura)
        print("Con un sueldo de: ",sueldo)
        time.sleep(5)
        os.system("cls")
    
    elif alternativa == "11":
        edad = int(input("Ingrese su edad: "))

        if edad > 18:
            print("Usted es mayor de edad.")
            time.sleep(2)
            os.system("cls")
        elif edad == 18:
            print("Tu edad es de 18 años")
            time.sleep(2)
            os.system("cls")
        else: 
            print("Usted es menor de edad.")
            time.sleep(2)
            os.system("cls")
    
    elif alternativa == "12":
        
        def evaluarSueldo(sueldo):
            if sueldo >= 850:
                print("Cuidado te toca pagar impuestos, ojo")
                time.sleep(2)
                os.system("cls")
            
            else: 
                print("Ganas menos que el sueldo mínimo")
                time.sleep(2)
                os.system("cls")
    
    elif alternativa == "13":
        if (5>3) and (8<15):
            print("Es una afirmación cierta")
            time.sleep(2)
            os.system("cls")
        
        else:
            print("Es una falacia")
    
    elif alternativa == "14":
        sexos = ("Hombre","Mujer")

        posicion = True
        sexo = sexos[posicion] 
        print(sexo)
        time.sleep(2)
        os.system("cls")

        sexo = sexos[not posicion]
        print(sexo)
        time.sleep(2)
        os.system("cls")
    
    elif alternativa == "15":
        numeros = range(4, 10)
        print(numeros[5])
        time.sleep(1)
        os.system("cls")

        numeros1 = range(10,100,8)
        print(numeros1[9])
        time.sleep(1)
        os.system("cls")

    elif alternativa == "16":
        for i in range(1,13):
            print("{} x {} es: {}".format(i,i,(i*i)))
        time.sleep(2)
        os.system("cls")

        for nom in["Karen","Oscar","Héctor","Leonardo"]:
            print("Cantidad de letras de {} es: {}".format(nom,len(nom)))
        time.sleep(4)
        os.system("cls")
    
    elif alternativa == "17":
        print("-"*8,"Curso","-"*8)
        print("Matemática - Biología - Lenguaje -Ciencias")
        curso = input("Ingrese el curso que desea ver: ")

        lis = ["Matemáticas", "Biología", "Lenguaje", "Ciencias"]
        
        if curso in lis:
            print("Su curso seleccionado '{}' está disponible".format(curso))
            time.sleep(2)
            os.system("cls")
        else: 
            print("No es un curso existente")
            time.sleep(2)
            os.system("cls")

    elif alternativa == "18":
        numero = int(input("Ingrese un número: "))

        factorial = 1
        for n in range (1, (numero + 1)):
            factorial *= n

        print("El factorial de {} es: {}".format(numero,factorial))
        time.sleep(2)
        os.system("cls")

    elif alternativa == "19":
        valor = 1
        while valor < 10:
            print("El número actual es: {}".format(valor))
            valor +=1

        print("Programa finalizado")
        time.sleep(3)
        os.system("cls")

        valor1 = 5
        while valor1 < 50:
            print("El número actual es: {}".format(valor1))
            valor1 +=8 
        
        print("Programa finalizado")
        time.sleep(3)
        os.system("cls")

    elif alternativa == "20":
        print("---Uso del Break---")
        for numero in range(1,6):
            if numero == 3:
                break
            print("El número actual es: {}".format(numero))
        print("Bucle finalizado")
        time.sleep(3)
        os.system("cls")

        print("---Uso del Continue---")
        for numero in range(1,6):
            if numero == 3:
                continue
            print("El número actual es: {}".format(numero))
        print("El bucle ha finalizado")
        time.sleep(3)
        os.system("cls")

        print("---Uso del Pass---")
        for numero in range(1,6):
            if numero <= 3:
                pass
            else:
                print("El número es mayor a 3 ")

            print("El número actual es: {}".format(numero))
        print("Bucle finalizado")
        time.sleep(3)
        os.system("cls")
        
    elif alternativa == "21":
        def multiDe7 (limite):
            numero = 1
            listNum = []
            
            while numero <= limite:
                listNum.append(numero*7)
                numero += 1
            return listNum 
        print("-"*10,"Múltiplos de 7","-"*10)
        print(multiDe7(10))
        time.sleep(3)
        os.system("cls")

        def geneMulti7(limite):
            numero = 1
            while numero <= limite:
                yield numero * 7
                numero = numero + 1
        obtienevalor = geneMulti7(10)
        print("-"*10,"Múltiplos de 7 mediante yield","-"*10)
        print(next(obtienevalor))
        print("Su siguiente número es: ")
        print(next(obtienevalor))
        print("Su siguiente número es: ")
        print(next(obtienevalor))
        time.sleep(3)
        os.system("cls")

    elif alternativa == "22":

        def devuelveLenguaje(*Lenguajes):
            for leng in Lenguajes:
                yield from leng
        
        lenguajesObt = devuelveLenguaje("Python","Java","PHP","Ruby","JavaScript")
        print(next(lenguajesObt))
        print(next(lenguajesObt))
        time.sleep(3)
        os.system("cls")
    elif alternativa == "23":
        numero1 = 20
        numero2 = 0
        
        try:
            print("La visión de {} entre {} es: {}".format(numero1,numero2,(numero1/numero2)))
            time.sleep(2)
            
        except ZeroDivisionError:
            print("No se puede dividir entre 0.")
            time.sleep(2)
            os.system("cls")

        finally:
            print("El programa ha finalizado")
            time.sleep(2)
            os.system("cls")
    
    elif alternativa == "24":
        
        def evaluarNota (nota):
            if nota < 0:
                raise ZeroDivisionError("No se permiten valores negativos.")
            
            elif nota >= 16:
                print("Tienes una excelente nota")
                time.sleep(1)
                os.system("cls")
            elif nota >= 11:
                print("Aprobado")
                time.sleep(1)
                os.system("cls")
            else: 
                print("Reprobado")
                time.sleep(1)
                os.system("cls")

        evaluarNota(int(input("Registre la nota de la materia: ")))

    elif alternativa == "25":
        valor2 = int(input("Ingrese su primer valor: "))
        valor3 = int(input("Ingrese su segundo valor: "))

        sum = sumar(valor2,valor3)
        print("La suma de esos valores son: ",sum)
        
        mul = multiplicar(valor2,valor3)
        print("Y la multiplicación es: ",mul)

        time.sleep(3)
        os.system("cls")
    
    elif alternativa == "26":
        n1 = int(input("Digite un número: "))
        n2 = int(input("Digite un segundo número: "))

        multip = multi(n1,n2)
        print("El resultado de la multiplicación es: ",multip)
        time.sleep(2)
        os.system("cls")


        resul = contarLetras("HolaMundo")
        print("La palabra 'HolaMundo' tiene: ",resul,"letras.")
        time.sleep(2)
        os.system("cls")

    elif alternativa == "27":
        class Persona():
            apellidos = ""
            nombres = ""
            edad = 0
            despierta = False

            def despertar(self):
                self.despierta = True
                print("Buenos días")

        persona1 = Persona()
        persona1.apellidos = "Garcia Fuentes"
        print(persona1.apellidos)
        persona1.despertar()
        time.sleep(3)

        persona2 = Persona()
        persona2.apellidos = "Armando Paredes"
        print(persona1.apellidos)
        time.sleep(3)

    elif alternativa == "28":
        class Curso():

            def __init__(self,nom,cre,pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro

        cur = Curso("Matemáticas",5,"Ingeniería civil")
        print(cur.nombre)
        time.sleep(2)

    elif alternativa == "29":
        class Curso():

            def __init__(self,nom,cre,pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "Virtual"

            def mostrarDatos(self):
                dat = "Nombre: {} / Créditos: {} / Modo de impartición: {}"
                print(dat.format(self.nombre,self.creditos,self.__imparticion))
                
                

        cur = Curso("Matemáticas",5,"Ingeniería civil")
        cur.mostrarDatos()
        time.sleep(2)

    elif alternativa == "30":
        class Curso():

            def __init__(self,nom,cre,pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "Virtual"

            def mostrarDatos(self):
                dat = "Nombre: {} / Créditos: {} / Modo de impartición: {}"
                print(dat.format(self.nombre,self.creditos,self.__imparticion))
                docenteAsig = self.__verificarDocente()
                if docenteAsig: 
                    print("Existe el docente")
                    time.sleep(2)
                    os.system("cls")
                else: 
                    print("No es necesario asignar un docente")

            def __verificarDocente(self):
                print("Verificando si existe un docente asignado")
                if self.__imparticion == "Presencial":
                    return True
                else:
                    return False

        curso = Curso("Matemáticas",5,"Ingeniería civil")
        curso.mostrarDatos()
        time.sleep(3)

    elif alternativa == "31":
            class Cuenta():
                def __init__(self, pro, sal, mon):
                    self.__propietario = pro 
                    self.__saldo = sal 
                    self.__moneda = mon
                
                # Getters (Método Get)
                def get_saldo(self):
                    return self.__saldo
                def get_propietario(self):
                    return self.__propietario
                def get_moneda(self):
                    return self.__moneda   
                    
                # Setters (Método set)
                def set_moneda(self,moneda):
                    self.__moneda = moneda

            cuenta1 = Cuenta("Martín Vélez","150","Dólares")

            print(cuenta1.get_saldo())
            print(cuenta1.get_moneda())
            cuenta1.set_moneda("Soles")
            print(cuenta1.get_moneda())
            time.sleep(4)

    elif alternativa == "32":
        class Curso():

            def __init__(self,nom,cre,pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "Virtual"

            def mostrarDatos(self):
                dat = "Nombre: {} / Créditos: {} / Modo de impartición: {}"
                print(dat.format(self.nombre,self.creditos,self.__imparticion))
                docenteAsig = self.__verificarDocente()
                if docenteAsig: 
                    print("Existe el docente")
                    time.sleep(2)
                    os.system("cls")
                else: 
                    print("No es necesario asignar un docente")

            def __verificarDocente(self):
                print("Verificando si existe un docente asignado")
                if self.__imparticion == "Presencial":
                    return True
                else:
                    return False

            def __str__(self):
                texto = "Nombre: {} Créditos {}"
                return texto.format(self.nombre, self.creditos)
                    
        curso = Curso("Matemáticas",5,"Ingeniería civil")
        print("Método __str__")
        print(curso)
        curso.mostrarDatos()
        time.sleep(3)

    elif alternativa == "33":
        class Persona():
            def __init__(self,apePat,apeMat,nom):
                self.apellidoPaterno = apePat
                self.nomrbreMaterno = apeMat
                self.nombres = nom
        
            def mostrarNombre(self):
                txt = "{} {},{}"
                return txt.format(self.apellidoPaterno,self.nomrbreMaterno,self.nombres)

        class Estudiante(Persona):
            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

        estu = Estudiante("Vélez","Segarra","Martín","Ingeniero Civil")
        print(estu.mostrarNombre())
        print(estu.profesion)
        time.sleep(3)
             
    elif alternativa == "34":

        class Persona():
            def __init__(self,apePat,apeMat,nom):
                self.apellidoPaterno = apePat
                self.nomrbreMaterno = apeMat
                self.nombres = nom
        
            def mostrarNombre(self):
                txt = "{} {},{}"
                return txt.format(self.apellidoPaterno,self.nomrbreMaterno,self.nombres)

            def datos(self):
                print(self.mostrarNombre())


        class Estudiante(Persona):
            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

            def datos(self):
                super().datos()
                print("La profesión es: {}".format(self.profesion))

        estu = Estudiante("Vélez","Segarra","Martín","Ingeniero Civil")
        estu.datos()
        time.sleep(3)

    elif alternativa == "35":
        class Persona():
            def __init__(self,apePat,apeMat,nom):
                self.apellidoPaterno = apePat
                self.nomrbreMaterno = apeMat
                self.nombres = nom
        
            def mostrarNombre(self):
                txt = "{} {},{}"
                return txt.format(self.apellidoPaterno,self.nomrbreMaterno,self.nombres)

            def datos(self):
                print(self.mostrarNombre())


        class Estudiante(Persona):
            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

            def datos(self):
                super().datos()
                print("La profesión es: {}".format(self.profesion))

        # estu = Estudiante("Vélez","Segarra","Martín","Ingeniero Civil")
        per = Persona("Vélez","Segarra","Martín")
        # estu.datos()
        # print("¿Es el objeto 'estu' instancia de la clase Estudiante?")
        # print(isinstance(estu, Estudiante))
        # print("¿Es el objeto 'estu' instancia de la clase Persona?")
        # print(isinstance(estu,Persona))
        print("¿Es el objeto 'per' instancia de la clase Estudiante?")
        print(isinstance(per,Estudiante))
        time.sleep(3)

    elif alternativa == "36":

        class ClaseA():
            def __init__(self,par1,par2):
                self.parame = par1
                self.parame2 = par2

            def mostrar(self):
                print(self.parame + self.parame2) 
        
        class ClaseB():
            def __init__(self, par3, par4, par5):
                self.parame3 = par3
                self.parame4 = par4
                self.parame5 = par5

        class ClaseX(ClaseA, ClaseB):
            pass

        cX1 = ClaseX(25,9)
        cX1.mostrar()
        time.sleep(2)

    elif alternativa == "37":
        class Estudiante():
            def describir(self):
                print("Soy un buen estudiante")

        class Profesor():
            def describir(self):
                print("Amo mi trabajo")
 
        class Trabajador():
            def describir(self):
                print("Laburo las 8 horas")

        def definirPersona(persona):
            persona.mostrar()

        pers = Trabajador()
        definirPersona(pers)

        time.sleep(4)

    elif alternativa == "38":
        class País():
            def __init__(self,nom, presi):
                self.nombre = nom
                self.presidente = presi

            def __str__(self):
                txt = "País {} - Presidente{}"
                return txt.format(self.nombre, self.presidente)

        class Ciudad():
            def __init__(self, nomb, habit, pai):
                self.nombre = nomb
                self.habit = habit 
                self.pais = pai
            
            def __str__(self):
                txt = "Ciudad: {} - N° Habitantes: {} ({})"
                return txt.format(self.nombre, self.habit, self.pais)
        
        
        class Urbanización():
            def __init__(self, nom, ciu):
                self.nombre = nom
                self.ciudad = ciu

            def __str__(self):
                txt = "Urbanización '{}' ({})"
                return txt.format(self.nombre, self.ciudad)

        pais1 = País("Ecuador", "Guillermo Lasso") 
        # print(pais1)

        ciu = Ciudad("Milagro", 78000, pais1)
        # print(ciu)
        
        urb = Urbanización("100 camas", ciu)
        print(urb)
        time.sleep(2)
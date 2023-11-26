class Herramientas:
    def __init__(self, awayList):
        if (type(awayList) != list):
            self.myList = []
            raise ValueError('Se ha creado una lista vacia, por favor ingresar un valor de tipo lista.')
        else:
            self.myList = awayList

    #--------------------------------------------------
    def listPrimo(self):
        primoList = []
        for value in self.myList:
            primoList.append(self.__Primo(value))
        return primoList

    def __Primo(self, num):
        if num < 2:
            return False
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
    
    #----------------------------------------------------
    def listRepetidos(self):
        return self.__Repetidos(self.myList)

    def __Repetidos(self, lista):
        dictNum = {}
        #Aqui se almacenan cuantas veces se repiten los valores.
        for key in lista:
            if key in dictNum:
                dictNum[key] += 1
            else:
                dictNum[key] = 1
        #Convertimos las claves a valores a las listas
        keysLista = list(dictNum.keys())
        valuesLista = list(dictNum.values())
        #Establecemos como maximo el primer valor
        moda = keysLista[0]
        maximo = valuesLista[0]
        #Aqui buscamos cual es el que más se repite
        for i, element in enumerate(valuesLista):
            if element > maximo:
                moda = keysLista[i]
                maximo = element
        return moda, maximo
    
    #--------------------------------------------------------------
    def listConversorTemperatura(self, origen, destino):
        valorEsperado = ['Celsius', 'Fahrenheit', 'Kelvin']
        listConversion = []
        if str(origen) not in valorEsperado and str(destino) not in valorEsperado:
            print(f'Origen y Destino ingresado invalido, se esperaba {valorEsperado}')
            return listConversion
        elif str(origen) not in valorEsperado:
            print(f'Origen ingresado invalido, se esperaba {valorEsperado}')
            return listConversion
        elif str(destino) not in valorEsperado:
            print(f'Destino ingresado invalido, se esperaba {valorEsperado}')
            return listConversion
        else:
            for value in self.myList:
                listConversion.append([value, self.__ConversorTemperatura(value, origen, destino)])
            return listConversion

    def __ConversorTemperatura(self, valor, origen, destino):
        temp = 0
        if origen == 'Celsius':
            if destino == 'Fahrenheit':
                temp = 32 + (valor * 9/5)
            elif destino == 'Kelvin':
                temp = 273.15 + valor
            else:
                return 'Destino ingresado incorrecto -> ' + destino
        elif origen == 'Fahrenheit':
            if destino == 'Celsius':
                temp = 5/9 * (valor - 32)
            elif destino == 'Kelvin':
                temp = 273.15 + 5/9 * (valor - 32)
            else:
                return 'Destino ingresado incorrecto - > ' + destino
        elif origen == 'Kelvin':
            if destino == 'Celsius':
                temp = valor - 273.15
            elif destino == 'Fahrenheit':
                temp = 32 + 9/5 * (valor - 273.15)
            else:
                return 'Destino ingresado incorrecto -> ' + destino
        else:
            return 'Origen ingresado incorrecto -> ' + origen
        return round(temp, 3)
    
    #-------------------------------------------------------
    def listFactorial(self):
        factorialList = []
        for value in self.myList:
            factorialList.append(self.__Factorial(value))
        return factorialList

    def __Factorial(self, num):
        if type(num) == int:
            if num < 0:
                return None #El número debe ser positivo.
            else:
                if num == 0:
                    return 1
                else:
                    num *= self.__Factorial(num - 1)
            return num
        else:
            return None #El valor ingresado debe ser de tipo entero.
class Utilidades:
    def __init__(self, lista):
        self.lista = lista

    #--------------------------------------------------
    def listPrimo(self):
        for value in self.lista:
            print(self.__Primo(value))

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
        print(self.__Repetidos(self.lista))
        
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
    def listConversorTemperatura(self):
        for value in self.lista:
            print(f'{value} de Celsius a Kelvin -> {self.__ConversorTemperatura(value, 'Celsius', 'Kelvin')}')

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
        for value in self.lista:
            print(f'{value}! -> {self.__Factorial(value)}')

    def __Factorial(self, num):
        if type(num) == int:
            if num < 0:
                return 'El número debe ser positivo.'
            else:
                if num == 0:
                    return 1
                else:
                    num *= self.__Factorial(num - 1)
            return num
        else:
            return 'El valor ingresado debe ser de tipo entero.'
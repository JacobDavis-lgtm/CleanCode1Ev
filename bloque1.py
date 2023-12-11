
#region NombresConSentido

#MAL: el nombre de la funcion no tiene sentido, y los nombres de las variables no indican lo que son
        def funcionNumeros():
            i = 2
            b = 3
            return i + b

#BIEN: El nombre de la funcion deja claro lo que hace, y los nombres de las variables tienen sentido.
        def sumaNumeros():
            numeroUno = 2
            numeroDos = 3
            return numeroUno + numeroDos

#endregion NombresConSentido

#region NombresPronunciables

#MAL: Los nombres de las cosas no se pueden pronunciar bien
        def nmbrsPrncbls():
            cdna = 'Hola que tal'
            return cdna

#BIEN: Los nombres son claros y se pueden pronunciar
        def nombresPronunciables():
            cadena = 'Hola que tal'
            return cadena

#endregion NombresPronunciables

#region NombresBuscables

#MAL: El maximo esta puesto como 10 en vez de ser una constante
        def nombresNoBuscables():
            numeroElegido = input('Elige un numero')
            if (numeroElegido < 10):
                print('Tu numero es menor a 10')
            else:
                print('Tu numero es mayor que 10')


#BIEN: He extraido NUM_MAX a una constante en vez de poner 10 directamente
        NUM_MAX = 10
        def nombresBuscables():
            numeroElegido = input('Elige un numero')
            if (numeroElegido < NUM_MAX):
                print('Tu numero es menor a 10')
            else:
                print('Tu numero es mayor que 10')

#endregion NombresBuscables

#region Nombres de Clases

#MAL: Este ejemplo esta fatal. El nombre de la funcion no tiene verbo ni nada, y los nombres de las variables son horribles con un verbo.
        def numeroMasNumero():
            introduceNumero1 = input('Introduce el primer Numero')
            introduceNumero2 = input('Introduce el segundo Numero')

            return introduceNumero1 + introduceNumero2

#BIEN: En este ejemplo el nombre de la funcion es una accion, y las variables tienen nombres normales y claras
        def sumarNumeros():
            numero1 = input('Introduce el primer Numero')
            numero2 = input('Introduce el segundo Numero')

            return numero1 + numero2



#endregion Nombres de Clases

#region Elegir Una Palabra


#MAL: Estas dos funciones hacen algo muy similar pero uno esta usando de nombre la palabra calculadora y la otra operador
        def calculadoraSuma():
            numero1 = input('Introduce el primer Numero')
            numero2 = input('Introduce el segundo Numero')

            return numero1 + numero2

        def operadorResta():
            numero1 = input('Introduce el primer Numero')
            numero2 = input('Introduce el segundo Numero')

            return numero1 - numero2

#BIEN: Como las dos funciones hacen casi lo mismo lo unico que cambia es que uno suma y el otro resta, usamos la palabra calculadora para los dos

        def calculadoraSuma():
            numero1 = input('Introduce el primer Numero')
            numero2 = input('Introduce el segundo Numero')

            return numero1 + numero2

        def calculadoraResta():
            numero1 = input('Introduce el primer Numero')
            numero2 = input('Introduce el segundo Numero')

            return numero1 - numero2


#endregion Elegir una Palabra
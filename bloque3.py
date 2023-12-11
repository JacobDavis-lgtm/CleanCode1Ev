#region Los comentarios Mienten, Codigo autoexplicativo

#MAL: Al usar a y b como nombres de dos numeros, se ve la necesidad de poner mucho comentario para
# que se entienda. Eso es lo que queremos evitar.

        def suma(a, b):
            """
            Esta función recibe dos números y devuelve su suma.

            Args:
            a: El primer número.
            b: El segundo número.

            Returns:
            La suma de los dos números.
            """
            # Se suma a y b
            resultado = a + b

            # Se devuelve el resultado de la suma
            return resultado

#BIEN: Esta funcion se entiende perfectamente sin comentarios, por usar nombres un poco mas claros

        def suma(numero1, numero2)

            resultado = numero1 + numero2

            return resultado


#endregion

#region Los comentarios dicen que hace el codigo no como

#MAL: El comentario encima de la funcion esta explicando exactamente como funciona la funcion

        #esta funcion consigue el resultado de una operacion cogiendo los dos numeros como parametros,
        # guardando el resultado en una variable, y devolviendo esa variable
        def suma(numero1, numero2)
            resultado = numero1 + numero2
            return resultado

#BIEN: El comentario de la funcion explica el objetivo de la funcion solamente

        #Esta funcion devuelve el resultado de una suma entre dos numeros
        def suma(numero1, numero2)
            resultado = numero1 + numero2
            return resultado

#endregion
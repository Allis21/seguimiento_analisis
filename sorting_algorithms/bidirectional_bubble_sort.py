"""
Bidirectional Bubble Sort (Cocktail Sort) para Strings Module

Es una variante del algoritmo de ordenamiento burbuja que recorre el arreglo
en ambas direcciones alternativamente, optimizada específicamente para trabajar con strings.

También conocido como:
- Cocktail Sort
- Cocktail Shaker Sort
- Shaker Sort
- Bidirectional Bubble Sort

El algoritmo funciona de la siguiente manera:
1. Primero recorre de izquierda a derecha, llevando el string más "grande" al final
2. Luego recorre de derecha a izquierda, llevando el string más "pequeño" al inicio
3. Este proceso se repite hasta que no se realizan más intercambios

En esta implementación para strings, se ofrecen múltiples criterios de ordenamiento:
- Lexicográfico (alfabético)
- Por longitud
- Sensible o insensible a mayúsculas/minúsculas
- Ascendente o descendente

Características:
- Estable: No cambia el orden relativo de elementos con valores iguales
- In-place: Solo requiere una cantidad constante de espacio adicional
- Más eficiente que el bubble sort estándar para ciertos tipos de datos
- Útil para arreglos que están parcialmente ordenados en ambas direcciones

Precauciones:
- Sigue teniendo una complejidad de tiempo O(n²) en el peor caso
- Con strings muy largos, las comparaciones pueden ser costosas
- Para listas grandes, otros algoritmos como Quick Sort o Merge Sort son más eficientes

O(n²) en tiempo de ejecución en el peor caso
O(n) en el mejor caso (arreglo ya ordenado)
O(1) en espacio
"""


class bidirectional_bubble_sort:
    """
    Una clase que implementa el algoritmo de ordenamiento burbuja bidireccional para strings.
    """

    @staticmethod
    def sort(arr, by_length=False, case_sensitive=True, reverse=False):
        """
        Implementación del algoritmo de ordenamiento burbuja bidireccional para strings.
        
        Args:
            arr: Lista de strings a ordenar
            by_length: Si es True, ordena por longitud; si es False, ordena lexicográficamente (por defecto)
            case_sensitive: Si es True, distingue entre mayúsculas y minúsculas; si es False, no distingue (por defecto True)
            reverse: Si es True, ordena en orden descendente; si es False, ordena en orden ascendente (por defecto)
            
        Returns:
            La lista ordenada (aunque también se modifica la original)
        """
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1
        
        while swapped:
            # Reiniciar la bandera de intercambio para la pasada de izquierda a derecha
            swapped = False
            
            # Pasada de izquierda a derecha
            for i in range(start, end):
                # Determinar el criterio de comparación
                if by_length:
                    # Ordenar por longitud
                    compare = len(arr[i]) > len(arr[i + 1])
                elif not case_sensitive:
                    # Ordenar lexicográficamente sin distinguir mayúsculas/minúsculas
                    compare = arr[i].lower() > arr[i + 1].lower()
                else:
                    # Ordenar lexicográficamente distinguiendo mayúsculas/minúsculas
                    compare = arr[i] > arr[i + 1]
                
                # Invertir la comparación si se requiere orden descendente
                if reverse:
                    compare = not compare
                
                # Realizar el intercambio si es necesario
                if compare:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            
            # Si no hubo intercambios, el arreglo está ordenado
            if not swapped:
                break
            
            # De lo contrario, reinicia la bandera para la pasada de derecha a izquierda
            swapped = False
            
            # Disminuir el límite superior porque el elemento más grande ya está en su posición
            end -= 1
            
            # Pasada de derecha a izquierda
            for i in range(end - 1, start - 1, -1):
                # Determinar el criterio de comparación (igual que antes)
                if by_length:
                    compare = len(arr[i]) > len(arr[i + 1])
                elif not case_sensitive:
                    compare = arr[i].lower() > arr[i + 1].lower()
                else:
                    compare = arr[i] > arr[i + 1]
                
                # Invertir la comparación si se requiere orden descendente
                if reverse:
                    compare = not compare
                
                # Realizar el intercambio si es necesario
                if compare:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            
            # Incrementar el límite inferior porque el elemento más pequeño ya está en su posición
            start += 1
        
        return arr
    
    @staticmethod
    def sort_with_custom_key(arr, key_func, reverse=False):
        """
        Implementación del algoritmo de ordenamiento burbuja bidireccional para strings con una función de clave personalizada.
        
        Args:
            arr: Lista de strings a ordenar
            key_func: Función que extrae un valor de comparación para cada elemento
            reverse: Si es True, ordena en orden descendente; si es False, ordena en orden ascendente (por defecto)
            
        Returns:
            La lista ordenada (aunque también se modifica la original)
        """
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1
        
        while swapped:
            swapped = False
            
            # Pasada de izquierda a derecha
            for i in range(start, end):
                # Usar la función clave para la comparación
                compare = key_func(arr[i]) > key_func(arr[i + 1])
                
                # Invertir la comparación si se requiere orden descendente
                if reverse:
                    compare = not compare
                
                if compare:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            
            if not swapped:
                break
            
            swapped = False
            end -= 1
            
            # Pasada de derecha a izquierda
            for i in range(end - 1, start - 1, -1):
                # Usar la función clave para la comparación
                compare = key_func(arr[i]) > key_func(arr[i + 1])
                
                if reverse:
                    compare = not compare
                
                if compare:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            
            start += 1
        
        return arr

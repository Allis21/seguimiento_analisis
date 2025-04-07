"""
Bubble Sort Module para strings

Es un algoritmo simple de ordenamiento que funciona comparando pares de elementos adyacentes
y los intercambia si están en el orden incorrecto.

Esta implementación está adaptada específicamente para trabajar con strings,
permitiendo ordenar tanto por orden lexicográfico (alfabético) como por longitud.

Características:
- Estable: No cambia el orden relativo de elementos con valores iguales
- In-place: Solo requiere una cantidad constante de espacio adicional
- Simple de implementar y entender
- Eficiente para conjuntos de datos pequeños o casi ordenados

Precauciones:
- No es eficiente para conjuntos de datos grandes
- Complejidad de tiempo: O(n²) en el peor y caso promedio
- Con strings muy largos, las comparaciones pueden ser costosas
- Para listas grandes, otros algoritmos como Quick Sort o Merge Sort son más eficientes

O(n²) en tiempo de ejecución
O(1) en espacio
"""


class bubble_sort:
    """
    Una clase que implementa el algoritmo de ordenamiento burbuja para strings.
    """

    @staticmethod
    def sort(arr, by_length=False, reverse=False):
        """
        Implementación del algoritmo de ordenamiento burbuja para strings.
        
        Args:
            arr: Lista de strings a ordenar
            by_length: Si es True, ordena por longitud; si es False, ordena lexicográficamente (por defecto)
            reverse: Si es True, ordena en orden descendente; si es False, ordena en orden ascendente (por defecto)
            
        Returns:
            La lista ordenada (aunque también se modifica la original)
        """
        n = len(arr)
        # Bandera para optimizar el algoritmo
        swapped = False
        
        # Recorrer todos los elementos del arreglo
        for i in range(n):
            swapped = False
            # Últimos i elementos ya están en su lugar correcto
            for j in range(0, n-i-1):
                # Función de comparación dependiendo de si se ordena por longitud o lexicográficamente
                compare = len(arr[j]) > len(arr[j+1]) if by_length else arr[j] > arr[j+1]
                
                # Invertir la comparación si se requiere orden descendente
                if reverse:
                    compare = not compare
                
                # Realizar el intercambio si es necesario
                if compare:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            
            # Si no hubo intercambios en esta pasada, el arreglo ya está ordenado
            if not swapped:
                break
        
        return arr

    @staticmethod
    def sort_case_insensitive(arr, reverse=False):
        """
        Ordena una lista de strings sin distinguir entre mayúsculas y minúsculas.
        
        Args:
            arr: Lista de strings a ordenar
            reverse: Si es True, ordena en orden descendente; si es False, ordena en orden ascendente (por defecto)
            
        Returns:
            La lista ordenada (aunque también se modifica la original)
        """
        n = len(arr)
        swapped = False
        
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                compare = arr[j].lower() > arr[j+1].lower()
                
                if reverse:
                    compare = not compare
                
                if compare:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            
            if not swapped:
                break
        
        return arr

"""
ShellSort module

Es un algoritmo de ordenación mejorado del insertion sort.

El algoritmo funciona dividiendo el arreglo en 'gaps' o intervalos,
que se van reduciendo progresivamente.

Para cada gap, se realiza un insertion sort en los subarreglos formados.
Al comenzar con gaps grandes, los elementos están más lejos entre sí,
lo que permite mover elementos grandes a sus posiciones correctas rápidamente.

A medida que el gap disminuye, el arreglo se va ordenando parcialmente,
lo que hace que las siguientes pasadas sean más eficientes.

Finalmente, cuando el gap es 1, se realiza un insertion sort completo
pero sobre un arreglo casi ordenado, lo que es muy eficiente.

Precauciones:
El rendimiento depende en gran medida de la secuencia de gaps utilizada.
Funciona bien para arreglos de tamaño medio.
La complejidad puede variar según la secuencia de gaps elegida.

O(n (log n)^2) en el caso promedio, aunque puede variar.
"""


class shellSort:
    """
    A class that implements the ShellSort algorithm for strings.
    """

    @staticmethod
    def sort(arr):
        """
        ShellSort algorithm implementation for strings.
        Sorts the array in ascending order.
        """
        n = len(arr)
        
        # Iniciar con un gap grande y reducirlo
        gap = n // 2
        
        while gap > 0:
            # Realizar insertion sort para el gap actual
            for i in range(gap, n):
                # Guardar el elemento actual
                temp = arr[i]
                
                # Mover elementos que son mayores que temp
                # a posiciones separadas por gap
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                
                # Colocar temp en su posición correcta
                arr[j] = temp
            
            # Reducir el gap para la próxima iteración
            gap = gap // 2
    
    @staticmethod
    def sort_string(text):
        """
        Sort a string using ShellSort algorithm.
        Returns the sorted string.
        """
        # Convertir string a lista de caracteres
        char_list = list(text)
        
        # Aplicar ShellSort
        shellSort.sort(char_list)
        
        # Convertir la lista ordenada de vuelta a string
        return ''.join(char_list)

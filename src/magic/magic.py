class Magic:

    def fibonacci(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def secuencia_fibonacci(self, n):
        seq = []
        a, b = 0, 1
        for _ in range(n):
            seq.append(a)
            a, b = b, a + b
        return seq

    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        return [i for i in range(2, n+1) if self.es_primo(i)]

    def es_numero_perfecto(self, n):
        suma = sum(i for i in range(1, n) if n % i == 0)
        return suma == n

    def triangulo_pascal(self, filas):
        tri = []
        for i in range(filas):
            if i == 0:
                tri.append([1])
            else:
                prev = tri[-1]
                row = [1] + [prev[j] + prev[j+1] for j in range(len(prev)-1)] + [1]
                tri.append(row)
        return tri

    def factorial(self, n):
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def mcm(self, a, b):
        return abs(a*b)//self.mcd(a, b)

    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        s = str(abs(n))
        return n == sum(int(d)**len(s) for d in s)

    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        if any(len(fila) != n for fila in matriz):
            return False
        s = sum(matriz[0])
        for fila in matriz:
            if sum(fila) != s:
                return False
        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != s:
                return False
        if sum(matriz[i][i] for i in range(n)) != s:
            return False
        if sum(matriz[i][n-1-i] for i in range(n)) != s:
            return False
        return True
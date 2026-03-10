class Matrix:

    def suma_matrices(self, A, B):
        if len(A) != len(B) or any(len(A[i]) != len(B[i]) for i in range(len(A))):
            raise ValueError("Dimensiones incompatibles")
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def resta_matrices(self, A, B):
        if len(A) != len(B) or any(len(A[i]) != len(B[i]) for i in range(len(A))):
            raise ValueError("Dimensiones incompatibles")
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def multiplicar_matrices(self, A, B):
        if len(A[0]) != len(B):
            raise ValueError("Dimensiones incompatibles para multiplicación")
        return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

    def multiplicar_escalar(self, matriz, escalar):
        return [[elemento * escalar for elemento in fila] for fila in matriz]

    def transpuesta(self, matriz):
        return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]

    def es_cuadrada(self, matriz):
        return len(matriz) == len(matriz[0]) if matriz else False

    def es_simetrica(self, matriz):
        if not self.es_cuadrada(matriz):
            return False
        return matriz == self.transpuesta(matriz)

    def traza(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz no es cuadrada")
        return sum(matriz[i][i] for i in range(len(matriz)))

    def determinante_2x2(self, matriz):
        if len(matriz) != 2 or len(matriz[0]) != 2:
            raise ValueError("La matriz no es 2x2")
        return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]

    def determinante_3x3(self, matriz):
        if len(matriz) != 3 or len(matriz[0]) != 3:
            raise ValueError("La matriz no es 3x3")
        a,b,c = matriz[0]
        d,e,f = matriz[1]
        g,h,i = matriz[2]
        return a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h

    def identidad(self, n):
        return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

    def diagonal(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz no es cuadrada")
        return [matriz[i][i] for i in range(len(matriz))]

    def es_diagonal(self, matriz):
        if not self.es_cuadrada(matriz):
            return False
        return all(matriz[i][j]==0 for i in range(len(matriz)) for j in range(len(matriz)) if i!=j)

    def rotar_90(self, matriz):
        return [list(reversed(col)) for col in zip(*matriz)]

    def buscar_en_matriz(self, matriz, valor):
        posiciones = []
        for i, fila in enumerate(matriz):
            for j, elemento in enumerate(fila):
                if elemento == valor:
                    posiciones.append((i,j))
        return posiciones

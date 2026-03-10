class Stats:

    def promedio(self, numeros):
        return sum(numeros)/len(numeros) if numeros else 0

    def mediana(self, numeros):
        n = len(numeros)
        if n == 0:
            return 0
        nums = sorted(numeros)
        mid = n // 2
        if n % 2 == 0:
            return (nums[mid-1] + nums[mid]) / 2
        else:
            return nums[mid]

    def moda(self, numeros):
        if not numeros:
            return None
        contador = {}
        for num in numeros:
            contador[num] = contador.get(num, 0) + 1
        max_freq = max(contador.values())
        for num in numeros:
            if contador[num] == max_freq:
                return num

    def varianza(self, numeros):
        if not numeros:
            return 0
        prom = self.promedio(numeros)
        return sum((x - prom)**2 for x in numeros)/len(numeros)

    def desviacion_estandar(self, numeros):
        return self.varianza(numeros)**0.5

    def rango(self, numeros):
        return max(numeros) - min(numeros) if numeros else 0
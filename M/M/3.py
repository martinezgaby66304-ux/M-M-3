import math 
class MM3:
    def __init__(self, landa,miu,c):
        self.landa = landa
        self.miu = miu
        self.c = c
    def calcular_utilizacion(self):
        return self.landa / (self.c * self.miu)
    
    def calcular_probabilidad_cola(self):
        rho = self.calcular_utilizacion()
        sumatoria = sum((self.landa / self.miu) ** n / math.factorial(n) for n in range(self.c))
        termino_c = ((self.landa / self.miu) ** self.c) / (math.factorial(self.c) * (1 - rho))
        p0 = 1 / (sumatoria + termino_c)
        pw = termino_c * p0
        return pw
    
    def calcular_p0(self):
       rho = self.landa / self.miu
       p = self.calcular_utilizacion()
       sumatoria = sum((rho ** n) / math.factorial(n) for n in range(self.c))
       termino_c = (rho ** self.c) / (math.factorial(self.c) * (1 - p))
       return 1 / (sumatoria + termino_c)

    
    def calcular_numero_promedio_cola(self):
        pw = self.calcular_probabilidad_cola()
        return pw * (self.landa / (self.c * self.miu - self.landa))
    
    def calcular_tiempo_promedio_cola(self):
        pw = self.calcular_probabilidad_cola()
        return pw / (self.c * self.miu - self.landa)
    
    def calcular_tiempo_promedio_sistema(self):
        return self.calcular_tiempo_promedio_cola() + 1/self.miu
    
    def calcular_numero_promedio_sistema(self):
        return self.landa * self.calcular_tiempo_promedio_sistema()
    
    def calcular_numero_promedio_servicio(self):
        return self.landa / self.miu

    
    


landa_promedio_llegada = float(input("Ingrese la tasa de llegada (landa): "))
miu_promedio_servicio = float(input("Ingrese la tasa de servicio (miu): "))
c = int(input("Ingrese el número de servidores (c): ")) 

modelo = MM3(landa_promedio_llegada,miu_promedio_servicio,c)  

print("Resultados del modelo M/M/c:")
print("p (utilización):", modelo.calcular_utilizacion())
print("P0 (probabilidad sistema vacío):", modelo.calcular_p0())
print("Pw (probabilidad de espera en cola):", modelo.calcular_probabilidad_cola())
print("Lq (número promedio en cola):", modelo.calcular_numero_promedio_cola())
print("Wq (tiempo promedio en cola):", modelo.calcular_tiempo_promedio_cola())
print("W (tiempo promedio en el sistema):", modelo.calcular_tiempo_promedio_sistema())
print("L (número promedio en el sistema):", modelo.calcular_numero_promedio_sistema())
print("Ls (número promedio siendo atendidos):", modelo.calcular_numero_promedio_servicio())
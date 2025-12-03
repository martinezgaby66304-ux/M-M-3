class MM3:
    def __init__(self, landa,miu,c):
        self.landa = landa
        self.miu = miu
        self.c = c
    def calcular_utilizacion(self):
        return self.landa / (self.c * self.miu)


landa_promedio_llegada = float(input("Ingrese la tasa de llegada (landa): "))
miu_promedio_servicio = float(input("Ingrese la tasa de servicio (miu): "))
c = int(input("Ingrese el número de servidores (c): ")) 

modelo = MM3(landa_promedio_llegada,miu_promedio_servicio,c)  

print("p(utilizacion):", modelo.calcular_utilizacion())
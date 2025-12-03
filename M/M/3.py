class MM3:
    def __init__(self, landa,miu,c):
        self.landa = landa
        self.miu = miu
        self.c = c

    landa_promedio_llegada = float(input("Ingrese la tasa de llegada (landa): "))
    miu_promedio_servicio = float(input("Ingrese la tasa de servicio (miu): "))
    c = int(input("Ingrese el número de servidores (c): ")) 
    
                                          
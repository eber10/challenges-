from collections import namedtuple
Fecha=namedtuple("Fecha",["dia","mes","anio"])
Personal=namedtuple("Personal",["dni","nombre","nacimiento"])
def comparar(f1: Fecha,f2: Fecha):
    if(f1.anio!=f2.anio):
        return f1.anio<f2.anio
    if(f1.mes!=f2.mes):
        return f1.mes<f2.mes
    return f1.dia<f2.dia
def ordenar(lista, n):
    for i in range(n-1):
        menor=i
        for j in range(i+1,n):
            if(comparar(lista[j].nacimiento,lista[menor].nacimiento)):
                menor=j
        if i!=menor:
            temp=arr[i]
            arr[i]=arr[menor]
            arr[menor]=temp
arr=[Personal("48720178","mateo",Fecha(1,3,2000)),
     Personal("72019382","camilo",Fecha(5,7,1978)),
     Personal("20918472","maribel",Fecha(8,11,2001)),
     Personal("72291083","camila",Fecha(1,8,1960))]
for i in range(4):
    print(arr[i].dni,arr[i].nombre,arr[i].nacimiento.dia,"/",arr[i].nacimiento.mes,"/",arr[i].nacimiento.anio)
print("-----------datos ordenados-----------")
ordenar(arr, 4)
for i in range(4):
    print(arr[i].dni,arr[i].nombre,arr[i].nacimiento.dia,"/",arr[i].nacimiento.mes,"/",arr[i].nacimiento.anio)

print("----BIENVENIDO A ALMACENES WC----")
#ARTICULOS Y PRECIOS
artypre={
"Zapatos":350000,
"Tennis":280000,
"Camisetas":175000,
"Jeans":200000
}
Ctotal= artypre["Zapatos"] + artypre["Tennis"] + artypre["Camisetas"] + artypre["Jeans"]
Pdprecios= Ctotal // 4
Npromediozapatos=artypre["Zapatos"]*(0.8/100)
Npromediojeanns=artypre["Jeans"]* (6.2/100)
print("-------ARTICULOS Y PRECIOS-------")
print(artypre)
print("----------------------------------")
print("-TOTAL:",Ctotal, "\n" "-PROMEDIO DE PRECIOS:",Pdprecios,"\n""-NUEVO PRECIO DE ZAPATOS:",Npromediozapatos - artypre["Zapatos"],"\n""-NUEVO PRECIO DE JEANS:",Npromediojeanns + artypre["Jeans"]) 
print("-------GRACIAS POR SU ATENCIÓN------")
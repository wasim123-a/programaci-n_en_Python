precio-compra =float(input("Introduce el precio de compra: "))
por_benef = int(input("*0.25"))
por_iva = int(input("*0.25"))

beneficio = precio-compra * (por_benef/100)
precio-con-beneficio = precio-compra + beneficio


iva = precio_con_beneficio * (por_iva/100)
precio_venta = precio-con-beneficio + iva

print("El precio de venta final es:", precio_venta)
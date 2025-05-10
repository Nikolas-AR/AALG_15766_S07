def voraz(denominaciones, monto):
    result = []
    
    for moneda in denominaciones:
        cant = int(monto//moneda)
        if cant > 0:
            result.append((cant, moneda))
            monto = round(monto - cant * moneda, 2)
            
    return result


denominaciones = [100, 50, 20, 10, 5, 2, 0.05]
monto = float(input("Ingrese el monto en soles: "))
result = voraz(denominaciones, monto)

print("-----------------------------------------------------")
print("------------RESPUESTAS------------")
if monto == 0: 
    print("No se puede dar vuelto porque el valor es 0")
else:
    for cant, moneda in result:
        print(f"{cant} de S/{moneda}")
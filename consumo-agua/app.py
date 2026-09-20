tipo = input("Informe o tipo de  imovél (comercial, apartamento ou casa): ")
consumo = float(input("Informe o consumo mensal de água em m³: "))

match tipo:
    case "comercial":
        print("Tarifa comercial aplicada - consulte o plano corporativo.")
    case "apartamento" if consumo < 10:
        print("Consumo econômico - excelente controle de água!")
    case "apartamento" | "casa" if consumo <= 25:
        print("Consumo moderado - dentro do padrão residencial.")
    case _:
        print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")
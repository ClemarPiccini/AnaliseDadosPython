numeros = ['4721102', '4782202', '4742300', '9329804', '5611203', '5611204', '4712100', '4520007', '4763601', '9511800', '4781400', '4930202', '9511800', '4930202', '5223100', '4782201', '4781400', '1610203', '4781400', '8599605', '4330403', '9313100', '1531902', '4729699', '4744004', '4649402', '4617600', '4789001', '5611203', '7500100', '4782201', '4712100', '4754701', '4781400', '7319003', '8599603', '1412601', '4789002', '4781400', '4789007', '4755503', '6201501', '4759899', '4530703', '4721102', '3831901', '4755503', '4712100', '4723700', '4712100', '4721102', '4744002', '8230001', '5510801', '5510801', '1813001', '8541400', '4789001', '8593700', '4789099', '7729202', '4744002', '8291100', '3101200', '4744099', '4742300', '4744099', '4772500', '5611203', '6920601', '5611204', '4789004', '4753900', '6319400', '3314710', '4781400', '4511102', '5320202', '4781400', '4789004', '4744099', '7722500', '4761002', '4923001', '4621400', '5611201', '4322301', '4712100', '6209100', '8211300', '4712100', '4763603', '4753900', '4512901', '8650004', '4649499', '4721102', '4930202', '5611203', '6821801']

contagem = 0
for numero in numeros:
    if numero.startswith('561'):
        contagem += 1

print(f"A quantidade de números que começam com '56.1' é: {contagem}")

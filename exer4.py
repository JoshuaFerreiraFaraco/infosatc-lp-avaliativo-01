valorT = float(input("Digite o valor total do premio: "))
imposto = valorT * 0.07
valorPI = valorT - imposto
p1 = valorPI * 0.46
p2 = valorPI * 0.32
p3 = valorPI - (p1 + p2)

print("Total do premio: ", valorT,
      "\nPremio pos imposto: ", valorPI,
      "\nPrimeiro ganhador recebera: ", p1,
      "\nSegundo ganhador recebera: ", p2,
      "\nTerceiro ganhador recebera: ", p3)
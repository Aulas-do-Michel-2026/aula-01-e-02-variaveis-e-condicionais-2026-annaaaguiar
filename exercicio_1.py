"""
#### Exercício 1

Receba três notas (números decimais) de um aluno e imprima a média.

Exemplo:

Digite a primeira nota:
8.5
Digite a segunda nota:
7.0
Digite a terceira nota:
9.0

Resposta:
Média: 8.17

Dica: Use inputs para receber os dados! 
Lembre de converter ele para o tipo necessário!
Print na tela com "print"
"""

num1 = (float(input("Digite um número: ")))
num2 = (float(input("Digite outro número: ")))
num3 = (float(input("Digite outro número: ")))

print (f"O seu primeiro número foi {num1}")
print (f"O seu segundo número foi {num2}")
print (f"O seu terceiro número foi {num3}")

media = (float(num1 + num2 + num3) /3)
print(f"A média dos 3 números é: {media:.2f}")

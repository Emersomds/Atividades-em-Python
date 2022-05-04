#QUESTÃO 1

print(f'{"Bem vindo a loja":^35} ')
print('-----------#-----------#------------')
preco = float(input('Informe o Valor do produto: ')) #Aqui é solicitado o valor do produto.
qtd = int(input('Informe a Quantidade de Produto? '))#Aqui é solicitado a quantidade.

# ↓ Neste if sendo inferior a 10 unidades não a desconto.
if qtd<=9:
    res = qtd * preco
    print(f"O valor total foi:  R$ {res}")

# ↓ Neste Bloco elif quantidade maior igual a 10 e menor igual a 99 dá desconto de 5% em produtos.
elif qtd >=10 and qtd <=99:
    res = qtd * preco
    print(f"O valor sem desconto foi R${res} ")
    des = res*5/100
    total = res-des
    print(f"O valor com desconto foi : R${total}  (Desconto de 5%).")

# ↓ Neste Bloco elif quantidade maior igual a 99 e menor igual a 999 dá desconto de 10% em produtos.
elif qtd >=99 and qtd <=999:
    res = qtd * preco
    print(f"O valor sem desconto foi R${res} ")
    des = res*10/100
    total = res - des
    print(f"O valor com desconto foi : R${total}  (Desconto de 10%).")

# ↓ E finalizando estruturas de decisão else quantidade maior que 1000 entõa o desconto é de 15%.
else:  
    qtd <=1000
    res = qtd * preco
    print(f"O valor sem desconto foi R${res} ")
    des = res*15/100
    total = res - des
    print(f"O valor com desconto foi : R${total}  (Desconto de 15%).")
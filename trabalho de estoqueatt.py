item = input("Item que deseja vender: ")
cp = float(input("Custo do produto: "))
cf = float(input("Porcentagem de custo fixo: "))
cv = float(input("Porcentagem de comissão de vendas: "))
iv = float(input("Porcentagem de imposto de venda: "))
ml = float(input("Porcentagem de margem de lucro: "))

cfp = cf / 100
cvp = cv / 100
ivp = iv / 100
mlp = ml / 100

pv = cp / (1 - (cfp + cvp + ivp + mlp))
A=(pv/pv)*100
B = (cp/pv) * 100
C = pv - cp
CP = (C/pv) * 100
D = cfp * pv
E = cvp * pv
F = ivp * pv
G = (cfp+cvp+ivp) * pv
GP = cf+cv+iv
H = C - G
HP = (H/pv) * 100
I = cp * (cfp + cvp + ivp)

pcp=(cp/pv)*100

print(f"O preço de venda deverá ser: {pv}, a porcentagem é:{A}")
print(f"O custo de aquisição foi: {cp}, a porcentagem é:{B}")
print(f"A receita bruta é: {C}, a porcentagem é:{CP}")
print(f"O custo fixo é: {D}, a porcentagem é:{cf}")
print(f"O valor de comissão é:{E}, a porcentagem é:{cv}")
print(f"O imposto de venda é:{F} a porcentagem é:{iv}")
print(f"Os outros custos são: {G}, a porcentagem é:{GP}")
print(f"A rentabilidade é: {H}, a porcentagem é: {HP}")

if H >= 0.2 * pv:
    print("O lucro é alto")
elif 0.1 * pv <= H < 0.2 * pv:
    print("O lucro é médio")
elif 0 < H < 0.1 * pv:
    print("O lucro é baixo")
elif H == 0:
    print("Não há lucro nem prejuízo")
else:
    print("Prejuízo")

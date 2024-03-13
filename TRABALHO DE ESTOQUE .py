item=str(input("item que deseja vender:"))
cpi=float(input("Custo do produto:"))
cf=float(input("porcentagem de custo fixo:"))
cfp=cf/100
cv=float(input("porcentagem de comissão de vendas: "))
cvp=(cv/100)
iv=float(input("porcentagem de imposto de venda:"))
ivp=(iv/100)
ml=float(input("porcentagem de margem de lucro:"))
mlp=(ml/100)
pv=cpi/(1-(cf+cv+iv+ml)/100)
C=(pv-cpi)
G=( cf + cv + iv )
E=(C-G)
print(f"O preço de venda deverá ser:{pv}")
print(f"O custo de aquisição foi:{cpi}")
print(f"A receita bruta é:{pv}-{cpi}")
print(f"O custo fixo é:{cf}")
print(f"A porcentagem de comissão é:{cv}")
print(f"A porcentagem de imposto é:{iv}")
print(f"Os outros custos são:{cf}+{cv}+{iv}")
print(f"A rentabilidade é:{C}-{G}")
if E<=20:
     print("O lucro é alto")
elif 10<=E<20:
      print("O lucro é médio") 
elif 0<E<10:
      print("O lucro é baixo")
elif E==0:
      print("Não há lucro nem prejuizo")
elif E<0:
      print("Prejuizo")
    
    
    
    
    
    
    
    
    
    
    
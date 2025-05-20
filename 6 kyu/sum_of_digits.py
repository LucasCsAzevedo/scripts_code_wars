# %%
'''
    link: https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
    Esse exercício tem por objetivo somar os digitos de um número, de maneira que o resultado da soma seja apenas um digito. 
    Ex: 
    16 --> 1 + 6 = 7
    132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
''' 

# %%
num_teste = 16
str_num = str(num_teste)

print(len(str_num))

# %%

for n in str_num:
    print(n)

# %%
num = 26

def digital_root(n):
    soma = 0
    n = str(n)
    
    while True:
        if len(n) > 1:
            for valor in n:
                soma += int(valor)
        else:
            break
        
    return soma
    

print(digital_root(num))

# %%

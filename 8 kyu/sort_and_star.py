# %%
'''
    link: https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python
    You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

    The returned value must be a string, and have "***" between each of its letters.

    You should not remove or add elements from/to the array.
'''

# %%
def two_sort(array):
    lista = []
    first_char = sorted(array)[0]
    
    for l in first_char:
        lista.append(l)
        
    final = '***'.join(lista)
    
    return final 


case1 = ['Lucas', 'Cardoso', 'de', 'Azevedo', 'AZEVEDO']

print(two_sort(array=case1))


# %%
# Solução que vi após enviar a minha:
def two_sort(array):
    return '***'.join(min(array))

# Achei bem interessante porque não sabia que o min já fazia esse sort! E no final não precisa de fazer uma lista, na string já consigo fazer o .join
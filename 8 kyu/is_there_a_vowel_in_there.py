# %%
'''
    Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

    If they are, change the array value to a string of that vowel.

    input [100,100,116,105,117,121]=>[100,100,116,"i","u",121] output Return the resulting array.
    
    codigo das vogais: a: 97, e: 101, i: 105, o: 111, u: 117
'''

# %%
def is_vow(array):
    lista_final = []

    for valor in array:
        if valor == 97:
            lista_final.append('a')
        elif valor == 101:
            lista_final.append('e')
        elif valor == 105:
            lista_final.append('i')
        elif valor == 111:
            lista_final.append('o')
        elif valor == 117:
            lista_final.append('u')
        else:
            lista_final.append(valor)
            
    return lista_final  


# %%
# Solução que achei após enviar minha resposta. Não sabia da existência desse método (chr)
def vogal(inp): 
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]


print(vogal([100,100,116,105,117,121]))

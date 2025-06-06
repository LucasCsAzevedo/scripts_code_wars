# %%
'''
    Input: Array of elements

    ["h","o","l","a"]

    Output: String with comma delimited elements of the array in th same order.

    "h,o,l,a"
'''

# %%
def print_array(arr):
    arr = [str(item) for item in arr]
    return ','.join(arr)


# %%
# Soluções que vi após enviar a minha:
def print_array(arr):
    return ','.join(map(str, arr))


def print_array(arr):
    return ','.join(str(a) for a in arr)
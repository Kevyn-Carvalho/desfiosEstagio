def inverte_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

# Exemplo de uso
string_original = input("Digite a string que deseja inverter: ")
string_invertida = inverte_string(string_original)
print(f"A string invertida é: {string_invertida}")

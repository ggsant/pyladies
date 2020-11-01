
#** Assertion é um tipo de checagem que pode ser feita para garantir que o seu  codigo nao esta fazendo algo obviamente errado 

ages = [26,57,92,54,22,15,17,80,47,73]
ages.sort()
ages[15,17,22,26,47,54,57,73,80,92]
assert ages[0] <= ages[-1]
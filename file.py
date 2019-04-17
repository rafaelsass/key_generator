import random 
import string as s

def gerador(dificuldade, num_caracteres):
    a = s.ascii_lowercase
    a = [i for i in a]
    A = [i.upper() for i in a]
    b = s.punctuation
    b = [i for i in b]
    c = s.digits
    c = [str(i) for i in c]
    if dificuldade == "FRACA":
        random_list = random.choices(b + a + c, k=num_caracteres)
        while all([any(x in random_list for x in a), any(x in random_list for x in b),any(x in random_list for x in c )])is False:
            random_list = random.choices(b + a + c, k=num_caracteres)
        random_list = [str(i) for i in random_list]
        print(random_list)
        print("Senha gerada:", "".join(random_list))

    elif dificuldade == "FORTE":
        random_list = random.choices(b + a + c + A, k=num_caracteres)
        while all([any(x in random_list for x in a), any(x in random_list for x in b),any(x in random_list for x in c), any(x in random_list for x in A)])is False:
             random_list = random.choices(b + a + c + A, k=num_caracteres)
        random_list = [str(i) for i in random_list]
        print("Senha gerada:", "".join(random_list))

def valores():
    loop = True
    while loop is True:
        print("\n")
        contador = 0
        while contador < 2:
            contador = 0
            dificuldade = input("Deseja sua senha forte ou fraca?: ")
            try:
                dificuldade = dificuldade.upper()
                if dificuldade == "FORTE" or dificuldade == "FRACA":
                    contador += 1
                num_caracteres = input(
                    "Quantos caracteres deseja em sua senha(ao menos 4 para senha fraca e ao menos 8 para forte)?: ")
                try:
                    num_caracteres = int(num_caracteres)
                    if dificuldade == "FORTE":
                        if num_caracteres >= 8:
                            contador += 1
                    elif dificuldade == "FRACA":
                        if num_caracteres >= 4:
                            contador += 1
                except:
                    print("entre um valor valido","\n")
            except:
                print("entre um valor valido","\n")

        gerador(dificuldade, num_caracteres)
        loop_loop = 0
        while loop_loop == 0:
            resp = input("Deseja gerar outra senha?: ")
            resp = resp.lower()
            if resp == "sim":
                loop_loop = 1
            elif resp =="não":
                loop = False
                loop_loop = 1

valores()

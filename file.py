import random 
import string as s

def gerador(dificuldade, num_caracteres):
    d = s.printable
    d = [x for x in d if x not in s.whitespace]
    if dificuldade == "FRACA":
        d = [x for x in d if x not in s.ascii_uppercase]
        random_list = random.choices(d, k=num_caracteres)
        while all([any(x in random_list for x in s.ascii_lowercase), any(x in random_list for x in s.digits),any(x in random_list for x in s.punctuation)])is False:
            random_list = random.choices(d, k=num_caracteres)
        random_list = [str(i) for i in random_list]
        print("Senha gerada:", "".join(random_list))

    elif dificuldade == "FORTE":
        random_list = random.choices(d, k=num_caracteres)
        while all([any(x in random_list for x in s.ascii_lowercase), any(x in random_list for x in s.digits),any(x in random_list for x in s.punctuation), any(x in random_list for x in s.ascii_uppercase)])is False:
             random_list = random.choices(d, k=num_caracteres)
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

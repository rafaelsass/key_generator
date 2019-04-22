import random 
import string as s

def gerador(dificuldade, num_caracteres):
	filtro = lambda x,y: any(a in x for a in y)
	d = s.printable
	d = [x for x in d if x not in s.whitespace]
	if dificuldade == "FRACA":
	    d = [x for x in d if x not in s.ascii_uppercase]
	    r_list = random.choices(d, k=num_caracteres)
	    while all([filtro(r_list,s.ascii_lowercase), filtro(r_list, s.digits),filtro(r_list,s.punctuation)])is False:
        	r_list = random.choices(d, k=num_caracteres)
	    r_list = [str(i) for i in r_list]
	    print("Senha gerada:", "".join(r_list))

	elif dificuldade == "FORTE":
	    r_list = random.choices(d, k=num_caracteres) 
	    while all([filtro(r_list,s.ascii_lowercase), filtro(r_list,s.digits),filtro(r_list,s.punctuation), filtro(r_list,s.ascii_uppercase)])is False:
	         r_list = random.choices(d, k=num_caracteres)
	    r_list = [str(i) for i in r_list]
	    print("Senha gerada:", "".join(r_list))

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

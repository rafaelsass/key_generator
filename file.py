import random
contador =0
while contador < 2:
	contador = 0
	dificuldade = input("Deseja sua senha forte ou fraca?: ")
	try: 
		dificuldade = dificuldade.upper()
		if dificuldade == "FORTE" or dificuldade == "FRACA":
			contador +=1
		num_caracteres = input("Quantos caracteres deseja em sua senha(pelo menos 4 para senha fraca e ao menos 8 para forte)?: ")
		try: 
			num_caracteres = int(num_caracteres)
			if dificuldade =="FORTE":	
				if num_caracteres >= 8:
					contador+=1
			elif dificuldade =="FRACA":
				if num_caracteres >= 4:
					contador+=1
		except: 
			print("entre um valor valido")
	except:
		print("entre um valor valido") 

a = ("a b c d e f g h i j k l m n o p q r s t u v w x y z")
b = ("! @ # $ % & ")

def gerador(dificuldade, num_caracteres):

	if dificuldade =="FRACA":
		var = 0
		random_list = random.choices((b+a).split()+random.choices(range(0,10),k=9), k=num_caracteres)
		while a.split()[random.choice(range(len(a.split())))] and b.split()[random.choice(range(len(b.split())))] and random.randint(0,9) not in random_list:
			random_list = random.choices((b+a).split()+random.choices(range(0,10),k=9),k=num_caracteres)
		random_list = [str(i) for i in random_list]
		print(random_list)
		print("Senha gerada:","".join(random_list))
		
	elif dificuldade =="FORTE":
		var = 0
		random_list = random.choices((b+a).split()+random.choices(range(0,10),k=9)+a.upper().split(), k=num_caracteres)
		while a.split()[random.choice(range(len(a.split())))] and b.split()[random.choice(range(len(b.split())))] and random.randint(0,9) and a.upper().split()[random.choice(range(len(a.split())))] not in random_list:
			random_list = random.choices((b+a).split()+random.choices(range(0,10),k=9)+a.upper().split(), k=num_caracteres)
		random_list = [str(i) for i in random_list]
		print(random_list)
		print("Senha gerada:","".join(random_list))


gerador(dificuldade, num_caracteres)
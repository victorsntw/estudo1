# aqui o programa pede um nome tirando os espaços e colocando a primeira letra do nome em maiusculo
nome = input("Qual é o seu nome?").strip().capitalize()

#Aqui verifica se o nome é igual a "João"
if nome == "João":
    # Se for "João" ele mostra essa mensagem e entra em um enquanto verdadeiro
    print("Seu nome é João!")
    while True:
        # aqui ele tenta com um "try", para tratamento de erros
        try:
            # ele pede para digitar um número de 10 até 20
            numero = int(input("Digite um número que esteja entre 10 e 20: "))
            # se o número for igual 25 ele mostra a mensagem feliz natal
            if numero == 25:
                print(f"Feliz natal {nome}")
                break # aqui ele para o programa após o número digitado for "25" e mostra a mensagem de feliz natal 
            # aqui compara com um recurso especial de operador de compração se o número está entre 10 e 20
            elif 10 <= numero <=20:
                # se o número estiver dentro de 10 a 20 ele mostra a mensagem de "o número está dentro do intervalo"
                print("O número está dentro do intervalo!")
                break # aqui ele para o programa se o número estiver dentro do intervalo de 10 a 20.
            # se o número estiver fora do intervalo ele mostra a mensagem "O número não está dentro do intervalo" e pede novamente o número pois está dentro do While True.
            else:
                print("O número não está dentro do intervalo!")
        # aqui mostra uma mensagem de erro caso a pessoa digite letras ou número com virgulas - tratamento de erros.
        except ValueError:
            print("Erro: Você precisa digitar apenas números inteiros")
# aqui a mensagem mostrada "Seu nome não é João" caso o nome seja diferente de "João".
else:
    print("Seu nome não é João!")


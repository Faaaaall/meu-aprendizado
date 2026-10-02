# consultor dns brute force (mesma coisa de antes) só que agora com sys, mais bonitinho e com wordlist pre definida


import dns.resolver
import sys 

resolver = dns.resolver.Resolver()

try:
    with open('wordlist.txt', 'r') as arq: 
          subdominio = arq.read().splitlines()
except:
      print('erro ao abrir arquivo')
      sys.exit()
alvo = 'sitealeatorio.com'
  
for subdominio in subdominios 
    try:
        sub_alvo = '{}.{}'.format(subdominio, alvo)
        resultados = resolver.resolve(sub_alvo, 'A')
        for resultado in resultados:
                          print('{} -> {}'.format(sub_alvo, resultado))
except:
      pass



# vai colocar a wordlist.txt dentro da variavel arq 
# subdominio vai ler este arquivo com arq.read()
# o splitlines vai servir para pegar cada arquivo por linha, ou seja, vai pegar cada linha e transformar num elemento de uma lista
# variavel subdominios vai ter todas as linhas da wordlist.txt 
# pra criar o arquivo que usaremos de wordlist é só criar no nano um arquivo chamado wordlist.txt q ele vai pegar de la a wordlist

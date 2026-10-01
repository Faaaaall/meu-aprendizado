# consultor de dns bruteforce só q dessa vez com wordlist pré definida, MUITO mais bonitinho e agora vai dar pra usar no terminal direto 

import sys
import dns.resolver

resolver = dns.resolver.Resolver()

try:
    alvo = sys.argv[1]
    wordlist = sys.argv[2]
except:
    print ('usage: python3 dnsbrute.py dominio wordlist.txt')
    sys.exit()

try:
    with open(wordlist, 'r') as arq:
          subdominios = arq.read().splitlines()
except:
    print('erro ao abrir arquivo')
    sys.exit()
for subdominio in subdominios:
    try:
        sub_alvo = '{}.{}'.format(subdominio, alvo)
        resultados = resolver.resolve(sub_alvo, 'A') 
        for resultado in resultados:
            print('{} -> {}'.format(sub_alvo, resultado))
except:
      pass 

# basicamente agora quando eu quiser usar script de enumaração pra dns, eu só escrevo no promtp 
# python3 dnsbrute site.com wordlist.txt
# ou seja, o nome da ferramenta, o site e a wordlist q eu quero
# é isso q o sys.argv faz, ele pega os primeiros argumentos mencionados, que no caso foram do promtp

# python3 dnsbrute | site.com | wordlist.txt 
#                   argumento1   argumento2

# sys.argv = argument give

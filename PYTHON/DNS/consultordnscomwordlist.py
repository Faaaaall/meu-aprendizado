import dns.resolver
wordlist = ['bosta', 'coco', 'oi', 'me da star', 'ola', 'pizza']
alvo = 'sitealeatorio.com'

  
for subdominio in wordlist:
    try:
        sub_alvo = '{}.{},' .format(subdominio, alvo)
        resultados = resolver.resolve(sub_alvo, 'A')
        for resultado in resultados:
      print('{} -> {}'.format(sub_alvo, resultado))
except:
      pass: 
      print('subdominio nao existe')


 # pra cada subdominio na wordlist ele vai fazer o teste que se encontra na variavel sub_alvo 
 # no qual vai ser a junção do subdominio com o alvo
 # ele vai entrar no for e para cada elemento da wordlist, ele vai entrar no try e criar um subalvo 
 # o subalvo vai ser o elemento do .format 
 # ou seja, vai ficar: 
 # bosta.sitealeatorio.com | coco.sitealeatorio.com | oi.sitealeatorio.com 
 # e assim vai..

 # o programa SEM O PASS ja é funcional, mas com o pass: 
 # ele só vai mostrar quando o subdominio existir 

 # no print do for ele mostra o subdominio -> IP, nada demais

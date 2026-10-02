import dns.resolver

resolver = dns.resolver.Resolver() 
try:
  resultados = resolver.resolve('sitealeatorio.com', 'A')
  for resultado in resultados:
  print (resultado)
except:
  print('subdominio nao existe)

        
        
        # explicando o for pra mim mesmo pq eu fiquei perdido 
        # o resultado é uma variável temporária que vc cria no for
        # o comando "for" já suporta essa criação de variável temporária
        # essa variável ''resultado'' só existe dentro do for
        # vc pode colocar qualquer coisa ali
        # for shit in resultados q vai dar no mesmo 

        # btw, o 'A' é o DNS q eu quero requisitar

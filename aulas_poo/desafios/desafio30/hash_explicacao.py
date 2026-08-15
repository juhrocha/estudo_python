import hashlib #Biblioteca nativa

texto = 'Coração'
cod = texto.encode('utf-8')
hash = hashlib.sha256(cod).hexdigest()
print(cod)
print(hash)

#Sempre salvar senhas com hash, Guanabara sugere SHA-256 como o ideal para esse processo.
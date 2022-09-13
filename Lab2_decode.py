import hashlib
################ Abrir archivo y guardar mensaje cifrado en variable
archivo_entrada = open('mensajeseguro.txt', 'r')
mensaje = archivo_entrada.readlines()
mensaje_cifrado = mensaje[0]
mensaje_cifrado = mensaje_cifrado.replace('\n','')
hash = mensaje[1]
print('El mensaje seguro es:',mensaje_cifrado)
print('El hash del mensaje original entrgado en el archivo es:',hash)

################## función para deshacer un rot() para un numero n
def decrypt_rotx(mensaje,numero):
    encrypted_text = mensaje.lower()
    number = numero
    text = "abcdefghijklmnopqrstuvwxyz"
    final = ""
    finaldecrypted = ''
    rotation = text[number:] + text[:number]

    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            final = text[rotation.index(encrypted_text[i])]
            finaldecrypted += final
        else:
            finaldecrypted += encrypted_text[i]
    return(finaldecrypted)

#################### Descifrado de mensaje en rot()
rot2 = decrypt_rotx(mensaje_cifrado,2)
print('Rot(2) del mensaje:',rot2)
rot8 = decrypt_rotx(rot2,8)
print('Rot(8) del anterior mensaje:',rot8)
rot13 = str(decrypt_rotx(rot8,13))
print('Rot(13) del anterior mensaje:',rot13)

################## Obtener hash del mensaje descifrado
hash_nuevo = hashlib.sha256(rot13.encode('utf-8')).hexdigest()
print('Hash del mensaje descifrado en SHA256 es:',hash_nuevo)

################# Comparacion de hashes

if hash != hash_nuevo:
    print('Los Hashes no son iguales, por lo tanto los mensajes no son iguales :´(')
else:
    print('Los Hashes son iguales!\n por lo que los mensajes son iguales :)')


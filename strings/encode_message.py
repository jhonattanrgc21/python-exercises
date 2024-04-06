import sys

def main():
    lines = sys.stdin.readlines()
    
    for line in lines:
        text = line.strip()
        size = len(text)
        letras_impares = []
        letras_pares = []
        for index in range(1, size + 1):
            if(index % 2 == 0):
                letras_pares.insert(0, text[index - 1])
            else:
                letras_impares.append(text[index - 1])
        
        nuevo_mensaje = []
        while(len(letras_pares) > 0 and len(letras_impares) > 0):
            letra_par = letras_pares.pop(0)
            letra_impar = letras_impares.pop(0)
            nuevo_mensaje.append(letra_impar)
            nuevo_mensaje.append(letra_par)
            
        nuevo_mensaje.extend(letras_pares)
        nuevo_mensaje.extend(letras_impares)
        
        print(''.join(nuevo_mensaje))
    
if __name__ == '__main__':
    main()
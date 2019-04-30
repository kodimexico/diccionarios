def HexToByte(hex_str):
    bytes = []
    hex_str = ''.join(hex_str.split(" "))

    for i in range(0, len(hex_str), 2):
        bytes.append(chr(int(hex_str[i:i + 2], 16)))

    return ''.join(bytes)

def ByteTOHex(byte_str):
    return ''.join(["%02X" % ord(x) for x in byte_str]).strip()

# Simulacion de senal de entrada
input = ({'D2': ['42.00.00.02.FF.FF.00.00', '32.44.AE.02.FF.FF.00.00'],
'170': ['30.01.2F.00.00.00.00.00'],
'17D': ['FE.30.40.0C.86.00.00.00'],
'18D': ['65.46.54.AA.0F.00.00.00'],
'3EC': ['16.60.00.00.00.00.00.00'],
'300': ['00.00.00.00.00.00.00.00'],
'18E': ['00.00.02.AE.9D.F8.8F.04'],
'357': ['00.00.00.00.03.00.00.00'],
'552': ['00.44.00.00.00.00.00.00'],
'2A': ['00.00.00.00.00.3C.00.CD'],
'15A': ['32.00.00.13.FF.00.40.00'],
'15B': ['33.43.28.90.00.00.00.00']})

# El codigo anterior se puede reemplazar con este que convierte cada senal
# a 'bytearray' o bytes en Hexadecimal
# inicializar un diccionario
input2 = dict()

# Por cada llave (en este caso estoy leyendo cada ID del diccionario)
for x in input:
    
    # Por cada valor en la lista de la llave x
    for y in input[x]: 
        # Reemplazar los puntos por espacios, esto se necesita para convertir en 
        # bytes; '42.00.00.02.FF.FF.00.00' -> '42 00 00 02 FF FF 00 00'
        y = y.replace('.', ' ')
        
        # Convertir el texto en bytes
        y = bytearray.fromhex(y)
        
        # Misma logica de antes, pero esta vez la inverti:
        # Si la llave no existe crearla y agregar el primer elemento de la lista
        if x not in input2:
            input2[x] = [y, ]
            
        # En caso contrario (si la llave ya existe), agregar un valor nuevo 
        # a la lista existente
        else:
            input2[x] += [y, ]

# Imprimir el nuevo diccionario
print(input2)

# Este es el resultado, todas las direcciones ahora estan en Hexadecimal
# 
# {'D2': [bytearray(b'B\x00\x00\x02\xff\xff\x00\x00'), bytearray(b'2D\xae\x02\xff\xff\x00\x00')], 
# '170': [bytearray(b'0\x01/\x00\x00\x00\x00\x00')], 
# '17D': [bytearray(b'\xfe0@\x0c\x86\x00\x00\x00')], 
# '18D': [bytearray(b'eFT\xaa\x0f\x00\x00\x00')], 
# '3EC': [bytearray(b'\x16`\x00\x00\x00\x00\x00\x00')], 
# '300': [bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00')], 
# '18E': [bytearray(b'\x00\x00\x02\xae\x9d\xf8\x8f\x04')], 
# '357': [bytearray(b'\x00\x00\x00\x00\x03\x00\x00\x00')], 
# '552': [bytearray(b'\x00D\x00\x00\x00\x00\x00\x00')], 
# '2A': [bytearray(b'\x00\x00\x00\x00\x00<\x00\xcd')], 
# '15A': [bytearray(b'2\x00\x00\x13\xff\x00@\x00')], 
# '15B': [bytearray(b'3C(\x90\x00\x00\x00\x00')]}

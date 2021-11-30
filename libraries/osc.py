#La direccion debe ser multiplo de 4 tambien (sin tener en cuenta la ,)
import struct
CODE = 'utf-8'
def message(addr, value):
    addr_zeros = addr_add_zeros(addr)
    tag = type_tag(value)
    
    encabezado = bytes(addr_zeros, CODE) + bytes(tag, CODE)
    elen = len(encabezado)
    zeros = (((elen+4) & ~3) - elen)
    msg = encabezado + bytes('\0'*zeros, CODE)
    
    if tag != 'T' and tag != 'F':
        data = struct.pack ('>'+tag, value)
        msg = msg + data        
    
    return msg

    
def addr_add_zeros(addr):
    alen = len(addr)
    #al hacer & ~3 obtenemos el multiplo de 4 mas cercano por debajo (por eso sumo 4)
    #algoritmo sacado de client.py
    zeros = (((alen+4) & ~3) - alen) 
    addr = addr + '\0'*zeros    
    addr_zeros = addr +','
    return addr_zeros
    
    
def type_tag(value):
    tipo = type(value)
    if tipo == int:
        tag = 'i'
    elif tipo == float:
        tag = 'f'
    elif tipo == bool:
        if value == True:
            tag = 'T'
        if value == False:
            tag = 'F'
            
    return tag

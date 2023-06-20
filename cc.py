#!/usr/bin/python
# -*- coding: utf-8 -*-

abecedario = 'abcdefghijklmnopqrstuvwxyz'

def banner():                                                   
    print ''
    print '  __     ___  __        __   __   __      __   ___  __        __  '
    print ' /  ` | |__  |__)  /\  |  \ /  \ |__)    /  ` |__  /__`  /\  |__) '
    print ' \__, | |    |  \ /--\ |__/ \__/ |  \    \__, |___ .__/ /--\ |  \ '
    print '                                                      by: wh04m1 ◐  '
    print '──────━━━━━━━━── ● Elige tu lado y diviértete... ○ ──━━━━━━━━──────'
    print ''

def cifrar(texto, clave):

    textocifrado = ''

    for letra in texto:
        suma = abecedario.find(letra) + clave
        modulo = int(suma) % len(abecedario)
        textocifrado = textocifrado + str(abecedario[modulo])
    
    return textocifrado

def descifrar(texto, clave):

    textodescifrado = ''

    for letra in texto:
        resta = abecedario.find(letra) - clave
        modulo = int(resta) % len(abecedario)
        textodescifrado = textodescifrado + str(abecedario[modulo])
    
    return textodescifrado

def main():
    print ''
    cifrado = str(raw_input('[?] Ingrese texto a cifrar: ')).lower()
    print ''
    clavecifrado = int(raw_input('[?] Ingrese clave de cifrado: '))
    print ''
    print '[+] Texto cifrado: ' + cifrar(cifrado, clavecifrado)
    print ''
    print ''
    print ''
    descifrado = str(raw_input('[?] Ingrese texto a descifrar: ')).lower()
    print ''
    clavedescifrado = int(raw_input('[?] Ingrese clave de descifrado: '))
    print ''
    print '[+] Texto descifrado: ' + descifrar(descifrado, clavedescifrado)

if __name__ == "__main__":
    banner()
    main()

# ESERCIZIO CON LE VLAN

Ci sono tre VLAN:

1)nome: Tecnico, numero: 10

2)nome: Amministrazione, numero: 20

3)nome: Accoglienza, numero: 30

---------------------------------------------------------------------

tec: 192.168.0.0/26

Converto in binario l'Ip => 11000000.10101000.00000000.00000000

sub: 255.255.255.192

Coverto in binario la sub => 11111111.11111111.11111111.11000000

Faccio la NOT della sub = >  00000000.00000000.00000000.00111111

Calcolo il broadcast => 11000000.10101000.00000000.00111111

Converto il broadcast in decimale => 192.168.0.63

---------------------------------------------------------------------

amm: 192.168.0.64/26

Converto in binario l'Ip =>

Faccio la NOT della sub = >

Calcolo il broadcast =>

Converto il broadcast in decimale => br: 192.168.0.127

---------------------------------------------------------------------

acc:192.168.0.128

Converto in binario l'Ip =>

Faccio la NOT della sub = >

Calcolo il broadcast =>

Converto il broadcast in decimale => br:192.168.0192

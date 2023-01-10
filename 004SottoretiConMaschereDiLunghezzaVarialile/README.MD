# SOTTORETI CON MASCHERE DI LUNGHEZZA VARIABILE(VLSM)

Rete base: 192.168.5.0/24 

rete A: 14 host

rete B: 28 hosts

rete C: 2 hosts

rete D: 7 hosts

rete E: 28 hosts


1°)

14 host + 2 = 2^4 = 16 >= 16

8-4= 4

maschera di rete => 4+24= 28


Ip => 192.168.5.0/28

Conversione in binario dell'Ip

11000000.10101000.00000101.00000000


sub => 255.255.255.240

Conversione in binario della sub

11111111.11111111.11111111.11110000

Faccio la NOT della sub

00000000.00000000.00000000.00001111


Faccio la OR con l' Ip

11000000.10101000.00000101.00001111

Conversione in decimale

br => 192.168.5.15


2°)
28 host + 2 =



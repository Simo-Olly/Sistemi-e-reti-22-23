# SOTTORETI CON MASCHERE DI LUNGHEZZA VARIABILE(VLSM)

Rete base: 192.168.5.0/24
rete A: 14 host
rete B: 28 hosts
rete C: 2 hosts
rete D: 7 hosts
rete E: 28 hosts

1°)
14 host + 2 = 2^5 = 32 > 16
8-5= 3
maschera di rete => 3+24= 27

Ip => 192.168.0.0/27
Conversione in binario
11000000.10101000.00000000.00000000

subnet-masck => 255.255.255.224
Conversione in binario
11111111.11111111.11111111.11100000
Faccio la NOT
00000000.00000000.00000000.00011111

Faccio la OR con l' Ip

11000000.10101000.00000101.00011111
Conversione in decimale
br => 192.168.0.31

2°)



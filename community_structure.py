import sys
import argparse
import itertools
import pprint
import math

    
parser = argparse.ArgumentParser()
parser.add_argument("-n",  "--modulus", type=int)
parser.add_argument("arxeio_grafou")
args = parser.parse_args()

g = {}

with open(args.arxeio_grafou) as graph_input:
    for line in graph_input:
        nodes = [int(x) for x in line.split()]
        if len(nodes) != 2:
            continue
        if nodes[0] not in g: g[nodes[0]] = []
        if nodes[1] not in g: g[nodes[1]] = []
        g[nodes[0]].append(nodes[1])
                
lista_omadwn = []

for i in g.keys():
    lista_omadwn.append(i)    
    
plithos_komvwn = len(lista_omadwn)
lista_omadwn.sort()
n=plithos_komvwn

Q = 0
a = 0    
#afou akoma exoume omades mono me 1 melos tote to eii=0, diladi sundeseis metaksi twn melwn twn kathe omadwn, ara Q0 = S(-a^2).
for i in lista_omadwn:
    for j in g[i]:
       a = (a + 1) / n
    Q = Q - (a^2) # arxiko Q
    
Eii = 0
Ejj = 0
Eij = 0
Ai = 0
Aj = 0
b = 0
maxim = 0
t = []
DQ = {}
if args.modulus:
    w = args.modulus
else:
    w = 3
while len(lista_omadwn)> w:
    for c in itertools.combinations( lista_omadwn , 2 ):
        if (c[0] in g[c[1]]) or (c[1] in g[c[0]]) : # elexgw ean ta group pou exw exoun kapoia odws sundesh 
            l=[c[0]]
            for melos in l:
                count = 0
                COUNT = 0
                for neighbor in g[melos]:
                    if neighbor in l:
                        COUNT +=2 # afou einai diplis katefphinsis
                        count +=2
                    else:
                        count +=1 # otan metraei tis sindeseis poy MONO(ti mia fora) kataleigoun sthn omada
                Ai = count
                Eii = COUNT
            k = [c[1]]
            for melos in k:
                count = 0
                COUNT = 0
                for neighbor in g[melos]:
                    if neighbor in k:
                        COUNT +=2
                        count +=2
                    else:
                        count +=1
                Aj = count
                Ejj = COUNT
            for i,j in zip(l,k): # upologismos twn sundesewn metaksi twn omadwn i,j pros enwsh
                for neighbor in g[i]:
                    if neighbor in g[j]:
                        Eij +=1
            b = 2*(Eij - Ai*Aj)
            DQ[c] = b
            if b > maxim: # evresi max DQ kai ekeines tis omades poy to paragoun.
                maxim = b
                t =[c[0],c[1],c] # c[0]:omada i, c[1]:omada j, c: h enwsh tous
    Q = Q + b
    print(lista_omadwn)
    print("\n\n")
    print(t)
    print("\n\n")   
    lista_omadwn.remove(t[0])
    lista_omadwn.remove(t[1])
    lista_omadwn.append(t[2])
    r=[]
    r= g[t[0]] + g[t[1]]
    g[t[2]]=r
    del g[t[0]]
    del g[t[1]]
        
for i in lista_omadwn:
    print (i)

print ('Q = {}'.format(Q))

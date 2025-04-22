a=["JUAN",20,1.8,True]

print(a[len(a)-1])
print(a[-1])
print(a[-2])

b=[4,2,6,3]
print(len(b))
print(sum(b))
print(max(b))
print(min(b))
print(sum(b)/len(b))

c = a+b
print(c) 

for x in b:
    print(x)
#DESTRUCTURACION
p="mesa"
q="silla"
print (p,q)
tmp=p
p=q
q=tmp
print (p,q)
p,q=q,p
print(a,b)

def suma5(e,f):
    return e+5, f+5
print (suma5(2,5))

def suma5(e,f):
    return e+5, f+5
x,y = suma5(2,5)
print (x,y)

busca=5
if busca in b: #[4,2,6,3]
    print("Encontrado")
    
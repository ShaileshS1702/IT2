from ast import For


class Planet:
    def __init__(self, navn, solavstand, radius):
        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius

    def test(self):
        return self.solavstand * self.radius

mars = Planet("Mars", 227.90, 3389.50)
print(mars.test())

def fakultet(n):
    if n == 1:
        return n
    else:
        return n*fakultet(n-1)

print(fakultet(7))

for i in range(1,11):
    print(f"fakultetet av {i} er {fakultet(i)}")


tall= [1,4,5,7,8,435,9,90,0,0,45,00,0,0,0,4125,65,63,64,8]
tall2 =  (i for i in tall)
print(tall2)
[print(i+201) for i in tall2]


def shailesh(var1:int, var2:int) -> int:
    """
    Koden tar inn to parametere var1, var 2.
    Koden opphøyer var1 i var2 og returnerer verdien
    """
    return var1**var2

print(shailesh(5,3), "ef")


i=1
while True:
  print(11*i%12,i, "I")
 
  if 11*i%12 == 0:
    print(11*i%12,i, "S")

    break
  i+=1
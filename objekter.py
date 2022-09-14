"""
prosjekter jeg kan prøve:
    class med personer
    class med figurer for turtle
    class som lager starten av et class
    noe med arv
"""

from pydoc import plain
from site import venv
import turtle as tr


class Personer:
    def __init__(self, navn:str, alder:int, karakterer:list):
        self.navn = navn
        self.alder = alder
        self.karakterer = karakterer

    def sumKarakterer(self) -> int:
        k = 0
        for i in self.karakterer:
            k += i
        return k


    def snitt(self) -> float:
        snittet = self.sumKarakterer()/len(self.karakterer)
        return snittet

Shailesh = Personer("Shailesh", 18, [6,4,6,4,6,4,2,6,1,3,5])
#print(Shailesh.sumKarakterer())
#print(Shailesh.snitt())

class Planet:
    def __init__(self, navn, mane):
        self.navn = navn
        self.mane = mane

    def info(self):
        if [maane.navn for maane in self.mane.values()] == []:
            print(f"Dette er planeten {self.navn} og har ingen måner")
        else:
            print(f'Dette er planeten {self.navn} og har månene:')
            [print("    -" +maane.navn) for maane in self.mane.values()]

            #print(f"Dette er {self.navn} og har månene {self.mane}" )
    

class Mane:
    def __init__(self, navn):
        self.navn = navn

    def info(self):
        print(f"Dette er månen {self.navn}" )


manen = Mane("Månen")

Jorda = Planet("Jorda", {"Månen":manen})

""" print(manen.info(),Jorda.info())
print(f'"DFD, {Jorda.navn}') """
""" print(Jorda.mane[0].navn) """

Solsystemet = {"Jorda": Jorda}

Deimos = Mane("Deimos")
Phobos = Mane("Phobos")

Mars = Planet("Mars", {"Deimos": Deimos, "Phobos": Phobos})
""" print(Mars.mane["Deimos"].navn)
print(Deimos.info(), "  !!test!!  ")
print(Mars.info()) """
Solsystemet["Mars"] = Mars
""" print(Solsystemet) """

Merkur = Planet("Merkur", {})
Solsystemet["Merkur"] = Merkur

Venus = Planet("Venus", {})
Solsystemet["Venus"] = Venus

""" print(Venus.info())
print(sorted(Solsystemet)) """


def lagClass(name, parametere):
        """
        name er navnete paa classet
        parametere er alle parameterene i init, utenom self
        """
        test = ""
        for a in parametere:
            test += ",  " + a

        """ print(test) """

        print(f"""
class {name}:
    def __init__(self{test}):""")
        [print(f'       self.{i} = {i}') for i in parametere]


""" help(lagClass) """
""" lagClass("Turtle",["lengde", "vinkel", "repetisjoner"] ) """

class Turtle:
    def __init__(self,  lengde,  vinkel,  repetisjoner):
       self.lengde = lengde
       self.vinkel = vinkel
       self.repetisjoner = repetisjoner

    def stjerne(self):
        tr.speed(1000)
        tr.color("red")
        tr.left(135)
        tr.fd(400)
        tr.right(165)
        for i in range(self.repetisjoner):
            
            tr.fd(self.lengde   + i)
            tr.right(self.vinkel)
            tr.fd(2*self.lengde   + i)
            tr.right(-self.vinkel)
            if i % 10 == 0:
                tr.right(90)


        
    
""" test1 = Turtle(10, 34, 100)

test1.stjerne() """

test2 = Turtle(1, 30, 1000)
test2.stjerne()


def shailesh(var1:int, var2:int) -> int:
    """
    Koden tar inn to parametere var1, var 2.
    Koden opphøyer var1 i var2 og returnerer verdien
    """
    return var1**var2

print(shailesh(5,3))

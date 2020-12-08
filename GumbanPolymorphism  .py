class man:
    def sound(self):
        print("Hello")

class girl:
    def sound(self):
        print("Hi")

def makesound(humantype):
    humantype.sound()

girlobj = girl()
manobj = man()
makesound(girlobj)
makesound(manobj)

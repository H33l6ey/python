class mammal:
    def walk(self):
        print("walk")

class dog(mammal):
    pass
     
class cat(mammal):
    def be_annoying(self):
        print("annoying")
    
cat1 =  cat()
cat1.be_annoying

dog1 = dog()
dog1.walk
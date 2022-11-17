# Rock,Paper or Sissior
import random
def gameWin(system,you):
    if system == you:
        return None
    elif system == "R":
        if you == "P":
            return True
        elif you == "S":
            return False
    elif system == "P":
        if you == "S":
            return True
        elif you == "R":
            return False
    elif system == "S":
        if you == "R":
            return True
        elif you == "P":
            return False

print("System Turn: rock(R) paper(P) or sissior(S)?")
system = ""
randNo = random.randint(1,3)
if randNo ==1:
    system == 'R'
elif randNo ==2:
    system =="P"
elif randNo ==3:
    system =="S"

you = input("Your Turn: rock(R) paper(P) or sissior(S)?")
a = gameWin(system,you)

print(f"computer chose{system}")
print(f"You chose{you}")

if a== None:
    print("The game is tie")
elif a:
    print("You Win")
else:
    print("You lose!")




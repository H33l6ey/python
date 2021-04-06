is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")

else:
    print("Have a nice day") 


if is_cold and is_hot:
    print("both are true")

if is_hot or is_cold:
    print("one is true")
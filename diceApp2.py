from random import randint

#Function to roll dice based on input sides and how many to roll
def dice(many):
        result = []
        for i in range(many):
            result.append(randint(1, dx))
        print(result)
        total = print(sum(result))

while True:
    try:
        dx = int(input("How many sides for your dice?: "))
        many = int(input("How many of these do you need to roll?: "))

        if type(dx) == int:
            print("Rolling the dice......")
            dice(many)
        else:
            print("OOPSIE")
    except:
        print("Only numbers please.")












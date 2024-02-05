answer = input("The Point(5,-7) is in: \n a = 1st Quadrant\n b = 2nd Quadrant\n c = 3rd Quadrant\n d = 4th Quadrant\n Answer: ")
answer = answer.strip()
if answer.lower() == "d":
    print('Correct!')
else:
    print("Incorrect!")
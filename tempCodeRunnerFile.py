expected_answers = ["spherical", "sphere", "hollow_sphere", "disk", "cylinder", "point", "star"]
answer = input("""Name three types of styli. If two word answer, use underscore (_)
               Answer:""")
user_words = answer.split()

crosscheck = [word for word in user_words if word.lower() in expected_answers]

if len(crosscheck) >= 3:
    print("Correct!")
    score += 1
else:
    print("Incorrect.")
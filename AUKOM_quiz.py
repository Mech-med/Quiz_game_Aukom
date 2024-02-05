from PIL import Image
import io
import os
import matplotlib.pyplot as plt


print("AUKOM quiz preparation!")

playing = input("Shall we start? ")

if playing.lower() not in ["yes", "y", "ye", "yes!"]:
    quit()


print("Great :)")
score = 0

answer = input("""Which of the following is not a measuring device? 
               a = Micrometer, 
               b = Dial indicator, 
               c = CMM , 
               d = Gap gage \n Answer:""")
answer = answer.strip()
if answer.lower() == "d":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("""Which principle covers the complete gaging of a geometric element? 
               a = The golden rule of metrology, b = Taylor's principle, 
               c = The Abbe comparator principle \n Answer:""")
answer = answer.strip()
if answer.lower() == "b":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Calculate the mean of the following measurement series: Values 1.1 1.1 1.5 1.2 1.1 \n Answer:")
answer = answer.strip()
if answer.lower() in ["1.2", "1,2"]:
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("Calculate the Range of the following measurement series: Values 1.1 1.1 1.5 1.2 1.1 \n Answer:")
answer = answer.strip()
if answer.lower() in ["0.4", "0,4"]:
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("The Point(2,190°) is in: a = 1st Quadrant, b = 2nd Quadrant, c = 3rd Quadrant, d = 4th Quadrant \n Answer:")
answer = answer.strip()
if answer.lower() == "c":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


expected_answers = ["Bright_field_incident_light", "Dark_field_incident_light", "Transmitted_light"]
answer = input("""Which of the following are illumination types for optical sensors?
                Asparagus_field_incident_light
                Bright_field_incident_light
                Grey_light
                Dark_room
                Dark_field_incident_light
                Transmitted_light
                Multiple Answers:""")

user_words = set(word.lower() for word in answer.split())
expected_answer = [ans.lower() for ans in expected_answers]
matching_words = set(user_words) & set(expected_answer)

if len(matching_words) >= 3:
    print("Correct!")
    score += 1
else:
    print("Incorrect.")


answer = input("The Point(2,190°) is in: \n a = 1st Quadrant, b = 2nd Quadrant, c = 3rd Quadrant, d = 4th Quadrant \n Answer:")
answer = answer.strip()
if answer.lower() == "c":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("The Point(5,-7) is in: \n a = 1st Quadrant\n b = 2nd Quadrant\n c = 3rd Quadrant\n d = 4th Quadrant\n Answer: ")
answer = answer.strip()
if answer.lower() == "d":
    print('Correct!')
else:
    print("Incorrect!")


answer = input("""How many translation and rotation axis locks a cylinder: 
               a = 2T and 2R, 
               b = 3T and 3R, 
               c = 1T and 3R, 
               d = 2T and 1R \n Answer: """)
answer = answer.strip()
if answer.lower() == "a":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("The thumb indicates which axis on the Right thumb rule: a = X, b = Y, c = Z \n Answer:")
answer = answer.strip()
if answer.lower() == "c":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")



answer = input("""What are the most sensible units to use when measuring a fit? 
               a =Kilometer 
               b =Dezimeter 
               c = Micrometer 
               d =Nanometer 
               Answer:""")
answer = answer.strip()
if answer.lower() == "c":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("""What are the most sensible units to use when measuring a fit? a = Meter b = Millimeter c =Zentimeter  d =Nanometer 
               Answer:""")
answer = answer.strip()
if answer.lower() == "b":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("""Which statement is incorrect? 
               a = When the axes are perpendicular to another a cartesian coordinate system is established.
               b = A point to the left of the Y axis has a positive X coordinate.
               Answer:""")
answer = answer.strip()
if answer.lower() == "b":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

while True:
    answer = input("Write an angle for a point in the third quadrant? e.g. 10° \n Answer:")
    try:
        answer_float = float(answer.replace(',', '.').strip("°"))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue  # Ask the user for input again

    if 180 <= answer_float <= 270:
        print('Correct!')
        score += 1
        break 
    else:
        print("Incorrect! Please try again.")

#defining the path of the image 
script_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(script_dir, "image1_question.jpg")
image = Image.open(image_path)
image.show()
answer = input("""Which statement is incorrect?
                a = The red coordinate system has first been rotated and then been moved (offset) to get the green coordinate system.
                b = The red coordinate system has first been moved (offset) and then been rotated to get the green coordinate system."
                Answer:""")
image.close()
answer = answer.strip()
if answer.lower() == "a":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

script_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(script_dir, "image2_question.jpg")
image = Image.open(image_path)
image.show()
answer = input("""Match the type to the diagram!
                a Gantry type
                b Bridge type
                c Cantilever type
                d column type
                Answer:""")
image.close()
answer = answer.strip()
if answer.lower() == "a":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

script_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(script_dir, "image3_question.jpg")
image = Image.open(image_path)
image.show()
answer = input("""Match the type to the diagram!
                a Gantry type
                b Bridge type
                c Cantilever type
                d column type
                Answer:""")
image.close()
answer = answer.strip()
if answer.lower() == "c":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")



expected_answers = ["spherical", "sphere", "hollow_sphere", "disk", "cylinder", "point", "star"]
answer = input("""Name three types of styli. If two word answer, use underscore (_)
               Multiple Answers:""")
user_words = answer.split()

crosscheck = [word for word in user_words if word.lower() in expected_answers]

if len(crosscheck) >= 3:
    print("Correct!")
    score += 1
else:
    print("Incorrect.")



expected_answers = ["Through_holes", "Edges"]
answer = input("""Which types of features can be measured with an image processing sensor
                with transmitted light illumination?
                Edges
                Through_holes
                Blind_holes
                Horizontal_surfaces
                Multiple Answers:""")

user_words = set(word.lower() for word in answer.split())
expected_answer = [ans.lower() for ans in expected_answers]
matching_words = set(user_words) & set(expected_answer)

if len(matching_words) >= 2:
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

script_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(script_dir, "image4_question.jpg")
image = Image.open(image_path)
image.show()
expected_answers = ["a", "d"]
answer = input("""Which of the following drawing callouts conforms to specification?
               a
               b
               c
               d \nMultiple Answers:""")

user_words = set(word.lower() for word in answer.split())
expected_answer = [ans.lower() for ans in expected_answers]
matching_words = set(user_words) & set(expected_answer)

if len(matching_words) >= 2:
    print("Correct!")
    score += 1
else:
    print("Incorrect.")


def plot_scores(score):
    labels = ['Correct', 'Incorrect']
    sizes = [score, 20 - score] # Assuming 20 questions in total
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['green', 'red'])
    ax.axis('equal')
    plt.title("Quiz Results")
    plt.show()
plot_scores(score)
result = round(float((score / 20) * 100) , 1) # Assuming 20 questions in total
print("You got " + str(score) + " questions correct!")
print(f"You got  {result}%.") 




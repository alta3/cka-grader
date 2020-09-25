from task01test import task01
from task02test import task02
from task03test import task03
from task04test import task04
from task05test import task05
from task06test import task06
from task07test import task07
from task08test import task08
from task09test import task09
from task10test import task10
from task11test import task11
from task12test import task12
from task13test import task13
from task14test import task14
from task15test import task15
from task16test import task16
from task17test import task17


def main():
    answers = [
            task01(),
            task02(),
            task03(),
            task04(),
            task05(),
            task06(),
            task07(),
            task08(),
            task09(),
            task10(),
            task11(),
            task12(),
            task13(),
            task14(),
            task15(),
            task16(),
            task17()
            ]
    score = [i['points'] for i in answers]
    print(f"\nYou received a {sum(score)}%")
    if sum(score) == 100:
        print("Did you cheat?!? Way to go!")
    if sum(score) > 66:
        print("Congratulations! You passed the practice exam!")
    else:
        print("You need a 66% or better to pass the CKA exam")
    score_output = ""
    for answer in answers:
        score_output += f"\n{answer['task']}, {answer['points']}/{answer['possible']}"
    print(score_output)


if __name__ == "__main__":
    print("Grading your CKA Practice Exam")
    main()

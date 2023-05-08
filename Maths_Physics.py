class Math:
    def _init_(self):
        self.questions = [
            ("What is 2 + 2?", 4),
            ("What is 5 * 3?", 15),
            ("What is the square root of 25?", 5),
            ("What is 10 / 2?", 5),
            ("What is 3 ** 4?", 81)
        ]

class Physics:
    def _init_(self):
        self.questions = [
            ("What is the formula for force?", "F = ma"),
            ("What is the unit of measurement for current?", "Ampere"),
            ("What is the speed of light in a vacuum?", "299,792,458 m/s"),
            ("What is the formula for kinetic energy?", "KE = 0.5 * mv^2"),
            ("What is the SI unit of temperature?", "Kelvin")
        ]

def calculate_math():
    math = Math()
    for question, answer in math.questions:
        print(question)
        user_answer = input("Your answer: ")
        if user_answer == str(answer):
            print("Correct!")
        else:
            print("Incorrect.")

def calculate_physics():
    physics = Physics()
    for question, answer in physics.questions:
        print(question)
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
        else:
            print("Incorrect.")

def main():
    subject = input("Enter 'math' or 'physics': ")
    operation = input("Enter 'calculate' to start: ")

    if subject.lower() == "math" and operation.lower() == "calculate":
        calculate_math()
    elif subject.lower() == "physics" and operation.lower() == "calculate":
        calculate_physics()
    else:
        print("Invalid input. Please try again.")

if __name__ == '__main__':
    main()
from flask import Flask, render_template, request
import random

app = Flask(__name__)

def valid_input(prompt):
    got_valid_input = False
    while got_valid_input == False:
        try:
            answer = int(request.form[prompt])
            got_valid_input = True
        except ValueError:
            print("Invalid input, try again!")
    return answer

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['POST'])
def test():
    number_students_test = int(request.form['number_students_test'])
    scores = []
    for test in range(number_students_test):
        score, time_program_start = main()
        scores.append((score, time_program_start))
    return render_template('result.html', scores=scores)

def main():
    score = 0
    time_program_start = 0
    start = True
    while start:
        num1 = random.randint(10, 20)
        num2 = random.randint(1, 9)
        user_input = int(request.form['user_input'])
        if user_input == 1:
            # 1 Plus question
            question = num1 + num2
            answer = valid_input("answer")
            while answer != question:
                score -= 1
                time_program_start += 1
                answer = valid_input("answer")
            else:
                score += 1
                time_program_start += 1
        elif user_input == 2:
            # 2 subtraction question
            question = num1 - num2
            answer = valid_input("answer")
            while answer != question:
                score -= 1
                time_program_start += 1
                answer = valid_input("answer")
            else:
                score += 1
                time_program_start += 1
        elif user_input == 3:
            # 3 multiplication question
            question = num1 * num2
            answer = valid_input("answer")
            while answer != question:
                score -= 1
                time_program_start += 1
                answer = valid_input("answer")
            else:
                score += 1
                time_program_start += 1
        elif user_input == 4:
            # 4 divide question
            question = round(num1 / num2)
            answer = valid_input("answer")
            while answer != question:
                score -= 1
                time_program_start += 1
                answer = valid_input("answer")
            else:
                score += 1
                time_program_start += 1
        elif user_input == 5:
            start = False
    return score, time_program_start

if __name__ == '__main__':
    app.run(debug=True)

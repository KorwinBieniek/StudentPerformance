import json
import os


NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]


def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card

def main():
    total_mark = 0

    subject_avg_grade = {"math": 0, "science": 0, "history": 0, "english": 0, "geography": 0}
    grade_avg_grade = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for i in range(NUM_STUDENTS):
        student_mark = 0
        report_card = load_report_card(os.getcwd() + '/students/', i)


        for subject in SUBJECTS:
            total_mark += report_card[subject]
            student_mark += report_card[subject]
            subject_avg_grade[subject] += report_card[subject]
            grade_avg_grade[report_card['grade']] += report_card[subject]
        report_card['total_mark'] = student_mark
        if i == 0:
            best_student = report_card
            worst_student = report_card
        if best_student['total_mark'] < report_card['total_mark']:
            best_student = report_card
        if worst_student['total_mark'] > report_card['total_mark']:
            worst_student = report_card

    print('Average Student Grade:', round(total_mark / (len(SUBJECTS) * NUM_STUDENTS), 2))
    print('Hardest Subject:', list(sorted(subject_avg_grade.items(), key=lambda x: x[1]))[0][0])
    print('Easiest Subject:', list(sorted(subject_avg_grade.items(), key=lambda x: x[1]))[-1][0])
    print('Best Performing Grade', list(sorted(grade_avg_grade.items(), key=lambda x: x[1]))[-1][0])
    print('Worst Performing Grade:', list(sorted(grade_avg_grade.items(), key=lambda x: x[1]))[0][0])
    print('Best Student ID:', best_student['id'])
    print('Worst Student ID:', worst_student['id'])


    # report_card = load_report_card(os.getcwd() + '/students/', 10)
    # print(report_card)
    # total_mark = 0
    # for subject in SUBJECTS:
    #     total_mark += report_card[subject]
    # print(total_mark / len(SUBJECTS))

if __name__ == '__main__':
    main()

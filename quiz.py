import json


class Quiz:
    def __init__(self, quiz_name, time_limit, question_list,
                 answer_list, correct_answer_list):
        self.quiz_name = quiz_name
        self.time_limit = time_limit
        self.question_list = question_list
        self.answer_list = answer_list
        self.correct_answer_list = correct_answer_list

    def to_json(self):
        questions = []
        for i in range(len(self.question_list)):
            question = {
                "question": self.question_list[i],
                "answer_list": self.answer_list[i],
                "correct_answer": self.correct_answer_list[i]
            }
            questions.append(question)
        with open('quiz_parser.json', 'w') as f:
            json.dump({"quiz_name": self.quiz_name, "time_limit": self.time_limit,
                      "question_list": questions}, f, indent=4)

    @staticmethod
    def from_json():
        with open('quiz_parser.json') as f:
            data = json.load(f)
        question_list = []
        answer_list = []
        correct_answer_list = []
        quiz_name = data['quiz_name']
        time_limit = data['time_limit']
        for iterator in data['question_list']:
            question_list.append(iterator['question'])
            answer_list.append(iterator['answer_list'])
            correct_answer_list.append(iterator['correct_answer'])
        return Quiz(quiz_name, time_limit, question_list,
                    answer_list, correct_answer_list)

import unittest
import json
from src.quiz import Quiz


class TestQuiz(unittest.TestCase):
    def test_to_json(self):
        quiz = Quiz(
            quiz_name="Math Quiz",
            time_limit=30,
            question_list=[
                "What is 2+2?",
                "What is the square root of 64?",
                "What is the capital of France?",
            ],
            answer_list=[
                ["4", "3", "5", "2"],
                ["4", "6", "8", "10"],
                ["Paris", "Rome", "Madrid", "Berlin"],
            ],
            correct_answer_list=["4", "8", "Paris"],
        )
        quiz.to_json()
        with open("quiz_parser_test.json") as f:
            data = json.load(f)
        self.assertEqual(data["quiz_name"], "Math Quiz")
        self.assertEqual(data["time_limit"], 30)
        self.assertEqual(
            data["question_list"],
            [
                {
                    "question": "What is 2+2?",
                    "answer_list": ["4", "3", "5", "2"],
                    "correct_answer": "4",
                },
                {
                    "question": "What is the square root of 64?",
                    "answer_list": ["4", "6", "8", "10"],
                    "correct_answer": "8",
                },
                {
                    "question": "What is the capital of France?",
                    "answer_list": ["Paris", "Rome", "Madrid", "Berlin"],
                    "correct_answer": "Paris",
                },
            ],
        )

    def test_from_json(self):
        with open("quiz_parser_test.json", "w") as f:
            json.dump(
                {
                    "quiz_name": "Math Quiz",
                    "time_limit": 30,
                    "question_list": [
                        {
                            "question": "What is 2+2?",
                            "answer_list": ["4", "3", "5", "2"],
                            "correct_answer": "4",
                        },
                        {
                            "question": "What is the square root of 64?",
                            "answer_list": ["4", "6", "8", "10"],
                            "correct_answer": "8",
                        },
                        {
                            "question": "What is the capital of France?",
                            "answer_list": ["Paris", "Rome", "Madrid", "Berlin"],
                            "correct_answer": "Paris",
                        },
                    ],
                },
                f,
            )
        quiz = Quiz.from_json()
        self.assertEqual(quiz.quiz_name, "Math Quiz")
        self.assertEqual(quiz.time_limit, 30)
        self.assertEqual(
            quiz.question_list,
            [
                "What is 2+2?",
                "What is the square root of 64?",
                "What is the capital of France?",
            ],
        )
        self.assertEqual(
            quiz.answer_list,
            [
                ["4", "3", "5", "2"],
                ["4", "6", "8", "10"],
                ["Paris", "Rome", "Madrid", "Berlin"],
            ],
        )
        self.assertEqual(quiz.correct_answer_list, ["4", "8", "Paris"])


if __name__ == "__main__":
    unittest.main()

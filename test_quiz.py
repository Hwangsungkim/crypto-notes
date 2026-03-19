# test_quiz.py
import data_handler

def test_get_quiz_question():
    # 퀴즈 모드에서 쓸 문제를 하나 가져옵니다.
    quiz = data_handler.get_quiz_question()
    
    # 퀴즈 데이터가 정상적으로 존재해야 하고, '질문(question)'과 '정답(answer)'이 있어야 합니다.
    assert type(quiz) is dict
    assert "question" in quiz
    assert "answer" in quiz

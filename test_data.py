# test_data.py
import data_handler

def test_get_dummy_notes():
    # '기초 용어' 카테고리의 노트를 요청합니다.
    notes = data_handler.get_dummy_notes("기초 용어")
    
    # 노트가 최소 1개 이상 있어야 하고, 첫 번째 제목이 '비트코인'이어야 테스트 통과!
    assert len(notes) > 0
    assert "비트코인" in notes[0]["title"]

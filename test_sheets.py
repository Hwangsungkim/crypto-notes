# test_sheets.py
import data_handler

def test_get_real_notes():
    # 구글 시트에서 '기초 용어' 카테고리의 실제 데이터를 가져옵니다.
    notes = data_handler.get_real_notes("기초 용어")
    
    # 결과가 리스트(목록) 형태여야 통과합니다.
    assert type(notes) is list

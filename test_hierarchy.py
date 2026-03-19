# test_hierarchy.py

def get_sub_categories(main_category):
    # 이 함수가 실제 앱에 구현될 로직의 핵심입니다.
    hierarchy = {
        "비트코인 (BTC)": ["비트코인: 탄생과 역사", "비트코인: 반감기와 공급", "비트코인: 네트워크 (PoW)"],
        "이더리움 (ETH)": ["이더리움 기초 용어", "이더리움: 레이어 1 (L1)", "이더리움: 레이어 2 (L2)", "이더리움: 디앱 (DeFi/DEX/DAO)"],
        "일반 기초 (Basic)": ["일반 기초 용어"],
        "학습 도구 (Tools)": ["퀴즈 모드 🧠"]
    }
    return hierarchy.get(main_category, [])

def test_ethereum_subcategories():
    # 이더리움을 선택했을 때 새로 추가한 '기초 용어'가 있는지 검증합니다.
    subs = get_sub_categories("이더리움 (ETH)")
    assert "이더리움 기초 용어" in subs
    assert len(subs) == 4

def test_bitcoin_subcategories():
    # 비트코인 하위 메뉴 개수 검증
    subs = get_sub_categories("비트코인 (BTC)")
    assert len(subs) == 3

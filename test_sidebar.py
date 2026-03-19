## test_sidebar.py

def test_expected_categories():
    # 1. 우리가 확정한 8가지 목표 카테고리
    expected = [
        "비트코인: 탄생과 역사",
        "비트코인: 반감기와 공급",
        "비트코인: 네트워크 (PoW)",
        "이더리움: 레이어 1 (L1)",
        "이더리움: 레이어 2 (L2)",
        "이더리움: 디앱 (DeFi/DEX/DAO)",
        "기초 용어",
        "퀴즈 모드 🧠"
    ]
    
    # 2. 현재 앱에 적용된 실제 카테고리 (들여쓰기 완료!)
    current_categories = [
        "비트코인: 탄생과 역사",
        "비트코인: 반감기와 공급",
        "비트코인: 네트워크 (PoW)",
        "이더리움: 레이어 1 (L1)",
        "이더리움: 레이어 2 (L2)",
        "이더리움: 디앱 (DeFi/DEX/DAO)",
        "기초 용어",
        "퀴즈 모드 🧠"
    ]
    
    # 3. 하나씩 대조하며 확인
    for category in expected:
        assert category in current_categories, f"{category} 가 목록에 없습니다!"

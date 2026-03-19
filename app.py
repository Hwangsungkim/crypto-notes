import streamlit as st
import data_handler

# 1. 페이지 기본 설정
st.set_page_config(page_title="Crypto Digital Note", page_icon="📓", layout="wide")

# 2. 좌측 사이드바 구성
# app.py (수정 부분)
# app.py 의 사이드바 부분

# app.py (사이드바 부분 정밀 수정)

with st.sidebar:
    st.title("📂 카테고리")
    
    # 1. 상위 카테고리 선택 (Selectbox)
    main_category = st.selectbox(
        "대분류 선택:",
        ["비트코인 (BTC)", "이더리움 (ETH)", "일반 기초 (Basic)", "학습 도구 (Tools)"]
    )
    
    # 2. 상위 선택에 따른 하위 카테고리 지도 (Dictionary)
    hierarchy = {
        "비트코인 (BTC)": ["비트코인: 탄생과 역사", "비트코인: 반감기와 공급", "비트코인: 네트워크 (PoW)"],
        "이더리움 (ETH)": ["이더리움 기초 용어", "이더리움: 레이어 1 (L1)", "이더리움: 레이어 2 (L2)", "이더리움: 디앱 (DeFi/DEX/DAO)"],
        "일반 기초 (Basic)": ["일반 기초 용어"],
        "학습 도구 (Tools)": ["퀴즈 모드 🧠"]
    }
    
    # 3. 하위 카테고리 선택 (Radio) - 위 지도에서 리스트를 가져옵니다.
    category = st.radio(
        "소분류 선택:",
        hierarchy[main_category]
    )
    
    st.markdown("---")
    st.write("나만의 크립토 디지털 공책 v1.0")

# 3. 메인 화면 구성
st.title("📓 크립토 학습 디지털 공책")
st.subheader(f"현재 선택된 탭: 📌 {category}")

# 4. 퀴즈 모드 로직
if category == "퀴즈 모드 🧠":
    st.write("### 🎯 오늘의 크립토 퀴즈")
    
    # 데이터 핸들러에서 퀴즈 하나를 가져옵니다.
    quiz = data_handler.get_quiz_question()
    st.info(f"**Q. {quiz['question']}**")
    
    # 3가지 학습 모드를 탭(Tab)으로 나눕니다.
    tab1, tab2, tab3 = st.tabs(["💡 플래시카드", "✍️ 주관식", "✅ 객관식"])
    
    with tab1:
        st.write("머릿속으로 정답을 먼저 떠올려 보세요!")
        if st.button("정답 보기 👀"):
            st.success(f"정답: {quiz['answer']}")
            
    with tab2:
        user_answer = st.text_input("정답을 입력하세요:")
        if st.button("제출", key="subjective_btn"):
            if user_answer == quiz['answer']:
                st.balloons() # 정답일 때 풍선 애니메이션!
                st.success("정답입니다! 🎉")
            elif user_answer:
                st.error("오답입니다. 다시 시도해 보세요!")
                
    with tab3:
        # 보기들을 라디오 버튼으로 보여줍니다.
        choice = st.radio("보기에서 정답을 고르세요:", quiz['options'], index=None)
        if st.button("제출", key="objective_btn"):
            if choice == quiz['answer']:
                st.balloons()
                st.success("정답입니다! 🎉")
            elif choice:
                st.error("오답입니다. 다시 시도해 보세요!")

# 5. 일반 노트 로직
else:
    notes = data_handler.get_real_notes(category)
    if notes:
        for note in notes:
            with st.expander(f"📝 {note['title']}", expanded=True):
                st.markdown(note['content'])
    else:
        st.warning("아직 작성된 노트가 없습니다. 새로운 내용을 추가해 보세요!")

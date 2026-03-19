import streamlit as st
import data_handler  # 우리가 방금 만든 데이터 모듈을 불러옵니다!

# 1. 페이지 기본 설정
st.set_page_config(page_title="Crypto Digital Note", page_icon="📓", layout="wide")

# 2. 좌측 사이드바 구성
with st.sidebar:
    st.title("📂 카테고리")
    category = st.radio(
        "학습 주제를 선택하세요:",
        ["기초 용어", "블록체인 구조", "디파이(DeFi)", "퀴즈 모드 🧠"]
    )
    st.markdown("---")
    st.write("나만의 크립토 디지털 공책 v1.0")

# 3. 메인 화면 구성
st.title("📓 크립토 학습 디지털 공책")
st.subheader(f"현재 선택된 탭: 📌 {category}")

# 4. 선택된 카테고리에 맞는 데이터 불러와서 화면에 그리기
if category == "퀴즈 모드 🧠":
    st.info("퀴즈 모드는 다음 태스크에서 구현됩니다! 🚀")
else:
    # data_handler를 통해 가짜 데이터를 가져옵니다.
    notes = data_handler.get_dummy_notes(category)
    
    # 가져온 노트가 있다면 화면에 아코디언(expander) 형태로 예쁘게 펼쳐줍니다.
    if notes:
        for note in notes:
            with st.expander(f"📝 {note['title']}", expanded=True):
                st.markdown(note['content'])
    else:
        # 노트가 없는 카테고리일 경우 경고창을 띄웁니다.
        st.warning("아직 작성된 노트가 없습니다. 새로운 내용을 추가해 보세요!")

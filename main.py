import streamlit as st
import time

def main():
    st.title("단어 보여주기 앱")

    # 사용자 입력
    sentence = st.text_input("문장을 입력하세요:")
    words = sentence.split()

    # 분당 보여줄 단어 수 조절
    words_per_minute = st.slider("분당 보여줄 단어 수", 1, 300, 10)

    # 단어를 보여줄 컨테이너 생성
    word_container = st.empty()

    # 반복 기능
    if st.button("시작"):
        for word in words:
            # 이전 단어를 지우고 새로운 단어로 대체
            word_container.markdown(f"<h1 style='font-size: 100px;'>{word}</h1>", unsafe_allow_html=True)
            time.sleep(60 / words_per_minute)  # 분당 단어 수에 따라 대기
        st.write("모든 단어를 보여주었습니다.")

if __name__ == "__main__":
    main()

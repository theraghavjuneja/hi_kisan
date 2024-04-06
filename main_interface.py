import streamlit as st
import pyttsx3
from return_statements import heading_statements,image_uploader

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    st.title('HI-KISAN')
    st.sidebar.title('Language/भाषा')
    language = st.sidebar.selectbox("", ["English", "Hindi"])
    heading_statement = heading_statements()

    if language == "English":
        for i, statement in enumerate(heading_statement):
            col1, col2 = st.columns([3, 1])  # Adjust the ratio as per your preference
            with col1:
                st.write(statement)
            with col2:
                st.button(f"Listen", key=f"speak_{i}", on_click=lambda text=statement: text_to_speech(text))
        image_uploader()  
    elif language == 'Hindi':
        pass

if __name__ == "__main__":
    main()

import streamlit as st
import pyttsx3
from return_statements import heading_statements, image_uploader

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  
    engine.setProperty('voice', 'hindi')  
    engine.say(text)
    engine.runAndWait()

def main():
    st.title('HI-KISAN')
    st.sidebar.title('Language/भाषा')
    language = st.sidebar.selectbox("", ["English", "Hindi"])
    screens = st.selectbox("Choose screens", ["Main Screen","Crop Predictor", "Chat with AI", "Screen 3", "Screen 4", "Screen 5"])
    if screens=="Main Screen":
        if language=="English":
            heading_statement = heading_statements()
            for i, statement in enumerate(heading_statement):
                col1, col2 = st.columns([3, 1]) 
                with col1:
                    st.write(statement)
                with col2:
                    st.button(f"Listen", key=f"speak_{i}", on_click=lambda text=statement: text_to_speech(text))     
        
    if screens=="Crop Predictor":
        image_uploader()

    
          
    

if __name__ == "__main__":
    main()

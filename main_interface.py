import streamlit as st
import pyttsx3
from return_statements import heading_statements, image_uploader,h_heading
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters
import os
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
    screens = st.selectbox("Choose screens", ["Main Screen","Crop Predictor", "Chat with AI", "Live Crop Prices by Government", "Screen 4", "Screen 5"])
    if screens=="Main Screen":
        if language=="English":
            heading_statement = heading_statements()
            for i, statement in enumerate(heading_statement):
                col1, col2 = st.columns([3, 1]) 
                with col1:
                    st.write(statement)
                with col2:
                    st.button(f"Listen", key=f"speak_{i}", on_click=lambda text=statement: text_to_speech(text))     
        elif language=="Hindi":
            heading_state=h_heading()
            for i in heading_state:
                st.write(i)
        
    if screens=="Crop Predictor":
        if language=="English":
            image_uploader("English")
        if language=="Hindi":
            image_uploader("Hindi")
        
    if screens=="Chat with AI":
        from dotenv import load_dotenv
        import google.generativeai as gen_ai

        load_dotenv()

        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

        gen_ai.configure(api_key=GOOGLE_API_KEY)
        model = gen_ai.GenerativeModel('gemini-pro')

        def translate_role_for_streamlit(user_role):
            if user_role == "model":
                return "assistant"
            else:
                return user_role

        if "chat_session" not in st.session_state:
            st.session_state.chat_session = model.start_chat(history=[])

        st.subheader("🤖 FarmHelper - ChatBot")

        for message in st.session_state.chat_session.history:
            with st.chat_message(translate_role_for_streamlit(message.role)):
                st.markdown(message.parts[0].text)

        user_prompt = st.chat_input("Ask me about crops...")

        if user_prompt:
            # Check if the user prompt contains farming-related keywords
            farming_keywords = [
            "thankyou", "soil", "rabi", "kharif", "crops", "land", "harvesting", "thanks", "great", "farm", 
            "livestock", "harvest", "agriculture", "irrigation", "tractors", "seeds", "fertilizers", "pesticides", 
            "crop rotation", "organic farming", "greenhouse", "horticulture", "aquaculture", "agribusiness", 
            "ranching", "agroforestry", "hello", "hi", "hey", "thankyou", "wheat", "rain", "barley", "rain", 
            "pesticide", "fungus", "crop rotation", "irrigation", "harvest", "fertilizer", "tractor", "plow", 
            "drought", "crop yield", "soil erosion", "weed control", "compost", "organic farming", "greenhouse", 
            "crop disease", "agricultural machinery", "soil pH", "crop insurance", "livestock", "agribusiness", 
            "crop protection", "agronomy", "agricultural science", "crop diversity", "agricultural extension", 
            "crop monitoring", "precision agriculture", "farm management", "soil fertility", "crop genetics", 
            "farm subsidy", "hydroponics", "soil conservation", "grain storage", "crop rotation", "agrochemicals", 
            "crop nutrition", "livestock management", "farm equipment", "soil health", "crop pest", 
            "harvesting equipment", "crop planting", "agricultural economics", "sustainable agriculture", 
            "plantation", "permaculture", "cover crops", "intercropping", "cash crops", "food security", 
            "vertical farming", "soil salinity", "livestock feed", "crop scouting", "biodynamic farming", 
            "food sovereignty", "agroecology", "soil testing", "crop genetics", "forage crops", "seed bank", 
            "agricultural subsidies", "silo", "crop management", "integrated pest management", "pasture rotation", 
            "fodder", "livestock breeding", "precision planting", "nutrient management", "farming technology", 
            "crop forecasting", "farm diversification", "food miles", "agricultural sustainability", 
            "farm infrastructure", "seed treatment", "drip irrigation", "water management", "farm labor", 
            "harvest storage", "post-harvest handling", "microclimate", "biotechnology in agriculture", 
            "farmland preservation", "crop scouting", "agricultural education", "farm succession planning", 
            "soil remediation", "agricultural marketing", "community-supported agriculture (CSA)", 
            "farm-to-table", "livestock health", "crop physiology", "farmers market", "soil compaction", 
            "farm bill", "food waste reduction", "agritourism", "farm safety", "crop innovation", 
            "agricultural grants", "dairy farming", "beekeeping", "viticulture", "agricultural policy", 
            "food labeling", "farm subsidies", "land use planning", "agricultural research", 
            "food and agriculture organization (FAO)", "agro-tourism", "farm succession", "seed saving", 
            "food preservation", "farming techniques", "livestock diseases", "green manure", "farm budgeting", 
            "soil analysis", "crop modeling", "farmer's markets", "food distribution", "agroecosystem", 
            "farming communities", "farm grants", "crop genetics", "soil amendment", "farm accounting", 
            "agricultural development", "farm risk management", "agrarian reform", "animal husbandry", 
            "agricultural policy", "land tenure", "crop genetics", "animal welfare", "farmworkers", 
            "sustainable land management", "agricultural innovation", "farm loans", "food processing", 
            "farm technology", "agrifood", "farm diversification", "soil biodiversity", "farmers' rights","grow","strategy","planted","cultivated"
            ]

            if any(keyword in user_prompt.lower() for keyword in farming_keywords):
                st.chat_message("user").markdown(user_prompt)
                gemini_response = st.session_state.chat_session.send_message(user_prompt)
                with st.chat_message("assistant"):
                    st.markdown(gemini_response.text)
            else:
                st.error("Sorry, your question seems unrelated to farming.")
    if screens=="Live Crop Prices by Government":
        data = pd.read_csv("commodities_data.csv")
        df = pd.DataFrame(data)

        dynamic_filters = DynamicFilters(df, filters=['State', 'District', 'Market','Commodity'])


        dynamic_filters.display_filters()


        dynamic_filters.display_df()


    
          
    

if __name__ == "__main__":
    main()

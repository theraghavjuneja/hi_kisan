import streamlit as st
import pyttsx3
from return_statements import heading_statements, image_uploader,h_heading
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters
import os
from dotenv import load_dotenv
import requests
from datetime import datetime
import pandas as pd
import plotly.graph_objs as go
import base64
load_dotenv()
API_KEY=os.getenv("OPEN_WEATHER_API")
def fetch_data_from_api(city):
    api_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appId=9fbad4ea130c7759ec312350195588c1'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data from API. Status code: {response.status_code}")
        return None
def timestamp_to_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
def display_tabular(data):
    rows = []
    humidity_data = []
    temperature_data = []
    for item in data['list']:
        timestamp = timestamp_to_datetime(item['dt'])
        temperature = item['main']['temp']
        humidity = item['main'].get('humidity', '-')
        weather_description = item['weather'][0]['description']
        rows.append([timestamp, temperature, humidity, weather_description])
        humidity_data.append((timestamp, humidity))
        temperature_data.append((timestamp, temperature))
    df = pd.DataFrame(rows, columns=['Date and Time', 'Temperature (°K)', 'Humidity (%)', 'Weather Description'])
    return df, humidity_data, temperature_data

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
    
    screens_dict = {
     "मुख्य स्क्रीन":"Main Screen",
     "फसल की पूर्वानुमान":"Crop Predictor",
     "एआई के साथ चैट करें":"Chat with AI",
     "सरकार द्वारा लाइव फसल के मूल्य":"Live Crop Prices by Government" ,
     "मौसम की जाँच करें":"Check Weather"  
    }
    if(language=="English"):    
        screens = st.selectbox("Choose screens", ["Main Screen","Crop Predictor", "Chat with AI", "Live Crop Prices by Government","Check Weather"])
    if(language=="Hindi"):
        screens = st.selectbox("Choose screens", list(screens_dict.keys()), index=0)
        screens=screens_dict[screens]
    

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
        if language=="English":    
            st.subheader("🤖 FarmHelper - ChatBot")
        elif language=="Hindi":
            st.subheader("🤖 फार्महेल्पर चैटबॉट")

        for message in st.session_state.chat_session.history:
            with st.chat_message(translate_role_for_streamlit(message.role)):
                st.markdown(message.parts[0].text)
        if language=='English':
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
        if language=='Hindi':
            user_prompt = st.chat_input("आप मुझसे फसलों के बारे में पूछ सकते हैं")
            if user_prompt:
                st.chat_message("user").markdown(user_prompt)
                gemini_response = st.session_state.chat_session.send_message(user_prompt)
                with st.chat_message("assistant"):
                    st.markdown(gemini_response.text)

        
    if screens=="Live Crop Prices by Government":
        data = pd.read_csv("commodities_data.csv")
        df = pd.DataFrame(data)

        dynamic_filters = DynamicFilters(df, filters=['State', 'District', 'Market','Commodity'])


        dynamic_filters.display_filters()


        dynamic_filters.display_df()
    if screens=="Check Weather":
        st.title("Weather Data")
        city = st.text_input('Enter city name:', 'New York')
        data = fetch_data_from_api(city)

        if data:
            df, humidity_data, temperature_data = display_tabular(data)
            st.subheader('Weather Data:')
            st.write(df)
            
            st.subheader('Humidity Variation')
            fig_humidity = go.Figure()
            fig_humidity.add_trace(go.Scatter(x=[item[0] for item in humidity_data], y=[item[1] for item in humidity_data], mode='lines', name='Humidity (%)'))
            st.plotly_chart(fig_humidity)

            st.subheader('Temperature Variation')
            fig_temperature = go.Figure()
            fig_temperature.add_trace(go.Scatter(x=[item[0] for item in temperature_data], y=[item[1] for item in temperature_data], mode='lines', name='Temperature (°K)'))
            st.plotly_chart(fig_temperature)

            st.subheader('Notes')
            notes = st.text_area("Write your notes here:")
            
            # Download button
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="weather_data.csv">Download weather data</a>'
            st.markdown(href, unsafe_allow_html=True)


    
          
    

if __name__ == "__main__":
    main()

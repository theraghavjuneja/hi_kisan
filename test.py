import streamlit as st

screens_dict = {
     "मुख्य स्क्रीन":"Main Screen",
     "फसल की पूर्वानुमान":"Crop Predictor",
     "एआई के साथ चैट करें":"Chat with AI",
     "सरकार द्वारा लाइव फसल के मूल्य":"Live Crop Prices by Government"
}

screens = st.selectbox("Choose screens", list(screens_dict.keys()), index=0)
screens=screens_dict[screens]
st.write(screens)
# selected_screen = [key for key, value in screens_dict.items() if value == screens][0]

# st.write("Selected screen:", selected_screen)

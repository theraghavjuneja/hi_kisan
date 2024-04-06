import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from googletrans import Translator
import os
import json
def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text
with open("disease_mapping.json", "r") as f:
    mapping = json.load(f)


def load_pretrained_model():
    return load_model('model.h5')


def heading_statements():
    return ['This app can predict crop diseases, generate solutions to diseases, help farmers by knowing the current prices of crops',
            'We also have a chat with AI option where you can ask anything about farming',
            'Refer [here](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset) for information']


def image_uploader(language):
    if language=="English":    
        st.subheader("Upload diseased leaf image of your crop")
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        st.info("Make sure you upload a clear leaf image")
        if uploaded_file is None:
            st.sidebar.warning("Status: Image not uploaded")
        else:
            st.sidebar.success('Image uploaded succesfully')
            st.sidebar.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
            if(st.sidebar.button("SUBMIT FOR PREDICTION")):
                loaded_model = load_pretrained_model()
                img = image.load_img(uploaded_file, target_size=(150, 150))
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                img_array /= 255.0
                list_of_images = os.listdir('train')
                predictions = loaded_model.predict(img_array)
                predicted_class_index = np.argmax(predictions)
                im_name = list_of_images[predicted_class_index]
                if "healthy" in im_name:
                    st.write(f"I think that this is a healthy image of {list_of_images[predicted_class_index]}")
                    st.write(f"You dont need to worry much. You have already done great as your crop is healthy")

                else:
                    st.write(f"I think that this is a diseased image of {list_of_images[predicted_class_index].split('___')[0]} which is effected by{list_of_images[predicted_class_index].split('___')[1]}")
                    if im_name in mapping['diseases']:
                        associated_array = mapping['diseases'][im_name]
                        st.write("You can follow the following steps to avoid more exposure to the disease:")
                        for idx, step in enumerate(associated_array, start=1):
                            st.write(f"{idx}.) {step}")
    elif language == "Hindi":
        st.subheader("अपनी फसल की प्रदूषित पत्ती की छवि अपलोड करें")
        uploaded_file = st.file_uploader("एक छवि अपलोड करें", type=["jpg", "jpeg", "png"])
        st.info("सुनिश्चित करें कि आप एक स्पष्ट पत्ती की छवि अपलोड कर रहे हैं")
        if uploaded_file is None:
            st.sidebar.warning("स्थिति: छवि अपलोड नहीं की गई")
        else:
            st.sidebar.success('छवि सफलतापूर्वक अपलोड की गई')
            st.sidebar.image(uploaded_file, caption="अपलोड की गई छवि", use_column_width=True)
            if st.sidebar.button("पूर्वानुमान के लिए प्रस्तुत करें"):
                loaded_model = load_pretrained_model()
                img = image.load_img(uploaded_file, target_size=(150, 150))
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                img_array /= 255.0
                list_of_images = os.listdir('train')
                
                predictions = loaded_model.predict(img_array)
                predicted_class_index = np.argmax(predictions)
                im_name = list_of_images[predicted_class_index]
                if "healthy" in im_name:
                    healthy=translate_text(list_of_images[predicted_class_index],"hi")
                    st.write(f"मुझे लगता है कि यह {healthy} की स्वस्थ छवि है")
                    st.write(f"आपको ज्यादा चिंता करने की आवश्यकता नहीं है। आपकी फसल स्वस्थ है, आपने पहले ही अच्छा काम किया है")
                else:
                    translated_label = translate_text(list_of_images[predicted_class_index].split('___')[0], "hi")
                    st.write(f"मुझे लगता है कि यह {translated_label} की प्रदूषित छवि है जिसे {list_of_images[predicted_class_index].split('___')[1]} के द्वारा प्रभावित किया गया है")
                    if im_name in mapping['diseases']:
                        associated_array = mapping['diseases'][im_name]
                        st.write("आप रोग के अधिक प्रकट होने से बचने के लिए निम्नलिखित कदम अपना सकते हैं:")
                        translated_steps = [translate_text(step, "hi") for step in associated_array]
                        for idx, step in enumerate(translated_steps, start=1):
                            st.write(f"{idx}.) {step}")

    
    
def h_heading():
    return[
        'यह ऐप किसानों को फसलों के रोगों का पूर्वानुमान कर सकता है, रोगों के समाधान उत्पन्न कर सकता है, फसलों के वर्तमान मूल्यों को जानने में किसानों की मदद कर सकता है।',
         'हमारे पास AI के साथ चैट करने का विकल्प भी है, जहां आप कृषि के बारे में कुछ भी पूछ सकते हैं।',
         'अधिक जानकारी के लिए यहाँ देखें।']




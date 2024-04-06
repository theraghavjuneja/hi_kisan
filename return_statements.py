import streamlit as st
def heading_statements():
    return ['This app can predict crop diseases, generate solutions to diseases, help farmers by knowing the current prices of crops'
            ,'We also have a chat with AI option where you can ask anything about farming'
            ,'Refer [here](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset) for information']
def image_uploader():
    st.subheader("Upload diseased leaf image of your crop")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
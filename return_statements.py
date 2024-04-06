import streamlit as st
def heading_statements():
    return ['This app can predict crop diseases, generate solutions to diseases, help farmers by knowing the current prices of crops'
            ,'We also have a chat with AI option where you can ask anything about farming'
            ,'Refer [here](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset) for information']
def image_uploader():
    st.subheader("Upload diseased leaf image of your crop")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    st.info("Make sure you upload a clear leaf image")
    
    if uploaded_file is None:
        st.sidebar.warning("Status: Image not uploaded")
    else:
        st.sidebar.success('Image uploaded succesfully')
        st.sidebar.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        if(st.sidebar.button("SUBMIT FOR PREDICTION")):
            st.write("Hello")

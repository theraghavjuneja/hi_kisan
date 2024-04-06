import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
def load_pretrained_model():
    return load_model('model.h5')

# Title of your Streamlit app
st.title('Image Classifier')

# File upload widget
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:

    loaded_model = load_pretrained_model()

   
    img = image.load_img(uploaded_file, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

   
    img_array /= 255.0
    list_of_images=os.listdir('train')

   
    predictions = loaded_model.predict(img_array)

   
    predicted_class_index = np.argmax(predictions)
    im_name=list_of_images[predicted_class_index]
    if "healthy" in im_name:
        st.write(f"I think that this is a healthy image of {list_of_images[predicted_class_index]}")
        st.write(f"You dont need to worry much. You have already done great as your crop is healthy")
    else:
        st.write(f"I think that this is a diseased image of {list_of_images[predicted_class_index].split('___')[0]} which is effected by{list_of_images[predicted_class_index].split('___')[1]}")

else:
    st.write("Please upload an image.")

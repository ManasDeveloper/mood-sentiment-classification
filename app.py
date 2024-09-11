import playsound
from transformers import pipeline
import streamlit as st

classifier = pipeline("text-classification") 


st.title("Mood Sentiment Classification")
text = st.text_input("Input the text")


if st.button("Predict"):


    results = classifier(text)

    print(results[0]['label'])

    label = results[0]['label']
    st.write(label)
    if(label=="NEGATIVE"):
        playsound.playsound('./sad_trombone.mp3')
    else:
        playsound.playsound('./happy_notification.mp3')
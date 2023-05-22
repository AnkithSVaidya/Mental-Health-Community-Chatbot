#importing necessary libraries

from json import load
import streamlit as st
from datetime import datetime
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
import pandas as pd
from streamlit_extras.let_it_rain import rain


st.set_page_config(
  page_title="OneFam.",
  page_icon="🐧",
)
st.title("OneFam. A Family you belong with.🌼")
story_text=""
st.sidebar.title("Welcome to Mental Health Community")

#Lottie Animations
# Directly via URL
#boy
url = requests.get("https://assets5.lottiefiles.com/packages/lf20_awP420Zf8l.json")
url_json = dict()
if url.status_code == 200:
    url_json = url.json()
else:
      print("Error in URL")

#medical 
medical=requests.get("https://assets7.lottiefiles.com/packages/lf20_pk5mpw6j.json")
medical_json=dict()
if medical.status_code ==200:
    medical_json= medical.json()
else:
    print("error")

#support
support = requests.get("https://assets4.lottiefiles.com/private_files/lf30_wwq2op12.json")
support_json = dict()
if support.status_code == 200:
    support_json = support.json()
else:
      print("Error in URL")


#chatbot
chat = requests.get("https://assets3.lottiefiles.com/packages/lf20_5e7wgehs.json")
chat_json = dict()
if chat.status_code == 200:
    chat_json = chat.json()
else:
      print("Error in URL")

#penguin
penguin = requests.get("https://assets4.lottiefiles.com/private_files/lf30_ttgwkuhd.json")
penguin_json = dict()
if penguin.status_code == 200:
    penguin_json = penguin.json()
else:
      print("Error in URL")      

c1,c2 = st.columns(2)
with c1:
  st.title("OneFam")
  st.subheader("A Story Driven Community")
  st.write("Empowering people facing health challenges with the magic of AI.")
with c2:
 st_lottie(support_json,
height=200,
width=200)            


st.sidebar.success("What can we do for you today?")
with st.sidebar.expander("You are not alone!. Click to read more"):
      st.write("It is estimated that 6-7 percent of population suffers from mental disorders.")
      st.write("Statistics show that 1 in every 5 individuals suffers from some form of mental health illness symptoms. 50 % of mental health conditions begin by age 14 and 75% of mental health conditions develop by age 24. ")
      st.write("These numbers have sky-rocketed due to the consequences of the pandemic including lockdowns, stress, concern, worry etc.")
      st.write("Hence, if you are feeling any of the symptoms, you must visit a psychiatrist or pschologist who will help you through the process. ") 
      st.write("Remember, mental helath issues are just like any other health issues and there is nothing to be ashamed of. There are always people to help out. We, here are more than ready to extend our hand!💓")

with st.sidebar.expander("Click here to access authoritative sources for mental health related information"):
      st.write("To know more about national govt approach to addressing mental health, visit the link: https://nhm.gov.in/index1.php?lang=1&level=2&sublinkid=1043&lid=359")
      st.write("WHO website for mentalhealth issues and related surveys: https://www.who.int/india/health-topics/mental-health")
      st.write("A clinician's guide to statistic sin mental health: https://books.google.co.in/books?hl=en&lr=&id=1dWgEAAAQBAJ&oi=fnd&pg=PR9&dq=mental+health+statistics")
      st.write("Mental Health Issues in India: Concerns and Response: https://www.ijpn.in/article.asp?issn=2231-1505;year=2018;volume=15;issue=1;spage=58;epage=60;aulast=Shankardass")
      st.write("Attitudes of undergraduates towards mental health: https://www.ajol.info/index.php/sajpsyc/article/view/92533")
      st.write("mental health of school stufdents during covid-19: https://www.mdpi.com/2306-5729/7/7/99")
navbar = st.radio('Page Navigation',('Home 🏠','Chat bot 📃', 'Resources 😃','Profile 🐧'))
if navbar=="Home 🏠":
      cl1,cl2 = st.columns(2)
      with cl1:
        st.header("Welcome, Dear!")
        st.subheader("You Matter. You can write your daily progress or feelings here:  ")
      with cl2:
        st_lottie(url_json,
          # change the direction of our animation
          reverse=True,
          # height and width of animation
          height=400,  
          width=400,
          # speed of animation
          speed=1,  
          # means the animation will run forever like a gif, and not as a still image
          loop=True,  
          # quality of elements used in the animation, other values are "low" and "medium"
          quality='high',
           # THis is just to uniquely identify the animation
          key='Car' )
      
      inputText = st.text_area('Start Away...') #text is stored in this variable
      extract = st.button("Share")
    
      if extract:
        st.subheader("Thankyou for sharing. I wish you the very best")
        st.session_state["story_text"]=inputText
      else:
            st.session_state["story_text"] = 'you havent shared your story yet'
if navbar=="Chat bot 📃":
      
      st.header("Hi! I am Liz. They call me Liz The Listener because I'm here to listen to you. Hopefully, I can give you some relief, or maybe even some answers 💓")
     
      components.html("""<script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
                            <df-messenger
                            intent="WELCOME"
                            chat-title="Lizthelistener"
                            agent-id="5fb094bb-2831-4c4b-81ee-062385369561"
                            language-code="en"
                            ></df-messenger> """, height=700,)  
            
if navbar=="Profile 🐧":
      
      story=st.session_state["story_text"]
      st.header("Your Profile: ")
      st.subheader("Your Story:")
      st.success(story)

if navbar=="Resources 😃":
      rain(
        emoji="🤍",
        font_size=54,
        falling_speed=5,
        animation_length=1
      )  

      st.header("You're not Alone.")
      st.subheader("Here are some resources to support you:")

      one,two,three = st.columns(3)
      with one:
        st.subheader("keep.meSAFE")
        st.write("keep.meSAFE’s innovative Student Support Program (SSP) helps students by promoting early intervention and 24/7 access to mental health support")
        st.write("https://www.keepmesafe.org")

      with two:
        st.subheader("FORTIS HOSPITAL NATIONAL HELPLINE")
        st.write("This helpline is open 24/7. It is an All-India Helpline. YOu can expect a call back if they don't answer you immediately. This helpline is also multilingual.")
        st.write("91-8376804102")

      with three:
        st.subheader("GOVT MH Rehabilitation HELPLINE ‘KIRAN’")
        st.write("If you’re thinking about suicide, are worried about a friend or loved one, the KIRAN Suicide Prevention Service is available 24/7 for voice.")
        st.write("1800-5990019")

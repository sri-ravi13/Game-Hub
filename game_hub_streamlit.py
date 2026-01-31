import streamlit as st
import subprocess
import sys
import os
import base64

st.set_page_config(
    page_title="Gesture Game Hub",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

@st.cache_data

def launch_game(script_name):
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    if not os.path.exists(script_path):
        st.error(f"Error: '{script_name}' not found!")
        return
    try:
        subprocess.Popen([sys.executable, script_path])
        st.toast('Controller is launching... 🚀')
        st.success("Controller is LIVE! The camera window should appear shortly.")
        st.info("Remember to press 'q' in the camera window to quit.")
    except Exception as e:
        st.error(f"An error occurred while launching the script: {e}")

def get_base64_of_bin_file(bin_file):

    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def apply_custom_styles():

    background_image_path = "assets/play.jpeg"  # Change if needed
    if not os.path.exists(background_image_path):
        st.error(f"❌ Background image not found at {background_image_path}")
        return

    encoded_image = get_base64_of_bin_file(background_image_path)

    st.markdown(f"""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Poppins', sans-serif;
    }}

    /* --- Main App Background --- */
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpeg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* --- Transparent "Frosted Glass" Card Effect --- */
    .game-card {{
        background-color: rgba(42, 42, 74, 0.5);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 12px 0 rgba(0,0,0,0.7);
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(5px);
    }}

    [data-testid="stHorizontalBlock"] .st-emotion-cache-13ln4jf {{
        background-color: rgba(42, 42, 74, 0.9);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 12px 0 rgba(42,42,74,0.7);
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(5px);
    }}

    /* Image styles */
    [data-testid="stHorizontalBlock"] .st-emotion-cache-13ln4jf img {{
        border-radius: 10px;
    }}

    [data-testid="stImage"] {{
        background-color: rgba(0, 0, 0, 0.7);
        border-radius: 15px;
        padding: 1rem;
        margin-bottom: 1rem;
    }}
    [data-testid="stImage"] img {{
        border-radius: 10px;
        width: 100%;
    }}

    /* Text container */
    .text-container {{
        background-color: rgba(42, 42, 75, 0.3);
        border-radius: 15px;
        padding: 1rem;
        margin-bottom: 1.5rem;
    }}

    /* Buttons */
    .stButton>button {{
        background-color: #5a4fcf;
        color: white;
        border-radius: 20px;
        border: 2px solid #8c82ff;
        padding: 10px 24px;
        font-size: 1.2em;
        font-weight: bold;
        transition: all 0.3s;
        font-family: 'Poppins', sans-serif;
    }}
    .stButton>button:hover {{
        background-color: #8c82ff;
        border-color: #5a4fcf;
        transform: scale(1.05);
    }}

    /* Headings */
    h1 {{
        color: #D4AF37;
        background-color: rgba(0, 0, 0, 0.8);
        border-radius: 15px;
        padding: 1rem;
        margin-bottom: 1.5rem;
        font-weight: 700;
    }}
    h2 {{
        color: #f63366;
        background-color: rgba(0, 0, 0, 0.8);
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1.5rem;
        font-weight: 600;
    }}
    h3 {{
        color: #98FF98;
        background-color: rgba(0, 0, 0, 0.8);
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1.5rem;
        font-weight: 500;
    }}

    /* Markdown, captions, expanders */
    .stMarkdown, .stSubheader, .stCaption {{
        color: #87CEEB !important;
        background-color: rgba(0, 0, 0, 0.8);
    }}
    .stExpander label {{
        color: #FFFFFF !important;
        background-color: rgba(0, 0, 0, 0.8);
    }}
    </style>
    """, unsafe_allow_html=True)

apply_custom_styles()

st.title("🎮 Hand Gesture Game Hub 🎮")
st.markdown("### Control your favorite games with a wave of your hand!")
st.markdown("---")

st.header("Choose Your Game")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container():

        st.image("assets/subway.jpg", caption="Subway Surfers")
        st.subheader("Subway Surfers")
        
        with st.expander("How to Play"):
            st.markdown("""
            - **Swipe Up:** Jump
            - **Swipe Down:** Roll
            - **Swipe Left:** Move Left
            - **Swipe Right:** Move Right
            """)
        
        if st.button("▶️ Play Now!", key="subway_surfers"):
            launch_game('subway_surfers_controller.py')
            

with col2:
    with st.container():

        st.image("assets/maxresdefault.jpeg", caption="Mr. Racer") # Changed to a consistent name
        st.subheader("Mr. Racer")

        with st.expander("How to Play"):
            st.markdown("""
            **Positional Controls (Hold):**
            - **Accelerate:** Hand in **Top Half**
            - **Brake/Reverse:** Hand in **Bottom Half**
            - **Steer Left/Right:** Hand on **Left/Right Side**

            **Gesture Controls (Action):**
            - **Nitro Boost:** Give a **Thumbs Up**
            - **Horn:** Make a **Fist**
            """)

        if st.button("▶️ Play Now!", key="mr_racer"):
            launch_game('mr_racer_controller.py')


with col3:
    with st.container():
        st.image("assets/plonky.jpeg", caption="Plonky")
        st.subheader("Plonky")
        
        with st.expander("How to Play"):
            st.markdown("""
            - **Jump:** Swipe Up
            - **Duck:** Swipe Down
            - **Move Left/Right:** Swipe Left / Right
            - **Special Move:** Thumbs Up
            """)

        if st.button("▶️ Play Now!", key="plonky"):
            launch_game('plonky_controller.py')

st.header("More Games Coming Soon")
col1, col2, col3 = st.columns(3)

with col2:
    with st.container():
        st.image("https://img.icons8.com/plasticine/200/controller.png", caption="More games coming soon!")
        st.subheader("Stay Tuned!")
        st.markdown("New gesture-controlled games are on the way. Check back soon!")
        st.button("Coming Soon", disabled=True)
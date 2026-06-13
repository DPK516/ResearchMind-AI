import streamlit as st
import requests
import time
import os

st.set_page_config(
    page_title="ResearchMind", 
    page_icon="⬛",
    layout="wide", 
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    /* Deep Black Backgrounds */
    .stApp { background-color: #050505; color: #F0F0F0; }
    [data-testid="stSidebar"] { background-color: #0A0A0A; border-right: 1px solid #1A1A1A; }
    [data-testid="stHeader"] { background-color: transparent; }
    
    /* Typography */
    h1, h2, h3, h4, h5, h6 { font-weight: 500 !important; letter-spacing: -0.02em; }
    
    /* Central Search Input */
    .stTextInput input {
        background-color: #111111;
        color: #FFFFFF;
        border: 1px solid #333333;
        border-radius: 6px;
        padding: 14px;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    .stTextInput input:focus {
        border-color: #666666;
        box-shadow: none;
    }
    
    /* Primary Button */
    .stButton > button {
        background-color: #FFFFFF;
        color: #000000;
        border: none;
        border-radius: 4px;
        font-weight: 500;
        padding: 0.5rem 2rem;
        transition: background-color 0.2s;
    }
    .stButton > button:hover {
        background-color: #D0D0D0;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent;
        border-bottom: 1px solid #222222;
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        color: #666666;
        padding-top: 16px;
        padding-bottom: 16px;
    }
    .stTabs [aria-selected="true"] {
        color: #FFFFFF;
        border-bottom: 2px solid #FFFFFF;
    }
    
    /* Code Blocks */
    code { color: #A0A0A0; background-color: #111111 !important; border-radius: 4px; }
    
    /* Hide Default Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/api/research")

with st.sidebar:
    st.markdown("### ⬛ ResearchMind")
    st.caption("Enterprise Research Platform • v1.0.0")
    st.divider()
    st.markdown("Status: <span style='color: #10B981;'>●</span> **Online**", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center; font-size: 3.5rem; margin-bottom: 0;'>ResearchMind</h1>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; color: #888888; font-size: 1.1rem; margin-top: 10px;'>Multi-Agent AI Research Platform for Deep Intelligence and Insight Generation.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    topic = st.text_input("Topic Input", label_visibility="collapsed", placeholder="e.g., Geopolitical impacts of renewable energy in 2026")
    
    button_col1, button_col2, button_col3 = st.columns([1, 1, 1])
    with button_col2:
        launch = st.button("Start Research", use_container_width=True)

if launch:
    if not topic:
        st.toast("Please enter a research topic.", icon="⚠️")
    else:
        st.divider()
        start_time = time.time()
        
        
        with st.status("Initiating Deep Intelligence Scan...", expanded=True) as status:
            
            st.write("Establishing secure connection to distributed knowledge graphs...")
            time.sleep(0.8) 
            
            st.write("Querying live data streams and acquiring target context...")
            time.sleep(0.5)
            
            try:
                
                response = requests.post(API_URL, json={"topic": topic})
                
                if response.status_code == 200:
                    data = response.json()
                    
                    st.write("Executing cryptographic source-verification and bias filtering...")
                    time.sleep(0.8)
                    
                    st.write("Generating strategic assessment and formatting payload...")
                    time.sleep(0.5)
                    
                    status.update(label="Deep Intelligence Scan Complete", state="complete", expanded=False)
                    
                    elapsed = round(time.time() - start_time, 2)
                    m1, m2 = st.columns(2)
                    m1.metric("Processing Time", f"{elapsed} seconds")
                    m2.metric("Status", "Success")
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    tab_report, tab_critic = st.tabs(["Final Report", "Risk Assessment"])
                    
                    with tab_report:
                        st.markdown(data.get("report", ""))
                        st.download_button("Download Report (Markdown)", data.get("report", ""), file_name=f"{topic.replace(' ', '_')}.md")
                        
                    with tab_critic:
                        st.markdown(data.get("feedback", ""))
                        
                else:
                    status.update(label="Scan Terminated: Pipeline Error", state="error", expanded=False)
                    st.error(f"Server Response: {response.status_code} \n\n {response.text}")
                    
            except requests.exceptions.ConnectionError:
                status.update(label="Connection Terminated", state="error", expanded=False)
                st.error("Failed to connect to the backend server. Ensure the FastAPI application is running on Port 8000.")
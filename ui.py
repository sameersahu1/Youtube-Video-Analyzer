import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="YouTube Video Analyzer",
    layout ="centered"
)

st.title("🎬 AI Youtube Video Analyzer")

@st.cache_resource 
def get_agent():
    return build_youtube_agent()

agent = get_agent()

# video_url = st.text_input("Enter Youtube Video Link")
video_url = st.text_input(
    "Enter YouTube URL",
    placeholder="https://youtube.com/watch?v=..."
)

#-----------------Button---------------------
# button = st.button("Analyze Button")
button = st.button("🚀 Analyze Video", use_container_width=True)
st.markdown("""
<style>
div.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    color: white;
    border: none;
    border-radius: 12px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.3s ease;
}

/* Hover Effect */
div.stButton > button:hover {
    background: linear-gradient(90deg, #ec4899, #8b5cf6);
    color: white;
    box-shadow: 0px 0px 20px rgba(236, 72, 153, 0.8);
}
</style>
""", unsafe_allow_html=True)

#---------------------Design of AI Video Analyzer-----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<h1 style='text-align:center;
background: -webkit-linear-gradient(#9333ea,#3b82f6);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
font-size:60px;'>
🎬 AI YouTube Video Analyzer
</h1>

<p style='text-align:center; color:gray; font-size:15px;'>
Summarize • Analyze • Extract Insights from YouTube Videos
</p>
""", unsafe_allow_html=True)


#---------------------Add Sidebar Section-----------------
with st.sidebar:
    st.title("⚙ Settings")
    model = st.selectbox(
        "Choose Model",
        ["Gemini", "OpenAI", "Groq"]
    )

#---------------------Add Features Section-----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📄 AI Summary")

with col2:
    st.info("🧠 Key Insights")

with col3:
    st.info("⏱ Timestamp Detection")


#-------------Video and Button Working--------------
if video_url and button:
    # analysis code
    with st.spinner("Analyzing video with AI..."):
        response = agent.run(
            f"Anayze this Video:{video_url}"
        )
    
    
    st.markdown("Analysis of Video:")  
    st.markdown(response.content)  

st.markdown("""
<hr>
<p style='text-align:center;color:gray;'>
Built with ❤️ using Streamlit + AI
</p>
<p style='text-align:center;color:gray;'>
© Sameer Sahu
</p>
            
""", unsafe_allow_html=True)

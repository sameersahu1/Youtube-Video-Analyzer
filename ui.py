import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="YouTube Video Analyzer",
    layout ="centered"
)

st.title("🎥AI Youtube Video Analyzer")

@st.cache_resource 
def get_agent():
    return build_youtube_agent()

agent = get_agent()

video_url = st.text_input("Enter Youtube Video Link")
button = st.button("Analyze Button")

if video_url and button:
    with st.spinner("Analyzing Video...."):
        response = agent.run(
            f"Anayze this Video:{video_url}"
        )

    st.markdown("Analysis of Video:")  
    st.markdown(response.content)  
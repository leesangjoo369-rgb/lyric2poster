
import streamlit as st

st.set_page_config(
    page_title="Lyric2Poster",
    page_icon="🎨",
    layout="wide"
)

st.title("🎵 Lyric2Poster")
st.subheader("Turn your lyrics into a visual poster")

st.write(
    "Transform the mood and emotions of your favorite song "
    "into a unique visual poster."
)

song_title = st.text_input("Song Title")
artist = st.text_input("Artist")
lyrics = st.text_area("Paste your lyrics", height=200)

style = st.selectbox(
    "Choose Poster Style",
    ["Minimal", "Vintage", "Dreamy", "Pop Art"]
)

if st.button("Create My Poster"):
    if not song_title or not artist or not lyrics:
        st.warning("Please fill in all fields.")
    else:
        st.success("Your poster project is ready!")
        st.write("Song:", song_title)
        st.write("Artist:", artist)
        st.write("Style:", style)

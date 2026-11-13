
import streamlit as st
from io import BytesIO

from lyric2poster.overlay import create_poster

st.set_page_config(
    page_title="Lyric2Poster",
    page_icon="🎨",
    layout="wide"
)

st.title("🎵 Lyric2Poster")
st.subheader("Turn your favorite songs into visual posters")

st.write(
    "Create a unique poster inspired by your favorite music."
)

st.divider()

song_title = st.text_input("Song Title", placeholder="Enter song title")
artist = st.text_input("Artist", placeholder="Enter artist name")

style = st.selectbox(
    "Choose Poster Style",
    ["Minimal", "Vintage", "Dreamy", "Pop Art"]
)

if st.button("🎨 Create My Poster", type="primary"):

    if not song_title.strip() or not artist.strip():
        st.warning("Please enter both the song title and artist.")

    else:
        poster = create_poster(
            song_title=song_title,
            artist=artist,
            style=style
        )

        st.success("Your poster has been created!")

        st.image(
            poster,
            caption=f"{song_title} - {artist}",
            use_container_width=True
        )

        image_buffer = BytesIO()
        poster.save(image_buffer, format="PNG")

        st.download_button(
            label="⬇️ Download Poster",
            data=image_buffer.getvalue(),
            file_name="lyric2poster.png",
            mime="image/png"
        )

st.divider()

st.caption(
    "Lyric2Poster | AI-powered music poster design project"
)

st.info(
    "This is the first demo version. "
    "AI lyric analysis and image generation will be added later."
)


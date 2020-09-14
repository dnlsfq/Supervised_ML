import streamlit as st 
import streamlit.components.v1 as components

# components.iframe("https://docs.streamlit.io/en/latest")


def github_gist(gist_creator, gist_id, height=600, scrolling=True):
    components.html(
        f"""
        <script src="https://gist.github.com/{gist_creator}/{gist_id}.js">

        </script>
        """,
        height = height,
        scrolling = scrolling
    )
    
github_gist('tc87','9832eafdb6eebde0bca0c33080d54b58')
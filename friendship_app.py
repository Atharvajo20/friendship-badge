import streamlit as st

st.set_page_config(page_title="Friendship Badge Generator", page_icon="💖", layout="centered")

st.title("💖 Friendship Badge Generator 💖")
st.markdown("Create a sweet badge for your best friends! 🎁")

name = st.text_input("👤 Enter your friend's name:")
trait = st.text_input("✨ What do you love about them?")
emoji = st.text_input("😊 Pick an emoji that reminds you of them:")

if st.button("Generate Badge 🎉"):
    if name and trait and emoji:
        st.success(f"""
        🎉 **Happy Friendship Day, {name.title()}!** 🎉

        You're truly *{trait}*! Never change! {emoji}

        — From your forever friend ❤️ Atharva
        """)
    else:
        st.warning("Please fill in all the fields!")

st.markdown("---")
st.caption("Built with 💖 by Atharva using Streamlit")



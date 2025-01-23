import streamlit as st

# Test Streamlit UI
st.title("✅ Streamlit Test App")
st.write("If you see this message, Streamlit is working!")

if st.button("Click Me!"):
    st.success("🎉 Your app is running!")

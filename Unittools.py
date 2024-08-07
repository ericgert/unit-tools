import streamlit as st
import ut_utils
import extra_streamlit_components as stx
from streamlit_js_eval import streamlit_js_eval


st.write("Unit Tools Home")

import datetime
st.write("# Cookie Manager")

st.subheader("All Cookies:")
cookies = ut_utils.get_all_cookies()
st.write(cookies)

c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("Get Cookie:")
    cookie = st.text_input("Cookie", key="0")
    clicked = st.button("Get")
    if clicked:
        value = cookie_manager.get(cookie=cookie)
        st.write(value)
with c2:
    st.subheader("Set Cookie:")
    cookie = st.text_input("Cookie", key="1")
    val = st.text_input("Value")
    if st.button("Add"):
        cookie_manager.set(cookie, val) # Expires in a day by default
        streamlit_js_eval(js_expressions="parent.window.location.reload()")
with c3:
    st.subheader("Delete Cookie:")
    cookie = st.text_input("Cookie", key="2")
    if st.button("Delete"):
        cookie_manager.delete(cookie)


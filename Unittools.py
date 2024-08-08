import streamlit as st
import auth_utils
import extra_streamlit_components as stx
from streamlit_js_eval import streamlit_js_eval
import os
from PIL import Image
import logging

logger = logging.getLogger(__name__) 

#determine runtime

if "K_SERVICE" in os.environ:
    runtime_env = 'prod'
else:
    runtime_env = 'dev'

def init_logging():
    logging.basicConfig(filename='ut.log', level=logging.INFO)

    logger.info('logging initialized')

def init_page():

    logger.info('page initialized')
    #set page config
    pi = Image.open("./images/moroni_icon.png")

    st.set_page_config(
        page_title="Unit Tools",
        page_icon=pi,
        initial_sidebar_state = 'collapsed'
    )


def main():

    #initialize logging
    init_logging()

    #initialize page
    init_page()

    #check auth
    auth_bool, auth_cookie = auth_utils.get_auth_state(logger)

    #TODO:login code (unauthenticated)

    if not auth_bool:

        email = 'eric.gert@gmail.com'
        rc, message = auth_utils.add_auth_cookie(logger, email)

        if not rc:
            st.write(f":red[{message}]")
            st.stop()
    
        logger.info(f'added user cookie for {email}')




if __name__ == '__main__':
    main()
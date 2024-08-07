import extra_streamlit_components as stx




def check_auth_cookie(user_email
                      ):
    cm = stx.CookieManager()

    return cm.get_all()

def add
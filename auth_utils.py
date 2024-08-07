import extra_streamlit_components as stx
from datetime import datetime, timedelta
import uuid

#global variables
auth_cookie_name = 'ut-authenticate'


def get_auth_state(logger):

    #Get the client cookie associated to the user to determine if they have authenticated recently
    logger.info('fetching auth cookie')
    cm = stx.CookieManager()

    auth_cookie = cm.get(cookie=auth_cookie_name)

    if auth_cookie == None:
        logger.warn('cookie not found')
        return False, None
    
    else:
        logger.info('')
        return True, auth_cookie

def add_auth_cookie(logger, email):

    cur_ts = datetime.now()
    two_week_exp_ts = cur_ts + timedelta(days=13)
    
    cookie_value = f"{email}||{uuid.uuid4()}||{two_week_exp_ts}"

    cm = stx.CookieManager()
    try:
        cm.set(cookie=auth_cookie_name, val=cookie_value, expires_at=two_week_exp_ts)
    except Exception as e:
        logger.error(f'Could not set the authentication cookie.  Cookie Name{auth_cookie_name}, value{cookie_value}')
        return False, 'The application encountered an error when saving your authentication state locally.  Please ensure that cookies are enabled'
        
    return True, None





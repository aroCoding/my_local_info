from pages import show_home
import streamlit as st

def main():
    '''
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        import pages.home as home
        home.show_home()
    else:
        import pages.login as login
        login.show_login()
    '''
    if 'region' not in st.session_state:
        st.session_state.region = '서울특별시'
        
    show_home()

if __name__ == "__main__":
    main()
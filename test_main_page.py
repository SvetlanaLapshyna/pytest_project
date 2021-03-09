from .pages.main_page import MainPage
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    print("\nInitiate Browser!")
    page.open()
    print("\nSite is opened!")
   
    page.should_be_login_link()
    print("\nChecked Login Page!")
    
    page.go_to_login_page()
    print("\nLoaded Login Page!")
    
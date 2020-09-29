
import smtplib
import datetime
from selenium import webdriver
from pages.login_page import LoginPage

mail_from = ''
gmail_api_key = ''
visma_email = ''
visma_pwd = ''
visma_url = 'https://www.vismaonline.com/index.html'

def main():
    browser = webdriver.Chrome()

    loginPage = LoginPage(browser, visma_url)
    loginPage.go()
    login(loginPage, visma_email, visma_pwd)

    switch_window(browser)
    status = clock_in_or_out(loginPage)
    message = f'Subject: Visma clocking\n\n {visma_email} successfully {status}!'
    send_report(message, visma_email)

    browser.close()

def login(loginPage, email, password):
    loginPage.get_username_input.input_text(email)
    loginPage.get_password_input.input_text(password)
    loginPage.get_save_button.click()
    loginPage.get_calendar_button.click()

def switch_window(browser):
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)

def clock_in_or_out(loginPage):
    in_btn = loginPage.get_in_button
    out_btn = loginPage.get_out_button

    now = datetime.datetime.now()
    status = None
    if in_btn.is_enabled():
        in_btn.click()
        status = f'logged in'
    elif out_btn.is_enabled():
        out_btn.click()
        status = f'logged out'

    return f'{status} @' + now.strftime("%Y-%m-%d %H:%M:%S")

def send_report(message, email):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(mail_from, gmail_api_key)
    server.sendmail(mail_from, mail_from, message)
    server.quit()

if __name__ == "__main__":
    main()
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/102.0.5005.115 Safari/537.36')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_extension('./driver/1.0.3_0.crx')

url = 'https://vk.com/'

browser = webdriver.Chrome('./driver/chromedriver.exe', options=options)
browser.set_window_size(600, 600)
browser.set_window_position(600, 200)
browser.implicitly_wait(5)
browser.get(url)

sign_in = browser.find_element(By.XPATH, '//*[@id="index_login"]/div/form/button[1]/span')
sign_in.click()

email_input = browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/section/div/div/div/input')
email_input.send_keys('LOGIN\n')

password_input = browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/'
                                                'div[1]/div/input')
password_input.send_keys('PASSWORD\n')

cod_input = browser.find_element(By.XPATH, '//*[@id="otp"]')
cod_input.send_keys(input('Verification code: '))
cod_input.send_keys('\n')
sleep(2)

main_window = browser.current_window_handle
def download():
    link = input('Link to playlist: ')
    browser.execute_script(f"window.open('{link}')")
    sleep(1)
    # window_after = browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[-1])

    download_all = browser.find_element(By.CLASS_NAME, 'vkd_download_all_btn')
    download_all.click()
    return download

download()
question = 'y'
while question != 'n':
    download_more = input('Download more? y/n ')
    if question == 'y':
        if download_more == 'y':
            download()
        else:
            break
    else:
        break

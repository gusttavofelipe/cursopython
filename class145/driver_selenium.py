import env
from time import sleep
from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


class Selenium:
    def __init__(self):
        logger.info('Iniciando Scraping')
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        logger.info('Iniciando Chrome')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))    
        logger.info('Chrome iniciado com sucesso')   

    def acessa(self, url):
        try:
            self.driver.get(url)
            find_header = self.driver.find_element(By.TAG_NAME, 'header')
            find_div = find_header.find_element(By.CLASS_NAME, 'flex-items-center')
            list_find_a = find_div.find_elements(By.TAG_NAME, 'a')

            for find in list_find_a:
                if find.get_attribute('href') == f'{url}login':
                    self.driver.execute_script("arguments[0].click();", find)

        except Exception as e:
            print('Erro ao clicar', e)
    
    def login(self):
        try:
            sleep(1)
            input_usr = self.driver.find_element(By.ID, 'login_field')
            input_password = self.driver.find_element(By.ID, 'password')
            login_button = self.driver.find_element(By.NAME, 'commit')

            input_usr.send_keys(env.USER_GITHUB)
            input_password.send_keys(env.PASSWORD_GITHUB)
            sleep(1)
            login_button.click()

        except Exception as e:
            print(e)
    
    def profile_click(self):
        try:
            sleep(3)
            profile = self.driver.find_element(By.CSS_SELECTOR,
            'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details'
            ) 

            profile.click()
        except Exception as e:
            print('Erro no click do perfil', e)
    
    def view_profile(self):
        try:
            sleep(2)
            overiew = self.driver.find_element(By.CLASS_NAME, 'user-profile-link') 
            overiew.click()
        except Exception as e:
            print('Erro ao visualizar overiew', e)


    def exit_profile(self):
        try:
            sleep(3)
            profile_quit = self.driver.find_element(By.CSS_SELECTOR,
            'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button'
            ) 

            profile_quit.click()
        except Exception as e:
            print('Erro ao sair do perfil', e)


    def exit_site(self):
        self.driver.quit()
        logger.info('Scraping Finalizado')


if __name__ == '__main__':
    selenium_driver = Selenium()      
    selenium_driver.acessa('https://github.com/')

    selenium_driver.login()
    selenium_driver.profile_click()
    selenium_driver.view_profile()

    selenium_driver.profile_click()
    selenium_driver.exit_profile()
    
    sleep(4)
    selenium_driver.exit_site()

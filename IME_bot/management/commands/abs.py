from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
import pip
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas
import os

from selenium.webdriver.support.wait import WebDriverWait

pip.main(["install", "openpyxl"])


def watbot(request):
    if request.method == 'POST':
        file_name = request.POST.get("filename")
        pre = os.path.dirname(os.path.realpath(__file__))
        f_name = file_name
        path = os.path.join(pre, f_name)
        # Z = pd.read_excel(path)

        # noinspection PyArgumentList
        f_name = pandas.read_excel(path)

        count = 0
        image_url = request.POST.get("url")

        driver = webdriver.Chrome(executable_path='D:/Old Data/Integration Files/new/chromedriver')
        driver.get('https://web.whatsapp.com')
        sleep(25)
        # input("Press ENTER after login into Whatsapp Web and your chats are visiable.")

        for column in f_name['Contact'].tolist():
            data = str(f_name['Contact'][count])[0:3]
            try:
                if data == str('977'):
                    driver.get('https://web.whatsapp.com/send?phone=+' + str(f_name['Contact'][count]) + str(
                        f_name['Messages'][0]))
                else:

                    driver.get(
                        'https://web.whatsapp.com/send?phone=+91' + str(f_name['Contact'][count]) + '&text=' + str(
                            f_name['Messages'][0]))

                sent = False
                sleep(6)
                # driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div').send_keys(str(f_name['Messages'][0]))

                # driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()

                driver.find_element(By.XPATH,
                                    '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()

                sendky = driver.find_element(By.XPATH,
                                             '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div['
                                             '2]/div/span/div/div/ul/li[1]/button/span')
                input_box = driver.find_element(By.TAG_NAME, 'input')
                input_box.send_keys(image_url)

                # It tries 3 times to send a message in case if there any error occurred
                try:
                    click_btn = WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.CLASS_NAME, '_33pCO')))

                except Exception as e:
                    print("Sorry message could not sent to " + str(f_name['Contact'][count]) + str(e))
                else:

                    sleep(3)
                    click_btn.click()
                    sleep(2)
                    print('Message sent to: ' + str(f_name['Contact'][count]))
                count = count + 1
                # driver.find_element(By.XPATH,
                #                     '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()



            except Exception as e:
                print("try again " + str(f_name['Contact'][count]), e)
                count = count + 1
            except Exception as e:
                print('Failed to send message to ' + str(f_name['Contact'][count]) + str(e))
        return HttpResponse('messeges')

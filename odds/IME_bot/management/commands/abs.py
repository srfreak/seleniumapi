from json import dumps

import json

from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pip

pip.main(["install", "openpyxl"])
from time import sleep
import pandas
import os


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

        driver = webdriver.Chrome(executable_path='D:/Old Data/Integration Files/new/chromedriver')
        driver.get('https://web.whatsapp.com')
        sleep(30)
        # input("Press ENTER after login into Whatsapp Web and your chats are visiable.")

        for column in f_name['Contact'].tolist():
            try:
                sleep(2)
                driver.get('https://web.whatsapp.com/send?phone=' + str(f_name['Contact'][count]) + '&text=' + str(f_name['Messages'][0]))

                sent = False
                sleep(3)
                # It tries 3 times to send a message in case if there any error occurred

                try:
                    sleep(2)
                    click_btn = driver.find_element(By.XPATH,
                                                    '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
                    sleep(1)
                except Exception as e:
                    print("Sorry message could not sent to " + str(f_name['Contact'][count]))
                else:
                    sleep(1)
                    click_btn.click()
                    sent = True
                    sleep(2)
                    print('Message sent to: ' + str(f_name['Contact'][count]))
                count = count + 1
            except Exception as e:
                print('Failed to send message to ' + str(f_name['Contact'][count]) + str(e))
        return HttpResponse('messeges')

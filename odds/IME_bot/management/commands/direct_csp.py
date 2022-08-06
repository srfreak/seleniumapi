from time import sleep


from django.forms import Select
from django.http import HttpResponse

import csv
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from django.core.management.base import BaseCommand


def string(request):
    if request.method == 'POST':
        admin = webdriver.Chrome(executable_path='D:/Old Data/Integration Files/new/chromedriver')

        admin.get("https://admin.imeforex-txn.net/admin/")

        main_page = admin.current_window_handle

        # login user
        admin.find_element("id", 'userName').send_keys("sunil")
        admin.find_element("id", 'pwd').send_keys("SUNIL@123456")
        admin.find_element("id", 'userCode').send_keys("10331")
        sleep(10)

        usr = admin.find_element("xpath", '//*[@id="bntSubmit"]').click()
        # user logged in
        for handle in admin.window_handles:
            if handle != main_page:
                login_page = handle

        admin.switch_to.window(login_page)

        get = admin.find_element("id", 'lnkMenu')
        get.click()

        sleep(3)
        admin.find_element(By.XPATH, '//*[@id="tblMain"]/tbody/tr[19]/td').click()

        admin.find_element("id", '20162300').click()

        get.click()
        admin.maximize_window()
        admin.switch_to.window(login_page)

        WebDriverWait(admin, 10)

        admin.switch_to.frame(
            admin.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/iframe'))
        # print(WebDriverWait(admin, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form1"]/table/tbody/tr[2]/td/table/tbody'))).text)
        # admin.find_element(By.XPATH, '').click()
        bel = Select(admin.find_element(By.ID,'dateType'))
        bel.select_by_value('t')
        sel = Select(admin.find_element(By.XPATH, '//*[@id="sAgentGrp"]'))
        sel.select_by_value('6207')

        admin.find_element(By.ID, 'btnNew').click()
        met = admin.get(
            'https://admin.imeforex-txn.net/SwiftSystem/Reports/AnalysisReport/TranAnalysisReport.aspx?reportName=20162310&fromDate=2022-7-30&toDate=2022-7-30&fromTime=00:00:00&toTime=23:59:59&dateType=P&status=&sCountry=&sAgent=&sBranch=&rCountry=Nepal&tranType=&groupBy=datewise&searchBy=sender&searchByText=&sAgentGrp=6207&sPartner=&controlNo=')
        get = admin.find_element(By.XPATH, '/html/body')

        # print(get.text)
        s = admin.get_window_size()
        # obtain browser height and width
        w = admin.execute_script('return document.body.parentNode.scrollWidth')
        h = admin.execute_script('return document.body.parentNode.scrollHeight')
        # set to new window size
        admin.set_window_size(w, h)
        # obtain screenshot of page within body tag
        abcd = admin.find_element(By.XPATH, '/html').screenshot("cspreport.png")
        admin.set_window_size(s['width'], s['height'])

    return HttpResponse('thank you </br>'
                        'report downloaded to server')



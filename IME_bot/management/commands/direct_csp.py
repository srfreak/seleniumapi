from time import sleep

from django.forms import Select
from django.http import HttpResponse


from selenium.webdriver.support.ui import Select
from selenium import webdriver

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

        date_type = request.POST.get('datetype')
        print(date_type)
        bel = Select(admin.find_element(By.ID, 'dateType'))
        bel.select_by_value(str(date_type))

        stat_s = request.POST.get('status')
        tel = Select(admin.find_element(By.ID, 'status'))
        tel.select_by_value(str(stat_s))

        date = request.POST.get('date')
        month = request.POST.get('date')

        date_b = date[0:2]

        month_b = month[3:5]

        if month_b[0] == str(0):
            month_b = int(month[4])
            month = int(month_b - 1)
            print(month)
        else:
            month_b = int(month[3:5])
            month = int(month_b - 1)
            print(month)
        if date_b[0] == str(0):
            date = date[1]
            print(date)
        else:
            date = date_b
            print(date)

        admin.find_element(By.CLASS_NAME, 'ui-datepicker-trigger').click()
        monthe = Select(admin.find_element(By.CLASS_NAME, 'ui-datepicker-month'))
        monthe.select_by_value(str(month))
        dat = admin.find_element(By.CLASS_NAME, 'ui-state-default')
        # dat = Select(admin.find_element(By.NAME,'fromDate'))
        sleep(1)
        admin.find_element(By.LINK_TEXT, str(date)).click()

        ## selecting report
        report = request.POST.get('sAgentGrp')
        print(report)
        sel = Select(admin.find_element(By.XPATH, '//*[@id="sAgentGrp"]'))
        sel.select_by_value(report)

        admin.find_element(By.ID, 'btnNew').click()
        sleep(2)
        admin.switch_to.window(admin.window_handles[2])
        get = admin.find_element(By.ID,'export').click()

        admin.find_element(By.XPATH, '/html/body')

        # print(get.text)
        s = admin.get_window_size()
        # obtain browser height and width
        w = admin.execute_script('return document.body.parentNode.scrollWidth')
        h = admin.execute_script('return document.body.parentNode.scrollHeight')
        # set to new window size
        admin.maximize_window()

        # obtain screenshot of page within body tag
        abcd = admin.find_element(By.XPATH, '/html').screenshot("cspreport.png")
        admin.set_window_size(s['width'], s['height'])
        sleep(30)
    return HttpResponse('thank you </br>'
                        'report downloaded to server')

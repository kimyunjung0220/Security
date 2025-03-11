from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import winsound
import ctypes

# 학번과 이름 정보
student_id = "" #학번
student_name = "" #이름 

driver = webdriver.Chrome()

last_warning_time = 0
warning_interval = 5 * 60  

last_quiz_warning_time = 0
quiz_warning_interval = 10 * 60  

is_done = True

try:

    driver.get("http://kopo.safetyedu.org/Account/LogOn")

    dropdown = driver.find_element(By.CLASS_NAME, "chosen-single")
    dropdown.click()

    campus_option = driver.find_element(By.XPATH, "//li[text()='강서캠퍼스']")
    campus_option.click()

    student_id_field = driver.find_element(By.ID, "UniqueKey1")
    student_id_field.send_keys(student_id)

    student_name_field = driver.find_element(By.NAME, "UserName")
    student_name_field.send_keys(student_name)


    login_button = driver.find_element(By.ID, "btnStudent")
    login_button.click()

    time.sleep(3)

    safety_education_image = driver.find_element(By.XPATH, "//img[@alt='연구실안전교육']")
    safety_education_image.click()

    time.sleep(3)
    while True:       
        if is_done : #지금 수강한 강의가 다 끝났는지?
            try:
                take_course_button = driver.find_element(By.XPATH, "//input[@value='수강하기' and @class='courseBtn']")
                take_course_button.click()
                time.sleep(3)
                driver.switch_to.window(driver.window_handles[-1])

                is_done = False
                time.sleep(5)
            except:
                pass
        try:
            text_bubble_button = driver.find_element(By.CLASS_NAME, "textBubble.view")
            time.sleep(3)
            text_bubble_button.click()
        except:
            pass

        try:
            text_bubble_button = driver.find_element(By.CLASS_NAME, "textBubble view")
            time.sleep(3)
            text_bubble_button.click()
        except:
            pass

        try:
            text_bubble_button = driver.find_element(By.ID, "text-bubble")
            time.sleep(3)
            text_bubble_button.click()
        except:
            pass

        try:
            text_bubble_button = driver.find_element(By.ID, "textBubble")
            time.sleep(3)
            text_bubble_button.click()
        except:
            pass

        try:
            play_button = driver.find_element(By.CLASS_NAME, "playingImg")
            time.sleep(3)
            play_button.click()
        except:
            pass

        try:
            quiz_start_button = driver.find_element(By.CLASS_NAME, "motion.quizStartBtn.sudden.view")
            time.sleep(3)
            quiz_start_button.click()
        except:
            pass

        try:
            option_button = driver.find_element(By.CLASS_NAME, "option.option_2.option_x")
            current_time = time.time()
            if current_time - last_warning_time > warning_interval:
                winsound.Beep(1000, 500)
                ctypes.windll.user32.MessageBoxW(0, "퀴즈", "경고", 0x40 | 0x1)
                last_warning_time = current_time
        except:
            pass

        try:
            quiz_button = driver.find_element(By.CLASS_NAME, "motion.quizStartBtn.view")
            current_time = time.time()
            if current_time - last_quiz_warning_time > quiz_warning_interval:
                winsound.Beep(1000, 500)
                ctypes.windll.user32.MessageBoxW(0, "퀴즈", "경고", 0x40 | 0x1)
                last_quiz_warning_time = current_time
        except:
            pass

        try:
            # cTime과 dTime이 동일하고, cPageNum과 tPageNum이 동일하며, "textBubble view"가 나타나지 않는 경우
            c_time = driver.find_element(By.CLASS_NAME, "cTime").text
            d_time = driver.find_element(By.CLASS_NAME, "dTime").text
            c_page_num = driver.find_element(By.CLASS_NAME, "cPageNum").text
            t_page_num = driver.find_element(By.CLASS_NAME, "tPageNum").text
            print(c_time, d_time, c_page_num, t_page_num)
            if c_time == d_time and c_page_num == t_page_num:
                try:
                    btn = driver.find_element(By.CLASS_NAME, "textBubble.view")
                    btn.click()
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    driver.refresh()
                    is_done = True
                except:
                    pass
                
                try:
                    btn = driver.find_element(By.CLASS_NAME, "moveBtn nextPageBtn")
                    btn.click()
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    driver.refresh()
                    is_done = True
                except:
                    pass
        except:
            pass
        time.sleep(1)



except:
    print("에러")

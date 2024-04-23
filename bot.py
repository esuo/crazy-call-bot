import time
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.common.by import By


def send_info(url: str, msg: str):
    print(msg)
    try:
        options = webdriver.ChromeOptions()
        # 无痕模式
        options.add_argument('--incognito')
        # 启动chrome浏览器无痕模式
        driver = webdriver.Chrome(options=options)
        # 打开百度
        driver.get("http://www.baidu.com")
        driver.get(url)
        time.sleep(1)
        driver.find_element(By.XPATH, '//textarea').send_keys(msg)
        driver.find_element(By.XPATH, '//div[text()="发送"]').click()
        driver.find_element(By.XPATH, '//textarea').send_keys("请电话联系我，谢谢")
        driver.find_element(By.XPATH, '//div[text()="发送"]').click()
        time.sleep(5)
        driver.quit()
    except Exception as exc:
        pass


def boom(phone):
    with open('api.txt', 'r') as file:
        urls = file.readlines()

    # 遍历链接地址
    for i, url in enumerate(urls):
        print(i, end=' - ')
        send_info(url, phone)
        time.sleep(1)


if __name__ == "__main__":
    process_list = []
    # todo Add more phone numbers if needed
    phones = ["name number1", "name number2", "name number3", ...]
    for phone in phones:
        p = Process(target=boom, args=(phone,))
        process_list.append(p)
        p.start()

    for p in process_list:
        p.join()

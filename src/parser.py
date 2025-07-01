import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def extract_data(data):
    driver = webdriver.Chrome()
    input_value = str(data)
    driver.get('https://www.wildberries.ru/')
    time.sleep(10)

    search_form = driver.find_element(by=By.ID, value='searchInput')
    search_form.send_keys(input_value)
    time.sleep(5)
    search_form.send_keys(Keys.RETURN)
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    # Собираем список для формирования поля 'title'
    web_element_for_find_title = driver.find_elements(By.CLASS_NAME, value='product-card__link ')
    list_for_find_title = []
    for e in web_element_for_find_title:
        list_for_find_title.append(e.get_attribute('outerHTML'))

    intermediate_title_list = [item.split('aria-label="')[1] for item in list_for_find_title]
    intermediate_title_list = [item.split('">')[0] for item in intermediate_title_list]
    intermediate_title_list = [item.replace('&quot;', '') for item in intermediate_title_list]
    title_list = [item.replace('&amp;', '') for item in intermediate_title_list]

    # print(len(title_list))
    # print(title_list)

    # Собираем список для формирования поля 'price'
    web_element_for_find_price = driver.find_elements(By.CLASS_NAME, value='price__lower-price')
    list_for_find_price = []
    for e in web_element_for_find_price:
        list_for_find_price.append((e.get_attribute('outerHTML')))

    intermediate_price_list = [item.split('">')[1] for item in list_for_find_price]
    intermediate_price_list = [item.split('&nbsp;₽')[0] for item in intermediate_price_list]
    price_list = [item.replace('&nbsp;', '') for item in intermediate_price_list]

    # print(len(price_list))
    # print(price_list)

    # Собираем список для формирования поля 'discounted_price'
    web_element_for_find_discounted_price = driver.find_elements(By.CLASS_NAME, value='price__wrap')
    list_for_find_discounted_price = []
    for e in web_element_for_find_discounted_price:
        list_for_find_discounted_price.append(e.get_attribute('outerHTML'))

    intermediate_discounted_price_list = [item.split('<del>')[1] for item in list_for_find_discounted_price]
    intermediate_discounted_price_list = [item.split('&nbsp;₽</del>')[0] for item in intermediate_discounted_price_list]
    discounted_price_list = [item.replace('&nbsp;', '') for item in intermediate_discounted_price_list]

    # print(len(discounted_price_list))
    # print(discounted_price_list)

    # Собираем список для формирования поля 'rating'
    web_element_for_find_rating = driver.find_elements(By.CLASS_NAME, value='address-rate-mini')
    list_for_find_rating = []
    for e in web_element_for_find_rating:
        list_for_find_rating.append(e.get_attribute('outerHTML'))

    intermediate_rating_list = [item.split('">')[1] for item in list_for_find_rating]
    intermediate_rating_list = [item.split('</span>')[0] for item in intermediate_rating_list]
    intermediate_rating_list = [item.replace(',', '.') for item in intermediate_rating_list]
    rating_list_prepare = []
    for item in intermediate_rating_list:
        if item == '':
            rating_list_prepare.append(0)
        else:
            rating_list_prepare.append(item)
    rating_list = list(map(float, rating_list_prepare))
    
    # print(len(rating_list))
    # print(rating_list)

    # Собираем список для формирования поля 'reviews'
    web_element_for_find_reviews = driver.find_elements(By.CLASS_NAME, value='product-card__count')
    list_for_find_reviews = []
    for e in web_element_for_find_reviews:
        list_for_find_reviews.append(e.get_attribute('outerHTML'))

    intermediate_reviews_list = [item.split('">')[1] for item in list_for_find_reviews]
    intermediate_reviews_list = [item.split('</span>')[0] for item in intermediate_reviews_list]
    intermediate_reviews_list = [item.replace('&nbsp;', '') for item in intermediate_reviews_list]
    intermediate_reviews_list = [item.replace(' оценок', '') for item in intermediate_reviews_list]
    intermediate_reviews_list = [item.replace(' оценки', '') for item in intermediate_reviews_list]
    intermediate_reviews_list = [item.replace(' оценка', '') for item in intermediate_reviews_list]
    intermediate_reviews_list = [item.replace('Нет', ' ') for item in intermediate_reviews_list]
    reviews_list = [item.replace(' ', '0') for item in intermediate_reviews_list]
    reviews_list = list(map(int, reviews_list))

    # print(len(reviews_list))
    # print(reviews_list)

    data_from_parser = list(zip(
        title_list,
        price_list,
        discounted_price_list,
        rating_list,
        reviews_list,
        ))

    # print(data_from_parser)


    time.sleep(5)

    driver.quit()
    return data_from_parser

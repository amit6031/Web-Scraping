import requests
from bs4 import BeautifulSoup
import numpy as np
import csv

csv_file = open('realme_scraped_data_multiple_pages.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Mobile Name', 'Rating', 'Number of Ratings', 'Storage', 'Screen', 'Camera', 'Battery', 'Type of Processor', 'Price'])

for page in np.arange(1,11):
    url = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&page={}".format(page)
    res = requests.get(url)

    try:
        res.raise_for_status()
        print(res.status_code)
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    soup = BeautifulSoup(res.text, 'lxml')
    objects = soup.find_all('div', class_="_1HmYoV _35HD7C")
    products_summaries = objects[1]
    all_products = products_summaries.find_all('div', class_="bhgxx2 col-12-12")
    print(len(all_products))
    for first_product in all_products[:-2]:

        try:
            mobile_name = first_product.find('div', class_="_3wU53n")
            # print(mobile_name.text)
            name = mobile_name.text
        except AttributeError:
            name = "None"


        try:
            mobile_rating = first_product.find('div', class_="hGSR34")
            # print(mobile_rating.text)
            rating = mobile_rating.text
        except AttributeError:
            rating = "None"


        try:
            number_of_ratings = first_product.find('span', class_="_38sUEc")
            ratings = number_of_ratings.span.span.text
            ratings = ratings.replace("Ratings", '')
            # print(ratings)
        except AttributeError:
            ratings = "None"


        mobile_summary = first_product.find_all('li', class_="tVe95H")

        try:
            storage_info = mobile_summary[0].text
            # print(storage_info)
        except AttributeError:
            storage_info = "None"

        try:
            screen_info = mobile_summary[1].text
            # print(screen_info)
        except AttributeError:
            screen_info = "None"

        try:
            camera_info = mobile_summary[2].text
            # print(camera_info)
        except AttributeError:
            camera_info = "None"

        try:
            battery_info = mobile_summary[3].text
            # print(battery_info)
        except AttributeError:
            battery_info = "None"

        try:
            processor_info = mobile_summary[4].text
            # print(processor_info)
        except AttributeError:
            processor_info = "None"

        try:
            mobile_price = first_product.find('div', class_="_1vC4OE _2rQ-NK")
            price = mobile_price.text
            price = price.replace("₹", "Rs.")
            # print(price)
        except AttributeError:
            price = "None"
        #print("***************************************")

        csv_writer.writerow([name, rating, ratings, storage_info, screen_info, camera_info, battery_info, processor_info, price])

csv_file.close()





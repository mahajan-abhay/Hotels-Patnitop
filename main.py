from flask import Flask,render_template,request
import selenium
from selenium import webdriver
import time
chrome_path = r"C:\Users\Abhay Mahajan\Downloads\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('https://www.google.com/travel/hotels/Patnitop?g2lb=2502548%2C2503781%2C4258168%2C4270442%2C4306835%2C4308226%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4515403%2C4518326%2C4536454%2C4545890%2C4270859%2C4284970%2C4291517&hl=en-IN&gl=in&ssta=1&ap=EgAwA2gB&q=hotels%20in%20patnitop&rp=EJGA_PHX1bqC1QEQ19a7_Ie0l5XUARDf46Xh8viNnHkQnIq2w5yr_OxVOAFAAEgCogEIUGF0bml0b3A&ictx=1&sa=X&utm_campaign=sharing&utm_medium=link&utm_source=htls&ts=CAESDgoCCAMKAggDCgIIAxAAGiwKDhIKOghQYXRuaXRvcBoAEhoSFAoHCOUPEAcYCRIHCOUPEAcYChgBMgIIASoLCgcoAToDSU5SGgA&ved=0CAAQ5JsGahgKEwiw3aOtkr_xAhUAAAAAHQAAAAAQwAI')
page = 0
hrefs = []
while page <= 1:
    time.sleep(5)
    hotels = driver.find_elements_by_class_name('PVOOXe')
    for hotel in hotels:
        hrefs.append(hotel.get_attribute("href"))
    time.sleep(5)
    # try:
    next_button = driver.find_element_by_xpath("//div[@class='U26fgb O0WRkf oG5Srb C0oVfc JDnCLc yHhO4c yNl8hd zbLWdb M9Bg4d']")
    next_button.click()
    page = page + 1
    # except:
    #     button = False
# names = []
# prices = []
# ratings = []
# addresses = []
# phone_numbers = []
data = []
for link in hrefs:
    driver.get(link)
    try:
        name = driver.find_element_by_xpath("//h1[@class='fZscne']").get_attribute('textContent')
        price = driver.find_element_by_xpath("//span[@class='qQOQpe prxS3d']").get_attribute('textContent')
        rating = driver.find_element_by_xpath("//div[@class='iDqPh BgYkof']").get_attribute('textContent')
        address = driver.find_element_by_xpath("//span[@class='CFH2De']").get_attribute('textContent')
        phone_number = driver.find_element_by_xpath("//span[@class='CFH2De'][2]").get_attribute('textContent')
        data.append({
            'name' : name,
            'price' : price,
            'rating' : rating,
            'address' : address,
            'phone_number' : phone_number
        })
        # names.append(name)
        # prices.append(price)
        # ratings.append(rating)
        # addresses.append(address)
        # phone_numbers.append(phone_number)
    except:
        continue
    
# from flask_sqlalchemy import SQLAlchemy
import json
# local_uri = True
# with open('config.json' , 'r') as f:
#     params = json.load(f)["params"]

app = Flask(__name__)

# if local_uri:
#     app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]

# db = SQLAlchemy(app)



# class Contacts(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     phone_num = db.Column(db.String(12), nullable=False)
#     message = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(12) , nullable = True)
#     email = db.Column(db.String(20), nullable=False)

@app.route('/')

def home():
    # for i in range(len(names)):
    #     print(names[i] , ' ' , prices[i])
    return render_template('index.html' , data = data)

# @app.route('/about')

# def about():
#     return render_template('about.html' , params = params)

# @app.route('/contact' , methods = ['GET' , 'POST'])

# def contact():
    
#     if (request.method == 'POST'):
#         name = request.form.get('name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         message = request.form.get('message')

#         entry = Contacts(name = name , phone_num = phone , message = message , email = email)
#         db.session.add(entry)
#         db.session.commit()

#     return render_template('contact.html' , params = params)

# @app.route('/post')

# def post():
#     return render_template('post.html' , params = params)

app.run(debug = True)
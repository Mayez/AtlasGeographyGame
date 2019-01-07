from flask import Flask, render_template, request
from random import randint
import urllib
import urllib.request
from bs4 import BeautifulSoup
import bs4 as bs

#with render template we can call upon any template we want to use
randomNum = randint(1,241)
import mysql.connector

test = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Password#1",
    database = "countries"
)

testCursor = test.cursor()
#testCursor.execute("CREATE DATABASE countries")
querycmd = "INSERT INTO countries (countryName,queryCheck) VALUES(%s,%s)"

countries = [
    ("afghanistan",0),
    ("ålandislands",0),
    ("albania",0),
    ("algeria",0),
    ("americansamoa",0),
    ("andorra",0),
    ("angola",0),
    ("anguilla",0),
    ("antarctica",0),
    ("antiguaandbarbuda",0),
    ("argentina",0),
    ("armenia",0),
    ("aruba",0),
    ("australia",0),
    ("austria",0),
    ("azerbaijan",0),
    ("bahamas",0),
    ("bahrain",0),
    ("bangladesh",0),
    ("barbados",0),
    ("belarus",0),
    ("belgium",0),
    ("belize",0),
    ("benin",0),
    ("bermuda",0),
    ("bhutan",0),
    ("bolivia",0),
    ("bosniaandherzegovina",0),
    ("botswana",0),
    ("bouvetisland",0),
    ("brazil",0),
    ("britishindianoceanterritory",0),
    ("bruneidarussalam",0),
    ("bulgaria",0),
    ("burkinafaso",0),
    ("burundi",0),
    ("cambodia",0),
    ("cameroon",0),
    ("canada",0),
    ("capeverde",0),
    ("caymanislands",0),
    ("centralafricanrepublic",0),
    ("chad",0),
    ("chile",0),
    ("china",0),
    ("christmasisland",0),
    ("cocosislands",0),
    ("colombia",0),
    ("comoros",0),
    ("congo",0),
    ("cookislands",0),
    ("costarica",0),
    ("coted'ivoire",0),
    ("croatia",0),
    ("cuba",0),
    ("cyprus",0),
    ("czechrepublic",0),
    ("democraticrepublicofthecongo",0),
    ("denmark",0),
    ("djibouti",0),
    ("dominica",0),
    ("dominicanrepublic",0),
    ("ecuador",0),
    ("egypt",0),
    ("elsalvador",0),
    ("equatorialguinea",0),
    ("eritrea",0),
    ("estonia",0),
    ("ethiopia",0),
    ("falklandislands",0),
    ("faroeislands",0),
    ("fiji",0),
    ("finland",0),
    ("france",0),
    ("frenchguiana",0),
    ("frenchpolynesia",0),
    ("frenchsouthernterritories",0),
    ("gabon",0),
    ("gambia",0),
    ("georgia",0),
    ("germany",0),
    ("ghana",0),
    ("gibraltar",0),
    ("greece",0),
    ("greenland",0),
    ("grenada",0),
    ("guadeloupe",0),
    ("guam",0),
    ("guatemala",0),
    ("guernsey",0),
    ("guinea",0),
    ("guinea-Bissau",0),
    ("guyana",0),
    ("haiti",0),
    ("heardislandandmcdonaldislands",0),
    ("honduras",0),
    ("hongkong",0),
    ("hungary",0),
    ("iceland",0),
    ("india",0),
    ("indonesia",0),
    ("iran",0),
    ("iraq",0),
    ("ireland",0),
    ("isleofman",0),
    ("israel",0),
    ("italy",0),
    ("jamaica",0),
    ("japan",0),
    ("jersey",0),
    ("jordan",0),
    ("kazakhstan",0),
    ("kenya",0),
    ("kiribati",0),
    ("kuwait",0),
    ("kyrgyzstan",0),
    ("laopeople'sdemocraticrepublic",0),
    ("latvia",0),
    ("lebanon",0),
    ("lesotho",0),
    ("liberia",0),
    ("libyanarabjamahiriya",0),
    ("liechtenstein",0),
    ("lithuania",0),
    ("luxembourg",0),
    ("macao",0),
    ("macedonia",0),
    ("madagascar",0),
    ("malawi",0),
    ("malaysia",0),
    ("maldives",0),
    ("mali",0),
    ("malta",0),
    ("marshall Islands",0),
    ("martinique",0),
    ("mauritania",0),
    ("mauritius",0),
    ("mayotte",0),
    ("mexico",0),
    ("micronesia",0),
    ("moldova",0),
    ("monaco",0),
    ("mongolia",0),
    ("montserrat",0),
    ("morocco",0),
    ("mozambique",0),
    ("myanmar",0),
    ("namibia",0),
    ("nauru",0),
    ("nepal",0),
    ("netherlands",0),
    ("netherlandsantilles",0),
    ("newcaledonia",0),
    ("newzealand",0),
    ("nicaragua",0),
    ("niger",0),
    ("nigeria",0),
    ("niue",0),
    ("norfolkisland",0),
    ("northernmarianaislands",0),
    ("northkorea",0),
    ("norway",0),
    ("oman",0),
    ("pakistan",0),
    ("palau",0),
    ("palestinianterritory",0),
    ("panama",0),
    ("papuanewguinea",0),
    ("paraguay",0),
    ("peru",0),
    ("philippines",0),
    ("pitcairn",0),
    ("poland",0),
    ("portugal",0),
    ("puertorico",0),
    ("qatar",0),
    ("reunion",0),
    ("romania",0),
    ("russia",0),
    ("rwanda",0),
    ("sainthelena",0),
    ("saintkittsandnevis",0),
    ("saintlucia",0),
    ("saintpierreandmiquelon",0),
    ("saintvincentandthegrenadines",0),
    ("samoa",0),
    ("sanmarino",0),
    ("saotomeandprincipe",0),
    ("saudiarabia",0),
    ("senegal",0),
    ("serbiaandmontenegro",0),
    ("seychelles",0),
    ("sierraleone",0),
    ("singapore",0),
    ("slovakia",0),
    ("slovenia",0),
    ("solomonislands",0),
    ("somalia",0),
    ("southafrica",0),
    ("southgeorgiaandthesouthsandwichislands",0),
    ("southkorea",0),
    ("spain",0),
    ("srilanka",0),
    ("sudan",0),
    ("suriname",0),
    ("svalbardandjanmayen",0),
    ("swaziland",0),
    ("sweden",0),
    ("switzerland",0),
    ("syrianarabrepublic",0),
    ("taiwan",0),
    ("tajikistan",0),
    ("tanzania",0),
    ("thailand",0),
    ("timor-leste",0),
    ("togo",0),
    ("tokelau",0),
    ("tonga",0),
    ("trinidadandtobago",0),
    ("tunisia",0),
    ("turkey",0),
    ("turkmenistan",0),
    ("turksandcaicosislands",0),
    ("tuvalu",0),
    ("uganda",0),
    ("ukraine",0),
    ("unitedarabemirates",0),
    ("unitedkingdom",0),
    ("unitedstatesofamerica",0),
    ("uruguay",0),
    ("uzbekistan",0),
    ("vanuatu",0),
    ("vaticancity",0),
    ("venezuela",0),
    ("vietnam",0),
    ("virginislands",0),
    ("wallisandfutuna",0),
    ("westernsahara",0),
    ("yemen",0),
    ("zambia",0),
    ("zimbabwe",0),
]

testCursor.execute("CREATE TABLE countries (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,countryName VARCHAR(150), queryCheck INTEGER(10))")
testCursor.executemany(querycmd, countries)
randcursor = test.cursor()
print("here is the :",randomNum)
randcursor.execute("SELECT countryName from countries WHERE id = (%s)", (randomNum,))
results = randcursor.fetchone()
print("1.here is the country " + results[0])
testCursor.execute("Drop table IF EXISTS countries")
test.commit()

#testCursor.execute("SELECT * from countries")
#results = testCursor.fetchall()

app = Flask(__name__)

@app.route('/')
def index():
        return render_template("index.html")

@app.route('/index2' , methods =['GET','POST'])
def index2():
    if request.method == 'POST':
        username = request.form['username']
        print(username)
        return render_template("index2.html", username=username, country=results[0])

@app.route('/index3', methods = ['POST'])
def index3():
    countryName = request.form['countryName']
    print(countryName)
    countryQuery(countryName)
    index2()
    return 'This is the %s' % (countryName)

def countryQuery(country):
    countryCurs = test.cursor()
    print("Country Query right here: " + country)
#    countryCurs.execute("SELECT * from countries WHERE countryName = (%s)", (country))


if __name__ == "__main__":
        app.run()



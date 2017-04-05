# -*- coding: cp1252 -*-
#This code for extracting weather data from the website www.wunderground.com for the city Banglore and Cochin
#This code can extract data from the year 2015 till present date.


from selenium import webdriver
from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.axis_project

chrome_path = r"C:\Users\Praveer\Desktop\chromedriver.exe"
driver =  webdriver.Chrome(chrome_path)
res = {'banglore':'BG','cochin':'CC'}
month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
heading = ['Year','Month','Date','Temperature_high','Temperature_avg','Temperature_low','Dew_Point_high','Dew_Point_avg','Dew_Point_low','Humidity_high','Humidity_avg','Humidity_low','Sea_Level_Press_hPa_high','Sea_Level_Press_hPa_avg','Sea_Level_Press_hPa_low','Visibility_km_high','Visibility_km_avg','Visibility_km_low','Wind_kmph_high','Wind_kmph_avg','Wind_kmph_low','Precip_mm_sum','Event_1','Event_2','Event_3']
city = input("Enter the city(banglore/cochin) : ")
year = input("Enter the year, from you want to start fetching data : ")
while True:
        driver.get("https://www.wunderground.com/history/airport/VO"+res[city]+"/"+str(year)+"/1/1/CustomHistory.html?dayend=31&monthend=12&yearend="+str(year)+"&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=")
        table = driver.find_element_by_id("obsTable")
        rows = table.find_elements_by_tag_name("tbody")
        for row in rows:
                a=str(row.text)
                a=a.split()
                if a[0] in month:
                        m = a[0]
                        continue
                if ',' in a:
                        a.remove(',')
                if ',' in a:
                        a.remove(',')
                _id_value = str(year)+m+str(a[0])
                value = [year,m]
                value.extend(a)
                doc = {'_id':_id_value}
                diff = len(heading) - len(value)
                l = len(value)
                if diff == 1:
                        for i in range(0,l):
                                doc.update({heading[i]:value[i]})
                        doc.update({heading[i+1]:'-'})
                elif diff == 2:
                        for i in range(0,l):
                                doc.update({heading[i]:value[i]})
                        doc.update({heading[i+1]:'-'})
                        doc.update({heading[i+2]:'-'})
                elif diff == 3:
                        for i in range(0,l):
                                doc.update({heading[i]:value[i]})
                        doc.update({heading[i+1]:'-'})
                        doc.update({heading[i+2]:'-'})
                        doc.update({heading[i+3]:'-'})
                else:
                        for i in range(0,l):
                                doc.update({heading[i]:value[i]})
                db.weather_cochin.insert_one(doc)
                
        year = year + 1
        if year == 2018:
                break


        
        













        

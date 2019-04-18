# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:55:57 2018

@author: user
"""

import requests
import csv
from bs4 import BeautifulSoup
from functools import cmp_to_key

states = [
('Alabama', 'AL'),
('Alaska', 'AK'),
('Arizona', 'AZ'),
('Arkansas', 'AR'),
('California', 'CA'),
('Colorado', 'CO'),
('Connecticut', 'CT'),
('Delaware', 'DE'),
('Florida', 'FL'),
('Georgia', 'GA'),
('Hawaii', 'HI'),
('Idaho', 'ID'),
('Illinois', 'IL'),
('Indiana', 'IN'),
('Iowa', 'IA'),
('Kansas', 'KS'),
('Kentucky', 'KY'),
('Louisiana', 'LA'),
('Maine', 'ME'),
('Maryland', 'MD'),
('Massachusetts', 'MA'),
('Michigan', 'MI'),
('Minnesota', 'MN'),
('Mississippi', 'MS'),
('Missouri', 'MO'),
('Montana', 'MT'),
('Nebraska', 'NE'),
('Nevada', 'NV'),
('New Hampshire', 'NH'),
('New Jersey', 'NJ'),
('New Mexico', 'NM'),
('New York', 'NY'),
('North Carolina', 'NC'),
('North Dakota', 'ND'),
('Ohio', 'OH'),
('Oklahoma', 'OK'),
('Oregon', 'OR'),
('Pennsylvania', 'PA'),
('Rhode Island', 'RI'),
('South Carolina', 'SC'),
('South Dakota', 'SD'),
('Tennessee', 'TN'),
('Texas', 'TX'),
('Utah', 'UT'),
('Vermont', 'VT'),
('Virginia', 'VA'),
('Washington', 'WA'),
('West Virginia', 'WV'),
('Wisconsin', 'WI'),
('Wyoming', 'WY')]

#WHaatt does this Custom compare do Why dont I document BEtter!!!!
def cmp(a, b):
    a = int(a[-10:-5:1])
    b = int( b[-10:-5:1])
    return ((a>b) - (a<b))

f = csv.writer(open('golf_courses.csv', 'w'))
f.writerow(['Name', 'Street', 'City', 'State', 'Zip1', 'Zip2', 'County', 'Email', 'Phone', 'Fax', 'Description','Public/Private', 'Year Built', 'Annual Rounds','Season', 'Manager', 'Club Pro', 'Superintendent', 'Guest Policy', 'Designer', 'Shop Hours', 'Dress Code', 'Fee Weekend', 'Fee Weekday', 'Tee Time Reservations', 'Online Reservations', 'Earliest Tee Time', 'Holes', 'Greens Type', 'Fairway Type', 'Water Hazards', 'Bunkers', 'Metal Spikes', 'Aeration', 'Fivesomes Alloweed'])

for tup in states:

    page = requests.get('http://www.golfnationwide.com/Golf-Courses-By-State/'+tup[0]+'-Golf-Courses__'+tup[1]+'.aspx')

    soup = BeautifulSoup(page.text, 'html.parser')

    course_list = soup.find('table')

    courses = course_list.find_all('a')
    names =[]
    for course in courses:
        name = 'http://www.golfnationwide.com' + course.get('href')
        names.append(name)

    urls = sorted(names, key = cmp_to_key(cmp))


    for page in urls:

        page = requests.get(page)

        soup = BeautifulSoup(page.text, 'html.parser')

        course_info = soup.find_all("dl")

        entry=[]
        for dl in course_info:
            info = dl.find_all('span')

            for data in info:
                try:
                    entry.append(data.contents[0])
                except:
                    entry.append('N/A')

        f.writerow(entry)



 

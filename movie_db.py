import requests
import json
import requests
import sys
import os
import subprocess
import openpyxl
import math
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "movies detail"
sheet.append(["total number", "page number", "sr# on page", "name of movie", "release date",
             "movie id"])


base_link = 'https://api.themoviedb.org/3/movie/'
apikey = 'api_key=09dca7662d0a1cfeb2c11cffa70c83ad'


intput_type = input('''please type any type between\n
>>now playing\n >>popular\n >>top rated\n >>upcoming\n >>  ''')

if intput_type == "now playing":
    base_link = base_link+'now_playing?'
    t_link = base_link+apikey
    print(t_link)
elif intput_type == "popular":
    base_link = base_link+'popular?'
    t_link = base_link+apikey
    print(t_link)
elif intput_type == "upcoming":
    base_link = base_link+'upcoming?'
    t_link = base_link+apikey
    print(t_link)
elif intput_type == "top rated":
    base_link = base_link+'top_rated?'
    t_link = base_link+apikey
    print(t_link)
else:
    ("print galat command")

# print("hahaha")
# print(t_link)
f = int(input("please enter a num you want to fetch>>  "))
g = f/20
g = math.ceil(g)
g = int(g)
st = "&page="
tcount = 1
for x in range(0, g):

    final = t_link+st+str(x+1)
    print("page", x+1, "\n")
    data = requests.get(final).text
    data = json.loads(data)
    a = data.get("results")
# print(a)
    for movies in range(len(a)):
        title = a[movies]["title"]
        date = a[movies]['release_date']
        overview = a[movies]['overview']
        i_d = a[movies]["id"]

        print(
            f"{tcount}>> [page{x+1}]..{movies+1}. name of movie: {title}. || date of release is: {date}. || id is: {i_d}")
        sheet.append([tcount, x+1, movies+1, title, date, i_d])
        excel.save("the_movies_db.xlsx")
        tcount += 1
        if tcount == f+1:
            break

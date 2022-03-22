import requests
import json

url = "https://theunitedstates.io/congress-legislators/legislators-current.json"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
url2 = "https://theunitedstates.io/congress-legislators/legislators-historical.json"
response2 = requests.get(url2)
data2 = response2.text
parsed2 = json.loads(data2)
parsed = parsed + parsed2
temp = []

"""
for i in parsed:
    if i["id"]["govtrack"] not in temp:
        temp.append(i)

parsed = temp
 """

year_list = []
for i in parsed:
    if i["bio"]["gender"] == "F":
        for k in i["terms"]:
            if k["type"] == "rep":
                start = int(k["start"][0:4])
                end = int(k["end"][0:4])
                while int(start) < end:
                    year_list.append(start)
                    start = int(start) + 1

year_list = list(dict.fromkeys(year_list))
year_list.sort()

year_count = []
for i in year_list:
    count = 0
    for j in parsed:
        if j["bio"]["gender"] == "F":
            for k in j["terms"]:
                if k["type"] == "rep":
                    start = int(k["start"][0:4])
                    end = int(k["end"][0:4])
                    while int(start) < end:
                        if int(start) == i:
                            count += 1
                        start = int(start) + 1


    year_count.append(count)

index = 0
for i in year_list:
    print(i, ": ", "#" * year_count[index])
    index += 1

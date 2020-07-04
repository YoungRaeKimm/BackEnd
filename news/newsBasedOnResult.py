import json
import math
import googlemaps
import sys
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import pandas as pd

with open('C:/Users/kimyoungrae/Desktop/UROP/Integrated_bjh_Clustering_Result.json', 'r') as f:  # json 파일을 입력받는다.
    json_data = json.load(f)
for i in range(len(json_data)):  # 클러스터 번호를 매긴다.
    json_data[i]["cluster"] = i + 1

num_cluster = len(json_data)  # 클러스터의 총 개수를 세어준다.

Count_of_cluster_point = [i * 0 for i in range(num_cluster + 1)]  # cluster 마다의 count 수
Stay_time_at_cluster = [i * 0 for i in range(num_cluster + 1)]  # cluster 마다의 stay_time

for i in range(num_cluster):  # 클러스터마다 data를 입력해준다.
    Count_of_cluster_point[json_data[i]["cluster"]] += float(json_data[i]["count"])
    Stay_time_at_cluster[json_data[i]["cluster"]] += float(json_data[i]["hourSpent"])

ROAVF = [i * 0 for i in range(num_cluster + 1)]  # ROAVF 를 담을 공간을 만들어준다
ROAVD = [i * 0 for i in range(num_cluster + 1)]  # ROAVD 를 담을 공간을 만들어준다

sum_all_Count_point = 0  # 모든 clustercount 합친다
for i in range(num_cluster):
    sum_all_Count_point += Count_of_cluster_point[i]

sum_all_Count_time = 0  # 모든 clustertime 합친다.
for i in range(num_cluster):
    sum_all_Count_time += Stay_time_at_cluster[i]

for i in range(1, num_cluster + 1):  # ROAVF , ROAVD 값을 구한다.
    ROAVF[i] = math.log10(float(sum_all_Count_point / Count_of_cluster_point[i]))
    ROAVD[i] = math.log10(float(sum_all_Count_time / Stay_time_at_cluster[i]))

for i in range(num_cluster):  # json 파일에 데이터를 넣는다.
    json_data[i]["ROAVD"] = ROAVD[i + 1]
    json_data[i]["ROAVF"] = ROAVF[i + 1]

min_ROAVD = json_data[0]["ROAVD"]
min_index = 0
# ROAVD 최소와 index의 최소에 뜬다.
for i in range(num_cluster):
    if (min_ROAVD > json_data[i]["ROAVD"]):
        min_ROAVD = json_data[i]["ROAVD"]
        min_index = i

min_lat = float(json_data[min_index]["latitude"])
min_long = float(json_data[min_index]["longitude"])
gmaps = googlemaps.Client(key="AIzaSyASGHS5UhPxrzP1nHXw2-AqLE9ZEHMqjuM")
sample = gmaps.reverse_geocode((min_lat, min_long), language='ko')
result = sample[0].get("formatted_address")
result_gu = result.split(" ")
location = result_gu[2]



location_text = ""
title_text = []
link_text = []
time_text = []
press_text = []
result = {}
RESULT_PATH = 'C:/Users/kimyoungrae/Desktop/UROP/NewsCrawling'
now = datetime.now()

finallocation = location


def crawler(finallocation):
    url = 'https://search.naver.com/search.naver?query=' + finallocation + '&where=news&ie=utf8&sm=nws_hty'
    hdr = {'User-Agent': (
        'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')}
    req = requests.get(url, headers=hdr)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    ErrorCheck = soup.find('div', {'id': 'notfound'})

    if not 'None' in str(ErrorCheck):
        print("Error! 지역 검색 오류! 정확한 지역 이름을 입력하십시오.")
        sys.exit(1)
    else:  # 지역 뉴스검색 결과 텍스트
        for i in soup.select('h1[class=blind]'):
            LocationInfo = i.text
            location_text = LocationInfo  # 뉴스 체크
        checknews = soup.find('ul', 'type01')

        print("* " + LocationInfo + " *\n=============================")  # 뉴스

        for i in range(0, 100):  # 뉴스 타이틀 출력을 위한 체크 단계
            firstnews1 = checknews.find('li', {'id': 'sp_nws{}'.format(i)})  # sp_nws의 숫자가 일정하지 않기 때문에 걸러주는 단계
            if str(firstnews1) == "None":
                continue

            firstnews2 = firstnews1.dl.dt.a
            firstnewsinfo1 = firstnews1.dl.dd  # 에러 체크 단계
            if str(firstnews2) == "None" or str(firstnewsinfo1) == "None":
                print("Error! 개발자에게 문의하십시오.")
                sys.exit(1)
            else:  # 타이틀 및 하이퍼링크 추출
                firstnews = firstnews2.get('title')
                title_text.append(firstnews)
                firstnewshref = firstnews2.get('href')
                link_text.append(firstnewshref)
                firstnewsinfo2 = firstnewsinfo1.text  # 신문사 및 기사 시간 추출
                if "언론사 선정" in firstnewsinfo2:
                    firstnewsinfo3 = firstnewsinfo2.split("언론사 선정")
                    firstnewsinfo = firstnewsinfo3[0]
                    press_text.append(firstnewsinfo)
                    firstnewsinfo4 = firstnewsinfo3[1].split(" ")
                    firstnewstime = firstnewsinfo4[1]
                    time_text.append(firstnewstime)
                else:
                    firstnewsinfo3 = firstnewsinfo2.split(" ")
                    firstnewsinfo = firstnewsinfo3[0]
                    press_text.append(firstnewsinfo)
                    firstnewstime = firstnewsinfo3[1]
                    time_text.append(firstnewstime)

            print(firstnews + " - " + firstnewsinfo + " - " + firstnewstime)
            print(firstnewshref + "\n")
        result = {"time": time_text, "title": title_text, "press": press_text, "link": link_text}

        df = pd.DataFrame(result)  # df로 변환

    outputFileName = '%s(%s.%s.%s %s시 %s분 %s초).xlsx' % (

        location_text, now.year, now.month, now.day, now.hour, now.minute, now.second)
    df.to_excel(RESULT_PATH + outputFileName, sheet_name='sheet1')


crawler(finallocation)
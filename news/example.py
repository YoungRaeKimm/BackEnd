import datetime as datetime



data=[{'author': 'SSY',
  'timestamp': '1560999668.0',
  'timezone': 'Asia/Seoul',
  'latitude': '37.54865',
  'longitude': '126.923'},
 {'author': 'SSY',
  'timestamp': '1621000394.0',
  'timezone': 'Asia/Seoul',
  'latitude': '37.548685',
  'longitude': '126.92308'},
 {'author': 'SSY',
  'timestamp': '1621000478.0',
  'timezone': 'Asia/Seoul',
  'latitude': '37.54865',
  'longitude': '126.92299833333334'},
 {'author': 'SSY',
  'timestamp': '1709001181.0',
  'timezone': 'Asia/Seoul',
  'latitude': '37.54864166666667',
  'longitude': '126.92275333333333'}]

#txt 파일 만들기
num_timestamp=float(data[0]["timestamp"])
d = datetime.datetime.fromtimestamp(int(num_timestamp))
f = open(str(d.year)+str(d.month)+str(d.day)+'.txt', 'w')

#txt 파일 안에 데이터 넣기
for i in range(len(data)):
    new_timestamp=float(data[i]["timestamp"])
    newd = datetime.datetime.fromtimestamp(int(new_timestamp))
    #timestamp가 다를 경우 timestamp 교체
    if(d.date()!=newd.date()):
        f.close()
        num_timestamp=new_timestamp
        d=newd
        f = open(str(d.year)+str(d.month)+str(d.day)+'.txt', 'w')
    #메모장 안에 데이터들 쓰기
    f.write(str(d.year)+'|'+str(d.month)+'|'+str(d.day)+'\t')
    f.write(str(d.hour)+':'+str(d.minute)+':'+str(d.second)+'|'+str('000')+'\t')
    f.write(str(float(data[i]["timestamp"]))+'|'+str('000')+'\t')
    f.write('%.12f\t' %float(data[i]["latitude"]))
    f.write('%.12f' %float(data[i]["longitude"])+'\n')
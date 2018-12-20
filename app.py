from flask import Flask,render_template,request
import requests
import random
import json
from faker import Faker
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/lotto')
def lotto(): #로또 당첨번호 for문으로 들고오기
    url ="https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"#동행로또링크
    res = requests.get(url).text
    lotto_dict = json.loads(res)#딕셔너리를 lotto_dict에 저장
    print(lotto_dict["drwNoDate"])
    week_format_num = []
    num_list = range(1,46)#1~45값 뽑아옴
    pick= random.sample(num_list,6)#sample 함수를 pick에 저장
    
    for i in range(1,7):
        week_format_num.append(lotto_dict["drwtNo{}".format(i)])#한줄로 코드만드는 방법
        #포맷팅 방법을이용해 i에 값을 넣는다
        #포멧팅하는 방식1
        #"오{}".format(b) #a=오 b=창희 
        #결과값 오창희
        
    #print(type(res))
    #print(type(json.loads(res))) #json이 res를 읽어서 딕셔너리로 바꿔줘
    t=0
    for j in range(1,7):
        for w in range(1,7):
            if(week_format_num[j-1]==pick[w-1]):
                t= t+1
    f= 6-t
    print(t)
    print(f)
    
    rank = ["꼴등","5등","4등","3등","2등","1등"]
    a = ""
    for i in range(6):
        if (t==i):
            print(rank[i])
            a = str(rank[i])
    
    
            
    return render_template("lotto.html",lotto=pick, week_format_num=week_format_num , t=t, a=a ,f=f)
    #pick 을 lotto에 담아서 lotto.html로보냄
    #html 하나를 사용자한테 보내줌
    #templates라는 폴더를 만들어줘야됨
    #규칙이기때문에 lotto.html을 templates에서 읽음
    #그리고 templates폴더에 lotto.html 파일생성
    #render_template는 플라스크에서 쓰는 함수
    
@app.route('/ping')
def ping():
     return render_template("ping.html")

@app.route('/pong')
def pong():
    input_name=request.args.get('name')#requests와 다름 파이썬에 기본적으로있는 모듈 불러오기
    #args 데이터를 의미 get가져옴
    #input_name에 넣음
    fake = Faker('ko_KR')
    fake_job = fake.city()
    return render_template("pong.html",html_name=input_name, fake_job=fake_job, fake= fake)
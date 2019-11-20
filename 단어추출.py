import json
import re


from konlpy.tag import Twitter
from collections import Counter

import pytagcloud
import webbrowser

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager , rc

def showGraph(wordinfo):
    font_location = 'C:\Windows\Fonts\malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font',family = font_name)

    plt.xlabel("주요 단어")
    plt.ylabel("빈도수")
    plt.grid(True)
#    plt.grid(False)

    sorted_Dict_values = sorted(wordinfo.values(), reverse = True)

    sorted_Dict_keys = sorted(wordinfo, key = wordinfo.get, reverse = True)
    '''
        막대 그래프 그리는 함수
        pyplot.bar 인자값
         = 데이터 인덱스(X축)
         = 데이터 리스트 값
         = 막대그래프의 폭(width)
         = 색상
         = 에러 편차 값 등
    '''
    plt.bar(range(len(wordinfo)), sorted_Dict_values, align = 'center')

    '''
        X축에 표시하는 내용이 많을경우
        내용이 겹치지 않게 하기 위해서 사용
        rotation = '70'
          ==> 문자열을 70도만큼 회전
    '''

    plt.xticks(range(len(wordinfo)), list(sorted_Dict_keys), rotation='70')

    plt.show()

def saveWordCloud(wordinfo, filename) :
    taglist = pytagcloud.make_tags(dict(wordinfo).items(), maxsize=80)
    pytagcloud.create_tag_image(taglist, filename, size = (640, 480), fontname = "korean")

    webbrowser.open(filename)
    
    

def main() :
    openFileName = "C:\python_exe\jtbcnews_facebook_2016-10-01_2017-03-12.json"
    cloudimagePath = openFileName + '.jpg'

    print("cloudimagePath : %s" % (cloudimagePath))
    rfile = open(openFileName, 'r', encoding='utf-8').read()

    jsonData = json.loads(rfile)
    message = ""

    for item in jsonData :
        if 'message' in item.keys() :
            message = message + re.sub(r"[^\w]",'', item['message'])+''

    nlp = Twitter()
    nouns = nlp.nouns(message)
    count = Counter(nouns)

    wordinfo = dict()
    for tags, counts in count.most_common(70):
        if len(str(tags)) > 1 :
            wordinfo[tags] = counts
            print("%s : %d" % (tags, counts))

    showGraph(wordinfo)

    saveWordCloud(wordinfo, cloudimagePath)

if __name__ == '__main__':
    main()

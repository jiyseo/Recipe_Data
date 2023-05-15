#라이브러리 import
import requests
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv
import os 
 
load_dotenv()

#요청url 잘게 자르기
url = "https://openapi.foodsafetykorea.go.kr/api"
serviceKey = os.environ.get('Servicekey')
info="/COOKRCP01"
data_format = "/xml"
startNum = "/1"
endNum = "/1000"
 
#항목 parsing 함수작성하기
def parse():
    try:
        RCP_SEQ = item.find("RCP_SEQ").get_text()
        RCP_NM = item.find("RCP_NM").get_text()
        RCP_WAY2 = item.find("RCP_WAY2").get_text()
        RCP_PAT2 = item.find("RCP_PAT2").get_text()
        RCP_PARTS_DTLS = item.find("RCP_PARTS_DTLS").get_text()
        INFO_WGT = item.find("INFO_WGT").get_text()
        INFO_ENG = item.find("INFO_ENG").get_text()
        ATT_FILE_NO_MAIN = item.find("ATT_FILE_NO_MAIN").get_text()
        ATT_FILE_NO_MK = item.find("ATT_FILE_NO_MK").get_text()
        MANUAL01 = item.find("MANUAL01").get_text()
        MANUAL_IMG01 = item.find("MANUAL_IMG01").get_text()
        MANUAL02 = item.find("MANUAL02").get_text()
        MANUAL_IMG02 = item.find("MANUAL_IMG02").get_text()
        MANUAL03 = item.find("MANUAL03").get_text()
        MANUAL_IMG03 = item.find("MANUAL_IMG03").get_text()
        MANUAL04 = item.find("MANUAL04").get_text()
        MANUAL_IMG04 = item.find("MANUAL_IMG04").get_text()
        MANUAL05 = item.find("MANUAL05").get_text()
        MANUAL_IMG05 = item.find("MANUAL_IMG05").get_text()
        MANUAL06 = item.find("MANUAL06").get_text()
        MANUAL_IMG06 = item.find("MANUAL_IMG06").get_text()
        MANUAL07 = item.find("MANUAL07").get_text()
        MANUAL_IMG07 = item.find("MANUAL_IMG07").get_text()
        MANUAL08 = item.find("MANUAL08").get_text()
        MANUAL_IMG08 = item.find("MANUAL_IMG08").get_text()
        MANUAL09 = item.find("MANUAL09").get_text()
        MANUAL_IMG09 = item.find("MANUAL_IMG09").get_text()
        MANUAL10 = item.find("MANUAL10").get_text()
        MANUAL_IMG10 = item.find("MANUAL_IMG10").get_text()
        MANUAL11 = item.find("MANUAL11").get_text()
        MANUAL_IMG11 = item.find("MANUAL_IMG11").get_text()
        MANUAL12 = item.find("MANUAL12").get_text()
        MANUAL_IMG12 = item.find("MANUAL_IMG12").get_text()
        MANUAL13 = item.find("MANUAL13").get_text()
        MANUAL_IMG13 = item.find("MANUAL_IMG13").get_text()
        MANUAL14 = item.find("MANUAL14").get_text()
        MANUAL_IMG14 = item.find("MANUAL_IMG14").get_text()
        MANUAL15 = item.find("MANUAL14").get_text()
        MANUAL_IMG15 = item.find("MANUAL_IMG15").get_text()
        MANUAL16 = item.find("MANUAL14").get_text()
        MANUAL_IMG16 = item.find("MANUAL_IMG16").get_text()
        MANUAL17 = item.find("MANUAL17").get_text()
        MANUAL_IMG17 = item.find("MANUAL_IMG17").get_text()
        MANUAL18 = item.find("MANUAL18").get_text()
        MANUAL_IMG18 = item.find("MANUAL_IMG18").get_text()
        MANUAL19 = item.find("MANUAL19").get_text()
        MANUAL_IMG19 = item.find("MANUAL_IMG19").get_text()
        MANUAL20 = item.find("MANUAL20").get_text()
        MANUAL_IMG20 = item.find("MANUAL_IMG20").get_text()

        return {
            "일련번호":RCP_SEQ,
            "메뉴명":RCP_NM,
            "조리방법":RCP_WAY2,
            "요리종류":RCP_PAT2,
            "재료정보":RCP_PARTS_DTLS,
            "중량":INFO_WGT,
            "열량":INFO_ENG,
            "이미지경로(소)":ATT_FILE_NO_MAIN,
            "이미지경로(대)":ATT_FILE_NO_MK,
            "만드는법_01":MANUAL01,
            "만드는법_이미지_01":MANUAL_IMG01,
            "만드는법_02":MANUAL02,
            "만드는법_이미지_02":MANUAL_IMG02,
            "만드는법_03":MANUAL03,
            "만드는법_이미지_03":MANUAL_IMG03,
            "만드는법_04":MANUAL04,
            "만드는법_이미지_04":MANUAL_IMG04,
            "만드는법_05":MANUAL05,
            "만드는법_이미지_05":MANUAL_IMG05,
            "만드는법_06":MANUAL06,
            "만드는법_이미지_06":MANUAL_IMG06,
            "만드는법_07":MANUAL07,
            "만드는법_이미지_07":MANUAL_IMG07,
            "만드는법_08":MANUAL08,
            "만드는법_이미지_08":MANUAL_IMG08,
            "만드는법_09":MANUAL09,
            "만드는법_이미지_09":MANUAL_IMG09,
            "만드는법_10":MANUAL10,
            "만드는법_이미지_10":MANUAL_IMG10,
            "만드는법_11":MANUAL11,
            "만드는법_이미지_11":MANUAL_IMG11,
            "만드는법_12":MANUAL12,
            "만드는법_이미지_12":MANUAL_IMG12,
            "만드는법_13":MANUAL13,
            "만드는법_이미지_13":MANUAL_IMG13,
            "만드는법_14":MANUAL14,
            "만드는법_이미지_14":MANUAL_IMG14,
            "만드는법_15":MANUAL15,
            "만드는법_이미지_15":MANUAL_IMG15,
            "만드는법_16":MANUAL16,
            "만드는법_이미지_16":MANUAL_IMG16,
            "만드는법_17":MANUAL17,
            "만드는법_이미지_17":MANUAL_IMG17,
            "만드는법_18":MANUAL18,
            "만드는법_이미지_18":MANUAL_IMG18,
            "만드는법_19":MANUAL19,
            "만드는법_이미지_19":MANUAL_IMG19,
            "만드는법_20":MANUAL20,
            "만드는법_이미지_20":MANUAL_IMG20
        }
    except AttributeError as e:
        return {
            "일련번호":None,
            "메뉴명":None,
            "조리방법":None,
            "요리종류":None,
            "재료정보":None,
            "중량":None,
            "열량":None,
            "이미지경로(소)":None,
            "이미지경로(대)":None,
            "만드는법_01":None,
            "만드는법_이미지_01":None,
            "만드는법_02":None,
            "만드는법_이미지_02":None,
            "만드는법_03":None,
            "만드는법_이미지_03":None,
            "만드는법_04":None,
            "만드는법_이미지_04":None,
            "만드는법_05":None,
            "만드는법_이미지_05":None,
            "만드는법_06":None,
            "만드는법_이미지_06":None,
            "만드는법_07":None,
            "만드는법_이미지_07":None,
            "만드는법_08":None,
            "만드는법_이미지_08":None,
            "만드는법_09":None,
            "만드는법_이미지_09":None,
            "만드는법_10":None,
            "만드는법_이미지_10":None,
            "만드는법_11":None,
            "만드는법_이미지_11":None,
            "만드는법_12":None,
            "만드는법_이미지_12":None,
            "만드는법_13":None,
            "만드는법_이미지_13":None,
            "만드는법_14":None,
            "만드는법_이미지_14":None,
            "만드는법_15":None,
            "만드는법_이미지_15":None,
            "만드는법_16":None,
            "만드는법_이미지_16":None,
            "만드는법_17":None,
            "만드는법_이미지_17":None,
            "만드는법_18":None,
            "만드는법_이미지_18":None,
            "만드는법_19":None,
            "만드는법_이미지_19":None,
            "만드는법_20":None,
            "만드는법_이미지_20":None
        }
 
#parsing 하기
url1 = url+serviceKey+ info + data_format + startNum + endNum
result = requests.get(url1)
result.raise_for_status()
soup = BeautifulSoup(result.text,'lxml-xml')
row = []
for i in range (0, 1000) :
    item = soup.find("row", attrs={"id":i})
    row.append(parse())
#print(row)
startNum = "/1001"
endNum = "/1058"
url2 = url + serviceKey+ info + data_format + startNum + endNum
result = requests.get(url2)
result.raise_for_status()
soup = BeautifulSoup(result.text,'lxml-xml')
for i in range (0, 61) :
    item = soup.find("row", attrs={"id":i})
    row.append(parse())
 
#pandas 데이터프레임에 넣기
df = pd.DataFrame(row)
 
#csv 파일로 저장하기
df.to_csv("공공데이터_레시피정보.csv",mode='w')

#csv 파일 불러오기        
data = pd.read_csv("공공데이터_레시피정보.csv",index_col=0)
df2 = pd.DataFrame(data)

print("save!")
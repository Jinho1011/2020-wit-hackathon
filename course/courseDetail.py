from bs4 import BeautifulSoup
import requests

TIMETABLE_URL = 'https://kupis.konkuk.ac.kr/sugang/acd/cour/time/SeoulTimetableInfo.jsp'
REMAIN_URL_GRADE = 'https://kupis.konkuk.ac.kr/sugang/acd/cour/aply/CourBasketInwonInq.jsp'
RATE_URL = 'https://api.everytime.kr/find/timetable/subject/list'


def get_grade(g, number):
    GRADE_RES = requests.post(REMAIN_URL_GRADE, data={
        'ltYy': 2020,
        'ltShtm': 'B01012',
        'sbjtId': number,
        'promShyr': g,
        'fg': 'B'
    })

    html = GRADE_RES.text
    soup = BeautifulSoup(html, 'html.parser')
    infos = soup.find_all('td')[1].text
    return infos


def main(number):
    object_list = {}
    data = {
        'ltYy': 2020,
        'ltShtm': 'B01012',
        'sbjtId': number
    }
    res = requests.post(TIMETABLE_URL,
                        data=data)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    infos = soup.select(
        'table.table_bg > tr.table_bg_white'
    )

    for tr in infos:
        object_list["courseCode"] = tr.select('td')[3].text
        object_list["courseProfessor"] = tr.select('td')[9].text
        object_list["courseTime"] = tr.select('td')[8].text
        object_list["courseType"] = tr.select('td')[2].text
        object_list["courseTarget"] = tr.select('td')[7].text
        object_list["courseTitle"] = tr.select('td')[4].text
        object_list["courseLink"] = 'https://kupis.konkuk.ac.kr/sugang/acd/cour/plan/CourLecturePlanInq.jsp?ltYy=2020&ltShtm=B01012&sbjtId=' + number
        object_list["courseRemain1"] = get_grade(1, number)
        object_list["courseRemain2"] = get_grade(2, number)
        object_list["courseRemain3"] = get_grade(3, number)
        object_list["courseRemain4"] = get_grade(4, number)

    return object_list

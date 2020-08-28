from bs4 import BeautifulSoup
import requests

TIMETABLE_URL = 'https://kupis.konkuk.ac.kr/sugang/acd/cour/time/SeoulTimetableInfo.jsp'
REMAIN_URL_ENTIRE = 'https://kupis.konkuk.ac.kr/sugang/acd/cour/aply/CourInwonInqTime.jsp'
REMAIN_URL_GRADE = 'https://kupis.konkuk.ac.kr/sugang/acd/cour/aply/CourBasketInwonInq.jsp'


def get_remain(code):
    REMAIN_ENTIRE_DATA = {
        'ltYy': 2020,
        'ltShtm': 'B01012',
        'sbjtId': code
    }

    REMAIN_ENTIRE_RES = requests.post(
        REMAIN_URL_ENTIRE, data=REMAIN_ENTIRE_DATA)
    REMAIN_ENTIRE_HTML = REMAIN_ENTIRE_RES.text
    REMAIN_ENTIRE_SOUP = BeautifulSoup(REMAIN_ENTIRE_HTML, 'html.parser')

    REMAIN_ENTIRE_RES = REMAIN_ENTIRE_SOUP.find_all(
        "td", {'class': 'table_bg_white', 'align': 'center'})

    res = []

    for r in REMAIN_ENTIRE_RES:
        res.append(r.text)

    return res


def main(courseInfo):
    object_list = []

    TIMETABLE_DATA = {
        'ltYy': 2020,
        'ltShtm': 'B01012',
        'openSust': courseInfo['openSust'],
        'pobtDiv': courseInfo['pobtDiv'],
        'sbjtId': courseInfo['sbjtId'],
        'sbjtNm': courseInfo['sbjtNm'],
    }

    TIMETABLE_RES = requests.post(TIMETABLE_URL, data=TIMETABLE_DATA)
    TIMETABLE_HTML = TIMETABLE_RES.text
    TIMETABLE_SOUP = BeautifulSoup(TIMETABLE_HTML, 'html.parser')

    TIMETABLE_TRS = TIMETABLE_SOUP.select(
        'table.table_bg > tr.table_bg_white'
    )

    for tr in TIMETABLE_TRS:
        course = {}
        course["courseGrade"] = tr.select('td')[0].text
        if course["courseGrade"].startswith("검색한"):
            return None
        course["courseType"] = tr.select('td')[2].text
        course["courseNumber"] = tr.select('td')[3].text
        course["courseTitle"] = tr.select('td')[4].text
        course["courseTime"] = tr.select('td')[8].text
        course["courseProfessor"] = tr.select('td')[9].text
        REMAIN_DATA = get_remain(course["courseNumber"])
        course["courseRemainAll"] = REMAIN_DATA[0]
        course["courseRemainCurrent"] = REMAIN_DATA[1]
        object_list.append(course)

    return object_list

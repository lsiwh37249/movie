import requests
import os

def req2dataframe():
    _, data = req()
    #data.get('').get('')
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    print(l[0])
    return l

def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key

def req(dt="20120101"):
    #url = gen_url('202420720')
    url = gen_url()
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    return code, data

def gen_url(dt="20120101"):
    base_url ="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json" 
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"
    return url

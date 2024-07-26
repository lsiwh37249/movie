from src.movie.api.call import gen_url, req, get_key, req2dataframe

def test_req2dataframe():
    data = req2dataframe()
    #print(data[0].get('rnum'))
    #assert len(l) > 0
    #assert 'rnum' in v.keys()
    #assert v['rnum'] == '1'
    assert data[0].get('rnum') == '1'
    

def test_비밀키숨기기():
    key = get_key()
    assert key    

def test_gen_url():
    url = gen_url()
    assert "http" in url
    assert "kobis" in url
    #assert url == "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=43e14f5940bd8b7cdab05226ec6e833a&targetDt=20120101" 
    
def test_req():
    code,data = req()
    print(code)
    print(data)
    assert code == 200

    code, data = req('20120101')
    assert code == 200

    

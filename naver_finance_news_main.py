import requests
from bs4 import BeautifulSoup

def get_news_from_naver_stock():
    # 네이버 증권 뉴스 섹션의 기본 URL
    base_url = 'https://finance.naver.com'

    # HTTP GET 요청을 보내어 웹 페이지의 HTML을 가져옵니다.
    response = requests.get(base_url + '/news/')

    # 200이면 성공한 거다.
    # 웹 페이지 로딩에 성공했는지 확인
    if response.status_code == 200:
        # BeautifulSoup 객체를 생성하여 HTML을 파싱합니다.
        soup = BeautifulSoup(response.text, 'html.parser')

        # 기사 제목과 링크가 포함된 HTML 요소를 찾습니다.
        # 이 부분은 네이버 증권 사이트의 HTML 구조에 따라 달라질 수 있습니다.
        news_area = soup.find('div', class_='main_news')

        if news_area:
            headlines = news_area.find_all("li")
            # 각 기사에 대한 제목과 링크를 추출합니다.
            for headline in headlines:
                title = headline.find('a').get_text().strip()
                # get_text()로 요소 내의 모든 텍스트를 추출한다. 그리고 strip()으로 불필요한 공백을 정리
                link = base_url + headline.find('a')['href']
                # href는 HTML <a> 태그의 속성으로, 링크가 가리키는 URL을 지정합니다.
                # 이때 얻게 되는 링크는 상대 URL이므로 절대 URL로 변환해주어야 사용 가능하다.
                print(f"Title: {title}")
                print(f"Link: {link}")
                print("-" * 40)
        else:
            print("Error: News area not found")
    else:
        print("Error: Unable to load the web page")

# 함수를 호출하여 뉴스를 가져옵니다.
get_news_from_naver_stock()
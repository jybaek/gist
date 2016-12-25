## summary
특정 종목(code)의 주식 정보를 [네이버](http://www.naver.com) 주식페이지를 통해 크롤링 합니다. 네이버로 과도한 트래픽을 발생시키거나 기타 문제를 발생시키는 행위는 프로그램을 사용하는 본인에게 있음을 잊지 마십시오.


## usage

실행 인자로 주식의 코드를 넘깁니다. 예를 들어 코드가 `123456789`라면 아래와 같이 실행하시면 됩니다.

```bash
    $ python finance.py 123456789

	종목 시세 정보
	2016년 12월 16일 16시 10분 기준 장마감
	종목명 xxxxxxxx
	종목코드 123456789 코스닥
	현재가 xxxxxx 전일대비 하락 80 마이너스 4.28 퍼센트
	전일가 xxxxxxx
	시가 xxxxxx
	고가 xxxxxx
	상한가 xxxxxxx
	저가 xxxxxxx
	하한가 xxxxxxx
	거래량 xxxxxxxxx
	거래대금 xxxxxxxx백만

	$
```

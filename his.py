import os

books = [{"num": 1, "제목": "안드로이드앱개발", "저자": "최전산", "출판사": "PCB", "출판년도": "2017", "재고": 0},
               {"num": 2, "제목": "파이썬", "저자": "강수라", "출판사": "연두", "출판년도": "2019", "재고": 0},
               {"num": 3, "제목": "자바스크립트", "저자": "박정식", "출판사": "SSS", "출판년도": "2018", "재고": 0},
               {"num": 4, "제목": "HTML5", "저자": "주환", "출판사": "대한", "출판년도": "2011", "재고": 0},
               {"num": 5, "제목": "컴파일러", "저자": "장진웅", "출판사": "PCB", "출판년도": "2011", "재고": 0},
               {"num": 6, "제목": "C언어", "저자": "헝말숙", "출판사": "한국", "출판년도": "2010", "재고": 0},
               {"num": 7, "제목": "프로그래밍언어론", "저자": "현정숙", "출판사": "정의출판", "출판년도": "2010", "재고": 0},
               {"num": 8, "제목": "안드로이드", "저자": "이광희", "출판사": "한국", "출판년도": "2013", "재고": 0},
               {"num": 9, "제목": "앱인벤터", "저자": "박규진", "출판사": "대한", "출판년도": "2015", "재고": 0}]

#,kmklmklmklmlk


def bookLental(): # 대여 기능
    while True:
        slt=input('1) 장바구니보기  2)대여하기 \n>>')
        if slt == '1':
            for all in books:
                print(all)
            choice=input('1) 확인  2) 선택 취소 \n>>')
            if choice == '1':
                print('확인을 누르셨습니다.')
                home=input('아무키 누르시면 홈으로 돌아갑니다.\n>>')
                os.system('clear')
            elif choice == '2':
                title = input('취소할 도서 이름: ')
                for x in books:
                    if x['제목'].find(title)!=-1:
                        books.remove(x)
                        print('취소완료되었습니다.')
                home=input('아무키 누르시면 홈으로 돌아갑니다.\n>>')
                os.system('clear')
            else:
                print('잘못입력했습니다.')
        elif slt=='2':
            print('대여완료되었습니다.')
            break
        else:
            print('잘못입력했습니다.')
bookLental()
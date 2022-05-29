import os

books = [{"num": 1, "제목": "안드로이드앱개발", "저자": "최전산", "출판사": "PCB", "출판년도": "2017"},
         {"num": 2, "제목": "파이썬", "저자": "강수라", "출판사": "연두", "출판년도": "2019"},
         {"num": 3, "제목": "자바스크립트", "저자": "박정식", "출판사": "SSS", "출판년도": "2018"},
         {"num": 4, "제목": "HTML5", "저자": "주환", "출판사": "대한", "출판년도": "2011"},
         {"num": 5, "제목": "컴파일러", "저자": "장진웅", "출판사": "PCB", "출판년도": "2011"},
         {"num": 6, "제목": "C언어", "저자": "헝말숙", "출판사": "한국", "출판년도": "2010"},
         {"num": 7, "제목": "프로그래밍언어론", "저자": "현정숙", "출판사": "정의출판", "출판년도": "2010"},
         {"num": 8, "제목": "안드로이드", "저자": "이광희", "출판사": "한국", "출판년도": "2013"},
         {"num": 9, "제목": "앱인벤터", "저자": "박규진", "출판사": "대한", "출판년도": "2015"}]
        #bookLental() > 장보구니에 담긴 것으로 간주 하여 삭제 기능 
        #bookGive()   > 도서 전체 책 리스트로 간주하여 추가 

def bookLental():  # 대여 기능
    while True:
        check=0
        slt = input('1) 장바구니보기  2)대여하기 \n>>')
        if slt == '1':
            print(*books, sep='\n')
            choice = input('1) 확인  2) 선택 취소 \n>>')
            if choice == '1':
                print('확인을 누르셨습니다.')
                home = input('아무키 누르시면 홈으로 돌아갑니다.\n>>')
                os.system('clear')
            elif choice == '2':
                title = input('취소할 도서 이름: ')
                for x in books:
                    if x['제목'].find(title)!= -1:
                        books.remove(x)
                        print('취소완료되었습니다.')
                        home = input('아무키 누르시면 홈으로 돌아갑니다.\n>>')
                        check=1
                if check ==0:
                    print('장바구니에 {} 도서는 없습니다.'.format(title))
                    home = input('아무키 누르시면 홈으로 돌아갑니다.\n>>')
                os.system('clear')
            else:
                print('잘못입력했습니다.')
        elif slt == '2':
            print('대여완료되었습니다.')
            break
        else:
            print('잘못입력했습니다.')


def bookGive():
    mybook = ['작별인사', '남매', '세상', '히어로', '행성']
    give = []
    while True:
        check=0
        print(*books, sep='\n')
        slt = input('1) 기증하기   2) 내 책 보기  3) 종료 \n>>')
        os.system('clear')
        if slt == '1':
            bookbye = input('기증할 책 이름을 적으세요\n>>')
            for x in mybook:
                if x == bookbye:
                    mybook.remove(bookbye)
                    a = len(books)+1
                    c = input('저자를 입력해주세요\n>>')
                    d = input('출판사를 입력해주세요\n>>')
                    e = input('출판 년도를 입력해주세요\n>>')
                    give = {'num': a, '제목': bookbye, '저자': c, '출판사': d, '출판 년도': e}
                    books.append(give)
                    print(give)
                    check=1
                    os.system('clear')
            if check == 0:
                print("보유중인 중인 책이 없어 '기증'할 수 없습니다.")
                print()
        elif slt =='2':
            os.system('clear')
            print(mybook)
            home = input('아무키나 입력하세요\n>>')
            os.system('clear')
        elif slt == '3':
            print('종료합니다.')
            break
        else:
            print('잘못입력했습니다.')



bookLental()
#bookGive()

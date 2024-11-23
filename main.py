import random as rd
import time as ti
<<<<<<< HEAD
import event as ev

# 텍스트 어드벤쳐 rpg
=======
# 텍스트 어드벤쳐 rgp
>>>>>>> 951974481f301870bb6d7c9c7d9ac4f306e47ddb
# 서울2033 패러디
# 개미친 김정은이 핵미사일을 광주에 떨궈서 그 여파로 난장판이 된 순천에서 살아남는 스토리
# 제한시간 6일동안 도시를 돌아다니며 물자를 획득 후 집으로 돌아와야됨
# 특정 이벤트 특정 선택지를 골라 >> 조건이 쌓여서 마지막에 갈림
# 이벤트마다 선택지에 다른 결과가 출력됨

# 상태 설정
hp = 3
san = 3

# 엔딩 조건
q1 = 0
q2 = 0
q3 = 0


<<<<<<< HEAD
=======
def day1(r):
    global hp, san
    global q1, q2, q3
    if r == 1:
        # print문하고 input문으로 문자 출력하고 선택지 제시해서 그에따른 결과 출력하도록 작성
        # 세미 아포칼립스이니 그에 맞는 지문
        print("쓰레기통을 발견했다")
        ans = int(input("1:  뒤진다 2: 무시한다 3: 옆 골목으로 향한다   "))
        if ans == 1:
            if rd.randint(1, 10) > 5:
                print("먹을것을 찾았다")
                print("음식을 먹고 기운을 차렸다 체력 상승 1 정신력 상승 1")
                if hp < 3:
                    hp += 1
                if san < 3:
                    san += 1
            else:
                print("더러운것을 보았다. 정신력 감소 1")
                san -= 1
        elif ans == 2:
            if rd.randint(1, 10) > 3:
                print("돌아오는 길에먹을 것을 발견했다. 체력 상승 1")
                if hp < 3:
                    hp += 1
            else:
                print("오늘은 빈손이다")
        else:
            if rd.randint(1, 10) > 8:
                print("이상한 여자를 만났다")
                ans2 = int(input("1: 말을 건다 2: 공격한다 3: 무시한다  "))
                if ans2 == 1:
                    if rd.randint(1, 10) > 6:
                        print("도움이 될거에요")
                        print("무전기를 얻었다")
                        q1 = 1
                    else:
                        print("더러우니까 말걸지 마세요.")
                        print("상처받았다 정신력 감소 1")
                        san -= 1
                elif ans2 == 2:
                    print("헛짓거리 하지 마세요")
                    print("역공 당했다 체력 감소 1")
                    hp -= 1
                else:
                    if rd.randint(1, 10) > 3:
                        print("잡지를 하나 주웠다")
                        print("재밌었다. 정신력 상승 1")
                        if san < 3:
                            san += 1
            else:
                print("오늘은 빈손이다")
    elif r == 2:
        print("야생 동물을 만났다")
        ans = int(input('1: 도망간다 2: 싸운다 3: 먹을 것을 준다    '))
        if ans == 1:
            print('무사히 도망쳤다.')
        if ans == 2:
            if rd.randint(1, 10) < 5:
                print('상처를 입었다. 체력 하락 1')
                hp -= 1
            else:
                print('동물을 사냥해 식량을 확보했다. 체력 상승 1')
                if hp < 3:
                    hp += 1
        if ans == 3:
            if rd.randint(1, 10) < 7:
                print('별 관심을 가지지 않더니 이내 사라졌다.')
            elif rd.randint(1, 10) >= 7 and rd.randint(1, 10) <= 9:
                print('동료를 얻었다. 상당히 귀엽다. 정신력 상승 1')
                if san < 3:
                    san += 1
            else :
                print('날 먹잇감으로 착각했다')
                hp = 0
                san = 0
    else:
        print("test")
def day2(r):
    print("Test")



>>>>>>> 951974481f301870bb6d7c9c7d9ac4f306e47ddb
# for문으로 6번 반복
for i in range(1, 7):
    # 현채 상태 출력해줌
    print(f"---{i}일차---")
    print(f"현재 건강상태 체력: {hp} 정신력: {san}")
    # i값은 날짜를 의미. 3일 이하를 전반기, 그 이후를 후반기로 보고 값은 나눔
    # 현재 날짜가 3일 이하일 시 day1함수 작동
    #if i <= 3:
<<<<<<< HEAD
    ev.day1(rd.randint(1, 3)) # randint(n, m) n에서 m사이의 정수 반환
    # 현재 날짜가 4 이상일 시 day2 작동
    #else:
    #   ev.day2(rd.randint(1, 3))
=======
    day1(rd.randint(1, 3)) # randint(n, m) n에서 m사이의 정수 반환
    # 현재 날짜가 4 이상일 시 day2 작동
    #else:
    #   day2(rd.randint(1, 3))
>>>>>>> 951974481f301870bb6d7c9c7d9ac4f306e47ddb
    if hp < 0 or san < 0:
        print("여기까지인듯 하다...")
        print("당신은 죽었습니다")
        break
    print("집으로 돌아왔다")
    ti.sleep(1)
    # 엔딩
    if i == 6:
        print("다시한번 폭탄이 떨어져습니다\n다행히 당신은 대피소 근처였고 서둘러 숨었으나 그곳엔 당신 뿐입니다\n이제 당신은 홀로 버텨야됩니다")
        ti.sleep(1)
        if q1 and q2 and q3:
            print("당신은 물건들을 활용해 버티는데 성공했습니다\n이제 당신은 다시 밖으로 나갈 차례입니다\nHappy Ending")
        else:
            print("슬프게도 당신은 생존에 도움될 물건이 부족했습니다\n홀로 벙커안에서 쓸쓸히 무너지게 되었습니다\nBad Ending")
        exit(0)

exit(0)
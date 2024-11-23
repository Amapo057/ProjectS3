import random as rd
# q1, q2, q3 모두 1로 만드는 조건 있어야함

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
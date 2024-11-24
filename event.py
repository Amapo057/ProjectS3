import random as rd
# q1 = 라디오, q2 = 보존식량, q3 = 총 모두 1로 만드는 조건 있어야함

# 상태 설정
hp = 3
san = 3

# 엔딩 조건
q1 = 0
q2 = 0
q3 = 0

def event1(r):
    global hp, san
    global q1, q2, q3
    # 랜덤 1일때
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
                        print("라디오를 얻었다")
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
    # 랜덤 2일떄
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
    # 랜덤 3일때
    else:
        print('피곤함이 몰려온다')
        ans = int(input('1: 졸음을 참는다 2: 잔다   '))
        if ans == 1:
            if rd.randint(1, 10) <= 5:
                print('정신이 몽롱하다. 정신력 하락 1')
                san -= 1
            else:
                print('아무일도 일어나지 않았다.')
        if ans == 2:
            if rd.randint(1, 20) < 6:
                print('잠든 사이 식량을 도둑맞았다. 체력 하락 1')
                hp -= 1
            elif rd.randint(1, 20) >= 6 and rd.randint(1, 20) < 19:
                print('몸이 개운해졌다. 체력 상승 1')
                if hp < 3:
                    hp += 1
            else:
                print('눈을 뜨니 내 방이다. 그렇다 꿈이였다.. 히든엔딩')
                exit(0)
def event2(r):
    global hp, san
    global q1, q2, q3
    if r == 1:
        print('아파트에 도착했다. 무엇을 할까?')
        ans = int(input('1: 웅성이는 집문을 두드려본다 2: 반쯤 열려있는 듯한 문을 열어본다 3: 옥상으로 올라간다'))
        if ans == 1:
            print('갑자기 조용해지더니 긴장감이 맴돈다. 급하게 밖으로 뛰어나왔다')
        elif ans == 2:
            if rd.randint(1, 10) <= 8:
                print('집에 사람은 없고 약간의 식량만 있었다. 체력 상승 1')
                if hp < 3:
                    hp += 1
            else:
                print('문에는 부비트랩이 설치되어 있었다.. 사망')
                hp = 0
        else:    
            if rd.randint(1, 10) <= 8:
                print('옥상은 잠겨있어 들어갈 수 없다.')
            else:
                print('로제와 브루노 마스가 옥상에 있었다. 아파트~ 아파트~ 히든 엔딩')
                exit(0)
    elif r == 2:
        print('백화점에 도착했다. 무엇을 할까?')
        ans = int(input('1:옷가게로 간다 2:식료품점으로 간다 3: 명품관에 간다'))
        if ans == 1:
            print('간만에 멀쩡한 옷을 마련했다. 정신력 상승 1')
            if san < 3:
                    san += 1
        elif ans == 2:
            if rd.randint(1, 3) > 2:
                print("식료품 가판대 사이에서 보존식품을 찾았다")
            else:
                print("아무것도 찾지 못했다")
        else:
            print('경보가 울리더니 이내 문이 잠겼다. 안에 고립됬다.')
            print('무엇을 해야할까?')
            act = int(input('1.근처의 무거운 물건을 유리창으로 던진다 2.사람의 힘으로 할 영역이 아닌 것 같다. 포기한다'))
            if act == 1:
                if rd.randint(1, 8) < 3:
                    print('유리창이 깨져 탈출할 수 있었다.')
                elif rd.randint(1, 8) <= 3 and rd.randint(1, 8) > 5:
                    print('유리창이 깨져 탈출할 수 있었다. 하지만 유리파편이 튀어 상처를 입었다. 체력 하락 1')
                    hp -= 1
                elif rd.randint(1, 8) <= 5 and rd.randint(1, 8) > 7:
                    print('유리창에 던진 무거운 물체가 튕겨나더니 내 머리로 날라왔다. 사망')
                    hp = 0
                else:
                    print('유리창을 부숴보려 별짓을 다했으나 끄덕없다. 이 안에 완전히 고립됬다. 사망')
                    hp = 0    
            else:
                if rd.randint(1, 8) < 3:
                    print('가방에 있던 식량으로 몇일을 버텼으나 결국 아사했다. 사망')
                    hp = 0
                elif rd.randint(1, 8) <= 3 and rd.randint(1, 8) > 5:
                    print('시간이 지나니 자동으로 잠겼던 문이 열렸다')
                elif rd.randint(1, 8) <= 5 and rd.randint(1, 8) > 7:
                    print('꼼짝없이 갇힌줄 알았지만 다행히도 직원전용 뒷문이 있었다.')
                else:
                    print('경보를 듣고 가게 앞으로 다른 생존자가 찾아왔다. 생존자들은 총기로 무장한듯 보인다')
                    print('무엇을 해야할까?')
                    act = int(input('1.아무도 없는 척 숨어본다 2.살려달라고 소리친다'))
                    if act == 1:
                        print('안을 몇번 살펴보더니 이내 사라졌다. 도움을 요청해야하나 고민했지만 혼자 죽는 것보다 사람들이 더 무섭다. 사망')
                        hp = 0
                    else:
                        if rd.randint(1, 2) == 1:
                            print('그들은 주변에서 악명높은 약탈자였다. 살려달라 하염없이 빌었지만 소용없었다. 사망')
                            hp = 0
                        else:
                            print('생존자들은 다행히도 좋은 사람들이였다. 경보가 들리길래 구하러 와줬다고 한다. 해피엔딩')
                            exit(0)
    else:
        print("버려진 창고를 발견했다")
        ans = int(input("1: 들어간다 2: 무시한다    "))
        if ans == 1:
            if rd.randint(1, 10) > 7:
                print("총과 총알 3발을 찾았다. ")
                q3 = 1
            else:
                print("빈 창고였다")
import random as rd
import time as ti
import event as ev

# 텍스트 어드벤쳐 rpg
# 서울2033 패러디
# 개미친 김정은이 핵미사일을 광주에 떨궈서 그 여파로 난장판이 된 순천에서 살아남는 스토리
# 제한시간 6일동안 도시를 돌아다니며 물자를 획득 후 집으로 돌아와야됨
# 특정 이벤트 특정 선택지를 골라 >> 조건이 쌓여서 마지막에 갈림
# 이벤트마다 선택지에 다른 결과가 출력됨


for i in range(1, 8):
    if i == 1:
        print("순천 2033")
        print("전쟁으로 인해 황폐해진 도시. 멀지 않은 도시에서 일어난 폭발이 핵폭탄이라는 말도있다.")
        print("그 상황에서 당신은 생존하기위한 도구를 찾아나선다.")
    # 현채 상태 출력해줌
    print(f"---{i}일차---")
    print(f"현재 건강상태 체력: {ev.hp} 정신력: {ev.san}")
    # i값은 날짜를 의미. 3일 이하를 전반기, 그 이후를 후반기로 보고 값은 나눔
    # 현재 날짜가 3일 이하일 시 event1함수 작동
    if i <= 3:
        ev.event1(rd.randint(1, 3)) # randint(n, m) n에서 m사이의 정수 반환
    elif i >=4 and i <= 5:
        ev.event2(rd.randint(1, 2))
    else:
        ev.event3()
    # 현재 날짜가 4 이상일 시 event2 작동
    #else:
    #   ev.event2(rd.randint(1, 3))
    if ev.hp == 0 or ev.san == 0:
        print("여기까지인듯 하다...")
        print("당신은 죽었습니다")
        break
    print("집으로 돌아왔다")
    ti.sleep(1)
    # 엔딩
    if i == 7:
        print("다시한번 폭탄이 떨어져습니다\n다행히 당신은 대피소 근처였고 서둘러 숨었으나 그곳엔 당신 뿐입니다\n이제 당신은 홀로 버텨야됩니다")
        ti.sleep(1)
        if ev.q1:
            if ev.q2 and ev.q3:
                print("당신은 물건들을 활용해 버티는데 성공했습니다\n이제 당신은 다시 밖으로 나갈 차례입니다\nHappy Ending")
            elif ev.q2:
                print("식량을 조금씩 나눠먹으며 버틴지 20일차, 라디오에서 소리가 들립니다")
                print("'생존하신 시민여러분은 밖으로 나와주시기 바랍니다. 전쟁은 끝났습니다.'")
                print("당신은 고민에 빠졌습니다")
                ans = int(input("1: 나간다 2: 가만히 있는다    "))
                if ans == 1:
                    if rd.randint(1, 10) > 5:
                        print("당신은 국군과 조우했습니다. 다행히 전쟁은 끝났으나 군대에 징집되게 되었습니다.")
                        print("Ending n.3 -Call of Duty")
                    else:
                        print("방송은 빨갱이들의 작전이였습니다. 당신은 그저 무력하게 끌려가는 수 밖에 없습니다.")
                        print("Ending n.4 -Call of Aoji")
                else:
                    print("당신은 자꾸만 떠오르는 의구심에 밖으로 나가지 못했습니다.")
            else:
                print("당신은 벽이 무너졌는지 열리지 않는 문을 열지 못하고 벙커 안에서 라디오만 붙들다 쓰러졌습니다")
                print("Bad Ending n.6 -radio")
        else:
            print("슬프게도 당신은 생존에 도움될 물건이 부족했습니다\n홀로 벙커안에서 쓸쓸히 무너지게 되었습니다")
            print("Bad Ending n.10 -Komm, süßer Tod")
        


exit(0)
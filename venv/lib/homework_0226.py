
import random

#답변리스트 10
ans1="오늘은 미세먼지 하나 없는 청명한 날씨네요."
ans2="달콤한 커피 한잔이 기분좋은 곳으로 데려가줄꺼예요."
ans3="명상을 해보세요. 이너피스-"
ans4="오늘은 이만 칼퇴하세요!"
ans5="여행은 언제나 옳죠!"
ans6="갑자기 떠나는건 어떨까요?"
ans7="대충살자!!"
ans8="오늘만 산다"
ans9="사는게 다 똑같죠"
ans10="글쎄요. 저도 이제 정말 모르겠네요."



print("파이썬 이번주 홈워크\n올라! 최첨단 인공지능 대화로봇이 되고 싶은 JEN입니다.")

text = ""


while text != 'Quit':
    text = input("무엇을 도와드릴까요?\n>")
    choice=random.randint(1, 10)
    if choice == 1:
        answer=ans1
    elif choice == 2:
        answer=ans2
    elif choice == 3:
        answer=ans3
    elif choice == 4:
        answer=ans4
    elif choice == 5:
        answer=ans5
    elif choice == 6:
        answer=ans6
    elif choice == 7:
        answer=ans7
    elif choice == 8:
        answer=ans8
    elif choice == 9:
        answer=ans9
    else:
        answer=ans10
    # 화면에 답변을 출력합니다.
    print(answer)


input("\n\n엔터키를 눌러서 종료하세요.")

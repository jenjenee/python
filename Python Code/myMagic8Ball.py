# MyMagic8Ball

import random

# 답변을 입력해봅시다.
ans1="자! 해보세요!"
ans2="됐네요, 이 사람아"
ans3="뭐라고? 다시 생각해보세요."
ans4="모르니 두려운 것입니다."
ans5="칠푼인가요?? 제 정신이 아니군요!"
ans6="당신이라면 할 수 있어요!"
ans7="해도 그만, 안 해도 그만, 아니겠어요?"
ans8="맞아요, 당신은 올바른 선택을 했어요."
ans9="후회해도 이미 늦었어요."
ans10="하늘은 언제나 당신편!"

print("안녕")

print("MyMagic8Ball에 오신 것을 환영합니다.")
# 사용자의 질문을 입력 받습니다.

question1 = input("당신의 이름은 무엇인가요? \n")
# 사용자의 이름을 입력 받습니다.

question2 = input("조언을 구하고 싶으면 질문을 입력하고 엔터 키를 누르세요.\n")
print("고민 중...\n"*4)
# 질문에 알맞는 답변을 하는 일에 randint() 함수를 활용합니다.

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

print("\n\n", question1, "님 게임을 즐겨주셔서 감사합니다. 마치려면 엔터 키를 누르세요.")

input("\n\n 엔터키를 눌러서 종료하세요.")
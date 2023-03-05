import random
#nums에 1 ~ 45까지 저장
nums = list(range(1,45+1))
#랜덤으로 고르게 설정
lotnum = random.choices(nums)
#1 ~ 45까지의 숫자를 섞기
lotnum = random.shuffle(nums)
#6개만 lotnum에 저장
lotnum = nums[:6]
#보기 좋게 작은 순서대로 정렬
lotnum.sort()

#lotnum 출력
print('''로또 당첨번호 입니다
담첨을 빕니다''', lotnum)



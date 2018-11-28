#A
price = int(input("투입할 금액을 입력하세요 : "))
amount = int(input("몇잔? : "))
change = price-amount*200
if(change<0):
    print("돈을 더 넣어주세요!")
else:
    print("거스름돈 : ",change,"원")

#B
list1 = ["하나","둘","셋"]
list2 = ["양수","한자리수"]
print([(x,y) for x in list1 for y in list2])
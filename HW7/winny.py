def winnie(phrase):
    list1 = phrase.lower().split()    
    print(list1)
    sumChar = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
    tmp = sumChar(list1[0])
    if all(sumChar(i) == tmp for i in list1):
        return 'Парам пам-пам'
    else:
        return 'Пам парам'
    
    # list2 = [sumChar(list1[i]) for i in range(len(list1))]
    # print(list2)
    # tmp = list2[0]
    # for j in range(1, len(list2)):
    #     if tmp != list2[j]:
    #         print(tmp)
    #         print(list2[j])
    #         return 'Пам парам'
    #     else:
    #         return 'Парам пам-пам'

 
print(winnie("пара-ра-рам рам-пам-папам па-ра-па-да"))
 
print(winnie("Пам-пара-рарам рам-пам-папам па-ра-па-да"))
 

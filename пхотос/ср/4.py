sentence = input("Введите предложение на английском: ")
print("Длина предложения: ",len(sentence))
print("Предложение в нижнем регистре:", sentence.lower())
print("Количество глассных в предложении: ", (sentence.count('a')+sentence.count('e')+sentence.count('i')+sentence.count('o')+sentence.count('u')+sentence.count('y')))
print("Красивое предложение: ", sentence.replace("ugly", "beauty"))
if sentence[:3] == "The" and sentence[-3:] == "end":
    print("Предлоожение начинается на The и заканчивается на end")
elif sentence[:3] == "The" and sentence[-3:] != "end":
    print("Предложение начинается на The, но не заканчивается на end")
elif sentence[:3] != "The" and sentence[-3:] == "end":
    print("Предложение заканчивается на end, но не начинается на The")
else:
    print("Предложение не начинается на The и не заканчивается на end")

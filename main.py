# Код написан 13.11.2023
# Автор: Кучук Милан Михайлович
print("\t\tПрограмма Кучук")
print("\t\tЧтение файла")

print("\nОткрываю и закрываю файл")
text_file = open("read_it.txt", "r", encoding='utf-8')
text_file.close()

print("\nЧитаю файл посимвольно")
text_file = open("read_it.txt", "r", encoding='utf-8')
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print("\nЧитаю файл целиком")
text_file = open("read_it.txt", "r", encoding='utf-8')
all_text = text_file.read()
print(all_text)
text_file.close()

print("\nЧитаю одну строку посимвольно")
text_file = open("read_it.txt", "r", encoding='utf-8')
print(text_file.readline(1))
print(text_file.readline(10))
text_file.close()

print("\nЧитаю одну строку целиком")
text_file = open("read_it.txt", "r", encoding='utf-8')
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("\nЧитаю весь файл в список")
text_file = open("read_it.txt", "r", encoding='utf-8')
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print("\nПеребираю файл построчно")
text_file = open("read_it.txt", "r", encoding='utf-8')
for line in text_file:
    print(line)
text_file.close()

print("\nОткрываю и закрываю файл")
text_file = open("write_it.txt", "w", encoding='utf-8')
text_file.write("Строка 1\n")
text_file.write("Это строка 2\n")
text_file.write("Это строка под номером 3\n")
text_file.close()

text_file = open("")


print("\t\tЗаконсервируем 203")

import pickle, shelve

f = open("pickles1.dat", "wb")
var1 = ["mama", "papa", "sestra"]
var2 = ["brat", "girl", "boy"]
var3 = ["drug", "jopa", "lalka"]

pickle.dump(var1, f)
pickle.dump(var2, f)
pickle.dump(var3, f)
f.close()

f = open("pickles1.dat", "rb")

var1 = pickle.load(f)
var2 = pickle.load(f)
var3 = pickle.load(f)

print(var1)
print(var2)
print(var3)
f.close()

print("Помещаем файлы на полку")
s = shelve.open("pickles2", "c")
s["var1"] = ["mama", "papa", "sestra"]
s["var2"] = ["brat", "girl", "boy"]
s["var3"] = ["drug", "jopa", "lalka"]

s.sync()

print("var1 - ", s["var1"])
print("var2 - ", s["var2"])
print("var3 - ", s["var3"])
s.close()

print("\t\tОбход ошибок try/except")

try:
    num = float(input("Введите число\n"))
except:
    print("Похоже это не число")

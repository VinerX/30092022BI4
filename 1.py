Name = input("Введите Имя: ")
SurName = input("Введите Фамилию: ")
Date = int(input("Введите год рождения: "))

print(Name, SurName ,Date, sep="_")
Name, SurName = SurName,Name
Date+=60
print(Name,SurName,Date,sep="_")
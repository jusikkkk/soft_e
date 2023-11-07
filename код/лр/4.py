def personal_info(name, age, company = 'unnamed'):
    print(f"Имя: {name} Возраст: {age} Компания : {company}")

mark = ("Марк", 27)
personal_info(*mark)

alex = ("Алексей", 38, "Google")
personal_info(*alex)
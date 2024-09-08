def send_email(message, recipient, sender = "university.help@gmail.com"):
    f = recipient.find("@")
    e1 = recipient.endswith(".com")
    e2 = recipient.endswith(".ru")
    e3 = recipient.endswith(".net")

    g = sender.find("@")
    w1 = sender.endswith(".com")
    w2 = sender.endswith(".ru")
    w3 = sender.endswith(".net")
    #print(g, w1, w2, w3)
    #print(f, e1, e2, e3)

    if g<0:
        print(f"Ошибка нет @ в {sender}")
    elif f<0:
        print(f"Ошибка нет @ в {recipient}")
    elif w1 == False and w2 == False and w3 == False :
                print(f"Ошибка1 допустимо (.com .ru .net)  {sender}")
    elif e1 == False and e2 == False and e3 == False :
                print(f"Ошибка2 допустимо (.com .ru .net) {recipient}")


    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {recipient} на адрес {sender}.")




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

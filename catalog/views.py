from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Contact


# Create your views here.
def home(request):
    return render(request, "home.html")


def contact(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        print(name)
        print(phone)
        print(message)
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")

    contact = Contact.objects.all()
    if len(contact) != 0:

        data = {"country": contact[0].country,
                "tax_num": contact[0].tax_reg_number,
                "address": contact[0].address,
                "phone": contact[0].phone
                }
    else:
        data = {"country": "не указано",
                "tax_num": "не указано",
                "address": "не указано",
                "phone": "не указано"
                }
    return render(request, "contact.html",context=data)

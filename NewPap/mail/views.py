from django.shortcuts import render, reverse, redirect
from django.views import View
# импортируем класс для создание объекта письма с html
from django.core.mail import EmailMultiAlternatives
from datetime import datetime

# импортируем функцию, которая срендерит наш html в текст
from django.template.loader import render_to_string
from .models import MailModel


class MailView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_mail.html', {})

    def post(self, request, *args, **kwargs):
        mail = MailModel(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            user_name=request.POST['user_name'],
            message=request.POST['message'],
        )
        mail.save()

        # получем наш html
        html_content = render_to_string(
            'mail_created.html',
            {
                'mail': mail,
            }
        )

        # в конструкторе уже знакомые нам параметры, да? Называются правда немного по другому, но суть та же.
        msg = EmailMultiAlternatives(
            subject=f'{mail.user_name} {mail.date.strftime("%Y-%M-%d")}',
            body=mail.message,  # это то же, что и message
            from_email='test.niolmo@yandex.ru',
            to=['niolmo@mail.ru'],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html
        msg.send()  # отсылаем

        return redirect('mail:make')
# создаём функцию обработчик с параметрами под регистрацию сигнала

from TaskMaster.celery import app
from django.core.mail import send_mail


@app.task(name='dead_line_mail_task')
def deadline_mail(email):
    print('Asynchronous task ready!')
    send_mail(
        subject='The limit date line is coming soon!',
        message='We have seen that you has effort a lot of, and for it we send this mail, ' \
                'do not forget that the deadline is neard',
        from_email='task_bot@taskmaster.com',
        recipient_list=[email],
        fail_silently=False
    )
import os
from celery import Celery

# Установите модуль настроек Django по умолчанию
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'visitka.settings')

app = Celery('visitka')

# Используйте строку здесь, чтобы рабочие процессы не сериализовали
# конфигурационный объект дочерним процессам.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загружайте задачи из всех зарегистрированных приложений Django
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

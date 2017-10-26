from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = "用户"

    def ready(self):
        import users.signals   # 触发信号

# ------------------------------------------- 8 -----------------------------
# Создайте пакет с всеми модулями, которые
# вы создали за время занятия. Добавьте в __init__
# пакета имена модулей внутри дандер __all__.
# В модулях создайте дандер __all__ и укажите только те функции,
# которые могут верно работать за пределами модуля.

__all__ = ['numbers', 'text', 'date']  # в init
__all__ = ['guess']  # угадай число
__all__ = ['secrets', 'storage']  # угадай загадку
__all__ = ['valid']  # проверь дату

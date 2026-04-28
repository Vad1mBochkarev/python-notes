try:
    import example
except ImportError:
    raise AssertionError('Модуль `example` не обнаружен.')

EXPECTED_FUNC_NAME = 'say_hello'


def test_say_hello_exists():
    assert hasattr(example, EXPECTED_FUNC_NAME), (
        f'Функция `{EXPECTED_FUNC_NAME}` не обнаружена в модуле `example`')


def test_say_hello_run_without_exceptions():
    try:
        example.say_hello()
    except Exception as error:
        raise AssertionError(
            f'При запуске функции `{EXPECTED_FUNC_NAME}` возникло '
            f'исключение: {type(error).__name__}: {error}`'
        )

from datetime import datetime
import os

def logger(path_logfile):
    os.makedirs(path_logfile, exist_ok=True)

    def _logger(function):

        def write_logfile(*args, **kwargs):
            with open(f'{path_logfile}\\log.log', 'a', encoding='utf-8') as f:
                result = function(*args, **kwargs)
                f.write(f'Дата и время вызова функции - {datetime.now()}\n'
                        f'Имя функции - {function.__name__}\n'
                        f'Аргументы - {args, kwargs}\n'
                        f'Возвращаемое значение - {result}\n\n')
            return result
        return write_logfile
    return _logger


@logger(r'D:\Projects\homeworks-advanced\3.Decorators\logfile')
def minus(a, b):
    return a - b

if __name__ == '__main__':
minus(5,3)
minus(7,3)
minus(8,3)
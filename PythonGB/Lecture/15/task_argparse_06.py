'''
Параметр action для аргумента
И напоследок ещё один интересный параметр уже без квадратных уравнений. Речь пойдёт о параметре action.
'''

import argparse
parser = argparse.ArgumentParser(description='Sample')
parser.add_argument('-x', action='store_const', const=42)
parser.add_argument('-y', action='store_true')
parser.add_argument('-z', action='append')
parser.add_argument('-i', action='append_const', const=int, dest='types')
parser.add_argument('-f', action='append_const', const=float, dest='types')
parser.add_argument('-s', action='append_const', const=str, dest='types')
args = parser.parse_args()
print(args)

"""
Примеры запуска в терминале:
python .\task_argparse_06.py -h
python .\task_argparse_06.py -x -y -z 42 -z 73 -i -f -s
"""

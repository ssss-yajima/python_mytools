'''
argparseを用いたコマンドラインツール
公式ドキュメント：https://docs.python.org/ja/3/library/argparse.html#allow-abbrev
'''

import argparse

def main():
    parser = argparse.ArgumentParser(description='argparseを用いたCLIツール')
    parser.add_argument('integers', type=int, metavar='N', action='store', nargs='+',
                        help='計算対象の整数値を2個以上入力')

    # 必須オプション引数にすると名称指定できるし、順番に影響されない
    parser.add_argument('-m', '--method', choices=['add', 'multiply'], required=True,
                        help='計算方法を指定')
    parser.add_argument('-l', '--logging', action='store_true',
                        help='オプション指定するとログ出力される')

    args = parser.parse_args()

    operand = args.integers
    operator = args.method
    logging = args.logging

    if len(operand)<2 :
        print('引数が足りません。2個以上の整数を入力してください')
        return
    ans = int(operator=="multiply")
    for i,o in enumerate(operand):
        if operator =='add': ans += o
        elif operator == 'multiply': ans *= o
        if logging:
            print('Logging... {}'.format(i))
    print('ans = {}'.format(ans))

if __name__ == "__main__":
    main()

'''
$ python pyToolWithArgparse.py 1 2 3 4 -m add
ans = 10

$ python pyToolWithArgparse.py 1 2 3 4 -m multiply
ans = 24

$ python pyToolWithArgparse.py 1 2 3 4 -m add -l
Logging... 0
Logging... 1
Logging... 2
Logging... 3
ans = 10
'''
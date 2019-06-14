'''
同一ディレクトリに置いた設定ファイルを読み取る。
対象を番号（Key)で指定し、ブラウザで開く。
'''
import subprocess
import os
from sys import argv

def read_bookmarks(display=False): #display=Trueのとき読込ながら整形して表示
    # 設定ファイル読込
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_PATH = os.path.join(CURRENT_DIR, 'bookmarks.txt')

    with open(FILE_PATH,'r') as f:
        bookmarks = {}
        for line in f:
            line = line[:-1]
            # コメント行、空行、要素不足を読み飛ばす
            if line =='' or line[0]=='#': continue
            elif line[0] == '*':
                if display: print(line[1:])
                continue
            else:
                key,title,url = line.split(',')
                bookmarks[key] = (title, url)
                if display: print(f'[{key}] {title:　<10} :{url}') # 全角スペース埋め
    return bookmarks

def main():
    IE_FULLPATH ="C:\\Program Files\\internet explorer\\iexplore.exe" # ブラウザのコマンド                                     

    if len(argv) > 2: # 引数多すぎ
        print('引数が不正です (整数2桁で環境を指定)')
        return
    if len(argv) == 1: #　番号指定なしの場合、一覧表示してコマンド受付
        bookmarks = read_bookmarks(display=True)
        print('\nブラウザで開く対象を指定')
        key = input('>>')
    else:
        bookmarks = read_bookmarks(display=False)
        key = argv[1]
    title,url = bookmarks[key]
    print(f'接続先:{title:　<10} : {url}') #全角スペース埋め
    subprocess.Popen(IE_FULLPATH + ' ' + url)

if __name__ == "__main__":
    main()

'''
# "#"始まりはコメント行（非表示、処理されない）
# "*"始まりは一覧に表示される
# 書式： Key, Title, URL
*表示コメント
01, 接続先1,https://www.xxx.com
02, 接続先2,https://www.yyy.com
# ※この1文を消さないこと。末尾の改行文字を削るので、本文を削らないよう予防策。
'''


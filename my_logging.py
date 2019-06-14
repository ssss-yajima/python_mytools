'''
loggingを用いたログ出力。
https://docs.python.org/ja/3/howto/logging.html
https://docs.python.org/ja/3/library/logging.html
'''
import logging
import os
from logging import getLogger,StreamHandler,Formatter,FileHandler

def get_logger(name="Logger"):

    logger = getLogger(name=name)   # name指定しないとroorのLoggerを取得する
    logger.setLevel(logging.DEBUG)  # 指定レベル以上のメッセージを出力する

    # 出力フォーマット指定
    handler_format = Formatter('%(asctime)s[%(name)s][%(levelname)s]%(message)s')
    # Formatter('%(asctime)s[%(name)s]%(module)s::%(funcName)s:%(lineno)d [%(levelname)s]%(message)s')

    # ファイルに出力
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_PATH = os.path.join(CURRENT_DIR, f'log_{name}.txt')
    file_handler = FileHandler(FILE_PATH, 'a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(handler_format)
    logger.addHandler(file_handler)

    # 標準エラー出力に出力
    stream_handler = StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(handler_format)
    logger.addHandler(stream_handler)

    # その他便利なHandler（他はドキュメント参照）
    # HTTPHandler Get/Postする
    # SMTPHandler メール送信する
    return logger

## Test Code
# if __name__ == "__main__":
#     logger = get_logger(name=__name__)

#     logger.info("Info msessage")
#     logger.debug("Debug message")
#     logger.warning("Warning message")
#     logger.error("Error message")
#     logger.critical("Critial message")
#     logger.exception("Exception message") # スタックトレースも出力される。例外でのみ使うべき。
#     logger.log(logging.INFO, "Log message")

#     # インスタントな使い方 root Loggerが使われる
#     logging.basicConfig(filename='example.log',level=logging.DEBUG)
#     logging.debug("simple debug message")

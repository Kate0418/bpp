# environ.py

import os

class Env:
    def __init__(self):
        pass

    def get(self, key, default=None):
        """
        環境変数を取得します。指定されたキーが存在しない場合は、デフォルト値を返します。
        """
        return os.environ.get(key, default)

    def require(self, key):
        """
        必須の環境変数を取得します。指定されたキーが存在しない場合は例外を発生させます。
        """
        value = os.environ.get(key)
        if value is None:
            raise ValueError(f"Environment variable '{key}' is required but not found.")
        return value

env = Env()

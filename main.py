import os
import glob
import re
import sys

from click import ParamType

# 日本のWindows は "cp932" なので、Unicodeに変換
sys.stdout.reconfigure(encoding='utf-8')

# ディレクトリーを選んでください
while True:
    print("""Which directory?
Example: .""")
    # C:\muzudho\picture\2021-08-pg

    path = input()
    os.chdir(path)

    # フィル名を一覧します
    print(f"""Current directory: {os.getcwd()}

Files
-----""")

    files = glob.glob("./*")

    # とりあえず一覧します
    for file in files:
        # `file` - Example: `.\20210815shogi67.png`
        basename = os.path.basename(file)
        print(basename)

    print("""
Are you sure this is the right directory (y/n)?""")

    answer = input()

    if answer == "y":
        break
    else:
        print("Canceld")

# 正規表現のパターンを入力してください
while True:
    print(r"""
Please enter a regular expression pattern.
Example: ^example-(\d{4})-(\d{2})-(\d{2}).txt$""")

    patternText = input()
    pattern = re.compile(patternText)

    print(r"""
Numbering
---------""")

    # とりあえず一覧します
    for i, file in enumerate(files):
        basename = os.path.basename(file)
        result = pattern.match(basename)
        if result:
            # Matched
            # グループ数
            groupCount = len(result.groups())
            buf = f"({i+1}) {basename}"
            for j in range(0, groupCount):
                buf += f" \\{j+1}=[{result.group(j+1)}]"
            print(buf)
        else:
            # Unmatched
            print(f"( ) {basename}")

    print("""
Was there a match (y/n)?""")

    answer = input()

    if answer == "y":
        break
    else:
        print("Canceld")

# 置換後の正規表現
while True:
    print(r"""
Enter the parameter type.
Example: 1:file-creation-year;2:file-creation-month;3:file-creation-day""")

    mappings = {}

    parameterTypes = input()
    parameterTypeArray = parameterTypes.strip().split(";")
    print(f"parameterTypeArray len={len(parameterTypeArray)}")
    for keyValuePair in parameterTypeArray:
        print(f"keyValuePair={keyValuePair}")
        keyValueArray = keyValuePair.strip().split(":")
        print(f"keyValueArray len={len(keyValueArray)}")
        print(f"keyValueArray[0]={keyValueArray[0]}")
        print(f"keyValueArray[1]={keyValueArray[1]}")
        mappings[keyValueArray[0]] = keyValueArray[1]

    # 確認表示
    print("""
Types
-----""")
    for k, v in mappings.items():
        print(f"{k} --> {v}")

    # シミュレーション
    print("""
Result
------""")
    for i, file in enumerate(files):
        print(f"WIP ({i+1}) {basename}")

    break

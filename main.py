import os
import glob
import re
import sys
from datetime import datetime

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

    typeTable = {}

    parameterTypes = input()
    parameterTypeArray = parameterTypes.strip().split(";")
    # print(f"parameterTypeArray len={len(parameterTypeArray)}")
    for keyValuePair in parameterTypeArray:
        # print(f"keyValuePair={keyValuePair}")
        keyValueArray = keyValuePair.strip().split(":")
        # print(f"keyValueArray len={len(keyValueArray)}")
        # print(f"keyValueArray[0]={keyValueArray[0]}")
        # print(f"keyValueArray[1]={keyValueArray[1]}")
        typeTable[keyValueArray[0]] = keyValueArray[1]

    # 確認表示
    print("""
Types
-----""")
    for k, v in typeTable.items():
        print(f"{k} --> {v}")

    # 間違い探し
    print("""
Invalid
-------""")

    countOfInvalid = 0

    for i, file in enumerate(files):
        basename = os.path.basename(file)
        result = pattern.match(basename)
        if result:
            # Matched
            # グループ数
            groupCount = len(result.groups())
            buf = f"({i+1}) {basename}"
            isUnmatched = False
            for j in range(0, groupCount):

                value = result.group(j+1)
                typeStr = typeTable[f"{j+1}"]

                if typeStr == "file-creation-year":
                    tick = os.path.getctime(file)
                    expected = datetime.fromtimestamp(tick).strftime('%Y')
                    # print(f"file={file} value={value} year={expected}")
                    if value != expected:
                        isUnmatched = True

                elif typeStr == "file-creation-month":
                    tick = os.path.getctime(file)
                    expected = datetime.fromtimestamp(tick).strftime('%m')
                    # print(f"file={file} value={value} month={expected}")
                    if value != expected:
                        isUnmatched = True

                elif typeStr == "file-creation-day":
                    tick = os.path.getctime(file)
                    expected = datetime.fromtimestamp(tick).strftime('%d')
                    # print(f"file={file} value={value} day={expected}")
                    if value != expected:
                        isUnmatched = True

                elif typeStr == "file-modified-year":
                    tick = os.path.getmtime(file)
                    expected = datetime.fromtimestamp(tick).strftime('%Y')
                    if value != expected:
                        isUnmatched = True

                elif typeStr == "file-modified-month":
                    tick = os.path.getmtime(file)
                    expected = datetime.fromtimestamp(tick).strftime('%m')
                    if value != expected:
                        isUnmatched = True

                elif typeStr == "file-modified-day":
                    tick = os.path.getmtime(file)
                    expected = datetime.fromtimestamp(tick).strftime('%d')
                    if value != expected:
                        isUnmatched = True

                elif typeStr == "digit":
                    expected = "#digit#"
                    if not value.isdigit():
                        isUnmatched = True

                else:
                    expected = "#type-failed#"

                buf += f" \\{j+1}=[{value}][{expected}]"

            if isUnmatched:
                print(buf)
                countOfInvalid += 1
        else:
            # Unmatched
            print(f"({i+1}) {basename}")
            countOfInvalid += 1

    break

print(f"Count of invalid = {countOfInvalid}")

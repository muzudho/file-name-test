# file-name-test

ファイル名のフォーマット整合性判定（＾～＾）

# Run

```shell
python main.py

# ファイルに出力するなら
python main.py > foo.log
```

# Hou to use

```plaintext
python main.py
Which directory?
Example: .      
.
Current directory: C:\Users\むずでょ\Documents\GitHub\file-name-test

Files
-----
example-2022-04-11.txt
LICENSE
main.py
README.md

Are you sure this is the right directory (y/n)?
y

Please enter a regular expression pattern.    
Example: ^example-(\d{4})-(\d{2})-(\d{2}).txt$
^example-(\d{4})-(\d{2})-(\d{2}).txt$

Numbering
---------
(1) example-2022-04-11.txt \1=[2022] \2=[04] \3=[11]
( ) LICENSE
( ) main.py
( ) README.md

Was there a match (y/n)?
y

Enter the parameter type.
Example: 1:file-creation-year;2:file-creation-month;3:file-creation-day
1:file-creation-year;2:file-creation-month;3:file-creation-day
parameterTypeArray len=3
keyValuePair=1:file-creation-year
keyValueArray len=2
keyValueArray[0]=1
keyValueArray[1]=file-creation-year
keyValuePair=2:file-creation-month
keyValueArray len=2
keyValueArray[0]=2
keyValueArray[1]=file-creation-month
keyValuePair=3:file-creation-day
keyValueArray len=2
keyValueArray[0]=3
keyValueArray[1]=file-creation-day

Types
-----
1 --> file-creation-year
2 --> file-creation-month
3 --> file-creation-day

Invalid
-------
(2) LICENSE
(3) main.py
(4) README.md
```

# Case study

## Case 1

例えばファイル名を以下のように付けているとする。  

```plaintext
201612__math__05-0853-.png
201701__2dfight__24-0856-a15a2b.png
```

これは以下のようなフォーマットであってほしい。  

```plaintext
{年}{月}__{いろいろ}__{日}-{いろいろ}.png
```

ならば正規表現は以下のようにする。  

```plaintext
^(\d{4})(\d{2})__.+__(\d{2})(?:-?[^.]*).png$
```

型のタイプは以下のように指定する

```plaintext
1:file-creation-year;2:file-creation-month;3:file-creation-day
```

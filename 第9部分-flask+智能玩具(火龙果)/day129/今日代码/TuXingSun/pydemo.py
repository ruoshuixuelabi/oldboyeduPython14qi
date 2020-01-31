from pypinyin import lazy_pinyin,TONE2

a = lazy_pinyin("先帝创业未半而中道崩殂",style=TONE2)
pinyin = "".join(a)

if "ye4we4iba4n" in pinyin: #
    print("oyeah!")
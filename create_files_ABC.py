import os
from collections import defaultdict


def main():
    isWindows = os.name == "nt"
    dir_separator = "\\" if isWindows else "/"

    n = int(input("回数を入力 : "))

    dic: defaultdict[int, set[int]] = defaultdict(set)

    # 400回目まで作成可能
    for i in range(40):
        for j in range(10):
            dic[f"{i*10+1}-{(i+1)*10}"].add(i * 10 + 1 + j)

    a = ""
    for k, v in dic.items():
        if n in v:
            a = str(k)
            break
    if a == "":
        print("その回数は作成できません")
        return

    dir_path = f"ABC{dir_separator}{a}{dir_separator}{n}"
    # D問題まで作成
    files = [f"{v}.py" for v in "ABCD"]

    # テンプレートの読み込み
    try:
        f = open(f".{dir_separator}template{dir_separator}init_template.py", "r")
        init_template = f.read()
        f.close()
    except:
        print("テンプレートが見つかりません")
        return

    # ディレクトリの作成 既に存在する場合はエラーを返す
    try:
        os.makedirs(dir_path)
    except:
        print("そのディレクトリは既に存在します")
        return

    # ファイルを作成してテンプレートを書き込む
    try:
        for val in files:
            f = open(f"{dir_path}{dir_separator}{val}", "x")
            f.write(init_template)
            f.close()
    except:
        print("ファイル作成に失敗しました")
        return


if __name__ == "__main__":
    main()

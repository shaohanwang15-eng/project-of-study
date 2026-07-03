import random
import json
import os

#单词库
word_lib = {
    "animal": ["cat", "dog", "bird", "tiger", "lion", "fish", "bear", "fox", "deer", "sheep",
               "rabbit", "mouse", "horse", "cow", "duck", "goose", "monkey", "panda", "wolf", "zebra"],
    "fruit": ["apple", "banana", "orange", "grape", "pear", "peach", "mango", "lemon", "cherry", "kiwi"],
    "sport": ["run", "swim", "jump", "play", "throw", "catch", "kick", "hit", "ride", "climb"],
    "color": ["red", "blue", "green", "yellow", "black", "white", "pink", "purple", "brown", "gray"]
}

# 把所有单词拉成一个列表
all_words = []
for category in word_lib.values():
    all_words.extend(category)

# 用户数据文件
USER_FILE = "users.json"

#用户注册登录
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=True, indent=2)

def register():
    users = load_users()
    username = input("请输入用户名：")
    if username in users:
        print("用户名已存在！")
        return None
    password = input("请输入密码：")
    users[username] = {"pwd": password, "score": 0}
    save_users(users)
    print("注册成功！")
    return username

def login():
    users = load_users()
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username in users and users[username]["pwd"] == password:
        print("登录成功！")
        return username
    print("用户名或密码错误")
    return None

#打乱单词
def shuffle_word(word):
    chars = list(word)
    random.shuffle(chars)
    return "".join(chars)

#难度选择
def choose_difficulty():
    print("\n=== 难度选择 ===")
    print("1. 简单（显示一半字符）")
    print("2. 中等（显示1/3字符）")
    print("3. 困难（只显示1个字符）")
    while True:
        choice = input("请选择难度（1/2/3）：")
        if choice in ["1", "2", "3"]:
            return int(choice)
        print("输入错误，请重新输入")

#获取提示
def get_hint(word, hint_count):
    hint = ["_"] * len(word)
    positions = random.sample(range(len(word)), hint_count)
    for pos in positions:
        hint[pos] = word[pos]
    return " ".join(hint)

#游戏主逻辑
def play_game(username, difficulty):
    users = load_users()
    target_word = random.choice(all_words)
    length = len(target_word)

    # 难度决定显示几个字符
    if difficulty == 1:
        hint_num = max(1, length // 2)
    elif difficulty == 2:
        hint_num = max(1, length // 3)
    else:
        hint_num = 1

    hint = get_hint(target_word, hint_num)
    print(f"\n【单词长度】{length}")
    print(f"【提示】{hint}")

    chance = 5
    while chance > 0:
        guess = input(f"\n你还有{chance}次机会，请输入猜测：").strip().lower()
        if guess == target_word:
            print("恭喜你，猜对了！")
            users[username]["score"] += 10
            save_users(users)
            return
        else:
            chance -= 1
            print("猜错了！")
    print(f"\n游戏结束！正确答案是：{target_word}")

#主菜单
def main():
    print("=" * 30)
    print("    欢迎来到猜单词游戏")
    print("=" * 30)
    while True:
        print("\n1. 注册")
        print("2. 登录")
        print("3. 退出")
        choice = input("请选择：")
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                diff = choose_difficulty()
                play_game(user, diff)
        elif choice == "3":
            print("谢谢游玩，再见！")
            break
        else:
            print("输入错误")

if __name__ == "__main__":
    main()
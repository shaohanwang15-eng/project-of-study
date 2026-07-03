
import string

# 1. 读取文本文件并预处理（转小写、去标点、分割单词）
def get_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()

        # 统一转小写
        text = text.lower()

        # 去掉所有标点符号
        for punc in string.punctuation:
            text = text.replace(punc, ' ')

        # 分割成单词列表
        words = text.split()
        return words

    except FileNotFoundError:
        print(f"错误：未找到文件 {filename}")
        return []

# 2. 初始化字典：键=单词，值=0
def init_word_dict(words):
    word_dict = {}
    for word in words:
        if word not in word_dict:
            word_dict[word] = 0
    return word_dict

# 3. 统计词频

def count_words(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# 5. 主程序
def main():
    filename = "text.txt"

    # 获取单词列表
    words = get_words(filename)
    if not words:
        return

    print("=" * 25)
    print(f"总单词数量：{len(words)}")
    print("=" * 25)

    result_opt = count_words(words)

    cnt = 0
    for w, c in result_opt.items():
        print(f"{w}: {c}")
        cnt += 1
        if cnt >= 20:
            print("...")
            break

    print("\n 统计完成！")

if __name__ == "__main__":
    main()
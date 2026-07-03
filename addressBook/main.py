import json
import os

CONTACTS_FILE = "contacts.json"

def save(contacts):
    try:
        with open(CONTACTS_FILE, "w",encoding='utf-8') as file:
            json.dump(contacts, file,ensure_ascii=False, indent=4)
    except Exception as e:
        print("数据保存失败")
def load():
    if not os.path.isfile(CONTACTS_FILE):
        return {}
    try:
        with open(CONTACTS_FILE, "r",encoding='utf-8') as file:
            contacts = json.load(file)
            print("加载成功")
            return contacts
    except (json.JSONDecodeError,Exception) as e:
        print("数据加载失败")
        return {}
# 通讯录程序 - 控制台版
def login():
    """登录验证功能，密码正确才能进入通讯录"""
    correct_pwd = "123456"
    for i in range(3):  # 最多输3次密码
        pwd = input("请输入登录密码：")
        if pwd == correct_pwd:
            print("登录成功！\n")
            return True
        else:
            print(f"密码错误！还剩 {2 - i} 次机会\n")
    print("密码错误次数过多，程序退出")
    return False


def insert_contact(contacts):
    """插入/更新联系人：存在则询问修改，不存在则新建"""
    name = input("请输入联系人姓名：").strip()
    if not name:
        print("姓名不能为空！")
        return

    if name in contacts:
        choice = input(f"联系人 {name} 已存在，是否修改号码？(y/n)：")
        if choice.lower() == "y":
            phone = input("请输入新的电话号码：").strip()
            contacts[name] = phone
            print(f"已更新 {name} 的联系方式")
            save(contacts)
        else:
            print("ℹ已取消修改")
    else:
        phone = input("请输入电话号码：").strip()
        contacts[name] = phone
        print(f"已新增联系人 {name}")
        save(contacts)


def search_contact(contacts):
    """查询单个联系人电话"""
    name = input("请输入要查询的联系人姓名：").strip()
    if name in contacts:
        print(f"\n{name}：{contacts[name]}")
    else:
        print(f"未找到联系人 {name}")


def show_all(contacts):
    """显示所有联系人信息"""
    if not contacts:
        print("ℹ通讯录为空，暂无联系人")
        return

    print("\n===== 所有联系人列表 =====")
    for idx, (name, phone) in enumerate(contacts.items(), 1):
        print(f"{idx}. {name}：{phone}")
    print("==========================\n")


def delete_contact(contacts):
    """删除指定联系人"""
    name = input("请输入要删除的联系人姓名：").strip()
    if name in contacts:
        del contacts[name]
        print(f"已删除联系人 {name}")
        save(contacts)
    else:
        print(f"未找到联系人 {name}，无法删除")


def init_30_contacts(contacts):
    """自动添加30条测试联系人"""
    test_data = {
        "张三": "13800138000",
        "李四": "13900139000",
        "王五": "13700137000",
        "赵六": "13600136000",
        "钱七": "13500135000",
        "孙八": "13400134000",
        "周九": "13300133000",
        "吴十": "13200132000",
        "郑十一": "13100131000",
        "王十二": "13000130000",
        "李十三": "15800158000",
        "张十四": "15900159000",
        "刘十五": "15700157000",
        "陈十六": "15600156000",
        "杨十七": "15500155000",
        "黄十八": "15300153000",
        "赵十九": "15200152000",
        "吴二十": "15100151000",
        "林二十一": "15000150000",
        "何二十二": "18800188000",
        "高二十三": "18700187000",
        "罗二十四": "18600186000",
        "郑二十五": "18500185000",
        "梁二十六": "18300183000",
        "谢二十七": "18200182000",
        "宋二十八": "18100181000",
        "唐二十九": "17700177000",
        "韩三十": "17600176000",
        "曹一一": "17800178000",
        "丁二二": "17900179000"
    }
    contacts.update(test_data)
    print("已自动添加30条测试联系人！")
    save(contacts)


def main():
    """主函数：程序入口"""
    contacts = load()

    # 登录验证
    if not login():
        return

    # 主菜单
    while True:
        print("\n===== 通讯录菜单 =====")
        print("1. 插入/修改联系人")
        print("2. 查询联系人")
        print("3. 显示所有联系人")
        print("4. 删除联系人")
        print("5. 增加30条联系人信息")
        print("0. 退出系统")
        print("=====================")

        choice = input("请输入功能编号：").strip()

        if choice == "1":
            insert_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            show_all(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            init_30_contacts(contacts)
        elif choice == "0":
            print("感谢使用，再见！")
            save(contacts)
            break
        else:
            print("输入无效，请重新选择！")


if __name__ == "__main__":
    main()
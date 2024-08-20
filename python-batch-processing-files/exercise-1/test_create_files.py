import os
from create_files import create_example_file  # 假设上面的代码在 main.py 中

def test_create_example_file():
    # 确保每次测试前都清空或删除 `example.txt` 文件
    if os.path.exists('example.txt'):
        os.remove('example.txt')
    
    # 调用要测试的函数
    create_example_file()

    assert os.path.exists('example.txt') == True, "创建 example.txt 失败"

    # 读取文件内容并验证
    with open('example.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()

    # 检查文件内容
    assert content == ['你好!程序员充电站(www.chengxuyuancd.com)\n'], "文件内容不匹配"


def test_create_example_file():
    # 确保每次测试前都清空或删除 `example.txt` 文件
    if os.path.exists('example.txt'):
        os.remove('example.txt')
    
    # 调用要测试的函数
    create_example_file()
    create_example_file()

    assert os.path.exists('example.txt') == True, "创建 example.txt 失败"

    # 读取文件内容并验证
    with open('example.txt', 'r', encoding='utf-8') as file:
        content = file.read()


    # 检查文件内容
    assert content.count("www.chengxuyuancd.com")==2, "文件内容不匹配"


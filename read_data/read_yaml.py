# 1. 导包
import yaml

from config import BASE_DIR


def build_data_func():  # 一. 自定义解析方法
    # 2. 打开文件
    with open( BASE_DIR + '/data/search_data.yml', encoding='utf-8') as f:
        # 3. 调用方法获取数据
        data = yaml.safe_load(f)
        print(data)
        return data

if __name__ == "__main__":
    print(build_data_func())
# -*- coding: UTF-8 -*-
from Bawangcan import Bawangcan

if __name__ == '__main__':
    bawangcan = Bawangcan("phone", "password")
    bawangcan.init_chrome_headless()
    cookies = [{
        'name': 'dper',
        'value': '629c3b997801cfae3b36021d21ba415844a507847a7cd5aa9d5e14c3d72a1046e959ee4e33214a08e88bf9a434f0ffa3fc07abec5c02ef0b4934ca275a40e3f26811ee92144cbbd0f4470d93b7f2601acf5453e8e2334e9a7c6500ee16'
    }, {
        'name': 'll',
        'value': '7fd06e815b796be3df069dec78'
    }]
    bawangcan.login_with_cookie(cookies)
    categories = [
        "1",# 美食
        "2",# 丽人
        "6",# 玩乐
        "3",# 婚嫁
        "4",# 亲子
        "5",# 家装
        "8",# 培训
        "10",# 生活服务
        "99",# 其他
    ]
    locations = ["beijing", "shanghai"]

    using_categories = ["1","2","6","8", "10","99"]
    for category in using_categories:
        bawangcan.sign_for_category(category, "shanghai", True)
    bawangcan.quit()

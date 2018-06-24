# -*- coding: UTF-8 -*-
from Bawangcan import Bawangcan

if __name__ == '__main__':
    bawangcan = Bawangcan("your_username", "your_password")
    # you can login with cookies by bawangcan.login_with_cookie(your_cookies)
    '''
    cookies = [{
        'name': 'dper',
        'value': '47a7cd5aa9d5e14c3d72a1046e959ee4e33214a08e88bf9a434f0ffa3fc07abec5c02ef0b4934ca275a40e3f26811ee92144cbbd0f4470d93b7f2601acf5453e8e2334e9a7c6500ee169994ef'
    }, {
        'name': 'll',
        'value': '15b796be3df069dec7836c3df'
    }]
    bawangcan.login_with_cookie(cookies)
    '''
    bawangcan.login()

    categories = [
        "1",# 美食
        "2",# 丽人
        "3",# 玩乐
        "4",# 婚嫁
        "5",# 亲子
        "6",# 家装
        "7",# 培训
        "8",# 酒旅
        "9" # 生活服务
    ]
    locations = ["beijing", "shanghai"]

    using_categories = ["1", "2", "3", "8", "9"]
    for category in using_categories:
        bawangcan.sign_for_category(category, "shanghai")

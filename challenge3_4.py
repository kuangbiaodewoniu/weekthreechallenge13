# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: challenge3_4.py 
@time: 2018/03/30 
"""

import re
from datetime import datetime

# 使用正则表达式解析日志文件，返回数据列表
def open_parser(filename):
    with open(filename) as logfile:
        # 使用正则表达式解析日志文件
        pattern = (r''
                   r'(\d+.\d+.\d+.\d+)\s-\s-\s'  # IP 地址
                   r'\[(.+)\]\s'  # 时间
                   r'"GET\s(.+)\s\w+/.+"\s'  # 请求路径
                   r'(\d+)\s'  # 状态码
                   r'(\d+)\s'  # 数据大小
                   r'"(.+)"\s'  # 请求头
                   r'"(.+)"'  # 客户端信息
                   )
        parsers = re.findall(pattern, logfile.read())
    return parsers


def main():

    # 使用正则表达式解析日志文件
    ip_result = {}
    url_result = {}
    logs = open_parser('nginx.log')
    for log in logs:
        if '11/Jan/2017' in log[1]:
            if log[0] in ip_result.keys():
                ip_result[log[0]] = ip_result[log[0]] + 1
            else:
                ip_result[log[0]] = 1
        if log[3] == '404':
            if log[2] in url_result.keys():
                url_result[log[2]] = url_result[log[2]] + 1
            else:
                url_result[log[2]] = 1
    try:
        ip_dict = max(ip_result.items(), key=lambda x: x[1])
        url_dict = max(url_result.items(), key=lambda x: x[1])
    except ValueError as e:
        print(e)
        exit(-1)
    return ip_dict, url_dict


if __name__ == '__main__':
    ip_dict, url_dict = main()
    print(ip_dict, url_dict)
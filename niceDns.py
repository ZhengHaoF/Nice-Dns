# coding=utf-8
import os

import dns.resolver
from PyQt5.QtWidgets import QApplication
from ping3 import ping

import Log
import info

Log = Log.Log()


# 获取所有修改的Host
def getModifyHost():
    f = open("C:/WINDOWS/system32/drivers/etc/HOSTS")
    lines = f.readlines()
    dns_list = []
    for line in lines:
        if "#DNS-Nice" in line:
            dns_list.append(line)
    f.close()
    return dns_list


# 清除所有修改的Host
def cleanHost():
    with open('C:/WINDOWS/system32/drivers/etc/HOSTS', 'r') as r:
        lines = r.readlines()
    with open('C:/WINDOWS/system32/drivers/etc/HOSTS', 'w') as w:
        for l in lines:
            if '#DNS-Nice' not in l:
                w.write(l)
    Log.consoleLog("已清除所有修改的Host")


# 添加Host
def addHost(add_ip, add_domain):
    f = open("C:/WINDOWS/system32/drivers/etc/HOSTS", 'a')
    f.write('\n  {ip}    {domain}\t#DNS-Nice'.format(ip=add_ip, domain=add_domain))
    f.close()


# 清除指定域名的Host
def removeHost(rem_domain):
    with open('C:/WINDOWS/system32/drivers/etc/HOSTS', 'r') as r:
        lines = r.readlines()
    with open('C:/WINDOWS/system32/drivers/etc/HOSTS', 'w') as w:
        for l in lines:
            if rem_domain not in l and l != '\n':
                w.write(l)


# 获取最快的IP
def getFastIp(_ip_list):
    _min_time = ""
    _min_ip = ""
    ips = []
    for ip in _ip_list:
        QApplication.processEvents()
        # 简单用法 ping地址即可，超时会返回None 否则返回耗时，单位默认是秒
        second = ""
        try:
            second = ping(ip, timeout=1)
        except:
            Log.consoleLog("请求失败")
        if second:
            t = int(float(second) * 1000)
            Log.consoleLog(ip + " 时间 " + str(t) + "ms")
            ips.append({"ip": ip, "time": t})
        else:
            Log.consoleLog(ip + " 超时")
    if len(ips) > 0:
        _min_time = ips[0]['time']
        _min_ip = ips[0]['ip']
        for ip in ips:
            if _min_time > ip['time']:
                _min_time = ip['time']
                _min_ip = ip['ip']
    return _min_ip


# 获取域名对应的IP
def getDomainIp(_domain):
    _ip_list = []
    for ser in info.server:
        QApplication.processEvents()
        my_resolver = dns.resolver.Resolver()
        try:
            my_resolver.nameservers = [ser]
            my_answers = my_resolver.resolve(_domain, "A")
            if my_answers.rrset is not None:
                for ip in my_answers.rrset:
                    _ip_list.append(str(ip))
        except:
            print("错误")

    _ip_list = list(set(_ip_list))
    return _ip_list


def run():
    for domain in info.domainName:
        Log.consoleLog("开始获取" + domain + "的IP列表")
        ip_list = getDomainIp(domain)
        Log.consoleLog(str(ip_list))
        min_ip = getFastIp(ip_list)
        if min_ip != "":
            Log.consoleLog(domain + " 最快IP：" + min_ip)
            removeHost(domain)
            addHost(min_ip, domain)

    if os.system("ipconfig /flushdns") == 0:
        Log.consoleLog("筛选Dns缓存成功")
    Log.consoleLog("IP筛选完成")

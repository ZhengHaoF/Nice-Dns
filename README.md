# DNS-Nice

解决国内GitHub慢的问题，目前只适配了Windows

## 原理

通常，一个拥有CND加速的网站在不同地区会对应多个不同的IP。

例如GitHub 的 CDN 域名容易遭到 DNS 污染，导致无法连接使用 GitHub 的CND服务器，才使得国内访问速度很慢。

不同的地区，不同的DNS服务商会对同一个域名返回不同的IP地址，我们对这些IP地址测速，找出当前访问最快的一个，并把它写入到Host文件中。这样在一定程度上可以加速GitHub等网站的访问速度。

## 其他

不只是对GitHub，理论上只要是使用了CDN加速的网站都可以使此应用加速访问。

## 默认使用的Dns

```
"8.8.8.8",  # 谷歌
"114.114.114.114",  # 114
"1.1.1.1",  # Cloudflare
"119.29.29.29",  # 腾讯
"182.254.116.116",  # 腾讯
"223.5.5.5",  # 阿里
"223.6.6.6",  # 阿里
"180.76.76.76",  # 百度
"9.9.9.9",  # Quad9
"149.112.112.112",  # PCH
"208.67.222.222",  # OpenDNS
"101.101.101.101",  # Quad 101
```

## 安装依赖

```shell
pip install -r requirements.txt
```

## 运行

```shell
python main.py
```

## 打包

``` shell
pyinstaller -F .\main.py  --hidden-import .\niceDns.py --hidden-import .\Log.py --hidden-import .\Dialog.py --hidden-import .\ui.py -p .\venv\Lib\site-packages\  --noconsole
```

或者直接使用

```shell
pyinstaller .\main.spec
```

打包完成后，还需要吧`info.json`复制到打包后的目录中
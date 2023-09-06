# DNS-Nice
解决国内GitHub慢的问题

## 原理
  通常，一个拥有CND加速的网站在不同地区会对应多个不同的IP。

  例如GitHub 的 CDN 域名容易遭到 DNS 污染，导致无法连接使用 GitHub 的CND服务器，才使得国内访问速度很慢。
  
  不同的地区，不同的DNS服务商会对同一个域名返回不同的IP地址，我们对这些IP地址测速，找出当前访问最快的一个，并把它写入到Host文件中。这样在一定程度上可以加速GitHub等网站的访问速度。
  
## 其他
 不只是对GitHub，理论上只要是使用了CDN加速的网站都可以使此应用加速访问。
 
## 打包
``` shell
pyinstaller -F .\main.py --hidden-import .\niceDns.py --hidden-import .\tools.py --hidden-import .\ui.py -p .\venv\Lib\site-packages\  --noconsole
```
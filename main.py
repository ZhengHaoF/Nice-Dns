import uiStart
import niceDns

if __name__ == '__main__':
    server = [
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
    ]
    domainName = [
        "github.com",
        "api.github.com",
        "github.githubassets.com",
        "favicons.githubusercontent.com",
        "raw.githubusercontent.com"
    ]
    niceDns.server = server
    niceDns.domainName = domainName
    U = uiStart.MyWindow(server, domainName)

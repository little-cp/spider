import requests
import json


def get_one_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3143.400 QQBrowser/9.6.11451.400'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    lis = json.loads(html)['data']['list']
    for li in lis:
        item = {
            'symbol': li['symbol'],  # 股票代码
            'name': li['name'],  # 股票名称
            'current': li['current'],  # 当前价
            'change': li['chg'],  # 涨跌额
            'percent': li['percent'],  # 涨跌幅
            'TTM': li['pe_ttm'],  # 市盈率
            'market_capital': li['market_capital']  # 市值
        }
        yield item


def main():
    with open('xueqiu.csv', 'w', encoding='utf-8') as fp:
        for i in range(1, 11):
            url = 'https://xueqiu.com/service/v5/stock/screener/quote/list?page=%s&size=10&order=desc&orderby=percent&order_by=percent&market=US&type=us' % (
                i)
            html = get_one_page(url)
            for item in parse_one_page(html):
                fp.write(json.dumps(item, ensure_ascii=False) + '\n')
                print(item)


main()

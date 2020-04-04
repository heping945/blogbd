from datetime import date

class IpRecord:
    def __init__(self, ipdb):
        self.ipdb = ipdb

    # 集合操作，键为当天日期，值为ip地址
    def set(self, ip, prefix='IP::'):
        key = f'{prefix}{str(date.today())}'
        self.ipdb.sadd(key, ip)

    # 获得当天ip
    def get(self,prefix='IP::'):
        key = f'{prefix}{str(date.today())}'
        return self.ipdb.smembers(key)
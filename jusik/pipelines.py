# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class JusikPipeline:
    def __init__(self):
        self.setupDBConnect()
        self.createTable()

    def process_item(self, item, spider):
        print(item)
        self.storeInDb(item)
        return item
    def storeInDb(self, item):
            # 각 아이템을 Table에 저장
            code = item.get('code','').strip()
            price = item.get('price','').strip()
            total = item.get('total','').strip()
            high = item.get('high','').strip()
            low = item.get('low','').strip()

            sql = "INSERT INTO snmsung(created_at,code,price,total,high,low) VALUES(now(),%s,%s,%s,%s,%s)"
            self.cur.execute(sql,(code,price,total,high,low))
            self.conn.commit()

    def setupDBConnect(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='toor',db='mydb',charset='utf8')
        self.cur = self.conn.cursor()
        print('DB Connect')

    def createTable(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS snmsung(
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            code VARCHAR(100),
            price VARCHAR(20),
            total VARCHAR(50),
            high VARCHAR(50),
            low VARCHAR(50)
        )""")
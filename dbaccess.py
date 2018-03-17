import sqlite3


class Database:
    
    def __init__(self, name):      
        self.name=name
        self.conn=None
        self.cursor=None


    def open(self):
        self.conn = sqlite3.connect(self.name)
        self.cursor = self.conn.cursor()

    
    def close(self):        
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
            self.conn=None
            self.cursor=None
            

    def exec(self,formula,typ,*args):
        if self.conn==None:
            self.open()
        self.q= formula.format(*args)
        try:
            self.cursor.execute(self.q)
            if typ=='output':
                rows = self.cursor.fetchall()
            return rows

        except Exception as ex: 
            return ex

        finally:
            self.close()


"""
form="select {0},{1} from {2} LIMIT {3};"
f1='id'
f2='nm'
tab='cities'
lim=20
dc='data.db'
typ='output'
dd= Database(dc)
print(dd.exec(form,typ,f1,f2,tab,lim))
"""


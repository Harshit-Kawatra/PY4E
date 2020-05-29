import sqlite3
import urllib.request,urllib.error,urllib.parse
import ssl

conn=sqlite3.connect('org.sqlite')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS COUNTS')
cur.execute('CREATE TABLE COUNTS(org TEXT, count INTEGER)')

fname=input('Enter file name: ')
if len(fname)<1:fname='mbox.txt'
fh=open(fname)
for line in fh:
    if not line.startswith('From: '):continue
    word=line.split()
    a=word[1].split('@')
    org=a[1]
    cur.execute('SELECT count FROM COUNTS WHERE org=?',(org,))
    row=cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO COUNTS(org,count) VALUES(?,1)',(org,))
    else:
        cur.execute('UPDATE COUNTS SET count=count+1 WHERE org=?',(org,))
conn.commit()
sqlstr='SELECT org,count FROM COUNTS ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
cur.close()

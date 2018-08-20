'''count emails per org via sqlite'''
import sqlite3

conn = sqlite3.connect('email_by_org.sqlite')
cur = conn.cursor()

#die
cur.execute('DROP TABLE IF EXISTS Counts')

#new
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fn = 'mbox.txt'
fh = open(fn)

for fl in fh:
    if fl.startswith('From: '):
        fromline = fl.split()
        et = fromline[1].find('@')+1
        ins = fromline[1][et::]
        cur.execute('SELECT count FROM Counts WHERE org = ? LIMIT 1', (ins, ))
        res = cur.fetchone()
        if res is None:
            cur.execute('''
            INSERT INTO Counts (org, count)
            VALUES (?, 1)
            ''', (ins, ))
        else:
            cur.execute('''
            UPDATE Counts 
            SET count = count + 1
            WHERE org = ?
            ''', (ins, ))
        conn.commit()
    else:
        continue

cntsql = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1'

for top in cur.execute(cntsql):
    print(str(top[0]), str(top[1]))

cur.close()

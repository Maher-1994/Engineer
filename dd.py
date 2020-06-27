import pymysql


class database:
    def conn(self):
        con = pymysql.connect ('localhost', 'root', '', 'my')
        return con

    def check(self):
        c1 = self.conn ()
        c = c1.cursor ()
        c.execute ('select * from Data')
        l = []
        l1 = []
        a = c.fetchall ()
        for i in range (len (a)):
            l.append (a[i][2])
            l1.append (a[i][3])
        return l, l1         # return all usernames in (l) and all passwords in (l1)

    def view(self):
        co = self.conn ()
        c = co.cursor ()
        c.execute ("select * from Data")
        v = c.fetchall ()
        return v

    def add_degree(self, id, m1, m2, m3):
        con = self.conn ()
        c = con.cursor ()
        av = (m1 + m2 + m3) / 3
        c.execute (f'insert into student values("{id}","{m1}","{m2}","{m3}","{av}")')
        con.commit ()
        print ("degree inserted")

    def search(self, id):
        con = self.conn ()
        c = con.cursor ()

        c.execute (f'select * from student where id="{id}"')
        a=c.fetchall()
        return a

    def degree_update(self, id, m1, m2, m3):
        print('Degrees Updating'
              '---------------------')
        con = self.conn ()
        c = con.cursor ()
        av = (m1 + m2 + m3) / 3
        c.execute (f'update student set mark1="{m1}" , mark2="{m2}" , mark3="{m3}", average="{av}" where id ="{id}"')
        con.commit ()
        print('Degrees Updated')
    def get_student(self):
        co = self.conn ()
        c = co.cursor ()
        c.execute ("select * from Data where type='student'")
        v = c.fetchall ()
        return v
    def get_pro(self):
        co = self.conn ()
        c = co.cursor ()
        c.execute ("select * from Data where type='professor'")
        v = c.fetchall ()
        return v
    def twice(self):
        con=self.conn()
        c=con.cursor()
        c.execute('select Data.id,fullname,department,mark1,mark2,mark3,average from Data,student where Data.id=student.id')
        a=c.fetchall()
        return a
    def new_user(self,f,u,p,t,d):
        m = self.conn ()
        c = m.cursor ()
        sql = f"insert into Data(fullname,username,password,type,department) values('{f}','{u}','{p}','{t}','{d}')"
        c.execute (sql)
        m.commit ()
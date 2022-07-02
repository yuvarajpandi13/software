mport sqlite3
con=sqlite3.connect('user.db')
con.execute("create table users(NAME,ACTOR,ACTRESS,DIRECTOR,YEAR);")
def insertData(name,actor,actress,director,year):
    qry=f'insert into users (NAME,ACTOR,ACTRESS,DIRECTOR,YEAR) values ("{name}","{actor}","{actress}","{director}","{year}");'
    con.execute(qry)
    con.commit()
    print("add")

def select(actor):
    qry='select * from users where actor="'+actor+'";'
    result=con.execute(qry)
    print("MovieName \t Actor \t Actress \t Director \t Year")
    for row in result:
        print("|\t    ".join(row))
def display():
    qry='select * from users;'
    result=con.execute(qry)
    print("Movie Name \t Actor \t Actress \t Director \t Year")
    for row in result:
        print("|\t    ".join(row))

print("1.Insert Data \n2.search Actor \n3.display all")
ch="y"
while(ch.lower()=='y'):
    c=int(input())
    if(c==1):
        print("add record")
        name=input("Enter the name of the movie:")
        actor=input("Enter the name of the actor:")
        actress=input("Enter the name of the actress")
        director=input("Enter the name of the Director")
        year=input("Enter the year of Movie")
        insertData(name,actor,actress,director,year)
    elif (c==2):
        print("select")
        select(input("ACTOR NAME:"))
    elif(c==3):
        display()
    else:
        print("Invalied option:" + c)
    ch = input("Do you want to continue[Y/n]: ")
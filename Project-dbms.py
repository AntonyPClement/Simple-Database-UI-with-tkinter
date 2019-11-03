from tkinter import *
import sqlite3 

root=Tk()
root.title('dbms')
root.geometry("500x250")
uidx=469

def login():
    conn=sqlite3.connect('DBMSproj.db')

    c=conn.cursor()

    o=se.get()
    
    c.execute("select Name from User where UserID =:o",{'o':se.get()})
    rec=c.fetchall()
    print(rec)


    lab=Label(root, text='Welcome back '+rec[0][0]+'!')
    lab.grid(row=12,column=0,columnspan=3,padx=100)

    c.execute('select Registration_Code,Name from Restaurant')
    options=c.fetchall()
    #options=['a','b']
    global click
    click=StringVar()
    rest=OptionMenu(root, click, *options)
    rest.grid(row=7,column=1,padx=30)
    
    rl=Label(root, text='Choose your restaurant:').grid(row=7,column=0)

    upd=Button(root,text='Update details',command=edit_u).grid(row=5,column=0)

    deb=Button(root,text='Delete Account',command=delete).grid(row=5,column=1)

    sh=Button(root,text="Show records",command=show_u).grid(row=5,column=2)

    srb=Button(root, text="Show Restaurant data",command=show_r).grid(row=8,column=1)

    conn.commit()

    conn.close()

def show_re():
    Label(root,text=click).grid(row=15,column=0)
    
def show_u():
    su=Tk()
    su.title('Records')
    su.geometry('300x300')

    conn=sqlite3.connect('DBMSproj.db')

    c=conn.cursor()

    o=se.get()
    
    c.execute("select * from User where UserID =:o",{'o':se.get()})
    rec=c.fetchall()
    print(rec)

    pr=''

    """for r in rec:
        for i in r:
            pr+=str(i)+'\n'
        pr+='\n'"""
    pr+='USER ID: '+str(rec[0][0])+'\n'
    pr+='USER NAME: '+str(rec[0][2])+'\n'
    pr+='PASSWORD: '+str(rec[0][1])+'\n'
    pr+='LOCATION: '+str(rec[0][3])+'\n'
    pr+='EMAIL ID: '+str(rec[0][4])+'\n'
    pr+='PHONE NO: '+str(rec[0][5])+'\n'
    pr+='EXPERIENCE: '+str(rec[0][6])+'\n'
    pr+='NO. OF LOCATIONS VISITED: '+str(rec[0][7])+'\n'

    lab=Label(su, text=pr, fg='blue',bg='white')
    lab.grid(row=0,column=1, padx=50,pady=50)

    conn.commit()

    conn.close()

def enter_u():
    conn=sqlite3.connect('DBMSproj.db')

    c=conn.cursor()

    c.execute('select UserID from User order by UserID DESC limit 1')
    lr=c.fetchall()
    uidx=int(lr[0][0])+1

    c.execute("insert into User values (:ou,:fn,:ln,:addr,:c,:s,:z,:p)",
            {
                'ou':uidx,
                'fn':passwordu.get(),
                'ln':nameu.get(),
                'addr':locu.get(),
                'c':eidu.get(),
                's':phu.get(),
                'z':exu.get(),
                'p':nlu.get()})
    #c.execute("insert into User_Experience(User_ID) values (:w)",{'w':uidx})

    se.delete(0,END)

    se.insert(0,uidx)

    conn.commit()

    conn.close()

    un.destroy()


def new_u():
    global un
    un=Tk()
    un.title("new records")
    un.geometry('400x200')

    conn=sqlite3.connect('DBMSproj.db')

    c=conn.cursor()

    global nameu
    global passwordu
    global locu
    global eidu
    global phu
    global exu
    global nlu
    
    nameu=Entry(un,width=30)
    nameu.grid(row=0,column=1,padx=20)
    passwordu=Entry(un,width=30)
    passwordu.grid(row=1,column=1,padx=20)
    locu=Entry(un,width=30)
    locu.grid(row=2,column=1,padx=20)
    eidu=Entry(un,width=30)
    eidu.grid(row=3,column=1,padx=20)
    phu=Entry(un,width=30)
    phu.grid(row=4,column=1,padx=20)
    exu=Entry(un,width=30)
    exu.grid(row=5,column=1,padx=20)
    nlu=Entry(un,width=30)
    nlu.grid(row=6,column=1,padx=20)

    fnl=Label(un, text='User Name').grid(row=0,column=0)
    lnl=Label(un, text='password').grid(row=1,column=0)
    addrl=Label(un, text='location').grid(row=2,column=0)
    cl=Label(un, text='email id').grid(row=3,column=0)
    sl=Label(un, text='phone no').grid(row=4,column=0)
    zl=Label(un, text='experience').grid(row=5,column=0)
    zql=Label(un, text='no of locations visited').grid(row=6,column=0)

    ub=Button(un, text="Save changes", command=enter_u)
    ub.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=136)

    conn.commit()

    conn.close()

def edit_u():
    global ud
    ud=Tk()
    ud.title("Update records")
    ud.geometry('400x200')

    conn=sqlite3.connect('DBMSproj.db')

    c=conn.cursor()

    recid=se.get()
    c.execute("select * from User where UserID = :q",{'q':recid})
    recl=c.fetchall()

    global namet
    global passwordt
    global loct
    global eidt
    global pht
    global ext
    global nlt
    
    namet=Entry(ud,width=30)
    namet.grid(row=0,column=1,padx=20)
    passwordt=Entry(ud,width=30)
    passwordt.grid(row=1,column=1,padx=20)
    loct=Entry(ud,width=30)
    loct.grid(row=2,column=1,padx=20)
    eidt=Entry(ud,width=30)
    eidt.grid(row=3,column=1,padx=20)
    pht=Entry(ud,width=30)
    pht.grid(row=4,column=1,padx=20)
    ext=Entry(ud,width=30)
    ext.grid(row=5,column=1,padx=20)
    nlt=Entry(ud,width=30)
    nlt.grid(row=6,column=1,padx=20)

    fnl=Label(ud, text='User Name').grid(row=0,column=0)
    lnl=Label(ud, text='password').grid(row=1,column=0)
    addrl=Label(ud, text='location').grid(row=2,column=0)
    cl=Label(ud, text='email id').grid(row=3,column=0)
    sl=Label(ud, text='phone no').grid(row=4,column=0)
    zl=Label(ud, text='experience').grid(row=5,column=0)
    zql=Label(ud, text='no of locations visited').grid(row=6,column=0)


    for r in recl:
        namet.insert(0,r[2])
        passwordt.insert(0,r[1])
        loct.insert(0,r[3])
        eidt.insert(0,r[4])
        pht.insert(0,r[5])
        ext.insert(0,r[6])
        nlt.insert(0,r[7])

    ub=Button(ud, text="Save changes", command=update_u)
    ub.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=136)

    conn.commit()

    conn.close()

def update_u():
    conn=sqlite3.connect('DBMSproj.db')

    c=conn.cursor()

    rec_id=se.get()
    
    c.execute("""update User set
    Name=:fn,
    Password=:ln,
    Location=:addr,
    EmailID=:c,
    PhoneNo=:s,
    Experience=:z,
    No_of_locations_visited=:p
    where UserID=:uy""",
            {   'fn':namet.get(),
                'ln':passwordt.get(),
                'addr':loct.get(),
                'c':eidt.get(),
                's':pht.get(),
                'z':ext.get(),
                'p':nlt.get(),
                'uy':rec_id   }   )  

    conn.commit()

    conn.close()

    ud.destroy()

def show_r():

    ur=Tk()
    ur.title('restaurant')

    c=str(click.get())
    choice=int(c[1])

    conn=sqlite3.connect('DBMSproj.db')

    c=conn.cursor()

    c.execute("select * from Restaurant where Registration_Code=:t",{'t':choice})
    rec=c.fetchall()
    print(rec)

    pr=''

    """for r in rec:
        for i in r:
            pr+=str(i)+'\n'
        pr+='\n'"""
    pr+='REGISTRATION CODE: '+str(rec[0][0])+'\n'
    pr+='NAME: '+rec[0][1]+'\n'
    pr+='EMAIL ID: '+rec[0][2]+'\n'
    pr+='PHONE NO.: '+str(rec[0][3])+'\n'
    pr+='MANAGER: '+rec[0][4]+'\n'
    pr+='CUISINE: '+rec[0][5]+'\n'
    pr+='PAYMENT: '+rec[0][6]+'\n'

    lab=Label(ur, text=pr, fg='red',bg='white')
    lab.grid(row=12,column=0,columnspan=2)

    c.execute("select Health_Score from Health_Certification where Registration_Code=:t",{'t':choice})
    rec=c.fetchall()
    print(rec)

    pr=''

    """for r in rec:
        for i in r:
            pr+=str(i)+'\n'
        pr+='\n'"""
    pr+='CERTIFIED HEALTH SCORE (OUT OF 100): '+str(rec[0][0])+'\n'

    lab1=Label(ur, text=pr,fg='white',bg='green').grid(row=13,column=0,columnspan=2,padx=150)

    c.execute("select delivers,fee,radius from Delivery join Restaurant_Delivery on Restaurant_Delivery.Delivery_ID=Delivery.Delivery_ID where Registration_Code=:t",{'t':choice})
    rec=c.fetchall()
    print(rec)

    pr=''

    """for r in rec:
        for i in r:
            pr+=str(i)+'\n'
        pr+='\n'"""
    pr+='DELIVERY SERVICE AVAILABLE?: '+rec[0][0]+'\n'
    pr+='DELIVERY FEE: '+str(rec[0][1])+'\n'
    pr+='DELIVERY RADIUS: '+str(rec[0][2])+'\n'

    lab2=Label(ur, text=pr,fg='white',bg='violet').grid(row=14,column=0,columnspan=2,padx=150)

    c.execute("select Starters,Mains,Desserts,Beverages,Veg_NonVeg from Menu join Restaurant on Restaurant.Registration_Code=Menu.Reg_Code where Registration_Code=:t",{'t':choice})
    rec=c.fetchall()
    print(rec)

    pr=''

    """for r in rec:
        for i in r:
            pr+=str(i)+'\n'
        pr+='\n'"""
    pr+='STARTERS: '+rec[0][0]+'\n'
    pr+='MAINS: '+rec[0][1]+'\n'
    pr+='DESSERTS: '+rec[0][2]+'\n'
    pr+='BEVERAGES: '+rec[0][3]+'\n'
    pr+='VEG / NONVEG: '+rec[0][4]+'\n'

    lab3=Label(ur, text=pr,fg='white',bg='black').grid(row=15,column=0,columnspan=2,padx=150)

    c.execute("""select UserID,User_Rating,User_Review
                from User_Experience join Restaurant_User_Experience
                on User_Experience.Sno=Restaurant_User_Experience.SNo
                where Registration_Code=:r""",
              {'r':choice})
    recc=c.fetchall()
    print(recc)
    pr=''
    for r in recc:
        pr+='USER ID: '+str(r[0])+' Rating: '+str(r[1])+'\nReview: '+r[2]+'\n\n'
    lab4=Label(ur, text=pr,fg='blue',bg='white').grid(row=16,column=0,columnspan=2,padx=150)

    rab=Button(ur, text="Rate",command=rate).grid(row=17,column=1)

    conn.commit()

    conn.close()

def delete():
    conn=sqlite3.connect('DBMSproj.db')

    c=conn.cursor()

    c.execute("delete from User where UserID=:x",{'x':se.get()})

    c.execute("delete from User_Experience where UserID=:x",{'x':se.get()})

    conn.commit()

    conn.close()

def rate():
    global rt
    rt=Tk()
    rt.title('Rating')

    conn=sqlite3.connect('DBMSproj.db')
    c=conn.cursor()

    cl=click.get()
    print(cl)
    global rid
    rid=int(cl[1])
    uid=se.get()

    c.execute("""select User_Rating,User_Review
                from User_Experience join Restaurant_User_Experience
                on User_Experience.Sno=Restaurant_User_Experience.SNo
                where UserID=:w and Registration_Code=:r""",
              {'w':uid,'r':rid})
    recc=c.fetchall()
    print(recc)

    global rating
    global review

    rating=Entry(rt, width=30)
    rating.grid(row=0,column=1)
    review=Entry(rt, width=30)
    review.grid(row=1,column=1)

    la1=Label(rt,text='Rating').grid(row=0,column=0)
    la2=Label(rt,text='Review').grid(row=1,column=0)

    for r in recc:
        rating.insert(0,r[0])
        review.insert(0,r[1])

    rv=Button(rt,text='submit',command=submit).grid(row=2,column=1)

    conn.commit()
    conn.close()

def submit():
    conn=sqlite3.connect('DBMSproj.db')
    c=conn.cursor()

    c.execute('select Sno from User_Experience order by Sno DESC limit 1')
    lo=c.fetchall()
    so=int(lo[0][0])+1
    
    c.execute("insert into User_Experience values(:s,:u,:ra,:re)",
              {'s':so,'u':se.get(),'ra':rating.get(),'re':review.get()})
    c.execute("insert into Restaurant_User_Experience values(:r,:s)",
              {'r':rid,'s':so})
    rt.destroy()

    conn.commit()
    conn.close()

    
#conn=sqlite3(' .db')
#c=conn.cursor()
se=Entry(root,width=30)
se.grid(row=0,column=1,padx=20)
sl=Label(root,text="Enter User id:").grid(row=0,column=0)
sb=Button(root, text='login',command=login)
sb.grid(row=1,column=1)
sb1=Button(root, text='New user',command=new_u)
sb1.grid(row=1,column=0)

"""#c.execute('select restaurantname from restaurant')
#options=c.fetchall()
click=StringVar()
options=['a','b']
rest=OptionMenu(root, click, *options)
rest.grid(row=5,column=1,padx=30)
rl=Label(root, text='Choose your restaurant:').grid(row=5,column=0)
"""

root.mainloop()


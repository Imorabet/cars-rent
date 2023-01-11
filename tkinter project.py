from tkinter import ttk
from tkinter import *
from tkinter import messagebox
huh=Tk()
huh.title('Login page')
huh.configure(bg='white')
huh.resizable(False,False)
huh.geometry('925x500+300+200')
class ListeLocations:
    def __init__(self,lloc=[]):
        self.__llocation=lloc
    @property
    def llocation(self):
        return self.__llocation
    @llocation.setter
    def llocation(self,i):
        self.__llocation=i
    #methods
    def __str__(self):
        return f"listes locations:{self.llocation}"
    def afficherlistelocation(self):
        for i in self.llocation:
            print(i)
    def afficherlistelocationCitadine(self):
        for i in self.llocation:
            if hasattr(i.voiture,i.voiture.gamme)==True:
                print(i)
    def afficherlistelocationVip(self):
        for i in self.llocation:
            if hasattr(i.voiture,i.voiture.type)==True:
                print(i)
    def afficherlocationMarque(self,marque):
        for i in self.llocation:
            if i.voiture.mar==marque:
                print(i)
    def afficherlocationClient(self,cin):
        for i in self.llocation:
            if i.client.cin==cin:
                print(i)
    def ajouterlocation(self,location):
        self.llocation.append(location)
    def supprimerlocation(self,location):
        for i in self.llocation:
            if i==location:
                del i
                break
        else:
            print('cette location n\'existe pas')
    def filtrerlocationDate(self,date):
        for i in self.llocation:
            if i.datel==date:
                print(i)
class ListeVoitures:
    def __init__(self,lvoi=[]):
        self.__lvoiture=lvoi
    @property
    def lvoiture(self):
        return self.__lvoiture
    @lvoiture.setter
    def lvoiture(self,i):
        self.__lvoiture=i
    #methods
    def __str__(self):
        return f"listes voitures:{self.lvoiture}"
class ListeClient:
    def __init__(self,lcli=[]):
        self.__lclient=lcli
    @property
    def lclient(self):
        return self.__lclient
    @lclient.setter
    def lclient(self,i):
        self.__lclient=i
    #methods
    def __str__(self):
        return f"listes voitures:{self.lclient}"
    def ajouterC(self):
        return

class Voiture:
    def __init__(self,imma=0,marque='',carburant='',modele='',puissance_fis=''):
        self._imma=imma
        self._mar=marque
        self._car=carburant
        self._mod=modele
        self._pui_fiscale=puissance_fis
    #immatriculation
    @property
    def imma(self):
        return self._imma
    @imma.setter
    def imma(self,f):
        self._imma=f
    #marque
    @property
    def mar(self):
        return self._mar
    @mar.setter
    def mar(self,f):
        self._mar=f
    #carburant
    @property
    def car(self):
        return self._car
    @car.setter
    def car(self,f):
        self._car=f
    #modele
    @property
    def mod(self):
        return self._mod
    @mod.setter
    def mod(self,f):
        self._mod=f
    #puissance fiscale
    @property
    def puifiscale(self):
        return self._pui_fiscale
    @puifiscale.setter
    def puifiscale(self,f):
        self._pui_fiscale=f
    #methods
    def __str__(self):
        return f"immatriculation:{self.imma} marque:{self.mar} carburant:{self.car} modele:{self.mod} puissance fiscale{self.puifiscale}"
    def ajouterV(self,v):
        v==Voiture()
    def supprimerV(self,imma):
            if self.imma==imma:
                del i
            else:
                print('shit aint here')
    def modifierV(self,v):
        v==Voiture()        
class VoitureVip(Voiture):
    def __init__(self,type='SUV',imma=0,marque='',carburant='',modele='',puissance_fis=''):
        self.__type=type
        super().__init__(imma,marque,carburant,modele,puissance_fis)
    #type
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self,f):
        if f!='4*4' and f!='minibus' and f!='limousine' and f!='SUV':
            print('Erreur')
        else:
            self.__type=f
    #methods
    def __str__(self):
        return f"{super().__str__()} type:{self.type}"
class VoitureCitadinne(Voiture):
    def __init__(self,gamme='A',imma=0,marque='',carburant='',modele='',puissance_fis=''):
        self.__gamme=gamme
        super().__init__(imma,marque,carburant,modele,puissance_fis)
    #gamme
    @property
    def gamme(self):
        return self.__gamme
    @gamme.setter
    def gamme(self,f):
        if f!='A' and f!='B' and f!='C':
            print('Erreur')
        else:
            self.__gamme=f
    #methods
    def __str__(self):
        return f"{super().__str__()} gamme:{self.gamme}"
class Personne:
    def __init__(self,cin=0,nom='n1',prenom='p1'):
        self._cin=cin
        self._nom=nom
        self._prenom=prenom
    #CIN
    @property
    def cin(self):
        return self._cin
    @cin.setter
    def cin(self,i):
        self._cin=i
    #nom
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self,i):
        self._nom=i
    #prenom
    @property
    def prenom(self):
        return self._prenom
    @prenom.setter
    def prenom(self,i):
        self._prenom=i
    #methods
    def __str__(self):
        return f"CIN:{self.cin} Nom:{self.nom} Prenom:{self.prenom}"
class Personne:
    def __init__(self,cin='L5474',nom='n1',prenom='p1'):
        self._cin=cin
        self._nom=nom
        self._prenom=prenom
    #CIN
    @property
    def cin(self):
        return self._cin
    @cin.setter
    def cin(self,i):
        self._cin=i
    #nom
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self,i):
        self._nom=i
    #prenom
    @property
    def prenom(self):
        return self._prenom
    @prenom.setter
    def prenom(self,i):
        self._prenom=i
    #methods
    def __str__(self):
        return f"CIN:{self.cin} Nom:{self.nom} Prenom:{self.prenom}"
class Utilisateur(Personne):
    def __init__(self,login='',password='',email='',cin='L6536',nom='n1',prenom='p1'):
        self.__login=login
        self.__password=password
        self.__email=email
        super().__init__(cin,nom,prenom)
    #login
    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self,f):
        self.__login=f
    #password
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,f):
        self.__password=f
    #email
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,f):
        self.__email=f
    def __str__(self):
        return f"Login:{self.login} mot de pass:{self.password} Email:{self.email}"
class Client(Personne):
    def __init__(self,numpermis=0,tele=0,cin='L3456',nom='n1',prenom='p1'):
        self.__numpermis=numpermis
        self.__tel=tele
        super().__init__(cin,nom,prenom)
        #functions
        
    #numpermis
    @property
    def numpermis(self):
        return self.__numpermis
    @numpermis.setter
    def numpermis(self,f):
        self.__numpermis=f
    #tel
    @property
    def tel(self):
        return self.__tel
    @tel.setter
    def tel(self,f):
        self.__tel=f
    #methods
    def __str__(self):
        return f"Personne:{super().__str__()} Nom{self.tel} Prenom{self.numpermis}"
    def ajouter(self,c):
        c==Client()
    def supprimerC(self,cin):
        if cin==self.cin:
            del self
    def modifierC(self,v):
        if v==self:
            self=v
class ListeUtilisateur:
    def __init__(self,master,lu=[]):
        self.__lu=lu
        my_fr=Frame(master)
        my_fr.grid()
        #label1
        self.my_label=Label(master,text='Vous infos :',bg='white',font=('Raleway',18,"bold"))
        self.my_label.grid(row=2,columnspan=3,pady=30,padx=1)
        #input:login
        self.my_login=Entry(master,width=25,textvariable=StringVar(),font=("Raleway",13),bg='white')
        self.my_login.insert(0,'Login')
        def enter(e):
            self.my_login.delete(0,'end')
        def leave(e):
            name=self.my_login.get()
            if name=='':
                self.my_login.insert(0,'Login')
        self.my_login.bind('<FocusIn>',enter)
        self.my_login.bind('<FocusOut>',leave)
        self.my_login.grid(row=4,columnspan=4,padx=12,pady=35)
        #input:password
        self.mdp=Entry(master,width=25,textvariable=StringVar(),font=("Raleway",13),bg='white')
        self.mdp.insert(0,'Mot de pass')
        def enter(e):
            self.mdp.delete(0,'end')
        def leave(e):
            name=self.mdp.get()
            if name=='':
                self.mdp.insert(0,'Mot de pass')
        self.mdp.bind('<FocusIn>',enter)
        self.mdp.bind('<FocusOut>',leave)
        self.mdp.grid(row=5,columnspan=4,padx=12)
        #btn
        self.btn=Button(master,text='Connexion',bg='black',fg='#ffffff',font=("Raleway",13),command=lambda :self.authentifier(self.my_login.get(),self.mdp.get()))
        self.btn.grid(row=6,columnspan=4,padx=1,pady=26)
    #liste utilisateur
    @property
    def lu(self):
        return self.__lu
    @lu.setter
    def lu(self,i):
        self.__lu=i
    #methods
    def __str__(self):
        return f"listes utilisateur:{self.lu}"
    def authentifier(self,loginn,mdp):
        for x in self.lu:
            if x.login==loginn and x.password==mdp:
                self.top=Toplevel()
                self.top.title('Main page')
                self.top.configure(bg='white')
                self.top.resizable(False,False)
                self.top.geometry('925x650')
                #functions
                def hidethings():
                    self.addUframe.place_forget()
                    self.displayUframe.place_forget()
                    self.displayCframe.place_forget()
                    self.addCframe.place_forget()  
                    self.displayVframe.place_forget()
                    self.addVframe.place_forget()           
                #utilisateur
                def addU():
                    hidethings()
                    self.addUframe.place(x=0,y=100,width=925,height=570)
                    #label again TT
                    label=Label(self.addUframe,text='Ajouter un utilisateur:',bg='white',font=("Raleway",20,'bold')).grid(row=3,columnspan=8,pady=20)
                    #nom
                    nom=Label(self.addUframe,text='Entrer votre nom:',bg='white',font=("Raleway",13)).grid(row=5,columnspan=2,pady=20)
                    nom_input=Entry(self.addUframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                    nom_input.grid(row=5,columnspan=2,column=6)
                    #prenom
                    prenom=Label(self.addUframe,text='Entrer votre prenom:',bg='white',font=("Raleway",13)).grid(row=7,columnspan=2,pady=20)
                    prenom_input=Entry(self.addUframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                    prenom_input.grid(row=7,columnspan=2,column=6)
                    #cin
                    cin=Label(self.addUframe,text='Entrer votre numero de CIN:',bg='white',font=("Raleway",13)).grid(row=9,columnspan=2,pady=20)
                    cin_input=Entry(self.addUframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                    cin_input.grid(row=9,columnspan=2,column=6)
                    #login
                    login=Label(self.addUframe,text='Entrer le login:',bg='white',font=("Raleway",13)).grid(row=11,columnspan=2,pady=20)
                    login_input=Entry(self.addUframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                    login_input.grid(row=11,columnspan=2,column=6)
                    #password
                    pwd=Label(self.addUframe,text='Entrer le mot de pass:',bg='white',font=("Raleway",13)).grid(row=13,columnspan=2,pady=20)
                    pwd_input=Entry(self.addUframe,textvariable=StringVar(),show='*',bg='white',font=("Raleway",13))
                    pwd_input.grid(row=13,columnspan=2,column=6)
                    #email
                    email=Label(self.addUframe,text='Entrer le email:',bg='white',font=("Raleway",13)).grid(row=15,columnspan=2,pady=20)
                    email_input=Entry(self.addUframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                    email_input.grid(row=15,columnspan=2,column=6)
                    #btn
                    btn=Button(self.addUframe,text='Ajouter',bg='black',fg='#fff',font=("Raleway",13),command=lambda:self.ajouterU(login_input.get(),pwd_input.get(),email_input.get(),cin_input.get(),nom_input.get(),prenom_input.get()))
                    btn.grid(row=16,columnspan=2,pady=20)
                def displayU():
                    hidethings()
                    self.displayUframe.place(x=0,y=100,width=925,height=570)
                    label=Label(self.displayUframe,text='les Utilisateurs :',bg='white',font=("Raleway",20,'bold')).place(y=14,x=50)
                                        
                    frame_styles = {"relief": "groove",
                                    "bd": 3}
                    frame1 =Frame(self.displayUframe,frame_styles)
                    frame1.place(height=200, width=600,x=40,y=100)
                    #data
                    tree1 = ttk.Treeview(frame1)
                    column_list_account = ['Prenom','Nom','CIN','Email','Login','Mot de pass']
                    tree1['columns'] = column_list_account
                    tree1["show"] = "headings"  # removes empty column
                    for column in column_list_account:
                        tree1.heading(column, text=column)
                        tree1.column(column, width=50)
                    count=0
                    for i in self.lu:
                        tree1.insert(parent='',index='end',iid=count,text='',values=[i.prenom,i.nom,i.cin,i.email,i.login,i.password])
                        count+=1
                    tree1.place(relheight=1, relwidth=0.995)
                    treescroll = Scrollbar(frame1)
                    treescroll.configure(command=tree1.yview)
                    tree1.configure(yscrollcommand=treescroll.set)
                    treescroll.pack(side="right", fill="y")

                    def supprimerU():
                        x=tree1.selection()
                        tree1.delete(x)
                    def modifierU():
                        #prenom
                        prenom=Label(self.displayUframe,text='Prenom',bg='white',font=("Raleway",13)).place(x=45,y=380)                
                        prenom_input=Entry(self.displayUframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        prenom_input.place(y=380,x=105)
                        #nom
                        nom=Label(self.displayUframe,text='Nom',bg='white',font=("Raleway",13)).place(x=276,y=380)                
                        nom_input=Entry(self.displayUframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        nom_input.place(y=380,x=370)  
                        #cin
                        cin=Label(self.displayUframe,text='CIN',bg='white',font=("Raleway",13)).place(x=45,y=440)                
                        cin_input=Entry(self.displayUframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        cin_input.place(y=440,x=105)  
                        #email
                        email=Label(self.displayUframe,text='Email',bg='white',font=("Raleway",13)).place(x=276,y=440)                
                        email_input=Entry(self.displayUframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        email_input.place(y=440,x=370) 
                        #login 
                        login=Label(self.displayUframe,text='Login',bg='white',font=("Raleway",13)).place(x=45,y=500)                
                        login_input=Entry(self.displayUframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        login_input.place(y=500,x=105) 
                        #pwd 
                        pwd=Label(self.displayUframe,text='Mot de pass',bg='white',font=("Raleway",13)).place(x=276,y=500)                
                        pwd_input=Entry(self.displayUframe,textvariable=StringVar(),show='*',bg='white',font=("Raleway",13))
                        pwd_input.place(y=500,x=370)
                        def selectin():
                            #clearin the damn zones T.T
                            nom_input.delete(0,'end')
                            prenom_input.delete(0,'end')
                            cin_input.delete(0,'end')
                            email_input.delete(0,'end')
                            login_input.delete(0,'end')
                            pwd_input.delete(0,'end')
                            #selectin
                            select=tree1.focus()
                            values=tree1.item(select,'values') 
                            #outputtin
                            nom_input.insert(0,values[0])
                            prenom_input.insert(0,values[1])
                            cin_input.insert(0,values[2])
                            email_input.insert(0,values[3])
                            login_input.insert(0,values[4])
                            pwd_input.insert(0,values[5])  
                        def updatin():
                            selected=tree1.focus()
                            #savin new data
                            tree1.item(selected,text='',values=(nom_input.get(),prenom_input.get(),cin_input.get(),email_input.get(),login_input.get(),pwd_input.get()))
                            #clearin data entries
                            nom_input.delete(0,'end')
                            prenom_input.delete(0,'end')
                            cin_input.delete(0,'end')
                            email_input.delete(0,'end')
                            login_input.delete(0,'end')
                            pwd_input.delete(0,'end')
                        btnselect=Button(self.displayUframe,text='Selectionner',font=("Raleway",13),fg='white',bg='black',command=selectin).place(x=560,y=500)
                        btnselect=Button(self.displayUframe,text='Actualiser',font=("Raleway",13),fg='white',bg='black',command=updatin).place(x=680,y=500)
                    #btns
                    btn_sup=Button(self.displayUframe,text='Supprimer',font=('Raleway',13),fg='#fff',bg='#000',command=supprimerU)
                    btn_sup.place(x=45,y=300)
                    btn_mod=Button(self.displayUframe,text='Modifier',font=('Raleway',13),fg='#fff',bg='#000',command=modifierU)
                    btn_mod.place(x=150,y=300)
                listesclient=([])
                listesvoitureCIT=([])
                listesvoitureVIP=([])
                #client
                def addC():
                    hidethings()
                    self.addCframe.place(x=0,y=100,width=925,height=570)
                    #label again TT
                    label=Label(self.addCframe,text='Ajouter un client:',bg='white',font=("Raleway",20,'bold')).grid(row=3,columnspan=8,pady=20)
                    #nom
                    nom=Label(self.addCframe,text='Entrer votre nom:',bg='white',font=("Raleway",13)).grid(row=5,columnspan=2,pady=20)
                    nom_input=Entry(self.addCframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                    nom_input.grid(row=5,columnspan=2,column=6)
                    #prenom
                    prenom=Label(self.addCframe,text='Entrer votre prenom:',bg='white',font=("Raleway",13)).grid(row=7,columnspan=2,pady=20)
                    prenom_input=Entry(self.addCframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                    prenom_input.grid(row=7,columnspan=2,column=6)
                    #cin
                    cin=Label(self.addCframe,text='Entrer votre numero de CIN:',bg='white',font=("Raleway",13)).grid(row=9,columnspan=2,pady=20)
                    cin_input=Entry(self.addCframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                    cin_input.grid(row=9,columnspan=2,column=6)
                    #login
                    login=Label(self.addCframe,text='Entrer num permission:',bg='white',font=("Raleway",13)).grid(row=11,columnspan=2,pady=20)
                    login_input=Entry(self.addCframe,textvariable=IntVar(),bg='white',font=("Raleway",13))
                    login_input.grid(row=11,columnspan=2,column=6)
                    #password
                    pwd=Label(self.addCframe,text='Entrer num telephone:',bg='white',font=("Raleway",13)).grid(row=13,columnspan=2,pady=20)
                    pwd_input=Entry(self.addCframe,textvariable=IntVar(),bg='white',font=("Raleway",13))
                    pwd_input.grid(row=13,columnspan=2,column=6)
                    
                    def ajouterC(loginN,passTEl,cin,nom,prenom):
                        c=Client(loginN,passTEl,cin,nom,prenom)
                        listesclient.append(c)
                    #btn
                    btn=Button(self.addCframe,text='Ajouter',bg='black',fg='#fff',font=("Raleway",13),command=lambda:ajouterC(login_input.get(),pwd_input.get(),cin_input.get(),nom_input.get(),prenom_input.get()))
                    btn.grid(row=16,columnspan=2,pady=20)
                def displayC():
                    hidethings()
                    self.displayCframe.place(x=0,y=100,width=925,height=570)
                    label=Label(self.displayCframe,text='les clients :',bg='white',font=("Raleway",20,'bold')).place(y=14,x=50)
                                        
                    frame_styles = {"relief": "groove",
                                    "bd": 3}
                    frame1 =Frame(self.displayCframe,frame_styles)
                    frame1.place(height=200, width=600,x=40,y=100)
                    #data
                    tree1 = ttk.Treeview(frame1)
                    column_list_account = ['Prenom','Nom','CIN','Telephone','Num permission']
                    tree1['columns'] = column_list_account
                    tree1["show"] = "headings"  # removes empty column
                    for column in column_list_account:
                        tree1.heading(column, text=column)
                        tree1.column(column, width=50)
                    count=0
                    for i in listesclient:
                        tree1.insert(parent='',index='end',iid=count,text='',values=[i.prenom,i.nom,i.cin,i.tel,i.numpermis])
                        count+=1
                    tree1.place(relheight=1, relwidth=0.995)
                    treescroll = Scrollbar(frame1)
                    treescroll.configure(command=tree1.yview)
                    tree1.configure(yscrollcommand=treescroll.set)
                    treescroll.pack(side="right", fill="y")

                    def supprimerU():
                        x=tree1.selection()
                        tree1.delete(x)
                    def modifierU():
                        #prenom
                        prenom=Label(self.displayCframe,text='Prenom',bg='white',font=("Raleway",13)).place(x=45,y=380)                
                        prenom_input=Entry(self.displayCframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        prenom_input.place(y=380,x=105)
                        #nom
                        nom=Label(self.displayCframe,text='Nom',bg='white',font=("Raleway",13)).place(x=276,y=380)                
                        nom_input=Entry(self.displayCframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        nom_input.place(y=380,x=370)  
                        #cin
                        cin=Label(self.displayCframe,text='CIN',bg='white',font=("Raleway",13)).place(x=45,y=440)                
                        cin_input=Entry(self.displayCframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        cin_input.place(y=440,x=105)  
                        #email
                        email=Label(self.displayCframe,text='Telephone',bg='white',font=("Raleway",13)).place(x=276,y=440)                
                        email_input=Entry(self.displayCframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        email_input.place(y=440,x=370) 
                        #login 
                        login=Label(self.displayCframe,text='Num permission',bg='white',font=("Raleway",13)).place(x=45,y=500)                
                        login_input=Entry(self.displayCframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        login_input.place(y=500,x=105) 
                        #pwd 
                        def selectin():
                            #clearin the damn zones T.T
                            nom_input.delete(0,'end')
                            prenom_input.delete(0,'end')
                            cin_input.delete(0,'end')
                            email_input.delete(0,'end')
                            login_input.delete(0,'end')
        
                            #selectin
                            select=tree1.focus()
                            values=tree1.item(select,'values') 
                            #outputtin
                            nom_input.insert(0,values[0])
                            prenom_input.insert(0,values[1])
                            cin_input.insert(0,values[2])
                            email_input.insert(0,values[3])
                            login_input.insert(0,values[4])
                            
                        def updatin():
                            selected=tree1.focus()
                            #savin new data
                            tree1.item(selected,text='',values=(nom_input.get(),prenom_input.get(),cin_input.get(),email_input.get(),login_input.get()))
                            #clearin data entries
                            nom_input.delete(0,'end')
                            prenom_input.delete(0,'end')
                            cin_input.delete(0,'end')
                            email_input.delete(0,'end')
                            login_input.delete(0,'end')
                            
                        btnselect=Button(self.displayCframe,text='Selectionner',font=("Raleway",13),fg='white',bg='black',command=selectin).place(x=560,y=500)
                        btnselect=Button(self.displayCframe,text='Actualiser',font=("Raleway",13),fg='white',bg='black',command=updatin).place(x=680,y=500)
                    #btns
                    btn_sup=Button(self.displayCframe,text='Supprimer',font=('Raleway',13),fg='#fff',bg='#000',command=supprimerU)
                    btn_sup.place(x=45,y=300)
                    btn_mod=Button(self.displayCframe,text='Modifier',font=('Raleway',13),fg='#fff',bg='#000',command=modifierU)
                    btn_mod.place(x=150,y=300)
                #voiture
                def displayV():
                    hidethings()
                    self.displayVframe.place(x=0,y=100,width=925,height=570)
                    label=Label(self.displayVframe,text='les voitures :',bg='white',font=("Raleway",20,'bold')).place(y=14,x=50)
                                        
                    frame_styles = {"relief": "groove",
                                    "bd": 3}
                    frame1 =Frame(self.displayVframe,frame_styles)
                    frame1.place(height=200, width=600,x=40,y=100)
                    #data
                    tree1 = ttk.Treeview(frame1)
                    column_list_account = [ 'immatriculation', 'marque', 'carburant', 'modèle', 'puissance fiscal','type']
                    tree1['columns'] = column_list_account
                    tree1["show"] = "headings"  # removes empty column
                    for column in column_list_account:
                        tree1.heading(column, text=column)
                        tree1.column(column, width=50)
                    count=0
                    for i in listesvoitureVIP:
                        tree1.insert(parent='',index='end',iid=count,text='',values=[i.imma,i.mar,i.car,i.mod,i.puifiscale,i.type])
                        count+=1
                    tree1.place(relheight=1, relwidth=0.995)
                    treescroll = Scrollbar(frame1)
                    treescroll.configure(command=tree1.yview)
                    tree1.configure(yscrollcommand=treescroll.set)
                    treescroll.pack(side="right", fill="y")

                    def supprimerU():
                        x=tree1.selection()
                        tree1.delete(x)
                    def modifierU():
                        #prenom
                        prenom=Label(self.displayVframe,text='immatriculation',bg='white',font=("Raleway",13)).place(x=45,y=380)                
                        prenom_input=Entry(self.displayVframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        prenom_input.place(y=380,x=140)
                        #nom
                        nom=Label(self.displayVframe,text='marque',bg='white',font=("Raleway",13)).place(x=276,y=380)                
                        nom_input=Entry(self.displayVframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        nom_input.place(y=380,x=370)  
                        #cin
                        cin=Label(self.displayVframe,text='carburant',bg='white',font=("Raleway",13)).place(x=45,y=440)                
                        cin_input=Entry(self.displayVframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        cin_input.place(y=440,x=140)  
                        #email
                        email=Label(self.displayVframe,text='modele',bg='white',font=("Raleway",13)).place(x=276,y=440)                
                        email_input=Entry(self.displayVframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        email_input.place(y=440,x=370) 
                        #login 
                        login=Label(self.displayVframe,text='puissance fiscale',bg='white',font=("Raleway",13)).place(x=45,y=500)                
                        login_input=Entry(self.displayVframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                        login_input.place(y=500,x=140) 
                        #pwd 
                        pwd=Label(self.displayUframe,text='type',bg='white',font=("Raleway",13)).place(x=276,y=500)                
                        pwd_input=Entry(self.displayUframe,textvariable=StringVar(),show='*',bg='white',font=("Raleway",13))
                        pwd_input.place(y=500,x=370)
                        def selectin():
                            #clearin the damn zones T.T
                            nom_input.delete(0,'end')
                            prenom_input.delete(0,'end')
                            cin_input.delete(0,'end')
                            email_input.delete(0,'end')
                            login_input.delete(0,'end')
                            pwd_input.delete(0,'end')
        
                            #selectin
                            select=tree1.focus()
                            values=tree1.item(select,'values') 
                            #outputtin
                            nom_input.insert(0,values[0])
                            prenom_input.insert(0,values[1])
                            cin_input.insert(0,values[2])
                            email_input.insert(0,values[3])
                            login_input.insert(0,values[4])
                            pwd_input.insert(0,values[5])
                        def updatin():
                            selected=tree1.focus()
                            #savin new data
                            tree1.item(selected,text='',values=(nom_input.get(),prenom_input.get(),cin_input.get(),email_input.get(),login_input.get(),pwd_input.get()))
                            #clearin data entries
                            nom_input.delete(0,'end')
                            prenom_input.delete(0,'end')
                            cin_input.delete(0,'end')
                            email_input.delete(0,'end')
                            login_input.delete(0,'end')
                            pwd_input.delete(0,'end')
                            
                        btnselect=Button(self.displayVframe,text='Selectionner',font=("Raleway",13),fg='white',bg='black',command=selectin).place(x=560,y=500)
                        btnselect=Button(self.displayVframe,text='Actualiser',font=("Raleway",13),fg='white',bg='black',command=updatin).place(x=680,y=500)
                    #btns
                    btn_sup=Button(self.displayVframe,text='Supprimer',font=('Raleway',13),fg='#fff',bg='#000',command=supprimerU)
                    btn_sup.place(x=45,y=300)
                    btn_mod=Button(self.displayVframe,text='Modifier',font=('Raleway',13),fg='#fff',bg='#000',command=modifierU)
                    btn_mod.place(x=150,y=300)
                def addV():
                    hidethings()
                    self.addVframe.place(x=0,y=100,width=925,height=570)
                    #label again TT
                    label=Label(self.addVframe,text='Ajouter une voiture:',bg='white',font=("Raleway",20,'bold')).grid(row=2,columnspan=8,pady=20)
                    #ask them
                    op=Label(self.addVframe,text='Entrer "CIT" pour Citadine et "VIP" pour Vip',bg='white',font=("Raleway",13)).grid(row=2,columnspan=2,column=2)
                    op_input=Entry(self.addVframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                    op_input.grid(row=2,columnspan=2,column=6)
                    def func(k):
                        if k=='CIT':
                            #nom
                            nom=Label(self.addVframe,text='Entrer immatriculation:',bg='white',font=("Raleway",13)).grid(row=4,columnspan=2,pady=20)
                            nom_input=Entry(self.addVframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                            nom_input.grid(row=4,columnspan=2,column=6)
                            #prenom
                            prenom=Label(self.addVframe,text='Entrer la marque:',bg='white',font=("Raleway",13)).grid(row=6,columnspan=2,pady=20)
                            prenom_input=Entry(self.addVframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                            prenom_input.grid(row=6,columnspan=2,column=6)
                            #cin
                            cin=Label(self.addVframe,text='Entrer le carburant:',bg='white',font=("Raleway",13)).grid(row=8,columnspan=2,pady=20)
                            cin_input=Entry(self.addVframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                            cin_input.grid(row=8,columnspan=2,column=6)
                            #login
                            login=Label(self.addVframe,text='Entrer le modele:',bg='white',font=("Raleway",13)).grid(row=10,columnspan=2,pady=20)
                            login_input=Entry(self.addVframe,textvariable=IntVar(),bg='white',font=("Raleway",13))
                            login_input.grid(row=10,columnspan=2,column=6)
                            #password
                            pwd=Label(self.addVframe,text='Entrer la puissance fiscale:',bg='white',font=("Raleway",12)).grid(row=13,columnspan=2,pady=20)
                            pwd_input=Entry(self.addVframe,textvariable=IntVar(),bg='white',font=("Raleway",13))
                            pwd_input.grid(row=12,columnspan=2,column=6)
                            #gamme
                            gm=Label(self.addVframe,text='Entrer la gamme :',bg='white',font=("Raleway",13)).grid(row=16,columnspan=2,pady=20)
                            gm_input=Entry(self.addVframe,textvariable=IntVar(),bg='white',font=("Raleway",13))
                            gm_input.grid(row=16,columnspan=2,column=6)
                            
                            def ajouterC(loginMO,passPF,cinC,nomMA,prenomIMMa,gam):
                                c=VoitureCitadinne(gam,prenomIMMa,nomMA,cinC,loginMO,passPF)
                                listesvoitureCIT.append(c)
                            #btn
                            btn=Button(self.addVframe,text='Ajouter',bg='black',fg='#fff',font=("Raleway",13),command=lambda:ajouterC(login_input.get(),pwd_input.get(),cin_input.get(),nom_input.get(),prenom_input.get(),gm_input.get()))
                            btn.grid(row=18,columnspan=2,pady=20)
                        elif k=='VIP':
                            #nom
                            nom=Label(self.addVframe,text='Entrer immatriculation:',bg='white',font=("Raleway",13)).grid(row=4,columnspan=2,pady=20)
                            nom_input=Entry(self.addVframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                            nom_input.grid(row=4,columnspan=2,column=6)
                            #prenom
                            prenom=Label(self.addVframe,text='Entrer la marque:',bg='white',font=("Raleway",13)).grid(row=6,columnspan=2,pady=20)
                            prenom_input=Entry(self.addVframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                            prenom_input.grid(row=6,columnspan=2,column=6)
                            #cin
                            cin=Label(self.addVframe,text='Entrer le carburant:',bg='white',font=("Raleway",13)).grid(row=8,columnspan=2,pady=20)
                            cin_input=Entry(self.addVframe,textvariable=StringVar(),bg='white',font=("Raleway",13))
                            cin_input.grid(row=8,columnspan=2,column=6)
                            #login
                            login=Label(self.addVframe,text='Entrer le modele:',bg='white',font=("Raleway",13)).grid(row=10,columnspan=2,pady=20)
                            login_input=Entry(self.addVframe,textvariable=IntVar(),bg='white',font=("Raleway",13))
                            login_input.grid(row=10,columnspan=2,column=6)
                            #password
                            pwd=Label(self.addVframe,text='Entrer la puissance fiscale:',bg='white',font=("Raleway",13)).grid(row=12,columnspan=2,pady=20)
                            pwd_input=Entry(self.addVframe,textvariable=IntVar(),bg='white',font=("Raleway",13))
                            pwd_input.grid(row=12,columnspan=2,column=6)
                            #gamme
                            gm=Label(self.addVframe,text='Entrer le type :',bg='white',font=("Raleway",13)).grid(row=16,columnspan=2,pady=20)
                            gm_input=Entry(self.addVframe,textvariable=IntVar(),bg='white',font=("Raleway",13))
                            gm_input.grid(row=16,columnspan=2,column=6)
                            
                            def ajouterC(loginMO,passPF,cinC,nomMA,prenomIMMa,type):
                                c=VoitureVip(type,prenomIMMa,nomMA,cinC,loginMO,passPF)
                                listesvoitureCIT.append(c)
                            #btn
                            btn=Button(self.addVframe,text='Ajouter',bg='black',fg='#fff',font=("Raleway",13),command=lambda:ajouterC(login_input.get(),pwd_input.get(),cin_input.get(),nom_input.get(),prenom_input.get(),gm_input.get()))
                            btn.grid(row=18,columnspan=2,pady=20)
                        else:
                            messagebox.showwarning('Erreur','Ce choix n\'existe pas *-*')
                    btnn=Button(self.addVframe,text='Selectionner',bg='black',fg='#fff',font=("Raleway",13),command=lambda:func(op_input.get())).grid(row=2,column=12)
                    

                #huge label ^^
                self.label1=Label(self.top,fg='black',bg='#ffffff',font=("Raleway",23,'bold'),text='Bienvenue !!!')
                self.label1.grid(row=0,columnspan=6,padx=350,pady=23)
                self.my_menu=Menu(self.top)
                self.top.config(menu=self.my_menu)
                #user interface
                self.utilisateur=Menu(self.my_menu)
                self.my_menu.add_cascade(label='Utilisateur',menu=self.utilisateur)
                self.utilisateur.add_command(label='Afficher les Utilisateurs',command=displayU)
                self.utilisateur.add_separator()
                self.utilisateur.add_command(label='Ajouter un utilisateur',command=addU)
                #client interface
                self.client=Menu(self.my_menu)
                self.my_menu.add_cascade(label='Client',menu=self.client)
                self.client.add_command(label='Afficher les clients',command=displayC)
                self.client.add_separator()
                self.client.add_command(label='Ajouter un client',command=addC)
                #car interface
                self.voiture=Menu(self.my_menu)
                self.my_menu.add_cascade(label='Voiture',menu=self.voiture)
                self.voiture.add_command(label='Afficher les voitures',command=displayV)
                self.voiture.add_separator()
                self.voiture.add_command(label='Ajouter une voiture',command=addV)
                #rent interface
                self.location=Menu(self.my_menu)
                self.my_menu.add_cascade(label='Location',menu=self.location)
                self.location.add_command(label='Afficher les locations')
                self.location.add_separator()
                self.location.add_command(label='Ajouter une location')
                #add frames
                self.addUframe=Frame(self.top,width=925,height=570,bg='#fff')
                self.displayUframe=Frame(self.top,width=925,height=570,bg='white')
                self.addCframe=Frame(self.top,width=925,height=570,bg='#fff')
                self.displayCframe=Frame(self.top,width=925,height=570,bg='white')
                self.addVframe=Frame(self.top,width=925,height=570,bg='#fff')
                self.displayVframe=Frame(self.top,width=925,height=570,bg='white')
               
                break
        else:
           messagebox.showerror('Erreur!','Mot de pass ou Login est incorrect') 
    def ajouterU(self,l,p,e,c,n,pre):
        user=Utilisateur(l,p,e,c,n,pre)
        self.lu.append(user)
    def supprimerU(self,loginn):
        for i in self.lu:
            if i.login==loginn:
                del i
                break
        else:
            print('ce utilisateur n\'existe pas')
    def modifierU(self):
        return
        
        
u=Utilisateur('1','1','yuuuh@.com',5850,'rodrigo','olivia')
u1=Utilisateur('me','1234','yuuuh@.com',5850,'johnson','jashua')
l=[u,u1]
ull=ListeUtilisateur(huh,l)
#label1
my_label=Label(huh,text='Bienvenue chez nous !',font=('Raleway',23,"bold"),bg='white')
my_label.grid(row=0,columnspan=6,padx=300,pady=25)

huh.mainloop()
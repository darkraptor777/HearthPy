#Hearth.py (OOP Edition) v2.2.1
#
#BUGS
#Fix minor text bugs
#
#ToDo
#Improve Name Generation
#Improve Spell generation
#^Add Secrets
#
#Rework "Counter" so it works in a satisfactory way
#Add stat buff and debuff ability
#Balance choose one ability (so one choice isn't always better than another)
#Add "enrage" ability
#Add "discover" ability
#Add summon ability
#Add "Joust"
#^implement database of existing cards to reference
#Add "Triggers" (e.g. at the end of your turn etc.)
#Add "Passives" (e.g. all friendly minions have +1 attack)
#
#Give AI better balancing of;
#^lategame cards with negative effects
#^negative inspire effects
#^negative combo effects
#^cards with stats above 10/10
#^early game cards
#
#Add ability to create weapons
#
#Give AI better understanding of class "flavor"
#Give AI better understanding of Legendary Cards
#Give AI better understanding of how to use Overload


import random
import L3P

class Card():

    def __init__(self,Type,S_Data):                            #Sets up default values
        self.Type=Type
        self.Class="Null"
        self.Mana="Null"
        self.Text=""
        self.Name="Null"
        self.Rarity="Null"
        self.Value="Null"
        if self.Type=="Minion":                              #If the card type is a minion also use these values
            self.Attack=0
            self.Health=0
            self.Tribe="Null"
        self.S_Data=S_Data 

    def Dump(self):                                     #Displays all relavent card information
        print("Type:",self.Type)
        print("Name:",self.Name)
        print("Class:",self.Class)
        print("Mana Cost:",self.Mana)
        if self.Type=="Minion":
            print("Attack:",self.Attack)
            print("Health:",self.Health)
        print("Text:",self.Text)
        if self.Type=="Minion":
            print("Tribe:",self.Tribe)
        print("Rarity:",self.Rarity)

    def Generate(self):                                 #Generate a new card
        self.Set_Class()
        self.Set_Mana()
        self.Set_Value()
        self.Set_Rarity()
        if self.Type=="Minion":
            self.Set_Tribe()
        self.Set_Text()
        if self.Type=="Minion":
            self.Set_Stats()
        self.Evolve_Name()

    def Get_Useable(self):
        Sets=L3P.HSImport()
##        Minions=Set_Basic.Minions()+Set_Classic.Minions() +Set_Naxxramus.Minions() +Set_GvG.Minions() +Set_BlckMT.Minions() +Set_TGT.Minions() +Set_LoE.Minions() +Set_WotOG.Minions() +Set_Kara.Minions() +Set_MSG.Minions()
##        Spells=Set_Basic.Spells()+Set_Classic.Spells() +Set_Naxxramus.Spells() +Set_GvG.Spells() +Set_BlckMT.Spells() +Set_TGT.Spells() +Set_LoE.Spells() +Set_WotOG.Spells() +Set_Kara.Spells() +Set_MSG.Spells()
##        Weapons=Set_Basic.Weapons()+Set_Classic.Weapons() +Set_Naxxramus.Weapons() +Set_GvG.Weapons() +Set_BlckMT.Weapons() +Set_TGT.Weapons() +Set_LoE.Weapons() +Set_WotOG.Weapons() +Set_Kara.Weapons() +Set_MSG.Weapons()
        Useable_Words=[]
        if self.Type=="Minion" or self.Type=="All":
            Data_Raw=[]
            for Set in Sets:
                Data_Raw+=Set.Minions()
            Data_Names=[]
            for x in range(len(Data_Raw)): #the raw data is a 2d array and so this loop retrieves the required information from the array and puts it in a list
                Name=Data_Raw[x][6]
                Useable_Words.append(Name)
                
        if self.Type=="Spell" or self.Type=="All":
            Data_Raw=[]
            for Set in Sets:
                Data_Raw+=Set.Spells()   
            for x in range(len(Data_Raw)): #the raw data is a 2d array and so this loop retrieves the required information from the array and puts it in a list
                Name=Data_Raw[x][3]
                Useable_Words.append(Name)

        if self.Type=="Weapon" or self.Type=="All":
            Data_Raw=[]
            for Set in Sets:
                Data_Raw+=Set.Weapons()    
            for x in range(len(Data_Raw)): #the raw data is a 2d array and so this loop retrieves the required information from the array and puts it in a list
                Name=Data_Raw[x][5]
                Useable_Words.append(Name)
                
        return Useable_Words

    def Set_Name(self): #the old method of getting card names
        #Handles selecting appropriate words for use in name generation
        Useable_Words=self.Get_Useable()
        
        Names=Get_Names(Useable_Words)                  #Puts the useable words into a suitable format

        name_valid=False
        while name_valid==False:
            Name=""
            for loop in range(random.randint(1,3)):
                Name+=Random_List(Names)
                Name+=" "
            if Name not in Minions and Name not in Weapons:                 #if the name hasn't already been used it is valid
                name_valid=True
        self.Name=Name

    def Evolve_Name_Setup(self):
        print("Loading...")
        Useable_Words=self.Get_Useable()
        S_Data=L3P.Score(L3P.Compile(Useable_Words))
        return S_Data
        
    def Evolve_Name(self): #This section uses L3P
        GenWord=L3P.GetWord(30,self.S_Data,100,False,0.001,False)
        if self.Type=="Minion":
            try:
                File=open('English.txt','r')
                List=[]
                for row in File:
                    List.append(row.replace('\n',''))
                File.close()
                NameFormat=random.randint(1,3)
                TitleOne=str(List[random.randint(0,len(List)-1)])
                TitleTwo=str(List[random.randint(0,len(List)-1)])
                if NameFormat==1:
                    self.Name=GenWord+", "+TitleOne+" of "+TitleTwo
                elif NameFormat==2:
                    self.Name=GenWord+" the "+TitleOne
                elif NameFormat==3:
                    self.Name=TitleOne+" of "+GenWord
            except FileNotFoundError:
                print("English.txt File Missing")
                self.Name=GenWord
                
        else:
            self.Name=GenWord
        

    def Set_Class(self):    #Randomly select a class
        Classes=["Neutral","Mage","Paladin","Priest","Warlock","Hunter","Druid","Shaman","Warrior","Rogue"]
        if self.Type=="Spell":
            Classes.remove("Neutral") #no neutral spells
        self.Class=Random_List(Classes)

    def Set_Mana(self):     #Randomly select mana cost
        self.Mana=random.randint(0,10)

    def Set_Value(self):    #Generate Useable value from mana cost
        self.Value=(self.Mana*2)
        self.Value+=1

    def Set_Text(self):     #Generate card text
        Effect=[]
        Cost=0

        if self.Type=="Minion":
            New_Keywords=True
            Static_Keywords=Compile_Keywords(self,"Static")
            Versatile_Keywords=Compile_Keywords(self,"Versatile")   #Compiles lists of keywords based on the keyword type
            Effect_Type_List=["Static","Versatile"]                     #NOTE: static keywords do not change (or change very little and versatile keywords are often different from eachother
            while New_Keywords:
                for word in Static_Keywords:
                    if word[1] > self.Value:
                        Static_Keywords.remove(word)    #if the inherent cost of a keyword is greater than the value available to the card, remove it from the selection pool
                for word in Versatile_Keywords:
                    if word[1] > self.Value:
                        Versatile_Keywords.remove(word) #if the inherent cost of a keyword is greater than the value available to the card, remove it from the selection pool
                try:
                    if len(Effect_Type_List)!=1:        #if a versatile keyword hasn't previously been selected
                        Effect_Type=Random_List(Effect_Type_List)
                    else:
                        Effect_Type=Effect_Type_List[0] #if it has use a static keyword

                    if Effect_Type=="Static":
                        Keyword=Random_List(Static_Keywords)
                        Static_Keywords.remove(Keyword)
                    if Effect_Type=="Versatile":
                        Keyword=Random_List(Versatile_Keywords)
                        Versatile_Keywords.remove(Keyword)   
                    
                except ValueError:      #triggers if the list is empty
                    New_Keywords=False


                Effect=[]
                #Static effects
                if Effect_Type=="Static":
                    if Keyword[0]=="Taunt":
                        Text,Value=Taunt(self)
                        self.Value+=Value
                    if Keyword[0]=="Stealth":
                        Text,Value=Stealth(self)
                        self.Value+=Value
                    if Keyword[0]=="Charge":
                        Text,Value=Charge(self)
                        self.Value+=Value
                    if Keyword[0]=="Divine Shield":
                        Text,Value=Divine_Shield(self)
                        self.Value+=Value
                    if Keyword[0]=="Windfury":
                        Text,Value=Windfury(self)
                        self.Value+=Value
                    if Keyword[0]=="Spell Damage":
                        Text,Value=Spell_Damage(self)
                        self.Value+=Value
                    if Keyword[0]=="Overload":
                        Text,Value=Overload(self)
                        self.Value+=Value
                    if Keyword[0]=="Elusive":
                        Text,Value=Elusive(self)
                        self.Value+=Value
                    if Keyword[0]=="Poisonous":
                        Text,Value=Poisonous(self)
                        self.Value+=Value
                    
                    self.Text+=Text
                    self.Text+=". "

                #Versatile effects
                if Effect_Type=="Versatile":
                    Repeats=1
                    if Keyword[0]=="Battlecry":
                        Text,Value=Battlecry(self)
                        self.Value+=Value
                    if Keyword[0]=="Deathrattle":
                        Text,Value=Deathrattle(self)
                        self.Value+=Value
                    if Keyword[0]=="Inspire":
                        Text,Value=Inspire(self)
                        self.Value+=Value
                    if Keyword[0]=="Combo":
                        Text,Value=Combo(self)
                        self.Value+=Value
                    if Keyword[0]=="Battlecry and Deathrattle":
                        Text,Value=BattlecryAndDeathrattle(self)
                        self.Value+=Value
                    if Keyword[0]=="Choose One":
                        Text,Value=ChooseOne(self)
                        self.Value+=Value
                        Repeats=2
                        AVG_Value=0
                    
                    for loop in range(Repeats): #used exclusively by the choose one mechanic so it can get 2 effects
                        Temp_Effect,Value=Get_Effect(self,Keyword)
                        Effect=Temp_Effect
                        if Keyword[0]=="Choose One":
                            AVG_Value+=Value
                        else:
                            self.Value+=Value
                            
                        #Text formating for choose one mechanic
                        
                        if Keyword[0]=="Choose One" and loop==0:
                            self.Text+="Choose One: "
                        Temp=Text_Format(Temp_Effect)
                        if Keyword[0]=="Choose One" and loop==0:
                            Temp=Temp.replace(".","")
                        self.Text+=Temp
                        if Keyword[0]=="Choose One" and loop==0:
                            self.Text+="OR "
                    if Keyword[0]=="Choose One":
                        self.Value+=int(AVG_Value/2)
                        
                    
                    Effect_Type_List.remove("Versatile")

                if random.randint(1,3)!=3 or self.Value<0:
                  New_Keywords=False
                else:
                    #self.Text+=". "
                    pass
                
        if self.Type=="Spell":
            Spell_Keywords=Compile_Keywords(self,"Spell")
            Keyword=Random_List(Spell_Keywords)
            Effect_Valid=False
            while Effect_Valid==False:
                Temp_Effect,Value=Get_Effect(self,Keyword)
                if self.Mana-int((self.Value+Value)/2)>0:
                    Effect_Valid=True
            self.Value+=Value
            #print("Temp_Effect:",str(Temp_Effect))
            Effect=Text_Format(Temp_Effect)
            self.Text+=Effect
            if self.Value>1:
                Cost_Reduction=int(self.Value/2)
                self.Mana-=Cost_Reduction
            
            
    
    def Set_Tribe(self):
        Tribes=Get_Tribes()
        if self.Class=="Shaman":
            Tribes.append("Totem")
        if self.Class=="Warlock":
            Tribes.append("Demon")
        Tribe_True=random.randint(1,3)
        if Tribe_True==1:
            self.Tribe=Random_List(Tribes)
            self.Value-=1
        else:
            self.Tribe="None"

    def Set_Rarity(self):
        Rarities=[["Common",-0.5],["Rare",0],["Epic",1],["Legendary",2]]
        Roll=random.randint(0,9) #Skews the odds against higher tier rarities being picked
        if Roll==1:
            self.Rarity=Rarities[3]
        if Roll==2 or Roll==3:
            self.Rarity=Rarities[2]
        if Roll==4 or Roll==5 or Roll==6:
            self.Rarity=Rarities[1]
        if Roll==7 or Roll==8 or Roll==9 or Roll==0:
            self.Rarity=Rarities[0]
        self.Value+=self.Rarity[1]
        self.Rarity=self.Rarity[0]

    def Set_Stats(self):
        self.Health+=1
        self.Value+=-1
        if self.Value<0: #if a versatile effect costed more than the card had value points available increase its mana cost so it has enough points
            Temp=self.Value*-1
            Temp=int(Temp/2)+1
            self.Mana+=Temp
            self.Value+=Temp*2
        while self.Value>0:
            if self.Value==0.5:
              self.Value=1

            if "Stealth" in self.Text or "Charge" in self.Text:
                if "Charge" in self.Text:
                    Min=1
                else:
                    Min=0
                Gen_Attack=random.randint(Min,int(self.Value))
                if self.Attack+Gen_Attack>12:
                    Gen_Attack=12-self.Attack
                self.Value-=Gen_Attack
                #print("Value:",Value)
                Gen_Health=random.randint(0,int(self.Value))
                if self.Health+Gen_Health>16:
                    Gen_Health=16-self.Health
                self.Value-=Gen_Health
                #print("Value:",Value)
            
            else:
                Gen_Health=random.randint(0,int(self.Value))
                if self.Health+Gen_Health>16:
                    Gen_Health=16-self.Health
                self.Value-=Gen_Health
                #print("Value:",Value)
                Gen_Attack=random.randint(0,int(self.Value))
                if self.Attack+Gen_Attack>12:
                    Gen_Attack=10-self.Attack
                self.Value-=Gen_Attack
                #print("Value:",Value)

            self.Health+=Gen_Health
            self.Attack+=Gen_Attack
            if self.Health==16 or self.Attack==12: #if the card has excess value, decrease it's mana cost and remove some of it's value
                Temp=int(self.Value/2)
                self.Mana-=Temp
                self.Value-=Temp*2
            
        #try:
        #    self.Attack=random.randint(0,int(self.Value))
        #except ValueError:
        #    self.Attack=0
        #self.Value+=-self.Attack
        #
        #try:
        #    self.Health=random.randint(0,int(self.Value))
        #except ValueError:
        #    self.Health=1
        #self.Value+=-self.Health


#General Functions

def Get_Tribes():
    Tribes=["Beast","Pirate","Dragon","Mech","Murloc"]
    return Tribes
    
def Get_Names(Useable_Words):    
    #Names_One=[]
    #Names_Two=[]
    #Names_Three=[]
    #Names_Four=[]
    Names=[]
    #for loop in range (len(Useable_Words)):
        #Name=Useable_Words[loop]
        
        #if len(Name)==1:
            #Names_One.append(Name)
        #else:
            #Name=Name.split()
            #print(len(Name))
            #for looptwo in range(len(Name)):
                #if looptwo==0:
                    #if Name[looptwo] not in Names_One:
                        #Names_One.append(Name[loop])
                #if loop==1:
                    #if Name[loop] not in Names_Two:
                        #Names_Two.append(Name[loop])
                #if loop==2:
                    #if Name[loop] not in Names_Three:
                        #Names_Three.append(Name[loop])
                #if loop==3:
                    #if Name[loop] not in Names_Four:
                        #Names_Four.append(Name[loop])

    
    #print (Useable_Words)
    for loop in range (len(Useable_Words)):
        Name=str(Useable_Words[loop])
        if len(Name)==1:
            Names.append(Name)
        else:
            Name=Name.split()
            for loop in range(len(Name)):
                if Name[loop] not in Names:
                    Names.append(Name[loop])
                    
    #print(Names_One)
    #print(Names_Two)
    #print(Names_Three)
    #print(Names_Four)
    return Names

def Compile_Keywords(Card,Keyword_Type):
    #print(Keyword_Type)
    if Keyword_Type=="Static":
        Static_Keywords=[["Taunt",-1],["Stealth",-1],["Charge",-2.5],["Spell Damage",0],["Elusive",0]]
        if Card.Class=="Neutral" or Card.Class=="Paladin":
            Static_Keywords.append(["Divine Shield",-2])
        if Card.Class=="Shaman":
            Static_Keywords.append(["Overload",0])
        if Card.Class=="Shaman" or Card.Class=="Neutral":
            Static_Keywords.append(["Windfury",-2])
        if Card.Class=="Rogue" or Card.Class=="Neutral":
            Static_Keywords.append(["Poisonous",-2])
        return Static_Keywords

    if Keyword_Type=="Versatile":
        Versatile_Keywords=[["Battlecry",0],["Deathrattle",0],["Inspire",0],["Battlecry and Deathrattle",0]]
        if Card.Class=="Rogue":
            Versatile_Keywords.append(["Combo",2])
        if Card.Class=="Druid":
            Versatile_Keywords.append(["Choose One",0])
        return Versatile_Keywords

    if Keyword_Type=="Spell":
        Spell_Keywords=[["Spell",2]]
        if Card.Class=="Rogue":
            Spell_Keywords.append(["Combo",2])
        if Card.Class=="Druid":
            Spell_Keywords.append(["Choose One",0])
        return Spell_Keywords

    

def Get_Target_Type():
    Target_Types=["Minion","Character","Hero","Weapon","Spell"]
    Target=Random_List(Target_Types)
    return Target

def Get_Effect(Card,Keyword):
    #print("Class:",str(Card.Class))
    Target_Type=Get_Target_Type()
    if Target_Type=="Minion":
        Target_Area_List=["Friendly","Enemy","Any"]
        Target_Amount_List=["Single","Multiple","All"]
        Target_Effect_List=["Damage","Heal","Destroy","Silence","Give Atk"]
        if Card.Class=="Mage":
            Target_Effect_List.append("Freeze")

    if Target_Type=="Character":
        Target_Area_List=["Friendly","Enemy","Any"]
        Target_Amount_List=["Single","Multiple","All"]
        Target_Effect_List=["Damage","Heal"]
        if Card.Class=="Mage":
            Target_Effect_List.append("Freeze")

    if Target_Type=="Hero":
        Target_Area_List=["Friendly","Enemy"]
        Target_Amount_List=["Single"]
        Target_Effect_List=["Damage","Heal","Draw"]
        if Card.Class=="Mage":
            Target_Effect_List.append("Freeze")
        if Card.Class=="Warlock":
            Target_Effect_List.append("Discard")

    if Target_Type=="Weapon":
        Target_Area_List=["Enemy"]
        if Card.Class=="Rogue" or Card.Class=="Warrior" or Card.Class=="Hunter" or Card.Class=="Shaman":
            Target_Area_List.append("Friendly")
        Target_Amount_List=["Single"]
        Target_Effect_List=["Damage","Destroy","Silence","Give Atk"]

    if Target_Type=="Spell":
        Target_Area_List=["Friendly","Enemy"]
        Target_Amount_List=["Single","All"]
        Target_Effect_List=["Reduce Cost","Increase Cost"] #,"Counter"
  
    Target_Area=Random_List(Target_Area_List)
    Target_Amount=Random_List(Target_Amount_List)
    Target_Effect=Random_List(Target_Effect_List)

    Target_Randoms=["Random",""]
    Target_Random=Target_Randoms[random.randint(0,1)]
    if Keyword[0]=="Deathrattle" or Keyword[0]=="Inspire" or Target_Amount=="Multiple" or Keyword[0]=="Battlecry and Deathrattle":
        Target_Random="Random"
    if Target_Type=="Hero" or Target_Effect=="Counter" or Target_Amount=="All" or Target_Type=="Weapon":
        Target_Random=""

    if Target_Effect=="Discard":
        Target_Area="Friendly"
        Target_Random="Random"

    if Target_Type=="Minion":
        Make_Tribe=random.randint(1,3)
        if Make_Tribe==1:
            Tribes=Get_Tribes()
            Target_Type=Random_List(Tribes)
            
    
  
    Temp_Effect=[Keyword[0],Target_Effect,Target_Amount,Target_Random,Target_Area,Target_Type]
    Temp_Cost=0
    Temp_Cost, Temp_Effect=Get_Cost(Temp_Effect,Temp_Cost)
    #print("New Keyword Cost:",Temp_Cost)
    return Temp_Effect, Temp_Cost

def Get_Cost(Temp_Effect,Temp_Cost):
    ##Quantity Selection##
    if Temp_Effect[1]=="Damage":
        Damage=random.randint(1,7)
        if Temp_Effect[5]=="Weapon":
            Damage=random.randint(1,2)
        Temp_Effect[1]=str(Damage)+" Damage"

    if Temp_Effect[1]=="Heal":
        Heal=random.randint(1,7)
        Temp_Effect[1]=str(Heal)+" Heal"

    if Temp_Effect[1]=="Increase Cost":
        Increase=random.randint(1,5)
        Temp_Effect[1]="Increase Cost "+str(Increase)

    if Temp_Effect[1]=="Reduce Cost":
        Decrease=random.randint(1,5)
        Temp_Effect[1]="Reduce Cost "+str(Decrease)

    if Temp_Effect[2]=="Multiple":
        Targets=random.randint(2,3)
        Temp_Effect[2]=str(Targets)+" Multiple"

    if Temp_Effect[1]=="Give Atk":
        Atk=random.randint(1,4)
        Temp_Effect[1]="Give "+str(Atk)+" Atk"

    if Temp_Effect[1]=="Discard":
        Amount=random.randint(1,3)
        Temp_Effect[1]="Discard "+str(Amount)

    ##If Friendly##

    if Temp_Effect[4]=="Friendly":
        if "Damage" in Temp_Effect[1]:
            Temp_Cost+=Damage
        if Temp_Effect[1]=="Destroy": 
            if Temp_Effect[5]=="Weapon":
                Temp_Cost+=0
            else:
                Temp_Cost+=10
        #if Temp_Effect[1]=="Debuff":

        if "Increase Cost" in Temp_Effect[1]:
            Temp_Cost+=Increase

        if Temp_Effect[1]=="Counter":
            Temp_Cost+=5

        if Temp_Effect[1]=="Silence":
            Temp_Cost-=1


        if "Heal" in Temp_Effect[1]:
            Temp_Cost-=Heal
        #or Temp_Effect[1]=="Buff" or
        if "Reduce_Cost" in Temp_Effect[1]:
            Temp_Cost-=Decrease

        if "Atk" in Temp_Effect[1]:
            Temp_Cost-=int(Atk/2)

        if Temp_Effect[1]=="Draw":
            Temp_Cost-=2

        if "Discard" in Temp_Effect[1]:
            Temp_Cost+=2*Amount


    ##If Enemy##     

    if Temp_Effect[4]=="Enemy":
        if "Damage" in Temp_Effect[1]:
            Temp_Cost-=Damage
        if Temp_Effect[1]=="Destroy":
            if Temp_Effect[5]=="Weapon":
                Temp_Cost-=1
            else:
                Temp_Cost-=10
        #if Temp_Effect[1]=="Debuff":
        if "Increase Cost" in Temp_Effect[1]:
            Temp_Cost-=Increase
        if Temp_Effect[1]=="Counter":
            Temp_Cost-=5
        if Temp_Effect[1]=="Silence":
            Temp_Cost-=1
        if "Heal" in Temp_Effect[1]:
            Temp_Cost+=Heal
        #if Temp_Effect[1]=="Buff":
        if "Reduce_Cost" in Temp_Effect[1]:
            Temp_Cost+=Decrease
        if "Atk" in Temp_Effect[1]:
            Temp_Cost+=int(Atk/2)
        if Temp_Effect[1]=="Draw":
            Temp_Cost+=2


    ##If Any##
            
    if Temp_Effect[4]=="Any":
        if "Damage" in Temp_Effect[1]:
            if Temp_Effect[2] =="All":
                Temp_Cost-=int(Damage/2)
            else:
                Temp_Cost-=Damage
        if Temp_Effect[1]=="Destroy":
            Temp_Cost-=10
        if Temp_Effect[1]=="Silence":
            Temp_Cost-=1
        if "Atk" in Temp_Effect[1]:
            Temp_Cost-=int(Atk/2)

    ##Other##
    Tribes=Get_Tribes()
    if Temp_Effect[5] in Tribes:
        Temp_Cost=int(Temp_Cost*0.6)

    if Temp_Effect[0]=="Deathrattle":
        Temp_Cost=int(Temp_Cost*0.5)

    if Temp_Effect[0]=="Battlecry and Deathrattle":
        Temp_cost=int(Temp_Cost*1.5)

    if Temp_Effect[0]=="Inspire":
        Temp_Cost+=2

    if Temp_Effect[2]=="Multiple":
        if Temp_Effect[4]=="Any" and Temp_Effect[3]=="Random":
            Temp_Cost=Temp_Cost*Targets

        if Temp_Effect[4]!="Any":
            Temp_Cost=Temp_Cost*Targets

    if Temp_Effect[2]=="All" and Temp_Effect[4]!="Any":
        Temp_Cost=int(Temp_Cost*3.5)

    if Temp_Effect[0]=="Inspire" and Temp_Cost>2:
        Temp_Cost=0

    return Temp_Cost,Temp_Effect


def Text_Format(Text):      #A complex translator of sorts, turns a list of information into readable sentences and descriptions
                            #The most complicated and difficult part of the program, will be reworked in future
    #print(Text)
    #print(type(Text))
    TempList=[Text]
    #print(type(TempList))
    Text=""
    for Keyword in TempList:
        Temp_Text=""
        #print(Keyword)
        #print(type(Keyword))
        if type(Keyword) is str:#not list
            Temp_Text+=Keyword.replace("'","")
            Temp_Text+="."
        else:
            if Keyword[0]=="Choose One" or Keyword[0]=="Spell":
                pass
            else:
                Temp_Text+=str(Keyword[0])
                Temp_Text+=": "

            #Keyword 1
            
            if "Heal" in Keyword[1]:
                Temp_Text+="Restore "
                Temp_Text+=str(Keyword[1][0])
                Temp_Text+=" Health to "
            elif "Damage" in Keyword[1]:
                Temp_Text+="Deal "
                Temp_Text+=str(Keyword[1][0])
                Temp_Text+=" Damage to "
            elif "Reduce" in Keyword[1]:
                pass
            elif "Increase" in Keyword[1]:
                pass
            elif "Atk" in Keyword[1]:
                Temp_Text+="Give "
            elif "Discard" in Keyword[1] and Keyword[1][8] == 1:
                Temp=Keyword[1]
                Temp[8]="a"
                Temp_Text+=Temp
                Temp_Text+=" "
            elif "Draw" in Keyword[1] and Keyword[4]=="Enemy":
                Temp_Text+="Your Opponent Draws "
            else:
                Temp_Text+=Keyword[1]
                Temp_Text+=" " 
            if Keyword[2]=="All":
                if "Cost" in Keyword[1]:
                    Temp_Text+="All "
                else:
                    Temp_Text+="all "                    
            elif "Draw" in Keyword[1]:
                Temp_Text+="a "

            #Keyword 2
            elif Keyword[2]=="Single":
                if Keyword[4]=="Enemy" and Keyword[3]!="Random":
                    if Keyword[5]=="Hero" or Keyword[5]=="Weapon":
                        Temp_Text+="the "
                    else:
                        if "Cost" in Keyword[1]:
                            Temp_Text+="An "
                        else:
                            Temp_Text+="an "
                else:
                    if Keyword[4]=="Friendly":
                        if Keyword[5]=="Hero" or Keyword[5]=="Weapon":
                            if "Discard" in Keyword[1]:
                                Temp_Text+="random "
                            else:
                                Temp_Text+="your "
                        else:
                            if "Cost" in Keyword[1]:
                                Temp_Text+="A "
                            else:
                                Temp_Text+="a "
                    else:
                        if "Cost" in Keyword[1]:
                            Temp_Text+="A "
                        elif Keyword[4]=="Enemy":
                            if Keyword[5]=="Hero" or Keyword[5]=="Weapon":
                                Temp_Text+="the "
                            else:
                                Temp_Text+="a "
            elif "Multiple" in Keyword[2]:
                Temp_Text+=Keyword[2][0]
                Temp_Text+=" "

            else:
                Temp_Text+="a "

                
            if Keyword[3]=="Random" and Keyword[2] != "All" and Keyword[5]!="Hero":
                if Keyword[5]!="Weapon" or Keyword[2]=="Any":
                    Temp_Text+="random " 
            if Keyword[4]=="Enemy":
                if ("the" in Temp_Text) or ("your" in Temp_Text):
                    if Keyword[5]!="Hero":
                        Temp_Text+="enemy's "
                    elif Keyword[4]=="Enemy" and "Draw" in Keyword[1]:
                        pass
                    else:
                        Temp_Text+="enemy "
                elif Keyword[4]=="Enemy" and "Draw" in Keyword[1]:
                    pass
                else:
                    Temp_Text+="enemy "
            elif Keyword[4]=="Friendly" and Keyword[5]!="Hero" and Keyword[5]!="Weapon":
                Temp_Text+="friendly "

            if "Draw" in Keyword[1]:
                Keyword[5]="Card"
            elif "Discard" in Keyword[1]:
                if Keyword[1][8]==1:
                    Keyword[5]="Card"
                else:
                    Keyword[5]="Cards"
            Temp_Text+=Keyword[5]
            if Keyword[2]!="Single":
                Temp_Text+="s"

            if "Cost" in Keyword[1]:
                if "All" in Temp_Text:
                    Temp_Text+=" cost ("
                else:
                    Temp_Text+=" costs ("
                Temp_Text+=Keyword[1][len(Keyword[1])-1]
                Temp_Text+=") "
                if "Reduce" in Keyword[1]:
                    Temp_Text+="less "
                elif "Increase" in Keyword[1]:
                    Temp_Text+="more "
                Temp_Text+="next turn"

            if "Atk" in Keyword[1]:
                Temp_Text+=" +"
                Temp_Text+=str(Keyword[1][5])
                Temp_Text+=" Attack"

            if "Counter" in Keyword[1]:
                Temp_Text+=" next turn"

            Temp_Text+="."

        Text+=Temp_Text
        Text+=" "

    return Text




##Versatile##

def Battlecry(Card):
    #WIP
    Keyword="Battlecry:"
    Value=0
    return Keyword,Value

def Deathrattle(Card):
    #WIP
    Keyword="Deathrattle:"
    Value=0
    return Keyword,Value

def Inspire(Card):
    #WIP
    Keyword="Inspire:"
    Value=0
    return Keyword,Value

def Combo(Card):
    #WIP
    Keyword="Combo:"
    Value=2
    return Keyword,Value

def BattlecryAndDeathrattle(Card):
    #WIP
    Keyword="Battlecry and Deathrattle:"
    Value=3
    return Keyword,Value

def ChooseOne(Card):
    #WIP
    Keyword="Choose One:"
    Value=1
    return Keyword,Value


##Static##

def Overload(Card):
    Overload=random.randint(1,10)
    Keyword="Overload ("+str(Overload)+")"
    return Keyword , Overload*2

def Taunt(Card):
    Keyword="Taunt"
    Value=-1
    return Keyword, Value

def Charge(Card):
    Keyword="Charge"
    Value=-2.5
    return Keyword, Value

def Stealth(Card):
    Keyword="Stealth"
    Value=-1
    return Keyword, Value

def Divine_Shield(Card):
    Keyword="Divine Shield"
    Value=-2
    return Keyword, Value

def Windfury(Card):
    Keyword="Windfury"
    Value=-2
    return Keyword, Value

def Spell_Damage(Card):
    Keyword="Spell Damage +"
    Amount=random.randint(1,3)
    Keyword+=str(Amount)
    Value=-(2*Amount)
    return Keyword, Value

def Elusive(Card):
    Keyword="This minion cannot be targeted by Spells or Hero Powers"
    Value=int(Card.Mana*-0.6)
    return Keyword, Value

def Poisonous(Card):
    Keyword="Poisonous"
    Value=-2
    return Keyword, Value


##Utility Functions##

def Random_List(List):
    Item=List[random.randint(0,len(List)-1)]
    return Item

if __name__=="__main__":
    Types=["Minion","Spell"]
    Generate=True
    Setup=Card("All",[])
    S_Data=Setup.Evolve_Name_Setup()
    while Generate==True:
        for loop in range(20):
            Type=Random_List(Types)
            New_Card=Card(Type,S_Data)
            New_Card.Generate()
            New_Card.Dump()
            print("\n\n\n\n")
        Generate=bool(input("Press Enter to stop generating >>"))

#Letter Prediction Program Project (L3P)
try:
    import random, csv, os, time
except ImportError as E:
    print("A default python library is missing")
    print(E)

#NOTE: using the Hearthstone(HS) name data and Elite enabled tends to result in lots of words with 'er' in them since it is a very common combination


#Data Key
#Data= the raw data
#C_Data= data that has been properly formatted/compiled
#S_Data= a table containing a 'score' for each character combination
#I_Data= the initial data generated before mutation
#E_Data= encoded data, it is in binary form
#M_Data= mutated data, this is the data that has been 'evolved'/'mutated' via the Mutate() function
#O_Data= the old data

###Variables Passed into GetWord()
##Population= the number of individuals in each generation
##S_Data= Score data(see above)
##Generations= the number of generations the program will cycle through before picking a result
##Export= For most purposes this will be False, it is used to export details about how the average individual's score changes across generations
##Mutate_Rate= how often mutations occur in an individual
##Elite= If set to True, the individual with the best score will always survive to the next generation

##Program Overlook
##DataError()= a custom error that is used to pick up issues with any data given to the program 
##HSImport()= tries to import the standard reference libraries, if any are missing an error message is displayed for each

class DataError(Exception): #An error that is used to flag any issues with the data given to the program
    def __init__(self, value):
        self.value=value
    def __str__(self):
        return self.value
    def Detail(self):
        print("A Data Error Has Occured:",self.value)

def HSImport(): #tries to import the standard reference libraries, if any are missing an error message is displayed for each
    Sets=[]
    try:
        import Set_Basic
        Sets.append(Set_Basic)
    except ImportError as E: #if the library file cannot be found (does this for all 'sets')
        print(E)
    try:
        import Set_Classic
        Sets.append(Set_Classic)
    except ImportError as E:
        print(E)
    try:
        import Set_Naxxramus
        Sets.append(Set_Naxxramus)
    except ImportError as E:
        print(E)
    try:
        import Set_GvG
        Sets.append(Set_GvG)
    except ImportError as E:
        print(E)
    try:
        import Set_BlckMT
        Sets.append(Set_BlckMT)
    except ImportError as E:
        print(E)
    try:
        import Set_TGT
        Sets.append(Set_TGT)
    except ImportError as E:
        print(E)
    try:
        import Set_LoE
        Sets.append(Set_LoE)
    except ImportError as E:
        print(E)
    try:
        import Set_WotOG
        Sets.append(Set_WotOG)
    except ImportError as E:
        print(E)
    try:
        import Set_Kara
        Sets.append(Set_Kara)
    except ImportError as E:
        print(E)
    try:
        import Set_MSG
        Sets.append(Set_MSG)
    except ImportError as E:
        print(E)
    return Sets


def DataSet(): #a default data set containing names
    Sets = HSImport()
    print("Importing Static Data Set...")
    Data_Raw=[]
    for Set in Sets:
        Data_Raw+=Set.Minions()
    Data_Names=[]
    for x in range(len(Data_Raw)): #the raw data is a 2d array and so this loop retrieves the required information from the array and puts it in a list
        Name=Data_Raw[x][6]
        Data_Names.append(Name)

    Data_Raw=[]
    for Set in Sets:
        Data_Raw+=Set.Spells()   
    for x in range(len(Data_Raw)): #the raw data is a 2d array and so this loop retrieves the required information from the array and puts it in a list
        Name=Data_Raw[x][3]
        Data_Names.append(Name)

    Data_Raw=[]
    for Set in Sets:
        Data_Raw+=Set.Weapons()    
    for x in range(len(Data_Raw)): #the raw data is a 2d array and so this loop retrieves the required information from the array and puts it in a list
        Name=Data_Raw[x][5]
        Data_Names.append(Name)
        
    return Data_Names

def DataSetText(): #a default data set containing descriptions
    Sets = HSImport()
    print("Importing Static Data Set...")
    Data_Raw=[]
    for Set in Sets:
        Data_Raw+=Set.Minions()
    Data_Names=[]
    for x in range(len(Data_Raw)): #the raw data is a 2d array and so this loop retrieves the required information from the array and puts it in a list
        Name=Data_Raw[x][4]
        Data_Names.append(Name)

    Data_Raw=[]
    for Set in Sets:
        Data_Raw+=Set.Spells()
    for x in range(len(Data_Raw)): #the raw data is a 2d array and so this loop retrieves the required information from the array and puts it in a list
        Name=Data_Raw[x][2]
        Data_Names.append(Name)

    Data_Raw=[]
    for Set in Sets:
        Data_Raw+=Set.Weapons()      
    for x in range(len(Data_Raw)): #the raw data is a 2d array and so this loop retrieves the required information from the array and puts it in a list
        Name=Data_Raw[x][4]
        Data_Names.append(Name)
        
    return Data_Names

def Compile(Data): #formats the data so that it can be used to generate score data by the program
    #the C_Data variable is a 2D array and looks like this;
    #[["W","o","r","d"],
    # ["N","a","m","e"],
    # ["e","t","c","."]]
    if __name__=="__main__":
        print("Compiling...")
    try: #does basic checks to makes sure the data given can actually be used
        if type(Data)!=list:
            raise DataError("Given Data is not a list!")
        elif len(Data)==0:
            raise DataError("Data is empty!")       
        for count in range(len(Data)-1):
            if len(str(Data[count]))<2:
                raise DataError("Data cannot contain single characters!")
                
    except DataError as E:
        E.Detail()
        return False
        
    C_Data=[]
    count=0
    for word in Data:
        Data[count]=" "+str(word)
        count+=1

    count=0
    for word in Data: #splits each item in the data set into a list
        C_Data.append([]) #creates an array
        try:
            for character in word:
                C_Data[count].append(character)#converts the string into a list of characters
        except TypeError: #if the data is not a string
            string=str(word) #convert it to a string
            for character in string:
                C_Data[count].append(character)#converts the string into a list of characters
        count+=1
    return C_Data #returns the formatted data

def Score(C_Data):#creates a set of data which contains letter combination scores
    #the S_Data variable is a 3D array, to help visualise it use the 'DisplaySData' function once score data has been generated
    if __name__=="__main__":
        print("Scoring...")
        Start=time.clock()#the process is timed to help get an idea of how practical a data set of a certain size is to process
    try:
        for name in C_Data:
            for char in name:
                if len(char)!=1:#checks that the data has been formatted properly
                    raise DataError("Data is not Compiled!") #if not the program cannot use the given data
    except DataError as E:
        E.Detail()
        return False #aborts trying to create score data
    #The Boundry Unicode Values the program will use
    Lower=32 
    Upper=127

##New, way better system##
    S_Data=[]
    for CharOne in range(Lower,Upper):#range is the number for ASCII characters,
                                      #Unicode could be used but would increase the data size massively with little gain in terms of usefulness
        #CharOne is the number for the first character in the 2 character combination
        S_Data.append([])
        for CharTwo in range(Lower,Upper):#same range and same reason as CharOne
            #CharTwo is the number for the second charcater in the 2 character combination
            Score=0#each score has a default value of 1, if it doesn't show up in the data set it has a very small chance of being generated
            S_Data[CharOne-Lower].append([chr(CharTwo),Score])

    for Word in C_Data:
        Pos=0
        for Letter in Word:
            try:
                S_Data[ord(Letter)-Lower][ord(Word[Pos+1])-Lower][1]+=10
            except IndexError:
                S_Data[ord(Letter)-Lower][0][1]+=10 #The word is considered to end in a space, because this is true for every word the score increase is smaller
            Pos+=1

##Old, inefficient system##
##    S_Data=[]
##    for CharOne in range(Lower,Upper):#range is the number for ASCII characters,
##                                      #Unicode could be used but would increase the data size massively with little gain in terms of usefulness
##                                      #CharOne is the number for the first character in the 2 character combination
##        S_Data.append([])
##        for CharTwo in range(Lower,Upper):#same range and same reason as CharOne
##            #CharTwo is the number for the second charcater in the 2 character combination
##            Score=0#each score has a default value of 0, if it doesn't show up in the data set it will not be generated
##            for Name in C_Data:#for each name/word in C_Data
##                Pos=0#This is the position(list index) of the letter currently being checked by the program
##                for CharC in Name:
##                    if CharC==chr(CharOne):#if the character whose table is being written is the same as being checked 
##                        try:
##                            if Name[Pos+1]==chr(CharTwo):#if the next character in the word is CharTwo
##                                Score+=1 #then there is an occurence of a CharOne CharTwo combination and it's score is increased
##                        except ValueError and IndexError:#if the letter is the last letter do nothing
##                            pass
##                    Pos+=1
##            
##            Score=Score*100
##            if CharTwo==32:#if the character is space 
##                Score=int(Score/2)#this is because space is present in every words and prevents the program being too heavily biased towards it
##            S_Data[CharOne-Lower].append([chr(CharTwo),Score])#add CharTwo's entry in the CharOne table

    if __name__=="__main__":
        print("Scoring Complete")
        print("Time Taken=",(time.clock()-Start))
    return S_Data

def DisplaySData(S_Data): #dispay the scored data (3d array)
    count=32
    for CharOne in S_Data:
        print(chr(count)+"'s Table")
        for CharTwo in CharOne:
            print(CharTwo)
        count+=1

def GenWord(S_Data): #responsible for generating a word for the initial set
    word=" "
    Score=0
    Ignore=True
    Finished=False
    Count=0
    while not Finished:
        if Count >100: #prevents the program getting 'stuck'
            print("Word reached max length")
            Finished=True
        Pos=ord(word[len(word)-1])-32 #character's score table location in 3d array
        if Pos==0 and Ignore==False: #if the character is a space and it is not the first space the word is finished
            Finished=True
        if Finished==False: #if the word is not finished
            try:
                Letter,TempScore=Select_Char(S_Data,Pos)
                ##print("Letter:",Letter)
            except TypeError: #error does not seem to occur anymore
                print("Letter",Letter)
                print("Letter Type",type(Letter))
                print("TempScore",TempScore)
                print("TempScore",type(TempScore))
            word+=str(Letter) #add the letter on the end of the word
            Score+=TempScore #add the letters score to the word's score
            if Ignore==True: #ignore only the first space
                Ignore=False
        Count+=1
    word=word[1:] #remove the first space
    return word,Score
    


def Select_Char(S_Data,Pos): #responsible for selecting the next caracter in a word for the initial set
    Valid=False
    Count=0
    while not Valid:
        if Count>100:
            print("Failed to select character")
            return "",0 #if it fails to get a valid character return blank with a score of 0
        Score_Total=0
        for loop in range(len(S_Data[Pos])):#calculates a total of all word scores
            Score_Total+=S_Data[Pos][loop][1]

        #wheel-of-fortune-esque selection system    
        pick=random.randint(0,Score_Total) 
        current=0
        for CharTwo in S_Data[Pos]:
            current+=CharTwo[1]
            if current > pick:
                if CharTwo[0]!=None:
                    return CharTwo[0],CharTwo[1]
        Count+=1
    

def GenISet(S_Data,Pop,Refresh,Epoch): #generates the initial set
    if __name__=="__main__" and not Refresh:
        print("Generating Words...")
    if __name__=="__main__" and Refresh:
        print("Gen",str(Epoch),"stale, introducing new members...")
    Words=[]
    Scores=[]
    for loop in range(Pop):
        Valid=False
        while not Valid:
            Word,Score=GenWord(S_Data)
            Word=Word.replace(" ","")
            try:
                Scores.append(int(Score/len(Word)))
                Valid=True
            except ZeroDivisionError:
                if __name__=="__main__":
                    print("Word with length zero was generated")
                    pass
        Words.append(Word)
    return Words,Scores

def DisplaySet(Set,Scores): #displays initial set
    print()
    print("Words:")
    for Pos in range(len(Set)):
        print(Set[Pos],Scores[Pos])


def Lookup(Lib): #contains dictionaries for converting to and from binary strings, almost entirely uninteresting
    if Lib=="Decode":#from binary to ASCII
        Library={"0000000":" ","0000001":"!","0000010":'"',"0000011":"#","0000100":"$","0000101":"%","0000110":"&","0000111":"'","0001000":"(","0001001":")","0001010":"*","0001011":"+","0001100":",","0001101":"-","0001110":".","0001111":"/","0010000":"0","0010001":"1","0010010":"2","0010011":"3","0010100":"4","0010101":"5","0010110":"6","0010111":"7","0011000":"8","0011001":"9","0011010":":","0011011":";","0011100":"<","0011101":"=","0011110":">","0011111":"?","0100000":"@","0100001":"A","0100010":"B","0100011":"C","0100100":"D","0100101":"E","0100110":"F","0100111":"G","0101000":"H","0101001":"I","0101010":"J","0101011":"K","0101100":"L","0101101":"M","0101110":"N","0101111":"O","0110000":"P","0110001":"Q","0110010":"R","0110011":"S","0110100":"T","0110101":"U","0110110":"V","0110111":"W","0111000":"X","0111001":"Y","0111010":"Z","0111011":"[","0111100":"\\","0111101":"]","0111110":"^","0111111":"_","1000000":"`","1000001":"a","1000010":"b","1000011":"c","1000100":"d","1000101":"e","1000110":"f","1000111":"g","1001000":"h","1001001":"i","1001010":"j","1001011":"k","1001100":"l","1001101":"m","1001110":"n","1001111":"o","1010000":"p","1010001":"q","1010010":"r","1010011":"s","1010100":"t","1010101":"u","1010110":"v","1010111":"w","1011000":"x","1011001":"y","1011010":"z","1011011":"{","1011100":"|","1011101":"}","1011110":"~"}
    if Lib=="Encode":#from ASCII to binary
        Library={" ":"0000000","!":"0000001",'"':"0000010","#":"0000011","$":"0000100","%":"0000101","&":"0000110","'":"0000111","(":"0001000",")":"0001001","*":"0001010","+":"0001011",",":"0001100","-":"0001101",".":"0001110","/":"0001111","0":"0010000","1":"0010001","2":"0010010","3":"0010011","4":"0010100","5":"0010101","6":"0010110","7":"0010111","8":"0011000","9":"0011001",":":"0011010",";":"0011011","<":"0011100","=":"0011101",">":"0011110","?":"0011111","@":"0100000","A":"0100001","B":"0100010","C":"0100011","D":"0100100","E":"0100101","F":"0100110","G":"0100111","H":"0101000","I":"0101001","J":"0101010","K":"0101011","L":"0101100","M":"0101101","N":"0101110","O":"0101111","P":"0110000","Q":"0110001","R":"0110010","S":"0110011","T":"0110100","U":"0110101","V":"0110110","W":"0110111","X":"0111000","Y":"0111001","Z":"0111010","[":"0111011","\\":"0111100","]":"0111101","^":"0111110","_":"0111111","`":"1000000","a":"1000001","b":"1000010","c":"1000011","d":"1000100","e":"1000101","f":"1000110","g":"1000111","h":"1001000","i":"1001001","j":"1001010","k":"1001011","l":"1001100","m":"1001101","n":"1001110","o":"1001111","p":"1010000","q":"1010001","r":"1010010","s":"1010011","t":"1010100","u":"1010101","v":"1010110","w":"1010111","x":"1011000","y":"1011001","z":"1011010","{":"1011011","|":"1011100","}":"1011101","~":"1011110"}
    return Library

def Mutate(Set,Scores,Population,S_Data,Epoch,Mutate_Rate,Elite): #Responsible for generating a new population based on the previous one
    if Elite:
        BestScore=0
        count=-1
        for score in Scores:
            count+=1
            if score > BestScore: #finds the best word (best being highest score)
                BestScore=score
                BestPos=count
        try:
            BestWord=[Set[BestPos],Scores[BestPos]]
        except IndexError:
            if __name__=="__main__":
                print("Set len",len(Set),"Scores len",len(Scores),"BestPos",BestPos) 

    Library=Lookup("Encode") #ASCII to Binary
    E_Data=[]
    for Item in Set:
        Temp=str()
        for Char in Item:
            Temp+=Library[Char] #translate the string into a binary string
        E_Data.append(Temp)

    M_Data=[]
    M_Scores=[]
    if Elite:
        PopLimit=Population-1
    else:
        PopLimit=Population
    while len(M_Data)<(PopLimit):
        Valid=False
        while not Valid:
            try:
                Pos=Mutate_Wheel(Scores)
                Items=[E_Data[Pos]]
                Valid=True
            except TypeError:
                pass
        Stored=[E_Data[Pos],Scores[Pos]]      
        E_Data.pop(Pos) #prevents it from picking the same string twice
        Scores.pop(Pos) #removes the words associated score
        Valid=False
        while not Valid:
            try:
                PosTwo=Mutate_Wheel(Scores)
                Items.append(E_Data[PosTwo])
                Valid=True
            except TypeError:
                pass
        E_Data.append(Stored[0])
        Scores.append(Stored[1])

        First=random.randint(0,1)
        if First==0:
            Last=1
        else:
            Last=0

        SepPosOne=random.randint(0,len(Items[First])-1)
        SepPosTwo=random.randint(0,len(Items[Last])-1)
        Length=SepPosOne+(len(Items[Last])-SepPosTwo)
        M_Item=str()
        for loop in range(Length): 
            if loop >= SepPosOne:
                try:
                    M_Item+=str(Items[Last][loop-SepPosOne])
                except IndexError:
                    print(len(Items[First]))
                    print(len(Items[Last]))
                    print(Length)
                    print("Crash:",loop)
                    
            else:
                M_Item+=str(Items[First][loop])                      
        M_List=list(M_Item)
        for loop in range(len(M_List)):
            if random.uniform(0,1) < Mutate_Rate:
                if M_List[loop]=="0":
                    M_List[loop]="1"
                elif M_List[loop]=="1":
                    M_List[loop]="0"
        
        M_Item=str()
        for Binary in M_List:
            M_Item+=Binary
            
        Count=0
        Temp=str()
        Temp_Item=[]
        for Bin in M_Item:
            if Count%7==0 and Count !=0:
                Temp_Item.append(Temp)
                Count=0
                Temp=str()
            Temp+=Bin
            Count+=1
            Storage=Temp
        Temp_Item.append(Storage)

        Item=Decode(Temp_Item)

        if len(Item)>0:
            M_Data.append(Item)
            Score=Score_Word(Item,S_Data)
            M_Scores.append(Score)

    if Elite:
        M_Data.append(BestWord[0])
        M_Scores.append(BestWord[1])
       
    Stale=False #checks if the population has 'gone stale' and is too homogenous
    for anotherloop in Scores:
        if M_Scores.count(anotherloop) >= int((len(M_Scores)/100)*30): #if over 60% of candidates have the same score
            Culprit=anotherloop #the common score
            Stale=True
            break
            
    if Stale:
        Percent=int((len(M_Scores)/100)*20)
        PossibleSwaps=[]
        for loop in range(len(M_Scores)):
            if M_Scores[loop]==Culprit:
                PossibleSwaps.append(loop)
        Swaps=[]
        for loop in range(Percent):
            Selected=random.randint(0,len(PossibleSwaps)-1)
            Swaps.append(PossibleSwaps[Selected])
            PossibleSwaps.pop(Selected)

        NewWords,NewScores=GenISet(S_Data,Percent,True,Epoch)

        for loop in range(len(Swaps)):
            M_Data[Swaps[loop]]=NewWords[loop]
            M_Scores[Swaps[loop]]=Score_Word(NewWords[loop],S_Data)
            
    return M_Data, M_Scores
    
def Score_Word(Word,S_Data): #Scores a Generated word
    ListWord=list(Word) #converts the word to a list so it can be read/manipulated easier
    ListWord.append(" ")
    Score=0
    for Position in range(len(ListWord)-1):
        Layer=ord(ListWord[Position])-32
        Row=ord(ListWord[Position+1])-32
        Score+=S_Data[Layer][Row][1] #checks the score for the two letter combination in the Score Data
    ListWord.pop(len(ListWord)-1)
    if len(Word) == 1: #single chracters tend not to be words and can show up too often
        Score=0.1
    elif len(Word)<4: #words less than 4 characters long tend to be rarer
        Score=int(Score/(len(Word)*2))
    elif len(Word) <= 12: #average word length
        Score=int(Score/len(Word))
    else: #not many words ar longer than 12 charracters
        Score=int(Score/(len(Word)*2))
    Score=int(Score*10) #increases the difference in score between words, so a difference of 1 becomes a difference of 10, this helps better words get selected more often 
    return Score

def Decode(Temp_Item): #decodes an item
    Library=Lookup("Decode") #Binary to ASCII
    Item=str()
    for Series in Temp_Item:
        try:
            Item+=Library[Series]
        except KeyError:
            Item+=""
    return Item


def Mutate_Wheel(Scores): #selects a word based on it's score using a wheel of fortune style system
    UsingWheel=True
    while UsingWheel:
        Score_Total=0
        for loop in range(len(Scores)):
            Score_Total+=Scores[loop]
        if Score_Total==0: #this is used when all words have a score of zero, an unlikely occurence but a possible one (due to mutations).
            return random.randint(0,len(Scores)-1)
        pick=random.randint(0,Score_Total)
        current=0
        for Pos in range(len(Scores)-1):
            current+=Scores[Pos]
            if current > pick:
                return Pos

def ManualCycle(Population,S_Data,Mutate_Rate,Elite=False,Export=False): #It has Elite Disabled by Default
    #If users want to see the words change generation by generation to gain an understanding of how the program works then they should use this function
    #if not then they should use GetWord

    #functions in pretty much the same way as GetWord except it asks the user what they would like to do
    Continue=True
    while Continue:
        Epoch=0
        I_Set,Scores=GenISet(S_Data,Population,False,Epoch) #creates an initial set
        print("Epoch:",Epoch) #epoch refers to the number of genrations so far
        DisplaySet(I_Set,Scores)
        NewEpoch=True
        O_Set=I_Set
        while NewEpoch:
            Epoch+=1
            try:
                M_Set,Scores=Mutate(O_Set,Scores,Population,S_Data,Epoch,Mutate_Rate,Elite) #creates a new generation
            except DataError as E:
                print("A Data Error Has Occured:",E.value)
            print()
            print()
            print("Epoch:",Epoch)
            print("New Set")
            DisplaySet(M_Set,Scores) #displays the new Generation
            O_Set=M_Set
                            
            Valid=False
            while not Valid: #validation for user input
                try:
                    print("Advance an Epoch?")
                    print("1) Yes")
                    print("2) No")
                    print()
                    Hold=int(input(">>"))
                    if Hold==1 or Hold==2:
                        Valid=True
                    else:
                        print("Please select one of the available options.")
                except ValueError:
                    print("Please select one of the available options.")

            if Hold==2:
                NewEpoch=False

        Valid=False
        while not Valid: #validation for user input
            try:
                print("Start with new initial set?")
                print("1) Yes")
                print("2) No")
                print()
                Hold=int(input(">>"))
            except ValueError:
                print("Please select one of the available options.")
            if Hold==1 or Hold==2:
                Valid=True
        if Hold==1:
            Continue=True
            
        elif Hold==2:
            Continue=False

def PercentDone(WordProgress): #displays how close a word is to being finished (to 1 decimal place)
    print("Word",str(round(WordProgress,4))+"% complete.")

def GetWord(Population,S_Data,Generations,Mutate_Rate,Elite=False,Export=False):
    WordProgress=0.00
    if __name__=="__main__":
        PercentDone(WordProgress)
    if Export==True: #if information about the generations is being exported
        FileName="BenchMark.csv"
        ExportData=[] #a list of the average that generation
        ExportHigh=[] #a list of the highest that generation
        Path='./'+FileName
        Open=False
        while not Open:
            try:
                if os.path.isfile(Path): #checks if the file exists already
                    File=open(FileName,'a') #if it exists it is appended too
                    
                else:
                    File=open(FileName,'w') #if not it is created
                Open=True
            except PermissionError:
                    print(FileName,"is currently unavailable, please close any other programs using the file.")
                    input("Press enter to retry.")
        FileWriter=csv.writer(File)
    Epoch=0
    I_Set,Scores=GenISet(S_Data,Population,False,Epoch) #creates an initial set
    WordProgress+=5
    if __name__=="__main__":
        PercentDone(WordProgress)
    O_Set=I_Set
    for loop in range(Generations):
        Epoch+=1
        try:
            M_Set,Scores=Mutate(O_Set,Scores,Population,S_Data,Epoch,Mutate_Rate,Elite) #create new set from old set
        except DataError as E:
            if __name__=="__main__":
                print("A Data Error Has Occured:",E.value)
            pass
        O_Set=M_Set #new set replaces old set as the new 'old set'
        WordProgress+=90/Generations #percent is based on total number of generations requested
        if __name__=="__main__":
            PercentDone(WordProgress)
        if Export==True:
            total=0
            Highest=0
            for number in Scores:
                total+=number
                if number > Highest: #finds the highest score that generation
                    Highest=number
            Average=total/len(Scores) #calculates average score of that generation
            
            ExportData.append(Average) #stores average
            ExportHigh.append(Highest) #stores highest
        
        if Epoch==Generations: #if last genration
            HighestScore=0
            HighestPosition=0
            for Item in range(len(M_Set)):
                if Scores[Item]>HighestScore: #find location of highest scoring word
                    HighestScore=Scores[Item]
                    HighestPosition=Item
    Word=M_Set[HighestPosition] #store highest scoring word
    if Export==True: #if being exported, export data
        FileWriter.writerow(ExportData)
        FileWriter.writerow(ExportHigh)
    WordProgress+=5
    if __name__=="__main__": #if L3P is being imported then return the word
        PercentDone(WordProgress)

    if __name__=="__main__":
        Word=[M_Set[HighestPosition],Scores[HighestPosition],len(M_Set[HighestPosition])] #if not imported return extra information
    else:
        Word=M_Set[HighestPosition]
    
    return Word

def Benchmark(): #A standard 'benchmark' test
    Population=100 #amount of individuals per generation
    Data=DataSet()
    C_Data=Compile(Data)
    S_Data=Score(C_Data)
    Generations=100 #number of times the program creates a new population
    Mutate_Rate=0.001 #the chance of a random mutations occuring
    Export=False
    Words=[]
    Elite=False #enables/disables elitist selection
    for loop in range(10): #creates 10 words
        Word=GetWord(Population,S_Data,Generations,Mutate_Rate,Elite,Export)
        Words.append(Word) #add the word to list of words

    for word in Words: #display list of words
        print(word)

    
if __name__=="__main__": #run Benchmark if not being imported  
    Benchmark()
    

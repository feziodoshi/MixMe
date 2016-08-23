import re
import random


myLibRap={}
myLibShakes={}
myLib={}
myLib[1]=myLibShakes
myLib[0]=myLibRap
##################################################################
###############getting data for the RAP #####################
f=open('allLyrics.txt','r')
allWords=f.read()
allWords=re.sub('\n',' \n ',allWords)
allWords=allWords.split(' ')
#######################################################
print'done1'

##############making the dataset ######################
start=0
end=len(allWords)-1
for i in range(start,end):
    current_word=allWords[i].lower()
    next_word=allWords[i+1].lower()
    if current_word not in myLibRap.keys():
        myLibRap[current_word]={next_word:1}
    else:
        if next_word not in myLibRap[current_word].keys():
            myLibRap[current_word][next_word]=1
        else:
            myLibRap[current_word][next_word]+=1

#####################################################

            
print'done2'
for c_word in myLibRap.keys():
    tot=0.0
    for n_word in myLibRap[c_word].keys():
        tot+=myLibRap[c_word][n_word]
    for n_word in myLibRap[c_word].keys():
        myLibRap[c_word][n_word]=myLibRap[c_word][n_word]/tot


##############################################################
##############################################################

################################################################
###############getting data for the TRUMP #####################
f=open('shakespeare.txt','r')
allWords=f.read()
allWords=re.sub('\n',' \n ',allWords)
allWords=allWords.split(' ')
#######################################################


##############making the dataset ######################
start=0
end=len(allWords)-1
for i in range(start,end):
    current_word=allWords[i].lower()
    next_word=allWords[i+1].lower()
    if current_word not in myLibShakes.keys():
        myLibShakes[current_word]={next_word:1}
    else:
        if next_word not in myLibShakes[current_word].keys():
            myLibShakes[current_word][next_word]=1
        else:
            myLibShakes[current_word][next_word]+=1

#####################################################

print'done2'
for c_word in myLibShakes.keys():
    tot=0.0
    for n_word in myLibShakes[c_word].keys():
        tot+=myLibShakes[c_word][n_word]
    for n_word in myLibShakes[c_word].keys():
        myLibShakes[c_word][n_word]=myLibShakes[c_word][n_word]/tot

#######################################################
########################################################

print'suppppper'
start_sent='be'

song=start_sent
length_song=10
chk=0
curr=start_sent
nextt=''
t=0
while(chk<length_song):
    add_curr=''
    for i in range(2):
        if(curr not in myLib[t].keys()):
            word=random.choice(myLib[t].keys())
            if(i==1):
                add_curr=word
            nextt+=' '+ word
        else:
            base_prob=random.uniform(0.0,1.0)
            chk_prob=0.0
            for word in myLib[t][curr].keys():
                chk_prob+=myLib[t][curr][word]
                if(chk_prob>=base_prob):
                    if(i==1):
                        add_curr=word
                    nextt+=' '+word
                    break
        
    if(t==0):
        t=1
    else:
        t=0
    song+=' '+nextt+' '
    curr=add_curr
    chk+=1
    
print song
##voices=engine.getProperty('voices')
##engine.setProperty('rate',100)
##print'addddd'
##engine.setProperty('voice',voices[9].id)
##print'kladqibwd'
##engine.say(song[:160])
##engine.runAndWait()

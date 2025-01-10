import random 
import time


class Kumanda():

    def __init__(self,tv_status="close",tv_audio=0,chanel_list=["trt"],chanel="trt"):
        self.tv_status=tv_status
        self.tv_audio=tv_audio
        self.chanel_list=chanel_list
        self.chanel=chanel

# bu iki def fonksiyonunda tv_statüsü inceledik 
    def open_tv(self):
        if (self.tv_status == "open"):
            print("already open")
        
        else:
            print("tv is opening...")
            self.tv_status = "open"

    def close_tv(self):
        if ( self.tv_status =="close"):
            print("Already close")

        else:
            print("Tv is closeing")
            self.tv_status ="close"


    #şimdi ise tv_audio kısmının fonksiyonlarını yapacağız
            
    
    def audio_settings(self):
        while True:
            answer=input("Audio close : '<'\nAudio open '>'\nExit='Exit'")
            
            if (answer == "<"):
                if (self.tv_audio !=0):
                    self.tv_audio=self.tv_audio - 1
                    print("New audio:",self.tv_audio)

            elif (answer == ">"):
                if (self.tv_audio < 32):
                    self.tv_audio=self.tv_audio + 1
                    print("New audio:",self.tv_audio)
            
            else:
                print("Audio is updateing",self.tv_audio)
                break


    #şimdi ise kanal listesi kısmını inceleyeceğiz  


    def add_chanel(self,chanel_name):
        print("Chanel is adding")
        time.sleep(1)
        self.chanel_list.append(chanel_name)
        print("Chanel added.")



    #bastığımız tuş ile kanalımız rastgele bir kanala geçicek şimdi inceleyelim
        
    
    def random_chanel(self):
        random=random.randint(0,len(self.chanel_list - 1))

        self.chanel=self.chanel_list(random)

        print("Current chanel:",self.chanel)


    #temel fonksiyonlarımızı şu ana kadar tamamladık şimdi özel fonks kullanacağız
     

    def __len__(self):

        return len(self.chanel_list)  #özel metod ile kanal listesi uzunluğunu elde ederiz
    



    def __str__(self):

        return ("TV Status:{}\nTV Audio:{}\nChanel List:{}\nChanel:{}".format(self.tv_status,self.tv_audio,self.chanel_list,self.chanel))
    
    #kumanda sınıfımızı bitirdik şimdi bunu kullanmaya dökeceğiz

kumanda=Kumanda()

print("""
TV PROGRAM
1-Open TV
2_Close TV
3-Audio Settings
4-Add Chanel
5-Total Chanel
6-Go Random Chanel
7-İnformation TV

Exit the push 'q'

          
          """)


#yukarıda giriş ekranımızı tasarladık
    

while True:
    process=input("Dial the process:")

    if (process=="q"):

        print("Program ending")
        break


    elif (process == "1"):
        c=kumanda.open_tv()
        
    
    elif(process == "2"):
        c=kumanda.close_tv()
        


    elif(process== "3"):
        c=kumanda.audio_settings()
        

    
    elif (process=="4") :

        chanel_name=input("Enter channel names separated by commas:")#kanal isimlerini virgülle ayırarak girin

        chanel_list=chanel_name.split(",")#kanal isimlerini virgülle ayırık liste yaptık

        for i in chanel_list:
            kumanda.add_chanel(i)
            

        
    elif (process== "5"):
        c=len(kumanda)
        print("Total Chanel:",c)


    
    elif (process == "6"):

        c=kumanda.random_chanel()
        print(c)


    elif (process == "7"):
        print(kumanda)

    
    else:
        print("Wrong dialing")






        



    








            


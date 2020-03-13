import os 
import time 
from selenium import webdriver
import pickle

lab=input('What lab do you want to upload (ex: 1,2,3) :')
print('**************************************************************************')
row=input('\nPlease count\nHow many these "[add new file]" are up to your lab(inclusive): ')
if(int(lab)<10):
    labName='lab0'+lab
else:
    labName='lab'+lab  

print(labName)

# function that takes the login information from the txt file 
def information():
    mylines=[]
    with open ('info.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
        for myline in myfile:    
         mylines.append(myline)             # For each line, read it to a string 
    folderpath=mylines[0].split()    
    username=mylines[1].split()   #taking the username and password
    password=mylines[2].split()
    myfile.close()
    return username[1],password[1],folderpath[1]

#login varialbes and folder path
username,password,folderPath=information()

#Connecting to the website 
#moving the os path where the txt files are located
os.chdir(folderPath)
fileName=os.listdir()
driver=webdriver.Chrome('chromedriver')
driver.get('https://helios.utcluj.ro/learn2code/login.php?SID')
try:
    usernameInput=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/div/table/tbody/tr[1]/td[2]/input')
    usernameInput.send_keys(username)
    passwordInput=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/div/table/tbody/tr[2]/td[2]/input')
    passwordInput.send_keys(password)
    loginBtn=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/div/table/tbody/tr[4]/td/button')
    loginBtn.click()
except:
    print("An error occured!, Please try again")

#after login selecting the lab you want 
try:
    workarea=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/div/table/tbody/tr[3]/td')
    workarea.click()
    print('The ',labName,' is selected')
        
    time.sleep(3)
    extension='.txt'
    try:
            for elements in fileName:
                if(labName in elements and extension in elements):
                    add_link=driver.find_elements_by_class_name('href2')
                    add_link[int(row)-1].click()
                    link=folderPath+'\\'+elements
                    uploadBtn=driver.find_element_by_class_name('input1').send_keys(link)
                    save=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/div/table/tbody/tr[7]/td/button')
                    save.click()
                    print(elements,' was uploaded!')              
    except:
        print("Error! Run again!")   
except:
    print("Error!")
exit
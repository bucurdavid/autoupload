#!/usr/bin/env python
import os 
import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys

lab=input('In wich lab do you want to upload (ex: 1,2,3) :')
print('**************************************************************************')
def lab_name():
    if(lab=='lab'):
        labName = lab
        return labName
    if(int(lab)<10):
        labName='lab0'+lab
        return labName
    else:
        labName='lab'+lab  
        return labName
 



print('We are selecting the ',lab_name(),' problems!')

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

username,password,folderPath=information()

def login(username,password):
    usernameInput=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/div/table/tbody/tr[1]/td[2]/input')
    usernameInput.send_keys(username)
    passwordInput=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/div/table/tbody/tr[2]/td[2]/input')
    passwordInput.send_keys(password)
    loginBtn=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/div/table/tbody/tr[4]/td/button')
    loginBtn.click()

if __name__ == "__main__":
    #login varialbes and folder path
    #Connecting to the website 
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://helios.utcluj.ro/learn2code/login.php?SID')
    actualURL='https://helios.utcluj.ro/learn2code/login.php?SID'
    try:
        print("Loging in....")
        login(username,password)
        if(driver.current_url==actualURL):
            print("\n You are not logged in!\n Plese reset the program and verify your account information in 'info.txt'")
            sys.exit()
        workarea=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/div/table/tbody/tr[3]/td')
        workarea.click()
        time.sleep(2)

        checked_upload=driver.find_elements_by_class_name('href1')
        for items in checked_upload:
            check=items.text
            print(check)

        answer=input('\nDo you want to continue?[y/n]: ')
        if(answer=='y'):
            #after login selecting the lab you want 
            try:
                row=input('\n_____________________Please count______________________\nHow many these "[add new file]" are up to your lab(inclusive): ')
                #add_link[int(lab)].click()
                print('The ',lab_name(),' is selected')
                    #moving the os path where the txt files are located
                extensions='.txt'
                os.chdir(folderPath)
                fileName=os.listdir()
                actualURL='https://helios.utcluj.ro/learn2code/work_area.php?SID'
                try:
                    for elements in fileName:
                        if(lab_name() in elements and extensions in elements):
                            add_link=driver.find_elements_by_class_name('href2')
                            add_link[int(row)-1].click()
                            link=folderPath+'\\'+elements
                            uploadBtn=driver.find_element_by_class_name('input1').send_keys(link)
                            save=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/div/table/tbody/tr[7]/td/button')
                            save.click()
                            if(driver.current_url==actualURL):
                                print(elements+" was uploaded!")                
                except:
                    print("Error! Run again!")  
                    sys.exit()
            except:
                print("Error!Maybe the lab dosn't exist!")
                sys.exit()
        else:
            sys.exit()
    except:
        print("Error!")                
sys.exit()
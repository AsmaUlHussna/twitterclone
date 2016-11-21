import csv

#First username+pass to make things easier to read
userpass = {"Bill": "123"}


#Read usernames and passwords from CSV file
with open('userandpass.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        userpass[row[0]] = row[1]
    print userpass

#Get User and Pass for login
login_username = raw_input('Enter your username: ')
login_password= raw_input('Enter your password: ')

#Check if Username and Password match what is in userandpass.csv, then proceed to program
if userpass.has_key(login_username):
    if userpass[login_username]==login_password:
        print('Thank you for logging in')

        print ("------------------------------------")
        print ("############## -------- ############")
        print("######## THIS IS YOUR TWEETS ########")
        print ("############## -------- ############")
        print ("------------------------------------")


        #create blank list of followers for the user
        userfollows = []

        #Read followers of the user that is logged in (login_username)
        with open('followdb.csv') as csvfile:
            readCSV = csv.reader(csvfile,delimiter=',')
            for row in readCSV:
                if (row[0] == login_username):
                    print "Hi " + login_username + " , lets try to get your followers"
                    userfollows = row
                    userfollows.pop(0)
                    userfollows.insert(0,login_username)




        print userfollows
        print "blah"



        #Print tweet if user is following
        for who in userfollows:
            with open('tweets.csv') as csvfile:
                readCSV = csv.reader(csvfile,delimiter=',')
                for row in readCSV:
                    if (who == row[0]):
                        print "@" + who + ": " + row[1]







    else:
        print('Wrong password.')
else:
    print('Your username or password is incorrect.')

#Register maybe?

#!/usr/bin/python

same = False
kind = raw_input("Register Or Login:")
database = open("user_database.txt", 'a+') #Open user_database.txt type append and read
#REGISTER
if(kind == 'register'):
   uname = raw_input("Enter username:")
   for l in database:
      lineList = l.split()
      if(uname == lineList[0]):#lineList[0] is Username
         print 'Failed: username"'+uname+'" is already taken.'
         same = True

   if(same == False):
      upass = raw_input("Enter Password:")
      database.write(uname+" "+upass+"\n") #append in user_database.txt
      print "Success Created new account"
#LOGIN
else:
   found = False
   uname = raw_input("Enter username:")
   upass = raw_input("Enter password:")
   for l in database:
      lineList = l.split()
      if (uname == lineList[0]):#lineList[0] is Username
         found = True
         if(upass == lineList[1]):#lineList[1] is Password
            print'Success: Username "'+uname+'" has already logged in'
         else :
            print 'Fail: Your password is incorrect.'
   if(not found):
      print 'Fail: No user data.'
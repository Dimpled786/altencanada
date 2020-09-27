import os
import smtplib
  
  if os.system("which java"):
       # It will check whether Java is installed or not
	   # If yes it will print the version otherwise it will install it
         print("Path: ")
         print(os.system("which java"))
         print("Java Version: ")
         print(os.system("java -version"))

  else:
    
	     print("Java not found")

         os.system("pip install urllib3")
         cookie = 'Cookie'
         license = 'oraclelicense=accept-securebackup-cookie'
         url = 'http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-windows-x64.exe'
         filename = 'jdk-8u131-windows-x64.exe'
         opener = urllib2.build_opener()
         opener.addheaders.append((cookie, license))
         f = opener.open(url)
         with open(filename, 'wb+') as save:
         save.write(f.read())
	
	#For alias in "BASH SRC"
    # alias python=python3	
	
	# sending status Via Email
	port = 2525
	smtp_server = "smtp.mailtrap.io"
	login = "xxxx"
	password = "xxxx"
	
	sender = "dimpygogna5@gmail.com"
	receiver = "dimple_d786gmail.com"
	
	message = f"""\
	Subject:  Status	
	Status has been succesfuly Updated."""
	
	try:
	     with smtplib.SMTP(smtp_server, port) as server:
	         server.login(login,password)
		     server.sendmail(sender, receiver, message)
			 print('sent')
     
    except smtplib.SMTPException as e:
        print('Error Occured: '+str(e) )	
	
	
	



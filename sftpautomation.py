import paramiko
import ftplib
import pyodbc
import os, string,sys

'''python script to automate downloads of new files from different folders by comparing files in the server directories to local directories using paramiko module.
And then run stored procedures on SQL Server through pyodbc connection''' 
#jinsei-no-gakusei

def getSData():
	host = "data.com"
	port = 2222
	transport = paramiko.Transport((host, port))

	# Auth
	password = "23658557"
	username = "blah"
	transport.connect(username = username, password = password)

	# Go!
	sftp = paramiko.SFTPClient.from_transport(transport)
	sftp.chdir('.')
	
	
	#sftp directories and files
	efiles = sftp.listdir('//EData')
	schdatafiles = sftp.listdir('//SchData')
	
	
	#local directories and files
	
	localschdatafiles = os.listdir(r"C:\Sch\Schd\SchDataFolder")
	
	
	#compare files in directories and download new files from sftp folders to local folders -- 
	#could use python's filecmp as alternative
	
	deltaschdatafiles = set(schdatafiles) - set(localschdatafiles)
	deltaschdatafiles = list(deltaschdatafiles)
	
	
	
	#open connection to sql server
	conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=HData;UID=myusername;PWD=mypassword')
	cursor = conn.cursor()
	count = 0
	
	#loop through the new files
	#download the new files and open each file and run stored proc
	for s in deltaschdatafiles:
		slocal_schdatafilename = os.path.join(r"C:\Raw_Data\SWGA\ScheduleDataFolder",s)
		sftp.get('//ScheduleData/' + s, slocal_schdatafilename)
		cursor.execute("""exec SP_Upsert_Data ?""",b)
		cursor.commit()
		#count = count + 1
		#print count
		
	sftp.close()
	transport.close()
	
	conn.close()
	

	return
getSData()


__author__ = 'xdyang'

# Import required python libraries
import os
import time
import tarfile


print "###################################################"
print "# This python script has features show below."
print "# Please select feature:"
print "# 0. Exit python script, press 0"
print "# 1. Backup database, press 1"
print "# 2. Archive your database before today, press 2"
print "###################################################"

# Database Configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_USER_PASSWORD = 'mysql.rzrk'
DB_NAME = 'ttmgrportal'
BACKUP_PATH = '/home/dbbackup/'

# Getting current datetime to create seprate backup folder like '20161018-141830'
TODAY = time.strftime('%Y%m%d')
DATETIME = time.strftime('%Y%m%d-%H%M%S')

select = raw_input('Enter your selection --> ')

if select == "0":
    exit()
elif select == "1":
    TODAYBACKUPPATH = BACKUP_PATH + TODAY
    BACKUPNAME = DB_NAME + DATETIME
    # Checking if backup folder already exists or not. If not exists will create it.
    print "Checking File Path..."
    if os.path.exists(TODAYBACKUPPATH):
        print "File already exist, done."
    else:
        print "Creating backup folder..."
        os.makedirs(TODAYBACKUPPATH)
    print "done."

    dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " > " + TODAYBACKUPPATH + "/" + BACKUPNAME + ".sql"
    result = os.system(dumpcmd)

    if result != 0:
        print "Backup Fail. Error info is:"
        print result
    else:
        print "Backup script completed."
        print "Your backups has been created in '" + TODAYBACKUPPATH + "' directory."

elif select == "2":
    if not os.path.exists(BACKUP_PATH):
        os.makedirs(BACKUP_PATH)
    tarPath = BACKUP_PATH + DB_NAME + ".tar.gz";
    items = os.listdir(BACKUP_PATH)
    for item in items:
        if item != TODAY:
            fullpath = os.path.join(BACKUP_PATH, item)
            if os.path.isdir(fullpath):
                if not os.path.exists(tarPath):
                    commend = "tar cvf " + tarPath + " " + fullpath;
                    result = os.system(commend)
                    print("commend: " + commend)
                    if result != 0:
                        print result
                    else:
                        print(item + " has been add to compressed file.")
                        os.system("rm -rf " + fullpath)
                else:
                    commend = "tar rvf " + tarPath + " " +fullpath;
                    result = os.system(commend)
                    print("commend: " + commend)
                    if result != 0:
                        print result
                    else:
                        print(item + " has been add to compressed file.")
                        os.system("rm -rf " + fullpath)

    print "Archive script completed."
    print "All your files has been added to " + BACKUP_PATH + DB_NAME + ".tar.gz"

else:
    print 'Wrong Input, program exit.'
    exit();
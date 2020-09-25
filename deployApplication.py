#!/usr/bin/python
# Author : Divya Kashyap
# Save Script as : deployApplication.py

import time
import getopt
import sys
import re

# Get location of the properties file.
properties = ''
try:
   opts, args = getopt.getopt(sys.argv[1:],"p:h::",["properies="])
except getopt.GetoptError:
   print 'set_datasource.py -p <path-to-properties-file>'
   sys.exit(2)
for opt, arg in opts:
   if opt == '-h':
      print 'set_datasource.py -p <path-to-properties-file>'
      sys.exit()
   elif opt in ("-p", "--properties"):
      properties = arg
print 'properties=', properties

# Load the properties from the properties file.

from java.io import FileInputStream
 
propInputStream = FileInputStream(properties)
configProps = Properties()
configProps.load(propInputStream)

# Set all variables from values in properties file.
adminUsername=configProps.get("admin.username")
adminPassword=configProps.get("admin.password")
adminURL=configProps.get("admin.url")
apppkg=configProps.get("apppkgfile")
appname=configProps.get("appname")
domainhome=configProps.get("domainhome")
appdir=configProps.get("appdir")
adminport=configProps.get("adminport")



# Connect to the AdminServer.
connect(adminUsername, adminPassword, adminURL)

edit()
startEdit()

deploy(appname, appdir + '/' + apppkg)

save()
activate()

disconnect()
exit()

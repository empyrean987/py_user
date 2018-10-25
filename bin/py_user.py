#!/usr/bin/env python
import argparse
import pwd
import os
parser = argparse.ArgumentParser(description="Add Delete List Users")
parser.add_argument("-k", "--key", help="Add User & SSH  key, use -k and -a together")
parser.add_argument("-a", "--add", help="Add User & SSH Key, use -k and -a together")
parser.add_argument("-d", "--delete", help="Delete User")
parser.add_argument("-l", "--list", action="store_true", help='list users')
args = parser.parse_args()

def add_user(user, key):
  try:
    all_users = pwd.getpwall()
    if user in str(all_users):
      print "User already exists"
    else:	
      os.system("mkdir -p /home/"+user+"/.ssh")
      path_split = key.split("/")
      key_file = path_split[-1]
      os.system("cp "+key+" /home/"+user+"/.ssh/authorized_keys")
      os.system("chmod 644 /home/"+user+"/.ssh/authorized_keys")
      os.system("useradd -d /home/"+user+" "+user)
      os.system("chown -R "+user+":"+user+" /home/"+user+"/")
      os.system("chown root:root /home/"+user)
      os.system("chmod 700 /home/"+user+"/.ssh")
      print "User has been added"
  except Exception, e:
    print "Issue Creating users Exception: "+str(e)

def delete_user(user):
  try:
    os.system("deluser --remove-home "+user)
  except Exception, e:
   print "Issue Deleteing users Exception: "+str(e)

def list_user():
  try:
    users = pwd.getpwall()
    for u in users:
      print "User_Name:"+u.pw_name+", UID:"+str(u.pw_uid)+", Comments:"+str(u.pw_gecos)
  except Exception, e:
    print "Issue listing users Exception: "+str(e)


if args.list:
  list_user()
elif args.key and args.add:
  add_user(args.add, args.key)
elif args.delete:
  delete_user(args.delete)
else:
  print "Use --help option to show Arguments"

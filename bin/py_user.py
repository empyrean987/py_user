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

def add_user():
  try:
    os.system("useradd foo")
  except Exception, e:
    print "Issue Creating users Exception: "+str(e)

def delete_user():
  try:
    os.system("deluser foo")
    print "bah"
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
  add_user()
elif args.delete:
  delete_user()
else:
  print "Use --help option to show Arguments"

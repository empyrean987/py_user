# BUILD IMAGE
We are using the base Ubuntu 16.0.4 image given by Amazon with the following script ran on it to create new AMI. No special python modules needed to be installed into this image.
To Build this AMI used the following process to build it.

apt-get update

apt-get -y install python-pip

pip install aws-ec2-assign-elastic-ip

apt-get -y install awscli

apt-get -y install cloud-utils

TODAYSDATE=`date +'%Y-%m-%d-%s'`

EC2_INSTANCE_ID=$(ec2metadata --instance-id)

aws ec2 create-image --instance-id $EC2_INSTANCE_ID --name UBUNTU-16.04-${TODAYSDATE} --description "Ubuntu 16.04 ${TODAYSDATE}" --no-reboot --region us-west-2

To deploy this repository you can clone it on the AMI above or base ubuntu 16.04 image from Amazon. You can also use the terraform deployment or chef deployment described in the following two repos.

https://github.com/empyrean987/chef_user

https://github.com/empyrean987/Terraform/tree/master/user_test/mgmt_blue


# ADD

root@ip-192-168-0-133:~/py_user/bin# cd /home/ubuntu/

root@ip-192-168-0-133:~# mkdir rsa

root@ip-192-168-0-133:~# cd rsa

root@ip-192-168-0-133:~/rsa# ssh-keygen -a 1000 -b 4096 -C "" -E sha256 -o -t rsa

Generating public/private rsa key pair.

Enter file in which to save the key (/root/.ssh/id_rsa): /home/ubuntu/rsa/user_test

Enter passphrase (empty for no passphrase):

Enter same passphrase again:

Your identification has been saved in /home/ubuntu/rsa/user_test.

Your public key has been saved in /home/ubuntu/rsa/user_test.pub.

The key fingerprint is:

SHA256:MpAtHN2dp+sL+Yx49iwbNdAlseGmrDlmkI9H8B/d2vk

The key's randomart image is:
+---[RSA 4096]----+
|    .. . .+o.    |
|   . +. .oo=.    |
|    * . . =o     |
|     * . =..     |
|    o = S +..    |
|     = * +.+ .   |
|    . O =.. o    |
|     + o+B.  .   |
|      .oo+*.  E  |
+----[SHA256]-----+

root@ip-192-168-0-133:~/rsa# cd /home/ubuntu/py_user/bin

root@ip-192-168-0-133:~/py_user/bin# ./py_user.py -a usertest -k /home/ubuntu/rsa/user_test.pub

User has been added


# DELETE

root@ip-192-168-0-133:~/py_user/bin# ./py_user.py -d usertest

Looking for files to backup/remove ...

Removing files ...

Removing user `usertest' ...

Warning: group `usertest' has no more members.

Done.


# LIST

root@ip-192-168-0-133:~/py_user/bin# ./py_user.py -l

User_Name:root, UID:0, Comments:root

User_Name:daemon, UID:1, Comments:daemon

User_Name:bin, UID:2, Comments:bin

User_Name:sys, UID:3, Comments:sys

User_Name:sync, UID:4, Comments:sync

User_Name:games, UID:5, Comments:games

User_Name:man, UID:6, Comments:man

User_Name:lp, UID:7, Comments:lp

User_Name:mail, UID:8, Comments:mail

User_Name:news, UID:9, Comments:news

User_Name:uucp, UID:10, Comments:uucp

User_Name:proxy, UID:13, Comments:proxy

User_Name:www-data, UID:33, Comments:www-data

User_Name:backup, UID:34, Comments:backup

User_Name:list, UID:38, Comments:Mailing List Manager

User_Name:irc, UID:39, Comments:ircd

User_Name:gnats, UID:41, Comments:Gnats Bug-Reporting System (admin)

User_Name:nobody, UID:65534, Comments:nobody

User_Name:systemd-timesync, UID:100, Comments:systemd Time Synchronization,,,

User_Name:systemd-network, UID:101, Comments:systemd Network Management,,,

User_Name:systemd-resolve, UID:102, Comments:systemd Resolver,,,

User_Name:systemd-bus-proxy, UID:103, Comments:systemd Bus Proxy,,,

User_Name:syslog, UID:104, Comments:

User_Name:_apt, UID:105, Comments:

User_Name:lxd, UID:106, Comments:

User_Name:messagebus, UID:107, Comments:

User_Name:uuidd, UID:108, Comments:

User_Name:dnsmasq, UID:109, Comments:dnsmasq,,,

User_Name:sshd, UID:110, Comments:

User_Name:pollinate, UID:111, Comments:

User_Name:ubuntu, UID:1000, Comments:Ubuntu

User_Name:john.doe, UID:1001, Comments:John Doe

User_Name:usertest, UID:1002, Comments:
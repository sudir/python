python 'docker_install' do
  code <<-EOH
''' Stage 1: Importing dependency modules'''

import os
import yum
yb = yum.YumBase()


''' Stage 2: Determining if Docker is already installed '''

if yb.rpmdb.searchNevra(name='docker'):


   print "Docker is already installed, take no action"


else: 


  ''' Stage 3: Setting TimeZone & Running Kernel Upgrades '''
  os.system('rm -fr /etc/localtime')
  os.system('ln -s /usr/share/zoneinfo/America/New_York /etc/localtime')
  os.system("sed -i 's/exclude=kernel*/#exclude=kernel*/g' /etc/yum.conf")
  os.system('yum update -y')



  ''' Stage 4: Installing docker-engine 1.12 and writing configuration files '''
  f = open("/etc/yum.repos.d/docker.repo","w")
  f.write("""
[dockerrepo]
name=Docker Repository
baseurl=https://yum.dockerproject.org/repo/main/centos/7/
enabled=1
gpgcheck=1
gpgkey=https://yum.dockerproject.org/gpg

""")  
  os.system('yum install -y docker')
 
  f = open("/etc/sysconfig/docker","w")
  f.write("""
# Modify these options if you want to change the way the docker daemon runs
OPTIONS='--selinux-enabled'

DOCKER_CERT_PATH=/etc/docker

# If you want to add your own registry to be used for docker search and docker
# pull use the ADD_REGISTRY option to list a set of registries, each prepended
# with --add-registry flag. The first registry added will be the first registry
# searched.

OPTIONS="--insecure-registry sldcinfdtrt01.mcms.isl.red.ihost.com"

# If you want to block registries from being used, uncomment the BLOCK_REGISTRY
# option and give it a set of registries, each prepended with --block-registry
# flag. For example adding docker.io will stop users from downloading images
# from docker.io
# BLOCK_REGISTRY='--block-registry'

# If you have a registry secured with https but do not have proper certs
# distributed, you can tell docker to not look for full authorization by
# adding the registry to the INSECURE_REGISTRY line and uncommenting it.
# INSECURE_REGISTRY='--insecure-registry'

# On an SELinux system, if you remove the --selinux-enabled option, you
# also need to turn on the docker_transition_unconfined boolean.
# setsebool -P docker_transition_unconfined 1

# Location used for temporary files, such as those created by
# docker load and build operations. Default is /var/lib/docker/tmp
# Can be overriden by setting the following environment variable.
# DOCKER_TMPDIR=/var/tmp

# Controls the /etc/cron.daily/docker-logrotate cron job status.
# To disable, uncomment the line below.
# LOGROTATE=false
""")

  f = open("/usr/lib/systemd/system/docker.service","w")
  f.write(""" 
# Custom_Config
[Unit]
Description=Docker Application Container Engine
Documentation=http://docs.docker.com
After=network.target

[Service]
Type=notify
EnvironmentFile=-/etc/sysconfig/docker
EnvironmentFile=-/etc/sysconfig/docker-storage
EnvironmentFile=-/etc/sysconfig/docker-network
Environment=GOTRACEBACK=crash
ExecStart=/usr/bin/docker daemon $OPTIONS \
          $DOCKER_STORAGE_OPTIONS \
          $DOCKER_NETWORK_OPTIONS \
          $ADD_REGISTRY \
          $BLOCK_REGISTRY \
          $INSECURE_REGISTRY
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
TimeoutStartSec=1min
# set delegate yes so that systemd does not reset the cgroups of docker containers
Delegate=yes
# kill only the docker process, not all processes in the cgroup
KillMode=process

[Install]
WantedBy=multi-user.target
""")

  f = open("/etc/docker/daemon.json","w")
  f.write("""{
    "graph": "/data/docker",
    "storage-driver": "overlay",
    "log-driver": "json-file",
    "log-opts": {
      "max-size": "10m"
    }
    }""")

  f = open("/etc/sysconfig/docker-network","w")
  f.write("""
  	DOCKER_NETWORK_OPTIONS=""
  	""")

  ''' Stage 5: Connecting to DTR '''
  os.system('curl -k https://dtr-556876752.us-east-1.elb.amazonaws.com/ca -o /etc/pki/ca-trust/source/anchors/dtr-556876752.us-east-1.elb.amazonaws.com.crt && update-ca-trust')
 

  ''' Final: setting run levels & permissions on essential services '''
  os.system('chkconfig docker on')
  os.system('systemctl disable firewalld')
  os.system('service firewalld stop')
  os.system('chkconfig firewalld off')
  os.system('systemctl stop docker.service')
  os.system('chown midouser:docker /data')
   
    EOH
end

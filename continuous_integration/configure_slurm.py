# This file is taken from the Pulsar project
# (https://github.com/galaxyproject/pulsar) which is apache 2.0
#


from socket import gethostname
from string import Template
from subprocess import call
from getpass import getuser

SLURM_CONFIG_TEMPLATE = '''
# slurm.conf file generated by configurator.html.
# Put this file on all nodes of your cluster.
# See the slurm.conf man page for more information.
#
ControlMachine=$hostname
#ControlAddr=
#BackupController=
#BackupAddr=
#
AuthType=auth/munge
CacheGroups=0
#CheckpointType=checkpoint/none
CryptoType=crypto/munge
MpiDefault=none
#PluginDir=
#PlugStackConfig=
#PrivateData=jobs
ProctrackType=proctrack/pgid
#Prolog=
#PrologSlurmctld=
#PropagatePrioProcess=0
#PropagateResourceLimits=
#PropagateResourceLimitsExcept=
ReturnToService=1
#SallocDefaultCommand=
SlurmctldPidFile=/var/run/slurmctld.pid
SlurmctldPort=6817
SlurmdPidFile=/var/run/slurmd.pid
SlurmdPort=6818
SlurmdSpoolDir=/tmp/slurmd
SlurmUser=$user
#SlurmdUser=root
#SrunEpilog=
#SrunProlog=
StateSaveLocation=/tmp
SwitchType=switch/none
#TaskEpilog=
TaskPlugin=task/none
#TaskPluginParam=
#TaskProlog=
InactiveLimit=0
KillWait=30
MinJobAge=300
#OverTimeLimit=0
SlurmctldTimeout=120
SlurmdTimeout=300
#UnkillableStepTimeout=60
#VSizeFactor=0
Waittime=0
FastSchedule=1
SchedulerType=sched/backfill
SchedulerPort=7321
SelectType=select/linear
#SelectTypeParameters=
AccountingStorageType=accounting_storage/none
#AccountingStorageUser=
AccountingStoreJobComment=YES
ClusterName=cluster
#DebugFlags=
#JobCompHost=
#JobCompLoc=
#JobCompPass=
#JobCompPort=
JobCompType=jobcomp/none
#JobCompUser=
JobAcctGatherFrequency=30
JobAcctGatherType=jobacct_gather/none
SlurmctldDebug=3
#SlurmctldLogFile=
SlurmdDebug=3
#SlurmdLogFile=
NodeName=$hostname CPUs=1 State=UNKNOWN
PartitionName=debug Nodes=$hostname Default=YES MaxTime=INFINITE State=UP
'''


def main():
    template_params = {"hostname": gethostname(), "user": getuser()}
    config_contents = Template(SLURM_CONFIG_TEMPLATE).substitute(template_params)
    open("/etc/slurm-llnl/slurm.conf", "w").write(config_contents)
    call("slurmctld")
    call("slurmd")

if __name__ == "__main__":
    main()

#script to kill a command


node default{


exec {'kill_process':
command  => 'pkill  killmenow',
provider => 'shell',
}
}
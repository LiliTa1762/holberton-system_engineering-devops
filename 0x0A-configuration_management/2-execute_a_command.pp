# Manifest that kills a process 
exec {'To kill a process':
  command  => 'pkill -9 -f killmenow',
  provider => 'shell',
}

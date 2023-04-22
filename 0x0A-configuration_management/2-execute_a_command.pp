#Killing A Process

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}

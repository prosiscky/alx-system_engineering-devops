# A script that increase the limit of cuncurrent tasks
file { '/etc/default/nginx':
  ensure  => file,
  content => "ulimit -n 4096\n",
}

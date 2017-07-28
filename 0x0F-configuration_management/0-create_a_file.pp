#  create a file in /tmp
file { '/tmp/holberton':
  ensure     => file,
  path       => '/tmp/holberton',
  permission => '0744',
  owner      => 'www-data',
  group      => 'www-data',
  contains   => 'I love Puppet',
}

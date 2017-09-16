# Adding user holberton
exec { 'change-os-configuration-for-holberton-user':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/g" /etc/security/limits.conf; \
  sed -i "s/holberton soft nofile 4/holberton soft nofile 4000/g" /etc/security/limits.conf;',
}

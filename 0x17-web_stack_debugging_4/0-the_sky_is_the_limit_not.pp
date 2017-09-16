# Reducing th number of requests failed, by increasing Limit of requests
exec { 'increase limit of requests':
  path    => '/usr/bin/:/usr/sbin/:/bin/',
  command => 'sed -i \"s/ULIMIT=\"-n 15"/ULIMIT=\"-n 15000\"/g" /etc/default/nginx; service nginx restart',
}

# Modify max open files limit setting
exec { 'modify max open files limit setting':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/usr/sbin:/bin',
}

# Restart Nginx service
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}

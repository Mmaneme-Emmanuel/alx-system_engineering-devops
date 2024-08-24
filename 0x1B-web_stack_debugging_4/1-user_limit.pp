# Increase the hard file limit for the 'holberton' user
exec { 'increase-hard-file-limit-holberton-user':
  command => 'sed -i "/^holberton hard nofile/s/^[0-9]*\s\+[0-9]*\s\+/\nholberton hard nofile 50000\n/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/bin'],
}

# Increase the soft file limit for the 'holberton' user
exec { 'increase-soft-file-limit-holberton-user':
  command => 'sed -i "/^holberton soft nofile/s/^[0-9]*\s\+[0-9]*\s\+/\nholberton soft nofile 50000\n/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/bin'],
}

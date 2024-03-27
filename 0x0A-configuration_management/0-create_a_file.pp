#Using Puppet, create a file in /tm
file { '/tmp/school':
  ensure  => file,             # Ensure that it's a file
  mode    => '0744',           # Set file permissions to 0744
  owner   => 'www-data',       # Set owner to www-data
  group   => 'www-data',       # Set group to www-data
  content => 'I love Puppet',  # Set file content
}

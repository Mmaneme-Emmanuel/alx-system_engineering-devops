#Using Puppet, install flask from pip3.
#Requirements:Install flask, Version must be 2.1.0

package { 'python3-pip':  # Ensure pip3 (Python package installer) is installed
  ensure => installed,
}

exec { 'install_flask':  # Use exec resource to execute pip3 command to install Flask
  command => '/usr/bin/pip3 install Flask==2.1.0',  # Install Flask version 2.1.0
  path    => ['/usr/bin'],  # Set the path to include pip3
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',  # Check if Flask is already installed at the desired version
  require => Package['python3-pip'],  # Ensure python3-pip package is installed before installing Flask
}

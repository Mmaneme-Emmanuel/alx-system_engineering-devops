# Puppet code that fixes a wordpress web 5XX error  to 200 is ok

#The mistyped .phpp has been editted in the /var/www/html/wp-settings.php file

exec { 'fix-wordpress-server-error':
	command => 'sed -i \'s/phpp/php/g\' /var/www/html/wp-settings.php',
	path    => '/usr/local/bin/:/bin/',
}

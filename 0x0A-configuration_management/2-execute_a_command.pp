#2-execute_a_command.pp
exec { 'killmenow_process':
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true,
  onlyif      => '/usr/bin/pgrep killmenow',
  logoutput   => true,
}

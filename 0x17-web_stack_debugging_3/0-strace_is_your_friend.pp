# command to fix php problem for debugging AD

exec { 'resource title':
command  => '/usr/bin/env sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}

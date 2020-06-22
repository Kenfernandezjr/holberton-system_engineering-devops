#script to increase limit
exec { 'increase':
  command => '/bin/sed -i "s/15/4000/g" /etc/default/nginx && sudo service nginx restart'
}
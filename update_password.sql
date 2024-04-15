ALTER USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
UPDATE mysql.user SET authentication_string = PASSWORD('hbnb_dev_pwd') WHERE user = 'hbnb_dev' AND host = 'localhost';
FLUSH PRIVILEGES;

ALTER USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'Pass@123' REPLACE 'hbnb_dev_pwd';

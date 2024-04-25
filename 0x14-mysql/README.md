0x14. MySQL

Task 0
Check if you already have mysql installed:
$ mysql --version

You should see something like this:
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
If it says mysql server not installed or If you saw another version apart from 5.7
Then you will have to purge the already installed version(any version than 5.7),

then you will have to install it with(also the same for uninstalling/purging the previous version):

Update the package

$ sudo apt update


Install mysql server package

$ sudo apt install mysql-server-5.7

If you get this kind of feedback:

Package mysql-server-5.7 is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source
However the following packages replace it:
  mariadb-server-10.3

E: Package 'mysql-server-5.7' has no installation candidate


Then it means:
 that the package mysql-server-5.7 is not available in your package repository.

Then you will have to use this command to fetch the repo and install it as well.

$ sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 &&  sudo ./mysql57


It will take you through some options, if you don’t know which to choose, just select:
Ubuntu bionic

Select OK

Then input a password, and confirm password.
This should get you set up.

You can start mysql server with:

$ sudo service mysql start

To check if it is running

$ sudo service mysql status

Task 1:

On your web-01

1]
Use this command to login to mysql server to create a user:

$ mysql -u root -p

2]
To create a user and give it the necessary permission.


$ CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
$ GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

Here, it means whenever you intend to work as holberton_user, the password will always be projectcorrection280hbtn

3]
Flush privileges to save and apply changes:

$ FLUSH PRIVILEGES;

4]
To exit
$ EXIT;

Now do the same for web-02

On your terminal(without opening mysql server), you can check for the permission on the new user you created with this command

$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"

You will be prompted to enter a password, note that the password is for the new user, and not the root user, so the password should be projectcorrection280hbtn

This should show you something like:

+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
+-----------------------------------------------------------------+


Task 2
a]
Creating a database:
To create a database, we first open mysql server with root
$ sudo mysql -uroot -p

Enter the password to root, and then create a database name tyrell_corp

$ CREATE DATABASE tyrell_corp;

After creating the database, we have to use the database to create a table, or rather create a table inside the database, to do that, we use:

$ USE tyrell_corp;

B]
Creating a table:
Now that we are in the database, we have to create a table with at least a row and a column;

$ CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));

Nexus6 is the name of the table, id and name are columns in the table, the INT for id means integer, AUTO_INCREMENT means we don’t need to add values to id as it increases itself for every row automatically, PRIMARY KEY means it is the connector for every row in the table. For the name, VARCHAR means the value for the name is of type character(utf-8).
C]
Adding values to a table;
After creating a table with a row and a column, next we add some values to it.

$ INSERT INTO nexus6 (name) VALUES ('leon');
Remember that id will increase by itself, so we only need to add value to name, by doing so, the table will have ‘1’ in the id, and ‘leon’ in the name.
D]
Giving necessary permission to holberton_user;
Next is to give permission on the database and table to the holberton_user to have executive privileges on the database and table.

$ GRANT ALL PRIVILEGES ON *.* TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn' WITH GRANT OPTION;

And flush privileges;

$ FLUSH PRIVILEGES;

After this, you can exit.
And test with:
$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
It should prompt you for the holberton_user password, once you enter the correct password, you would see something like this similar table:

+----+------+
| id | name |
+----+------+
|  1 | leon |
+----+------+

Now do the same for the other web server.


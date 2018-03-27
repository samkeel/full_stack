# Logs analysis

Udacity Logs Analysis project.

## Project Overview

This project is about practicing with data that could have come from a
real-world web server log, including fields such HTTP status codes, articles
and authors.

## Configuration

- Install Virtual box and Vagrant using the default installation options.
- Download the supplied VM Configuration - [FSND-Virtual-Machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip).
- Use a Unix-style terminal, Git Bash is recommended.
- Bring Vagrant online by executing the following commands.
```
vagrant up
vagrant ssh
/vagrant
```

1. Download the mock database [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
2. Unzip the 'newsdata.zip' file and place the 'newsdata.sql' file in the 
    /vagrant shared folder.
3. Populate the database by running the SQL file.
```
psql -d news -f newsdata.sql
```

## Running

- Run the program by running news.py:
```
Python news.py
```

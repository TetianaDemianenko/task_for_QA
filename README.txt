Description how to use code
============================================

Create a folder on your computer and download all files in it.
Open the command terminal and navigate to this directory:
	
	$ cd pathname


*Python task
---------------------------------------------

To verify that all endpoints (methods) on server work as expected follow these steps

1) install library Requests for Python:
 	 
	$ python -m pip install requests

2) install library Redis for Python:
	
	$ python -m pip install redis

3) generate the database to Redis (run file generate_data_for_redis.py):
	
	$ python generate_data_for_redis.py

4) execute the tests of verification methods on the server (run file test_server_methods.py):
	
	$ python test_server_methods.py

On the terminal you will see the results of tests



*Datamining task
---------------------------------------------

To count # and % of successful requests per hour from datamining.log

1)Give execute permission to script datamining_analyze_new.sh:
	
	$ chmod +x datamining_analyze_new.sh

2)Run script datamining_analyze_new:

	$ ./datamining_analyze_new.sh

3)In the directory where you are located results.txt file will be created
  Read file and view the results: 
	
	$ cat results.txt



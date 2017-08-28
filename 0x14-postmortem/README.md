### Postmortem - new Nginx server configured with wrong port on the load balancer 

* On August 25th, 2017 we started recieving alerts that our pages were displaying error messages.
  * Outage lasted 22 minutes. It started at 7:46 AM PST and ended at 8:08 AM PST 
  * The root of the problem was that our new server was not added to load balancer with the correct port. It affected about 33% of our customers. The pages were not loading CSS pages.
  * Config file had port 80 instead of 8080 for the new server

* Timeline:
  * 7:46 AM - there was and alert that traffic was not going through our new server
  * 7:47 AM - SRE on call was notified
  * 7:48 AM - on call SRE pinged URL address to confirm that the webserver is running
  * 7:50 AM - SRE ran ```service nginx status``` and got ```nginx is running```
  * 7:52 AM - pinged load balancer 3 times and got 404 error message on the last one
  * 7:55 AM - got a hold of the sysadmin who set up the load balancer for the server before deployment
  * 8:01 AM - sysadmin updated load balancer config file with correct port and restarted the service
  * 8:08 AM - server was back up and running

* Root cause and resolution:
  * it was ran with a script that by default has a port setup to 80 but the server was running on port 8080
  * sysadmin had to modify haproxy.cfg file manually

* Corrective and preventative measures:
  * script needs to be updated so that it asks for the port when it's ran
  * all the servers should be set up with the script as to avoid big differences and prevent these kind of mistakes from happening

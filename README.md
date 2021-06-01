# UOCIS322 - Project 6 #


Brevet time calculator with AJAX, MongoDB, and a RESTful API!

* Use the boilerplate given in DockerRestAPI folder, and create the following three basic APIs:
    * "http://<host:port>/listAll" should return all open and close times in the database
    * "http://<host:port>/listOpenOnly" should return open times only
    * "http://<host:port>/listCloseOnly" should return close times only

* Design two different representations: one in csv and one in json. For the above, JSON should be your default representation for the above three basic APIs. 
    * "http://<host:port>/listAll/csv" should return all open and close times in CSV format
    * "http://<host:port>/listOpenOnly/csv" should return open times only in CSV format
    * "http://<host:port>/listCloseOnly/csv" should return close times only in CSV format

    * "http://<host:port>/listAll/json" should return all open and close times in JSON format
    * "http://<host:port>/listOpenOnly/json" should return open times only in JSON format
    * "http://<host:port>/listCloseOnly/json" should return close times only in JSON format

* Add a query parameter to get top "k" open and close times. For examples, see below.

    * "http://<host:port>/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format 
    * "http://<host:port>/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format
    * "http://<host:port>/listCloseOnly/csv?top=6" should return top 5 close times only (in ascending order) in CSV format
    * "http://<host:port>/listCloseOnly/json?top=4" should return top 4 close times only (in ascending order) in JSON format

* Design consumer programs (e.g., in jQuery) to use the service that you expose. `website` inside `DockerRestAPI` is an example of that. It is uses PHP. You're welcome to use either PHP or jQuery to consume your services. NOTE: your consumer program should be in a different container like example in `DockerRestAPI`.


## Author

Melodie Collins, mcolli11@uoregon.edu


## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.

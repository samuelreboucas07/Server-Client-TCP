# Scope and objective

This work aims to allow the exchange of information between the client and server, retrieving stored files through customer requests.

For this, a socket structure was used that allows the connection between the parties involved, so that from the knowledge of the information related to the server's address and port, any customer was able to request files.

# Starting ....

## Clone the current repository

* ``` https://github.com/samuelreboucas07/Sistemas-distribu-dos.git ```

# Requirements

You must have installed on your computer version 3 of the Python programming language. 

# Protocol

The socket provides communication between two parties. The representation is given by ```IP:port```, so that the socket uses the set of TCP/IP protocols to exchange information between the parties.

According to the OSI model, sockets are between the application and transport layer.

![protocol of comunication](https://github.com/samuelreboucas07/Sistemas-distribu-dos/blob/master/Practical%20work%201/imgs/protocol.png)

To initiate communication between client and server, the client needs to know the server's address (IP) and port, otherwise it will not be possible to carry out communication between the parties, once this type of connection is always initiated by the client.

# Application execution

## Server startup

To start the server, the command must respect the following standard:

* ``` python3 server_main.py port file_repository ```

The value referring to the field **port** represents the point of communication between the server and the client (as long as combined with the correct IP address). The field **file_repository** represents the folder to which the server will have "control" over the files, being able to transfer them upon request of the client.

## Client request

### File request to the server

To make a request to the server, the following command must be performed:

* ``` python3 client.py address port file_name destination_directory ```

Based on the address where the current server is running, the field **address** should be replaced by **127.0.0.1**, since the server is running on the same machine as the client. Thus, the command to execute the client is as follows:

* ``` python3 client.py 127.0.0.1 port file_name destination_directory ```

The field **file_name** refers to the file that will be requested from the server, which will be saved in the directory informed through the field **destination_directory**.

### Request for cache memory status information

In addition to requesting files from the server, the client can request that it send the current state of its cache memory, informing which files are currently allocated. 

* ``` python3 client.py 127.0.0.1 port list_files ```

**Note:** The field **port** it must be the same on both the server and the client, otherwise communication between the parties will not be possible.

# Modeling

## Organization of files

The present work was modularized in order to guarantee that possible future refactorings and new functionalities are carried out in an easier way, thus the server was divided into 3 files and the client only 1 file.

* ```server_main.py: ``` Server boot file, it is responsible for enabling the socket and ensuring that the port defined in this address is heard by the socket, so that as soon as new clients try to connect to the server, it is aware of the request.
In this same file the Thread instantiation is performed, which will be explained in the next sections.

* ```server.py: ``` This file is characterized as the main server file, it contains all file reading routines, client communication (receiving messages and sending results), as well as the interaction with the cache memory, among others.
  
* ```cache.py: ``` Given the configuration of the cache memory and the methods employed, modularization was considered necessary, so that all interactions have a well-defined context, from its instantiation to the return of the result of its processing.

The above files represent the application server, from the client interaction layer to the storage of files in memory.

* ```client.py: ``` This file comprises the treatment of information given by the client when executing the present file, as well as the request to the server for the data transaction or listing of the items contained in the cache memory.

## Execution flow

The present project presents different scenarios resulting from the client's request to the server, which are described below.

1. File request present in cache memory:
   
   This scenario is the most suitable with regard to saving resources, the server cache is designed to store recurrently required files for a limited time, so that the cost of reading the same file for each request is reduced.

   Observe the flow of execution in this scenario in the figure below:

   ![execution flow, file in cache](https://github.com/samuelreboucas07/Sistemas-distribu-dos/blob/master/Practical%20work%201/imgs/req_file_1.png)

   The client requests a file from the server, in sequence, the server will check if the requested file is in the cache memory, if the result is positive the file is returned to the server and serialized to send to the requesting client. Otherwise, the server receives information related to the absence of the file in the cache memory, and moves on to the next scenario.

2. File request missing from cache memory:
   
   Starting from the previous situation, where the server receives information from the cache memory that the requested file is not present, we have the following flow:

    ![execution flow, file out of cache](https://github.com/samuelreboucas07/Sistemas-distribu-dos/blob/master/Practical%20work%201/imgs/req_file_2.png)

    Note that as soon as the server is aware of the absence of this file in the cache memory it goes directly to the knowledge directory to read the file and bring it to the server.

    Sequentially the cache memory is accessed, and the file requested for transfer is checked for size less than or equal to the memory limit, if the result is positive the memory will free up occupied space (if it's necessary) and thus the file will be stored in the cache. After this process the file is sent to the server, to be sent to the client.

    If the file read from the directory system is larger than the limit allowed by the cache memory, it is sent directly to the client and will not be stored in cache memory.

3. Request for list of files present in cache memory:
   
   This process represents the smallest flow of execution between client and server. The client makes the listing request, the server receives this request,access cache memory, go through all the stored data and return the list with the name of each file to the server, in sequence, the server will return this information to the client.

   ![execution flow, file listing](https://github.com/samuelreboucas07/Sistemas-distribu-dos/blob/master/Practical%20work%201/imgs/list_files.png)


## Comments

Given the topology of a requisition system between client and server, all the information transferred between the parties is serialized,  for this, the module was used [Pickle](https://docs.python.org/3/library/pickle.html), which transforms information into a byte stream to be transferred, later the same information is deserialized so that the applicant is aware of it.

# Cache Memory

The cache memory must have a structure that provides access speed and efficiency in temporary storage. Therefore, it was simulated using a data structure based on key and value, called a dictionary.

In this way the cache memory has a structure whose key for each element is characterized by the name of the stored file, and its value is described because it contains the binary information of the file read, as well as the size in Megabytes. Note in the diagram below:

```
{
   "file_name" : {
                        "content": '[b'', .... ]',
                        "size": 10,0 
                    }
}
```

# Multiprocessing

Given the peculiarities of systems similar to this project, multiprocessing is a characteristic generally requested due to the need for different clients to make requests to the server in the same period of time without the request of one client burdening the experience of another due to the impossibility of access at that moment.

That way, it was necessary to apply the concept of Threads, which allow the operating system to execute multiple requests simultaneously,sharing system resources, but running independently.

# Examples

The tests performed below are performed on the same machine, so that the server's access address is defined as the local address.

1. Server startup and file request out of cache:

   ![Server and cache miss](https://github.com/samuelreboucas07/Sistemas-distribu-dos/blob/master/Practical%20work%201/imgs/cache_miss.gif)

2. Server startup and request for file in cache memory:

   ![server and cache hit](https://github.com/samuelreboucas07/Sistemas-distribu-dos/blob/master/Practical%20work%201/imgs/cache_hit.gif)

3. Request for listing of files in the cache memory:

   ![list files](https://github.com/samuelreboucas07/Sistemas-distribu-dos/blob/master/Practical%20work%201/imgs/list_files.gif)

The directories used in the examples above should not be used in other test environments, since the organization and naming of folders is a particular characteristic of each environment.
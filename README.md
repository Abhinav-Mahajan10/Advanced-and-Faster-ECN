# Advanced-and-Faster-ECN
## Instructions to run the project: -
First step is to go inside any of the 4 directories, each of which corresponds to a particular case of our implementation (Traditional ECN UDP, Traditional ECN TCP, Enhanced ECN UDP and Enhanced ECN TCP).  
The run the following commands: -  
make  
// then the mininet should open up with out topology  
h2 ./receive.py > h2.txt &  
h22 iperf -s -u &
h1 ./send.py 10.0.2.2 "Hello h2" 50 &  
h11 iperf -c 10.0.2.22 -t 15 -u  
  
// then we wait for the simulation to end. You can open the h2.txt file geenrated to see the packets received at h2. And if you want to just see the tos or ecn fields of the packets received, you can run the command: - grep tos h2.txt  

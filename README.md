## **Learning Python**

These are some of my personal projects developed during my Python learning journey. I will track my progress here, including a description on what each project does.

### **Dice Roller**

This code is a simple dice roller game - the user is asked to input the number of sides and then a random value is generated. Also, the user has access to the history of the generated values during a single run.

### **g16sub**

This code is an automation script used for submission of *Gaussian Job File* (GJF) to a cluster that uses HTCondor workload management system. The script takes as an argument the GJF and retrieve from that the number of CPUs and the memory that must be allocated to that job. If the GJF does not have any information regarding the number of CPUs or the necessary memory, the script will allocate by default 4 CPUs and 4 GB of memory. The script is configured for Gaussian 16.

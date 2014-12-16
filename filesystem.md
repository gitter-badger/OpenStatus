OpenStatus FileSystem
====

##Layout

###Diagram

Below is a text made diagram made to explain and show the layout of the **OpenStatus FileSystem**.

````
+ .config/OpenStatus
+   --config
+     --config/config.txt
+ --network
+   --network/default.txt
````

###Explanation

Below we explain the above diagram.

1. The `.config/OpenStatus` folder is a directory that holds everything for OpenStatus in terms of information, not the binaries and libraries though.
2. The sub-directory `--config` is a sub-directory of `.config/OpenStatus`, it holds the configuration files for your OpenStatus installation.

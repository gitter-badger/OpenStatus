OpenStatus FileSystem
====

##Layout

###Diagram

Below is a text made diagram made to explain and show the layout of the **OpenStatus FileSystem**.

````
+ .config/OpenStatus
+   --config
+     --config/config.txt
+   --network
+     --network/default.txt
+     --network/archive
````

###Explanation

Below we explain the above diagram.

1. The `.config/OpenStatus` folder is a directory that holds everything for OpenStatus in terms of information, not the binaries and libraries though.
2. The sub-directory `--config` is a sub-directory of `.config/OpenStatus`, it holds the configuration files for your OpenStatus installation.
3. The file placed in `--config` named `config.txt` holds the user=specific configuration, such as the user's chosen username.
4. The sub-directory `--network` is a sub-directory of `.config/OpenStatus`, it holds all the network files that are getting synced by [**Syncthing**](http://syncthing.net) to your machine.
5. The file placed in `--network` named `default.txt` holds the currently active/default timeline of the network.
6. The sub-directory placed in `--network`is a sub-directory of `.config/OpenStatus`, its directory is named `archive`, it holds all of the archived timelines that were archived by [**DynamicShift**]().

Dynamic-Shift
====

##What is DynamicShift?

**DynamicShift** is a core component of the OpenStatus environment, it ensures that the API doesn't slow down and keeps the network fast then. What is basically does, is when the active timeline a.k.a `default.txt` reaches the size of **1MB** or sometimes higher (this is a hard-coded constant value known as the heap_szi), DynamicShift will then place the active timline into a directory named, `archive`, the timeline will be timestamped from thereforewards in the form of naming it with a timestamp as a filename. Once this is completed DynamicShift will then exit. After this when the Python code executes a `post` method, kit will automatically create a new text file as Python does things that way.

##Why do we need it?

**Network health**, that is why. In order for the network to be opperating efficiently for everyone we need to keep things small so that things work fast.

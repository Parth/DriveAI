
ROS
===
Robot Operating System

Creating a Workspace
--------------------

You need to `source` the `/opt/ros/indigo/setup.zsh` or the .sh, or the .bash. depending on your environment.

```zsh
source /opt/ros/indigo/setup.zsh
```

In the directory you want to make your workspace, create a `src` folder
`ws` is your workspace
```zsh
mkdir ws/src
catkin_init_workspace
```

You can build by

```zsh
cd ws
catkin_make
```

Then you need to `source` the following
```zsh
source devel/setup.zsh
```

Some ROS Commands
* rospack = ros+package
* roscd = ros + cd
* rosls = ros + ls

Creating a Package
------------------
Goto your `src` folder and execute
```zsh
catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
```

You can use rospack to review the *first-order* dependencies

```zsh
rospack depends1 <package_name>
```

You can recursively inspect these dependencies
```zsh
rospack depends1 <dependency returned by <rospack depends1 <package_name>>>
```

Building a ROS Package
----------------------
In your workspace execute: 
```zsh
catkin_make
```

Launching ROS
-------------
Goto your workspace, keep in mind that you should have the ros `setup.zsh` and your `devel/setup.zsh` sourced 
```zsh
roscore
```

To see a list of currently running nodes:
```zsh
rosnode list
```

rosrun allows you to use the package name to directly run a node within a package (without having to know the package path).

```zsh
rosrun [package_name] [node_name]
```

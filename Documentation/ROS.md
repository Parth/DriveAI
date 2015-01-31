
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



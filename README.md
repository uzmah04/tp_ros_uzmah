# tp_ros_uzmah

Ce devoir ROS consiste à calculer les coordonnées (x,y) afin de suivre la trajectoire d’un carré en utilisant rviz.
Il y a aussi un bouton intégré dans ce devoir.Quand on appuie sur le bouton, le programme va être sur pause et quand on reclique dessus, le programme va continuer.

Les fichiers :
- CMakeLists.txt
- Package.xml
- Publisher.py -- qui se trouve dans le dossier src
- Coordonnee_rviz.rviz -- qui se trouve dans le dossier config
- LaunchPub.launch -- qui se trouve dans le dossier launch
  
## Pour lancer le program:

- Il faut d’abord avoir les outils ROS et un workspace avec les dossiers build, devel, logs et src.

- Dans le dossier src du workspace, il faut cloner ce repository ainsi celui qui contient le code pour le bouton
> Example: mon workspace -> catkin_ws
```sh
        $ cd ~/catkin_ws/src
```
> Ce programme
 ```sh
        $ git clone https://github.com/uzmah04/tp_ros_uzmah.git
```
> Pour le bouton
 ```sh
        $ git clone https://github.com/Kramoth/button_gui.git
```

- Ensuite il faut faire:
```sh
        $ catkin build
        $ source ~/catkin_ws/devel/setup.bash
```

- Et pour lancer le program, il faut faire:
```sh
        $ roslaunch tp_ros_uzmah launchPub.launch
```

<!--
  Posted at https://gist.github.com/noahcoad/fc9d3984a5d4d61648269c0a9477c622
  Locally at ~/code/py/learn/minecraft_py/gist/fc9d3984a5d4d61648269c0a9477c622

  Screen capture: https://screencast.com/t/KVRBNQjM
-->

# Code Minecraft with Python on Mac OSX

Here's a step-by-step to get started scripting Minecraft with Python on Mac OSX

## Overview 
There was a special build of Minecraft for the [Raspberry Pi](https://www.raspberrypi.org/) called [Minecraft Pi](https://minecraft.net/en-us/edition/pi/) that had a Python interface and library.  You could code in Python to manipulate your Minecraft world!  But you'd have to code on a Raspberry Pi computer.  However thanks to using the [RaspberryJuice](https://dev.bukkit.org/projects/raspberryjuice) plugin with a [Spigot](https://www.spigotmc.org/) server, you can do this locally on a Mac.  Probably in Linux or Windows too, but I'll leave that up to you.

Here we have a rainbow created by the [rainbox script](https://www.dropbox.com/s/k29ms42nzvgehjk/rainbow.py?dl=0).
![rainbow](https://content.screencast.com/users/NoahCoad/folders/Jing/media/b6e388d6-e9c5-4941-9dac-afdf6949f30a/00000130.png)

## Step-by-step

    # guide for Minecraft v1.16.5 server
    # update minecraft server and spigot links for latest versions
     
    # get started
    cd ~/Applications/"Minecraft Tools"/
    mkdir minecraft_py; cd minecraft_py; mkdir spigot; mkdir spigot_builder; cd spigot
     
    # download minecraft server from https://minecraft.net/en-us/download/server/
    wget https://launcher.mojang.com/v1/objects/fe123682e9cb30031eae351764f653500b7396c9/server.jar
     
    # download spigot server from https://getbukkit.org/download/spigot
    # wget -O spigot.jar https://cdn.getbukkit.org/spigot/spigot-1.16.5.jar
    # will change that to manually build spigot
    
    # build spigot.jar from sources
    cd ~/Applications/"Minecraft Tools"/minecraft_py/spigot_builder
    wget https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
    java -jar BuildTools.jar 
    
    cd ../spigot
    ln -s ../spigot_builder/spigot-1.16.5.jar spigot.jar
    
    # agree to eula
    echo eula=true > eula.txt
     
    # get RaspberryJuice from https://dev.bukkit.org/projects/raspberryjuice
    mkdir plugins; cd plugins
    
    wget -O raspberryjuice-1.11.jar https://dev.bukkit.org/projects/raspberryjuice/files/latest
     
    # get the mcpi libraries from https://github.com/zhuowei/RaspberryJuice
    #cd ../..
    #git clone https://github.com/zhuowei/RaspberryJuice.git
    #mkdir py
    #cp -r RaspberryJuice/src/main/resources/mcpi/api/python/modded/mcpi py/
     
    conda activate minecraft
    pip install mcpi




## Run a new server

Je crois qu'il suffit de supprimer les 3 rep sous server: world, world_nether, world_the_end

et relancer le server



  

## You're Running!

Start minecraft making sure the version matches (1.13.1 in this case), go into multiplayer mode, add a server with address: `localhost`

Connect, look around you, and you'll see the rainbow!

Want a first challenge?  try making the rainbow thicker =)

## Also
* Set up to run automatically, https://github.com/Ahtenus/minecraft-init
* See more examples!
  * https://www.101computing.net/minecraft-python-challenges/
  * https://www.stuffaboutcode.com/p/minecraft.html
* See the list of commands implemented at https://dev.bukkit.org/projects/raspberryjuice
* See the Minecraft Pi protocal at https://wiki.vg/Minecraft_Pi_Protocol
* "stop" at server prompt will close the server
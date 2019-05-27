1. 首先在VMware tool安装成功（有需要更新就更新）
2. 在VMware中设置共享目录（虚拟机的设置选项卡，虚拟机-设置-选项）
3. 命令vmware-hgfsclient确认是否有设置的共享文件
4. 命令apt-get install open-vm-dkms;然后mkdir /mnt/hgfs;然后mount -t vmhgfs .host:/ /mnt/hgfs
5. 步骤四如果不行，命令apt-get install open-vm-tools-dkms；然后mkdir /mnt/hgfs;然后vmhgfs-fuse .host:/ /mnt/hgfs。
6. 步骤5安装成功，但是在user目录下没有权限访问共享文件夹。在user目录下强制修改文件夹hgfs权限，然后执行 vmhgfs-fuse .host:/ /mnt/hgfs即可成功。
7. 缺憾：网上说可以将命令写到/etc/fstab文件中可以在机器重启后自动挂载，我的虚拟机在添加后Ubuntu会启动不了，搜了一些方法也没有用，所以就每次重启后手动挂载。
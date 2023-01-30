#json formater
    python -m json.tool -h

# zip
    python -m zipfile -h
# http server
   python -m http.server -h
# 检测usb插入
    $ udevadm monitor --environment --udev

# find 使用
    搜索目录所有以disc开头的目录：
    find . -path "./disc*"
# git 使用ssh登录
  * 方法一
  1. eval "$(ssh-agent -s)"
  2. ssh-add .ssh/[private key file]
  3. 改remote为 git@github.com:[project path]
  * 方法二
    git config core.sshCommand "ssh -i ~/.ssh/your_private_key"

# pacman
  当更新出现key错误时，运行命令

    $ sudo pacman -S archlinux-keyring
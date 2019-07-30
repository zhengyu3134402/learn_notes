
# 说明：
#     此文档包含github相关信息



# =================================================
# github

# 删除一个项目中的文件夹（必须通过命令）
    # 前提保持本地和git数据一致
    # git rm -r --cached target              # 删除target文件夹
    # git commit -m '删除了target'        # 提交,添加操作说明


# 1 安装

    # 1 windows安装和使用

        # 1 进入下载网址 https://www.git-scm.com/download/win
        # 2 若速度慢用迅雷下载（选择合适的版本）
        # 3 安装默认下一步下一步下一步
        # 4 建议是否安装成功 ，鼠标右键桌面菜单中会出现
            # Git GUI Here
            # Gir Bash Here

    # 2 windows使用说明

    # 1 创建一个文件夹
        # 1 初始化基本信息

            # 1 设置用户名
                # git config --global user.name '用户名'
            # 2 设置用户邮箱
                # git config --global user.name 'xxx@xxx.com'
        # 2 初始化仓库
            # git init
        # 3 尝试下载任意一个项目为了获取.ssh
            # git clone xxxxx  会在 ~/下生成.ssh文件
        # 4 获取秘钥为了连接远程仓库
            # 1 在文件中 右键点击Gir Bash Here
            # 2 在弹出的页面进行操作 操作命令是linux命令
            # 3 cd ~/.ssh文件中执行命令
                # ssh-keygen -t rsa -C 174927390@qq.com
            # 4 将生成的id_rsa.pub文件中的代码添加到github网站ssh and GPG keys中
        # 5 即可正常使用命令

            # git add ..
            # git commit -m "xx"
            # git push origin master

    # 2 linux安装和使用
        # 1 安装GIT
            # sudo apt-get install git
        # 2 注册帐号
        # 3 建立仓库
        # 4 生成公钥
            # 进入 .ssh文件夹
                # ssh-keygen -t rsa -C “your_email@committermail.com”
        # 5添加公钥
            # 网站中setting中 添加 .ssh目录中xxx.pub的内容复制粘贴 点击添加
        # 6验证
            # ssh -T git@github.com
        # 7设置
            # git config –-global user.name “your_name”
            # git config –-global user.email “your_email@youremail.com”
        # 8链接仓库
            # git clone 仓库地址的复制链接
        # 9命令
            # git add xxx
            # git commit -m 'xxx'
            # git push origin master

# =================================================
```bash
$ cat ~/.pip/pip.conf
[global]
index-url = https://pypi.mirrors.ustc.edu.cn/simple
```

```bash
$ virtualenv -p ~/anaconda3/bin/python3 env
Running virtualenv with interpreter /home/tzx/anaconda3/bin/python3
Using base prefix '/home/tzx/anaconda3'
New python executable in /home/tzx/git/python-helloworld/env/bin/python3
Also creating executable in /home/tzx/git/python-helloworld/env/bin/python
Installing setuptools, pip, wheel...done.

$ tree -L 2
.
├── env
│   ├── bin
│   ├── include
│   ├── lib
│   └── pip-selfcheck.json
└── LICENSE

4 directories, 2 files

$ source env/bin/activate
(env)

$ pip install -r requirements.txt

$ charm .

$ deactivate
```

```bash
$ sudo pip install pipreqs
$ pipreqs . --force
# if failed, reinstall pyOpenSSL:
#       sudo pip uninstall pyOpenSSL
#       sudo pip install pyOpenSSL
```
# SSH Tricks

## tmux/byobu/screen
Tmux and screen are *terminal multiplexers*, they provide a way to have multiple
shells open over the same connection at the same time, and reconnect to these
shells (usually called a session).

If you have something you want to keep running when you log out (and view it
later when you log in again), or you are on wifi or have a poor connection, the
sessions created by tmux and screen remain, and you can keep working with too
much interruption.

### Quick tmux intro

To start tmux, run
```
tmux
```
and to reattach to tmux, run
```
tmux attach
```

Generally, when I log in, I have my `.bash_profile` run
```
tmux attach || tmux
```
which will attach to an existing session, or create a new one if there is no
existing session.

There is a list of the default shortcuts in the tmux man page under `KEY BINDINGS`,
but the one you will use most often is:

Ctrl-b d – this means hit Ctrl and b at the same time, then let go of them and
hit d (all of tmux's commands work like this, screen is very similar). This is
the detach command, which exits tmux but keeps the session going.

Read the tmux man page or website (https://tmux.github.io) for more tips, such
as splitting the terminal or having multiple windows.

### Byobu
Byobu (previously screen profiles) is a wrapper around screen, and more recently
tmux (screen is hard to configure/use, byobu provided some tools to make that
easier).

Generally, when connecting to a new server, try seeing if tmux is available
first, then byobu, then screen. If none of them are installed, request that they
be installed.

## SSH Keys

SSH keys are a more secure way of logging into SSH servers (vs passwords). They
also allow you to avoid repeatedly typing the same password over and over.
These keys are stored in `~/.ssh`, which can only be read by you.

We create keys by running `ssh-keygen`, which by default creates two files:
`~/.ssh/id_rsa` (the private key) and `~/.ssh/id_rsa.pub` (the public key).

Services like GitHub require that you use SSH keys, hence you need to copy the
contents of `~/.ssh/id_rsa.pub` and follow the instructions on their website
(see https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account).

On servers that you can connect via a password, using `ssh-copy-id` is the
easiest thing to do.
Running
```
ssh-copy-id server-name
```
will copy the public key to the server named `server-name`.

If you have keys on GitHub (or Launchpad) you can install the public keys via
`ssh-import-id` (run this on the server **not** on you local laptop/desktop). To
do this, run
```
ssh-import-id gh:you-github-username
```
Note that `ssh-import-id` may not be installed though.

## SSH config files

Config file stored at ~/.ssh/config — avoid repeatedly typing the same thing:
`ssh ceres` will "just work". (FYI, this applies for OpenSSH, the default on
MacOS/Linux, PuTTY is different).

### Basics (Host/Port/Username/Hostname/ForwardX)

The simplest config file for logging into ceres is:

```
Host ceres
User my-science-id
Port 22
Hostname ceres.science.mq.edu.au
```

`Host` is the name we use on the command line.
`User` is the username we want to log in with (the bit before the @) - uses your
current login by default.
`HostName` is the full name of server (the bit after the @)
`Port` is the port we connect to (usually 22 used, which is the default, but
sometimes you need to change this

We tell ssh to always use X11 forwarding (`ssh -X`) by adding
```
ForwardX11 yes
```
so our new config file looks like

```
Host ceres
User my-science-id
Port 22
Hostname ceres.science.mq.edu.au
ForwardX11 yes
```

We can expand this to other servers by using %h which will be expanded as the
string used in `Host` like so:

```
Host gesualdo ceres dopey
User my-science-id
Port 22
ForwardX11 yes
Hostname %h.science.mq.edu.au
```

## Proxies (ProxyJump/ProxyCommand)
SSH has built in support for connecting to a server via other servers, which we
can use to get to ceres from outside MQ. The easiest way is to define another
`Host` section like so:
```
Host mqproxy-legacy
User my-science-id
Port 22
ForwardX11 yes
HostName remus.science.mq.edu.au

Host mqproxy
User my-one-id
Port 22
ForwardX11 yes
HostName romulus.science.mq.edu.au
```

and then add `ProxyJump` to connect:
```
Host gesualdo ceres dopey
User my-science-id
Port 22
ForwardX11 yes
Hostname %h.science.mq.edu.au
ProxyJump mqproxy
```

`ProxyJump` is quite new, see
https://superuser.com/questions/1253960/replace-proxyjump-in-ssh-config
for alternatives which will work on older systems.

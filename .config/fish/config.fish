if status is-interactive
    # Commands to run in interactive sessions can go here
    #fastfetch
    pfetch
    bind \e\[3\~ kill-whole-line
end

# start X at login
#if status --is-login
#    if test -z "$DISPLAY" -a $XDG_VTNR = 2
#       exec startx
#    end
#end

# start X at login
#if status --is-login
#    if test -z "$DISPLAY"; and test (tty) = /dev/tty2
#        exec startx
#    end
#end

alias ls='lsd'
alias tree='lsd --tree'

# быстрые команды для управления zapret
alias zapret-config='$HOME/zapret-configs/install.sh'
alias zapret-utils='$HOME/zapret-configs/utils-zapret.sh'
set -x PYENV_ROOT $HOME/.pyenv
set -x PATH $PYENV_ROOT/bin $PATH
pyenv init - | source
set -x PYENV_ROOT $HOME/.pyenv
set -x PATH $PYENV_ROOT/bin $PATH
pyenv init - | source

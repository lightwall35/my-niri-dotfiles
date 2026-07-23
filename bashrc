#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '
export PATH=~/.npm-global/bin:$PATH


# Added by Antigravity CLI installer
export PATH="/home/minec/.local/bin:$PATH"

# Set terminal language to English
export LANG=C.UTF-8
export LC_ALL=C.UTF-8


alias ff='fastfetch'

alias rs='sudo systemctl restart mihomo'

alias comfy="cd ~/playground/comfyui && ./start.sh"

alias regrub="sudo grub-mkconfig -o /boot/grub/grub.cfg+"

showart() {
	local dir="/home/minec/ascii-art/nahida-2-animate"
	local files=("$dir"/*.txt)

	alacritty msg config "font.size=1.2"
	tput civis  # 隐藏光标

	while true; do
		for f in "${files[@]}"; do
			tput home  # 光标回到左上角（避免 clear 闪烁）
			sed 's/./& /g' "$f"
			# 检测按键，按任意键退出；同时作为帧间延迟
			if read -t 0.0417 -n 1 -s; then
				tput cnorm  # 恢复光标
				clear
				alacritty msg config "font.size=9"
				return
			fi
		done
	done
}

showart

HISTSIZE=10000
HISTFILESIZE=20000




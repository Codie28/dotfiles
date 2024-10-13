packages() { 
	sudo pacman -Sy --needed zsh fzf zoxide tmux stow findutils playerctl
	sudo pacman -Sy --needed polybar qtile kitty nitrogen rofi picom dunst
	sudo pacman -Sy --needed xorg xorg-xinit

	# TODO better python setup
	sudo pacman -Sy --needed python python-setuptools

	if [[ ! -d "$HOME/git/yay" ]]; then
		git clone https://aur.archlinux.org/yay-bin.git $HOME/git/yay
		cd $HOME/git/yay
		makepkg -si
		cd $HOME
	fi

	yay -Sy --needed python-catppuccin oh-my-posh neovim-nightly-bin zen-browser-bin ttf-meslo-nerd zscroll-git

	
}

packages

# TODO auto detect this
DOTSDIR=dots

cd $HOME

ln -s $DOTSDIR/mybin .
ln -s $DOTSDIR/.zprofile .

chsh $USER -s /usr/bin/zsh

# generate it if not present
mkdir $HOME/.config

QTILE_THEME_HOME=.qtheme ~/mybin/switch strap
QTILE_THEME_HOME=.qtheme ~/mybin/switch catppuccin

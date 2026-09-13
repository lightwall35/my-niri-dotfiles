# niri配置文件

| 文件名 | 描述 | 真实位置 |
| --- | --- | --- |
| `config.kdl` | niri窗口管理器的配置文件 | `/home/lightwall/.config/niri/config.kdl` |
| `alacritty.toml` | alacritty终端模拟器的配置文件 | `/home/lightwall/.config/alacritty/alacritty.toml` |
| `config` | cava配置文件 | `/home/lightwall/.config/cava/config` |
| `kitty` | kitty终端模拟器配置目录，包括 `kitty.conf`、`dank-tabs.conf`、`dank-theme.conf` | `/home/lightwall/.config/kitty` |
| `bashrc` | bash终端配置 | `/home/lightwall/.bashrc` |
| `.zshrc` | zsh终端配置 | `/home/lightwall/.zshrc` |
| `settings.json` | dms配置文件 | `/home/lightwall/.config/DankMaterialShell/settings.json` |
| `scripts/change_wallpaper.sh` | niri 双后端（swaybg + awww）壁纸同步切换脚本 | `/home/lightwall/.config/niri/scripts/change_wallpaper.sh` |
| `grub` | grub配置文件 | `/etc/default/grub` |
| `fstab` | 系统挂载配置（exfat/ntfs/swap） | `/etc/fstab` |
| `mkinitcpio.conf` | initramfs 构建配置 | `/etc/mkinitcpio.conf` |
| `modprobe.d` | 内核模块参数（nvidia modeset 等） | `/etc/modprobe.d` |
| `dms` | niri 的 DMS 组件配置目录，包括 `binds.kdl`、`windowrules.kdl`、`layout.kdl`、`outputs.kdl`、`colors.kdl` 等 | `/home/lightwall/.config/niri/dms` |
| `gtk-3.0` | GTK3 自定义主题，包括 `settings.ini`、`gtk.css`、`colors.css`、`dank-colors.css`、`window_decorations.css` 等 | `/home/lightwall/.config/gtk-3.0` |
| `gtk-4.0` | GTK4 自定义主题，包括 `settings.ini`、`gtk.css`、`colors.css`、`dank-colors.css`、`window_decorations.css` 等 | `/home/lightwall/.config/gtk-4.0` |
| `environment.d` | 用户环境变量，包括 `envvars.conf`（设置系统的默认语言为中文）和 `im.conf`（关于 Fcitx5 输入法的环境变量设置） | `/home/lightwall/.config/environment.d` |
| `profile` | fcitx5 输入法配置 | `/home/lightwall/.config/fcitx5/profile` |
| `pinyin.conf` | fcitx5 拼音输入配置 | `/home/lightwall/.config/fcitx5/conf/pinyin.conf` |
| `qt6ct.conf` | Qt6 主题配置 | `/home/lightwall/.config/qt6ct/qt6ct.conf` |
| `m.conf` | qt6ct 自定义配色 | `/home/lightwall/.config/qt6ct/colors/m.conf` |
| `fonts.conf` | fontconfig 字体渲染配置 | `/home/lightwall/.config/fontconfig/fonts.conf` |
| `mimeapps.list` | 默认应用程序关联 | `/home/lightwall/.config/mimeapps.list` |
| `config.yaml` | mihomo 代理配置 | `/home/lightwall/.config/mihomo/config.yaml` |
| `swaybg.service` | swaybg 壁纸用户服务 | `/home/lightwall/.config/systemd/user/swaybg.service` |
| `pacman.conf` | pacman 包管理器配置 | `/etc/pacman.conf` |
| `gdm.service.d` | gdm 系统服务 override（KillSignal=SIGKILL） | `/etc/systemd/system/gdm.service.d` |
| `mihomo.service.d` | mihomo 系统服务 override（User=lightwall） | `/etc/systemd/system/mihomo.service.d` |
| `ollama.service.d` | ollama 系统服务 override（OLLAMA_HOST） | `/etc/systemd/system/ollama.service.d` |
| `google-chrome.desktop` | Google Chrome 自定义 .desktop 文件 | `/home/lightwall/.local/share/applications/google-chrome.desktop` |
| `clavis-effects.kdl` | niri 毛玻璃特效配置 | `/home/lightwall/.config/niri/clavis-effects.kdl` |
| `sync_dotfiles.py` | 同步脚本 | *(仓库内工具)* |

## 文件位置结构图

```text
/
├── etc/
│   ├── default/
│   │   └── grub
│   ├── fstab
│   ├── mkinitcpio.conf
│   ├── modprobe.d/
│   │   ├── nvidia.conf
│   │   ├── nvdia.conf
│   │   └── supergfxd.conf
│   ├── pacman.conf
│   └── systemd/system/
│       ├── gdm.service.d/override.conf
│       ├── mihomo.service.d/override.conf
│       └── ollama.service.d/override.conf
└── home/lightwall/
    ├── .bashrc
    ├── .zshrc
    ├── .config/
    │   ├── alacritty/
    │   │   └── alacritty.toml
    │   ├── cava/
    │   │   └── config
    │   ├── DankMaterialShell/
    │   │   └── settings.json
    │   ├── environment.d/
    │   │   ├── envvars.conf
    │   │   └── im.conf
    │   ├── fcitx5/
    │   │   ├── conf/
    │   │   │   └── pinyin.conf
    │   │   └── profile
    │   ├── fontconfig/
    │   │   └── fonts.conf
    │   ├── gtk-3.0/
    │   │   ├── assets/
    │   │   ├── colors.css
    │   │   ├── dank-colors.css
    │   │   ├── gtk.css
    │   │   ├── settings.ini
    │   │   └── window_decorations.css
    │   ├── gtk-4.0/
    │   │   ├── colors.css
    │   │   ├── dank-colors.css
    │   │   ├── gtk.css
    │   │   ├── settings.ini
    │   │   └── window_decorations.css
    │   ├── kitty/
    │   │   ├── dank-tabs.conf
    │   │   ├── dank-theme.conf
    │   │   └── kitty.conf
    │   ├── mihomo/
    │   │   └── config.yaml
    │   ├── mimeapps.list
    │   ├── niri/
    │   │   ├── clavis-effects.kdl
    │   │   ├── config.kdl
    │   │   ├── dms/
    │   │   │   ├── alttab.kdl
    │   │   │   ├── binds.kdl
    │   │   │   ├── colors.kdl
    │   │   │   ├── cursor.kdl
    │   │   │   ├── layout.kdl
    │   │   │   ├── outputs.kdl
    │   │   │   ├── windowrules.kdl
    │   │   │   └── wpblur.kdl
    │   │   └── scripts/
    │   │       └── change_wallpaper.sh
    │   ├── qt6ct/
    │   │   ├── colors/
    │   │   │   └── m.conf
    │   │   └── qt6ct.conf
    │   └── systemd/
    │       └── user/
    │           └── swaybg.service
    └── .local/share/applications/
        └── google-chrome.desktop
```
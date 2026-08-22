# niri配置文件

| 文件名 | 描述 | 真实位置 |
| --- | --- | --- |
| `config.kdl` | niri窗口管理器的配置文件 | `/home/minec/.config/niri/config.kdl` |
| `alacritty.toml` | alacritty终端模拟器的配置文件 | `/home/minec/.config/alacritty/alacritty.toml` |
| `config` | cava配置文件 | `/home/minec/.config/cava/config` |
| `settings.json` | dms配置文件 | `/home/minec/.config/DankMaterialShell/settings.json` |
| `tui.json` | opencode交互界面的配置文件 | `/home/minec/.config/opencode/tui.json` |
| `grub` | grub配置文件 | `/etc/default/grub` |
| `kdeglobals` | kde窗口效果，已弃用 | `/home/minec/.config/kdeglobals` |
| `environment.d` | 用户环境变量，包括 `envvars.conf`（设置系统的默认语言为中文）和 `im.conf`（关于 Fcitx5 输入法的环境变量设置） | `/home/minec/.config/environment.d` |
| `bashrc` | 终端配置 | `/home/minec/.bashrc` |
| `DankPopoutStandalone.qml` | DankMaterialShell 的独立弹出窗口组件 | `/usr/share/quickshell/dms/Widgets/DankPopoutStandalone.qml` |
| `dms` | niri 的 DMS 组件配置目录，包括 `binds.kdl`（快捷键）、`windowrules.kdl`、`layout.kdl`、`outputs.kdl`、`colors.kdl` 等 | `/home/minec/.config/niri/dms` |
| `scripts/change_wallpaper.sh` | niri 双后端（swaybg + awww）壁纸同步切换脚本 | `/home/minec/.config/niri/scripts/change_wallpaper.sh` |
| `clavis-effects.kdl` | niri 毛玻璃特效配置 | `/home/minec/.config/niri/clavis-effects.kdl` |
| `.bash_profile` | 登录 shell 配置，追加了 PATH | `/home/minec/.bash_profile` |
| `.gitconfig` | git 用户配置 | `/home/minec/.gitconfig` |
| `gtk-3.0` | GTK3 自定义主题，包括 `settings.ini`、`gtk.css`、`window_decorations.css` 等 | `/home/minec/.config/gtk-3.0` |
| `fonts.conf` | fontconfig 字体渲染配置 | `/home/minec/.config/fontconfig/fonts.conf` |
| `mpv.conf` | mpv 播放器配置 | `/home/minec/.config/mpv/mpv.conf` |
| `config.ini` | waypaper 壁纸工具配置 | `/home/minec/.config/waypaper/config.ini` |
| `swaybg.service` | swaybg 壁纸用户服务 | `/home/minec/.config/systemd/user/swaybg.service` |
| `profile` | fcitx5 输入法配置 | `/home/minec/.config/fcitx5/profile` |
| `pinyin.conf` | fcitx5 拼音输入配置 | `/home/minec/.config/fcitx5/conf/pinyin.conf` |
| `qt6ct.conf` | Qt6 主题配置 | `/home/minec/.config/qt6ct/qt6ct.conf` |
| `m.conf` | qt6ct 自定义配色 | `/home/minec/.config/qt6ct/colors/m.conf` |
| `kvantum.kvconfig` | Kvantum 主题设置 | `/home/minec/.config/Kvantum/kvantum.kvconfig` |
| `config.yaml` | mihomo 代理配置 | `/home/minec/.config/mihomo/config.yaml` |
| `fcitx5.desktop` | fcitx5 自启动项 | `/home/minec/.config/autostart/fcitx5.desktop` |
| `.Xresources` | X 资源（光标主题） | `/home/minec/.Xresources` |
| `mimeapps.list` | 默认应用程序关联 | `/home/minec/.config/mimeapps.list` |
| `user-dirs.dirs` | 用户目录设置（含自定义 Projects） | `/home/minec/.config/user-dirs.dirs` |
| `fstab` | 系统挂载配置（exfat/ntfs/swap） | `/etc/fstab` |
| `mkinitcpio.conf` | initramfs 构建配置 | `/etc/mkinitcpio.conf` |
| `pacman.conf` | pacman 包管理器配置 | `/etc/pacman.conf` |
| `modprobe.d` | 内核模块参数（nvidia modeset 等） | `/etc/modprobe.d` |
| `mihomo.service.d` | mihomo 系统服务 override（User=minec） | `/etc/systemd/system/mihomo.service.d` |
| `ollama.service.d` | ollama 系统服务 override（OLLAMA_HOST） | `/etc/systemd/system/ollama.service.d` |
| `gdm.service.d` | gdm 系统服务 override（KillSignal=SIGKILL） | `/etc/systemd/system/gdm.service.d` |
| `hostname` | 主机名 | `/etc/hostname` |
| `locale.conf` | 系统语言 | `/etc/locale.conf` |

## 文件位置结构图

```text
/
├── etc/
│   ├── default/
│   │   └── grub
│   ├── fstab
│   ├── hostname
│   ├── locale.conf
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
├── home/minec/
│   ├── .bash_profile
│   ├── .bashrc
│   ├── .config/
│   │   ├── alacritty/
│   │   │   └── alacritty.toml
│   │   ├── autostart/
│   │   │   └── fcitx5.desktop
│   │   ├── cava/
│   │   │   └── config
│   │   ├── DankMaterialShell/
│   │   │   └── settings.json
│   │   ├── environment.d/
│   │   │   ├── envvars.conf
│   │   │   └── im.conf
│   │   ├── fcitx5/
│   │   │   ├── conf/
│   │   │   │   └── pinyin.conf
│   │   │   └── profile
│   │   ├── fontconfig/
│   │   │   └── fonts.conf
│   │   ├── gtk-3.0/
│   │   │   ├── assets/
│   │   │   ├── dank-colors.css
│   │   │   ├── gtk.css
│   │   │   ├── settings.ini
│   │   │   └── window_decorations.css
│   │   ├── kdeglobals
│   │   ├── Kvantum/
│   │   │   └── kvantum.kvconfig
│   │   ├── mihomo/
│   │   │   └── config.yaml
│   │   ├── mimeapps.list
│   │   ├── mpv/
│   │   │   └── mpv.conf
│   │   ├── niri/
│   │   │   ├── clavis-effects.kdl
│   │   │   ├── config.kdl
│   │   │   ├── dms/
│   │   │   │   ├── alttab.kdl
│   │   │   │   ├── binds.kdl
│   │   │   │   ├── colors.kdl
│   │   │   │   ├── cursor.kdl
│   │   │   │   ├── layout.kdl
│   │   │   │   ├── outputs.kdl
│   │   │   │   ├── windowrules.kdl
│   │   │   │   └── wpblur.kdl
│   │   │   └── scripts/
│   │   │       └── change_wallpaper.sh
│   │   ├── opencode/
│   │   │   └── tui.json
│   │   ├── qt6ct/
│   │   │   ├── colors/
│   │   │   │   └── m.conf
│   │   │   └── qt6ct.conf
│   │   ├── systemd/
│   │   │   └── user/
│   │   │       └── swaybg.service
│   │   ├── user-dirs.dirs
│   │   └── waypaper/
│   │       └── config.ini
│   ├── .gitconfig
│   └── .Xresources
└── usr/
    └── share/
        └── quickshell/
            └── dms/
                └── Widgets/
                    └── DankPopoutStandalone.qml
```
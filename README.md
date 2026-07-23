# niri配置文件

| 文件名 | 描述 | 真实位置 |
| --- | --- | --- |
| `config.kdl` | niri窗口管理器的配置文件 | `/home/minec/.config/niri/config.kdl` |
| `alacritty.toml` | alacritty终端模拟器的配置文件 | `/home/minec/.config/alacritty/alacritty.toml` |
| `config` | cava配置文件 | `/home/minec/.config/cava/config` |
| `settings.json` | dms配置文件 | `/home/minec/.config/DankMaterialShell/settings.json` |
| `tui.json` | opencode交互界面的配置文件 | `/home/minec/.config/opencode/tui.json` |
| `grub` | grub配置文件 | `/etc/default/grub` |
| `kdeglobals` | kde窗口效果，已弃用 | `~/.config/kdeglobals` |
| `environment.d` | 用户环境变量，包括 `envvars.conf`（设置系统的默认语言为中文）和 `im.conf`（关于 Fcitx5 输入法的环境变量设置） | `/home/minec/.config/environment.d` |
| `bashrc` | 终端配置 | `~/.bashrc` |

## 文件位置结构图

```text
/
├── etc/
│   └── default/
│       └── grub
└── home/minec/
    ├── .bashrc
    └── .config/
        ├── alacritty/
        │   └── alacritty.toml
        ├── cava/
        │   └── config
        ├── DankMaterialShell/
        │   └── settings.json
        ├── environment.d/
        │   ├── envvars.conf
        │   └── im.conf
        ├── kdeglobals
        ├── niri/
        │   └── config.kdl
        └── opencode/
            └── tui.json
```
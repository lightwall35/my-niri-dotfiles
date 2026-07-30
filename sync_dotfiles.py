#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

def main():
    repo_dir = Path(__file__).resolve().parent
    readme_path = repo_dir / "README.md"
    exclude_files = {"DankPopoutStandalone.qml", "README.md", os.path.basename(__file__)}

    mappings = {}
    if readme_path.exists():
        with open(readme_path, "r", encoding="utf-8") as f:
            in_table = False
            for line in f:
                line = line.strip()
                if line.startswith("| 文件名"):
                    in_table = True
                    continue
                if in_table and line.startswith("| ---"):
                    continue
                if in_table and line.startswith("|"):
                    parts = [p.strip() for p in line.split("|")[1:-1]]
                    if len(parts) >= 3:
                        filename = parts[0].strip("`")
                        real_path = parts[2].strip("`")
                        if real_path.startswith("~"):
                            real_path = os.path.expanduser(real_path)
                        if filename not in exclude_files:
                            mappings[filename] = real_path
                elif in_table and not line:
                    in_table = False

    for filename, real_path_str in mappings.items():
        real_path = Path(real_path_str)
        repo_path = repo_dir / filename

        if not real_path.exists():
            print(f"找不到真实路径文件，跳过: {real_path}")
            continue

        if real_path.is_dir():
            for root, _, files in os.walk(real_path):
                for f in files:
                    rp = Path(root) / f
                    rel = rp.relative_to(real_path)
                    repo_p = repo_path / rel
                    
                    if not repo_p.exists() or rp.stat().st_mtime > repo_p.stat().st_mtime:
                        print(f"更新目录文件: {rp} -> {repo_p}")
                        repo_p.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(rp, repo_p)
                    else:
                        print(f"无需更新 (目录文件已是最新): {rel}")
            continue

        if not repo_path.exists() or real_path.stat().st_mtime > repo_path.stat().st_mtime:
            print(f"更新文件: {real_path} -> {repo_path}")
            repo_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(real_path, repo_path)
        else:
            print(f"无需更新 (仓库内已是最新): {filename}")

if __name__ == "__main__":
    main()

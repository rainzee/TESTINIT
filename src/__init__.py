from pathlib import Path


def creat_folder(folder_name: str):
    current_dir: Path = Path.cwd()
    project_dir: Path = current_dir / folder_name
    try:
        project_dir.mkdir(exist_ok=False)
    except FileExistsError:
        pass
    except Exception as e:
        pass

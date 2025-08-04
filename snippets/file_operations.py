"""
📁 文件操作常用片段合集
作者: Floyd
用途: 快速搬砖复用，提高日常开发效率
"""


def read_file(filepath: str, encoding: str = "utf-8") -> str:
    """
    读取文本文件内容
    """
    with open(filepath, "r", encoding=encoding) as f:
        return f.read()


def list_files_with_os_walk(directory: str, suffixes: list[str], recursive: bool = False) -> list[str]:
    """
    列出目录下所有指定后缀的文件
    """
    import os

    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if len(suffixes) == 0 or any(filename.endswith(suffix) for suffix in suffixes):
                files.append(os.path.join(root, filename))
        if not recursive:
            break
    return files


def list_files_with_os_listdir(directory: str, suffixes: list[str]) -> list[str]:
    """
    列出目录下所有指定后缀的文件，（os.listdir 不支持递归，要递归只能手动实现）
    """
    import os

    files = []
    for filename in os.listdir(directory):
        if len(suffixes) == 0 or any(filename.endswith(suffix) for suffix in suffixes):
            files.append(os.path.join(directory, filename))
    return files


def list_files_with_pathlib(directory: str, suffixes: list[str], recursive: bool = False) -> list[str]:
    """
    列出目录下所有指定后缀的文件
    """
    from pathlib import Path

    path = Path(directory)
    if recursive:
        files = [str(file) for file in path.rglob("*") if file.suffix in suffixes]
    else:
        files = [str(file) for file in path.glob("*") if file.suffix in suffixes]
    return files


def list_files_with_pathlib2(directory: str, suffix: str, recursive: bool = False) -> list[str]:
    """
    列出目录下所有指定后缀的文件
    """
    from pathlib import Path

    if recursive:
        expr = f"**/*{suffix}"
    else:
        expr = f"*{suffix}"

    # glob("**/*.mp3") 和 rglob("*.mp3") 是一样的
    return [str(file) for file in Path(directory).glob(expr)]


def pathlib_demo(directory: str):
    """
    演示如何使用 pathlib 读取的文件操作
    """
    import pathlib

    files = pathlib.Path(directory).glob("*.html")
    for file in files:
        print(file.name)  # 打印文件名
        print(str(file))  # 打印文件的绝对路径
        print(file.stem)  # 打印不带后缀的文件名
        print(file.suffix)  # 打印文件后缀
        print(file.is_file())  # 判断是否为文件
        print(file.is_dir())  # 判断是否为目录


if __name__ == "__main__":
    files = list_files_with_os_listdir(".", [".lock"])
    for file in files:
        print(file)

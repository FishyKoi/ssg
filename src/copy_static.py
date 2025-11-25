import os
import shutil


def copy_static(src, dst):
    """Recursively copy static/ → public/ directory, deleting public first."""

    # Remove destination directory entirely
    if os.path.exists(dst):
        shutil.rmtree(dst)

    # Create a clean destination root
    os.mkdir(dst)

    # Start recursive copy
    _copy_recursive(src, dst)


def _copy_recursive(src, dst):
    """Recursive helper function."""

    # List all items in src
    for name in os.listdir(src):
        src_path = os.path.join(src, name)
        dst_path = os.path.join(dst, name)

        # Copy files
        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)

        # Copy directories recursively
        else:
            print(f"Creating directory: {dst_path}")
            os.mkdir(dst_path)
            _copy_recursive(src_path, dst_path)

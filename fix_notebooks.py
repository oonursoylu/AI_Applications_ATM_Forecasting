import nbformat, glob

for path in glob.glob("notebooks/*.ipynb"):
    nb = nbformat.read(path, as_version=4)

    # Ensure required fields exist
    nb.setdefault("metadata", {})
    nb["metadata"].setdefault("kernelspec", {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    })
    nb["metadata"].setdefault("language_info", {
        "name": "python",
        "version": "3.x",
    })

    # Force-save with proper nbformat
    nbformat.write(nb, path)
    print(f"Fixed metadata in {path}")



def install_lib(lib):
    try:
        __import__(lib)
    except ImportError:
        import subprocess
        print("Устанавливаем нужные библиотеки, подождите пожалуйста...")
        subprocess.call(f"python -m pip install {lib}",
                        shell=True,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)
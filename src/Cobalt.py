try:
    import run_main
except KeyboardInterrupt:
    try:
        from colorama import init, Fore
        init(autoreset=True)
        print(Fore.RED + "You stopped the program!")
    except ImportError:
        print("You stopped the program")

try:
    import run_main
except KeyboardInterrupt:
    try:
        from colorama import init, Fore
        init()
        print(Fore.RED + "You stopped the program!" + Fore.RESET)
    except ImportError:
        print("You stopped the program")

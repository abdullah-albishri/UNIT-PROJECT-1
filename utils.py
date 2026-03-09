from __future__ import annotations

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class _Codes:
        RED = "\033[31m"
        GREEN = "\033[32m"
        YELLOW = "\033[33m"
        BLUE = "\033[34m"
        MAGENTA = "\033[35m"
        CYAN = "\033[36m"
        RESET = "\033[0m"
        RESET_ALL = "\033[0m"
    Fore = _Codes()
    Style = _Codes()

def colored(text: str, color: str) -> str:
    return f"{color}{text}{Style.RESET_ALL}"

def info(text: str) -> str:
    return colored(text, Fore.CYAN)

def success(text: str) -> str:
    return colored(text, Fore.GREEN)

def warning(text: str) -> str:
    return colored(text, Fore.YELLOW)

def error(text: str) -> str:
    return colored(text, Fore.RED)

from subprocess import run as run_block, Popen, PIPE, CalledProcessError
from sys import executable


class Escape:
    def __init__(self, avoid: str):
        self.avoid = avoid

    def __call__(self, string):
        i = 0
        s = []
        add = s.append
        size = len(string)
        avoid = self.avoid
        while i < size:

            # ignore back slashes and the char after them
            if string[i] == '\\':
                while i < size:
                    add(string[i])
                    i += 1

                    if string[i] != '\\':
                        add(string[i])
                        i += 1
                        break

            # avoid
            elif string[i] in avoid:
                add('\\')
                add(string[i])
                i += 1

            else:
                add(string[i])
                i += 1

        return "".join(s)


escape = Escape('"')
# escape_single_quote = Escape("'")
# escape_space = Escape(" ")
executable = '"'+executable+'"'


def bs(value: bytes):
    """bytes to string converter"""
    return str(value)[2:-1]


def run(*args) -> bytes:
    command = ' '.join(args)
    try:
        r = run_block(command, shell=True, stdout=PIPE, check=True)
    except CalledProcessError as e: raise OSError(
        f'{command} failed\n'
        f'{e.stderr}, Exit Code: {e.returncode}\n')
    if r.stderr: raise OSError(
        f'{command} failed\n'
        f'{r.stderr}, Exit Code: {r.returncode}\n')
    return r.stdout


def run_async(*args) -> Popen:
    """https://stackoverflow.com/questions/16071866/non-blocking-subprocess-call
    p = run_async("command")
    while p.poll() is None:
        ...
    p.stdout
    p.stderr
    """
    command = ' '.join(args)
    return Popen(command, shell=True, stdout=PIPE)


def python(*args): return run(executable, *args)
def python_code(*args): return run(executable, '-c', f'"{escape(";".join(args))}"')
def pytest(*args): return run(executable, '-m', 'pytest', *args)

def python_async(*args): return run_async(executable, *args)
def python_code_async(*args): return run_async(executable, '-c', f'"{escape(";".join(args))}"')
def pytest_async(*args): return run_async(executable, '-m', 'pytest', *args)

def pip(*args): return run(executable, '-m', 'pip', *args)
def git(*args): return run('git', *args)

def foo(a):
    return a + 1


def main():
    six = foo(5)
    print(six)

main()
    # line 9 calls main, goes to line 5 where main is defined, executes line 6, which calls foo, then goes to line 1,
    # where foo is defined, then executes line 2, which calculates a+1, where a=5, goes back to line 6, which calls foo
    # (Caller function), executes line 7, which prints 6


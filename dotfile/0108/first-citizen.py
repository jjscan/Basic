def answer():
    print(42)
    answer()

    def run_something(func):
        func()

        run_something(answer)
        print(type(run_something))

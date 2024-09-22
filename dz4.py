# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.
import argparse

def main():
    parser = argparse.ArgumentParser(description="Process a number and a string.")

    parser.add_argument("number", type=int, help="An integer number.")
    parser.add_argument("string", type=str, help="A string to be processed.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")
    parser.add_argument("--repeat", type=int, help="Number of times to repeat the string.")

    args = parser.parse_args()

    if args.verbose:
        print(f"Received number: {args.number}")
        print(f"Received string: '{args.string}'")
    repeat_count = args.repeat if args.repeat is not None else 1
    if args.verbose:
        print(f"Repeating string {repeat_count} time(s).")
    result = (args.string + ' ') * repeat_count
    result = result.strip()

    print(result)

if __name__ == "__main__":
    main()
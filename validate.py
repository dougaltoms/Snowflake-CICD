def main():

    import subprocess

    with open("files.txt", "r") as file:
        sql_files = file.read().splitlines()

    for script in sql_files:
        if '.sql' in script:
            result = subprocess.run(['sqlfluff', 'lint', script, '-d', 'snowflake'] , capture_output=True, text=True)
            print(f"Linting {script}")
            print(result.stdout)
            print("="*20)

if __name__ == "__main__":
    main()

def main():

    import subprocess
    import sys

    with open('sql_scripts.txt', 'r') as file:
        sql_files = file.read().splitlines()

    for script in sql_files:

        if script.endswith('.sql'):

            print('='*70)
            print(f'Validating {script}')

            result = subprocess.run(['sqlfluff', 'lint', script, '-d', 'snowflake'] , capture_output=True, text=True)
    
            if result.returncode == 1:
                print('Validation FAILED')
                print(f'{result.stdout}')
                sys.exit(1)

            else:
                print(f'{result.stdout}')
                print('='*70)

if __name__ == "__main__":
    main()

def main():

    import subprocess

    with open("files.txt", "r") as file:
        sql_files = file.read().splitlines()

    for script in sql_files:
        
        if '.sql' in script:
            print("="*70)
            print(f"Validating {script}")
            result = subprocess.run(['sqlfluff', 'lint', script, '-d', 'snowflake'] , capture_output=True, text=True)
            
            if result.returncode == 1:
                print(f"{result.stdout}")
                sys.exit(1)

            else:
                print(result.stdout)
                print("="*70)   

if __name__ == "__main__":
    main()

import db_utils


def main():
    with open('migration-script.sql', 'r') as file:
        script = file.readlines()

    db_utils.execute(script)


if __name__ == '__main__':
    main()

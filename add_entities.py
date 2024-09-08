import db_utils


def main():
    db_utils.execute("""
        CREATE OR REPLACE TABLE nicks (nick VARCHAR(100));
        INSERT INTO nicks VALUES
        ('fatty_dev'),
        ('cloud_master'), 
        ('god_of_gcp'), 
        ('fluffy_ops');
    """)


if __name__ == '__main__':
    main()

def main():

    from snowflake.snowpark import Session
    import pandas as pd
    
    snowflake_connection_parameters = {
                            "account": "nh13284.west-europe.azure"
                            , "user": "DOUGALTOMS" 
                            , "password": "Password123"
                            , "role": "ACCOUNTADMIN"
                            , "warehouse": "COMPUTE_WH"
                            }
    session = Session.builder.configs(snowflake_connection_parameters).create()

    print('Starting Deployment')
    df = session.sql('''SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.LOGIN_HISTORY;''').to_pandas()
    df.head()
    return print('Deployment Successful')

if __name__ == "__main__":
    main()

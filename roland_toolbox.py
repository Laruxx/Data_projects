import pyodbc, time, teradata, os
import pandas as pd
from math import ceil, floor

#####################################################################################################
# READ ME
#####################################################################################################

# Copy roland_toolbox.py file into your local directory similar to C:\Users\rheinze\AppData\Local\Programs\Python\Python36\Lib
# You will need to update the connect_db() function using the following guidelines:
# -- If using a DSN (Data Source Names) to connect to Teradata or Hive, you will need to create User Environment Variables called "TD_DSN" and "HIVE_DSN" with the same values as your local DSNs
# -- For example, my local DSNs are named "TeradataODBC" and "hive_lax1", so I created 2 User Environment Variables named "TD_DSN" with value "TeradataODBC" and "HIVE_DSN" with value "hive_lax1"
# -- To view your local DSNs, use pyodbc.dataSources()
# -- Otherwise, you will need to explicitly specify all the connection string parameters; you can use pyodbc.drivers() to view the names of the local drivers you have installed

#####################################################################################################
# EXAMPLES OF USING TOOLBOX FUNCTIONS
#####################################################################################################

# NOTE: if you need help with specific toolbox functions, use Python's help() function: e.g. help(query_db)
# NOTE: to use the write_table_from_query_batch() function you will need to create TABLEAU_LOGIN and TABLEAU_PASS User Environment Variables using your pod's login and password

# EXAMPLE 1

# from roland_toolbox import connect_db, query_db, write_table_from_query
# td = connect_db("td")
# td_query_str = '''
# SELECT *
# FROM acct.blizzard_login_daily bld
# JOIN acct.d_bnet_account dba
# ON dba.bnet_account_key = bld.bnet_account_key
# WHERE bld.login_date = '2018-10-23'
# SAMPLE 10
# '''
# td_df = query_db(td, td_query_str)

# EXAMPLE 2

# from roland_toolbox import connect_db, query_db, write_table_from_query_batch
# td = connect_db("td")
# hive = connect_db("hive")
# hive_query_str = "SELECT * FROM telem_pro.pro_lobby_endorsementlevelchange LIMIT 10"
# write_table_from_query_batch(
# hive,
# td,
# hive_query_str,
# 'dlab_rheinze.new_table',
# ['col_name1', 'col_name2', ...],
# ['integer', 'varchar(30)', 'col_name3 dtype', ...],
# 10000
# )
# query_db(td, 'dlab_rheinze.new_table')

#####################################################################################################

def connect_db(db_name):

    """
    use format " conn_obj = connect_db(str) ", e.g. " hive = connect_db('hive') "
    """
    
    print('CALLED CONNECT_DB FROM ROLAND_TOOLBOX')

    if db_name == 'hive':
        con = pyodbc.connect(dsn='{}'.format(os.environ.get('HIVE_DSN')),
                            trusted_connection='yes',
                            autocommit=True)
        print('Connected to Hive!')

    elif db_name == 'irvaag':
        con = pyodbc.connect(driver='ODBC Driver 17 for SQL Server',
                            server='IRVAAG4003.corp.blizzard.net,54003',
                            database='SALESFORCE',
                            trusted_connection='yes',
                            autocommit=True)
        print('Connected to IRVAAG!')

    elif db_name == 'td':
        con = pyodbc.connect(dsn='{}'.format(os.environ.get('TD_DSN')),
                            database='BIDW',
                            autocommit=True)
        print('Connected to Teradata!')

    elif db_name == 'tox':
        con = pyodbc.connect(driver='MySQL ODBC 8.0 ANSI Driver',
                            server='dev17-bi-toxicity.dev.cloud.blizzard.net',
                            port='3306',
                            database='toxic_db',
                            user='{}'.format(os.environ.get('TOX_LOGIN')),
                            password='{}'.format(os.environ.get('TOX_PASS')))
        print('Connected to ToxOrNot!')

    cur = con.cursor()
    return con, cur

#####################################################################################################

def connect_db_q(db_name):

    """
    this version of connect_db displays no output / print statements
    use format " conn_obj = connect_db(str) " or " hive = connect_db('hive') "
    """

    if db_name == 'hive':
        con = pyodbc.connect(dsn='{}'.format(os.environ.get('HIVE_DSN')),
                            trusted_connection='yes',
                            autocommit=True)

    elif db_name == 'irvaag':
        con = pyodbc.connect(driver='ODBC Driver 17 for SQL Server',
                            server='IRVAAG4003.corp.blizzard.net,54003',
                            database='SALESFORCE',
                            trusted_connection='yes',
                            autocommit=True)

    elif db_name == 'td':
        con = pyodbc.connect(dsn='{}'.format(os.environ.get('TD_DSN')),
                            database='BIDW',
                            autocommit=True)

    elif db_name == 'tox':
        con = pyodbc.connect(driver='MySQL ODBC 8.0 ANSI Driver',
                            server='dev17-bi-toxicity.dev.cloud.blizzard.net',
                            port='3306',
                            database='toxic_db',
                            user='{}'.format(os.environ.get('TOX_LOGIN')),
                            password='{}'.format(os.environ.get('TOX_PASS')))

    cur = con.cursor()
    return con, cur

#####################################################################################################

def disconnect_db(db_obj):

    print('CALLED DISCONNECT_DB FROM ROLAND_TOOLBOX')

    src_con, src_cur = db_obj

    src_cur.close()
    del src_cur
    src_con.close()

#####################################################################################################

def disconnect_db_q(db_obj):

    """
    this version of disconnect_db displays no output / print statements
    """

    src_con, src_cur = db_obj

    src_cur.close()
    del src_cur
    src_con.close()

#####################################################################################################

def query_db(src_obj, query_str):

    print('CALLED QUERY_DB FROM ROLAND_TOOLBOX')

    src_con, src_cur = src_obj

    start_time = time.time()
    df = pd.read_sql(query_str, src_con)
    end_time = time.time()
    
    print('Successfully Ran Query in {} Minutes!'.format(round((end_time-start_time)/60, 1)))
    return df

#####################################################################################################

def query_db_q(src_obj, query_str):

    """
    this version of query_db displays no output / print statements
    """

    src_con, src_cur = src_obj

    start_time = time.time()
    df = pd.read_sql(query_str, src_con)
    end_time = time.time()
    
    return df


#####################################################################################################

def command_db(src_obj, query_str):

    """
    this function executes a single command against a database
    """

    print('CALLED COMMAND_DB FROM ROLAND_TOOLBOX')

    src_con, src_cur = src_obj

    start_time = time.time()
    src_cur.execute(query_str)
    end_time = time.time()

    print('Successfully Ran Command in {} Minutes!'.format(round((end_time - start_time) / 60, 1)))

#####################################################################################################

def write_table_from_query(src_obj, dst_obj, query_str, table, cols, types, primary_index = None):

    """
    this function writes single rows sequentially to a table
    pass connect_db objects to src_obj and dst_obj
    e.g. write_table_from_query(td, hive, ...)
    pass column names and data types as lists of strings
    e.g. write_table_from_query(..., ['name_col1', 'name_col2'], ['data_type_col1', 'data_type_col2'], ...)
    primary_index is not required, but must be passed as a list of strings if included
    """

    print('CALLED WRITE_TABLE_FROM_QUERY FROM ROLAND_TOOLBOX')

    src_con, src_cur = src_obj
    dst_con, dst_cur = dst_obj

    cols_str = ', '.join(map(lambda x: str(x), cols))
    
    cols_types_str = ''
    for element in range(len(cols)):
        cols_types_str = cols_types_str + '{} {},'.format(cols[element], types[element])
    cols_types_str = cols_types_str[:len(cols_types_str)-1]

    df = pd.read_sql(query_str,src_con)
    df.dropna(how='all', inplace=True)

    try:
        dst_cur.execute('drop table {}'.format(table))
        print('{} Table Dropped!'.format(table))
    except:
        print('No {} Table to Drop!'.format(table))

    try:
        if primary_index == None:
            dst_cur.execute('create table {} ( {} )'.format(table, cols_types_str))
        else:
            primary_index_str = ','.join(primary_index)
            dst_cur.execute('create table {} ( {} ) unique primary index ( {} )'.format(table,
                                                                                        cols_types_str,
                                                                                        primary_index_str))
    except:
        print('{} Table Already Exists!'.format(table))

    df_tuples = list(map(lambda x: tuple(x), df.values.tolist()))

    values_str = '?,'*len(cols)
    values_str = values_str[:len(values_str)-1]

    print('Writing {} Records to {}...'.format(len(df_tuples),
                                               table))
    start_time = time.time()
    dst_cur.executemany('insert into {} ( {} ) values ( {} )'.format(table, cols_str, values_str), df_tuples)
    end_time = time.time()

    print('Table {} Successfully Written in {} Minutes!'.format(table, round((end_time-start_time)/60, 1)))


#####################################################################################################

def write_table_from_query_q(src_obj, dst_obj, query_str, table, cols, types, primary_index=None):

    """
    this version of write_table_from_query displays no output / print statements
    this function writes single rows sequentially to a table
    pass connect_db objects to src_obj and dst_obj
    e.g. write_table_from_query_q(td, hive, ...)
    pass column names and data types as lists of strings
    e.g. write_table_from_query_q(..., ['name_col1', 'name_col2'], ['data_type_col1', 'data_type_col2'], ...)
    primary_index is not required, but must be passed as a list of strings if included
    """

    src_con, src_cur = src_obj
    dst_con, dst_cur = dst_obj

    cols_str = ', '.join(map(lambda x: str(x), cols))

    cols_types_str = ''
    for element in range(len(cols)):
        cols_types_str = cols_types_str + '{} {},'.format(cols[element], types[element])
    cols_types_str = cols_types_str[:len(cols_types_str) - 1]

    df = pd.read_sql(query_str, src_con)
    df.dropna(how='all', inplace=True)

    try:
        dst_cur.execute('drop table {}'.format(table))
    except:
        pass

    try:
        if primary_index == None:
            dst_cur.execute('create table {} ( {} )'.format(table, cols_types_str))
        else:
            primary_index_str = ','.join(primary_index)
            dst_cur.execute('create table {} ( {} ) unique primary index ( {} )'.format(table,
                                                                                        cols_types_str,
                                                                                        primary_index_str))
    except:
        pass

    df_tuples = list(map(lambda x: tuple(x), df.values.tolist()))

    values_str = '?,' * len(cols)
    values_str = values_str[:len(values_str) - 1]

    start_time = time.time()
    dst_cur.executemany('insert into {} ( {} ) values ( {} )'.format(table, cols_str, values_str), df_tuples)
    end_time = time.time()

#####################################################################################################

def write_table_from_query_batch(src_obj, dst_obj, query_str, table, cols, types, batch_size, primary_index = None):

    """
    this function uses teradata python package for writing batches of rows to a table
    pass connect_db objects to src_obj and dst_obj
    e.g. write_table_from_query_batch(td, hive, ...)
    pass column names and data types as lists of strings
    e.g. write_table_from_query_batch(..., ['name_col1', 'name_col2'], ['data_type_col1', 'data_type_col2'], ...)
    primary_index is not required, but must be passed as a list of strings if included
    """

    print('CALLED WRITE_TABLE_FROM_QUERY_BATCH FROM ROLAND_TOOLBOX')

    src_con, src_cur = src_obj
    dst_con, dst_cur = dst_obj

    cols_str = ', '.join(map(lambda x: str(x), cols))
    
    cols_types_str = ''
    for element in range(len(cols)):
        cols_types_str = cols_types_str + '{} {},'.format(cols[element], types[element])
    cols_types_str = cols_types_str[:len(cols_types_str)-1]

    df = pd.read_sql(query_str, src_con)
    df.dropna(how='all', inplace=True)

    try:
        dst_cur.execute('drop table {}'.format(table))
        print('{} Table Dropped!'.format(table))
    except:
        print('No {} Table to Drop!'.format(table))

    try:
        if primary_index == None:
            dst_cur.execute('create table {} ( {} )'.format(table, cols_types_str))
        else:
            primary_index_str = ','.join(primary_index)
            dst_cur.execute(
                'create table {} ( {} ) unique primary index ( {} )'.format(table, cols_types_str, primary_index_str))
    except:
        print('{} Table Already Exists!'.format(table))

    values_str = '?,'*len(cols)
    values_str = values_str[:len(values_str)-1]

    df_current_index = 0
    df_index_end = len(df)

    start_time = time.time()

    batch_size_exception = 1

    while batch_size_exception == 1:

        try:

            batches = ceil((df_index_end-df_current_index)/batch_size)
            print('Writing {0} Records with {1} Batches of Size {2} to {3}...'.format(len(df), batches, batch_size, table))

            for i in list(range(batches)):

                df_batch = df.iloc[df_current_index:min(df_current_index+batch_size,df_index_end)]
                df_tuples = list(map(lambda x: tuple(x), df_batch.values.tolist()))

                with teradata.UdaExec(appName="roland_write_table",
                                      version="1.0",
                                      logConsole=False)\
                        .connect(method="odbc",
                                 system="bidw",
                                 username="{}".format(os.environ.get('TABLEAU_LOGIN')),
                                 password="{}".format(os.environ.get('TABLEAU_PASS'))) as session:
                    session.executemany('insert into {} ( {} ) values ( {} )'.format(table, cols_str, values_str),
                                        df_tuples,
                                        batch=True
                                        )

                df_current_index += batch_size

            batch_size_exception = 0

        except Exception as e:

            batch_size = int(floor(batch_size/2))
            # except Exception as e: print(e)
            print('Exception Encountered:\n{0}, Reducing Batch Size to {1}...'.format(e,batch_size))

    end_time = time.time()
    print('Table {} Successfully Written in {} Minutes!'.format(table, round((end_time-start_time)/60, 1)))

#####################################################################################################

def write_table_from_df(dst_obj, df, table, types, primary_index = None):

    """
    pass connect_db objects to dst_obj
    e.g. write_table_from_df(td, ...)
    pass column data types as lists of strings
    e.g. write_table_from_df(..., ['data_type_col1', 'data_type_col2'], ...)
    primary_index is not required, but must be passed as a list of strings if included
    """

    print('CALLED WRITE_TABLE_FROM_DF FROM ROLAND_TOOLBOX')

    dst_con, dst_cur = dst_obj

    cols_str = ','.join(df.columns.tolist())
    
    cols_types_str = ''
    for element in range(len(df.columns)):
        cols_types_str = cols_types_str + '{} {},'.format(df.columns[element], types[element])
    cols_types_str = cols_types_str[:len(cols_types_str)-1]

    try:
        dst_cur.execute('drop table {}'.format(table))
        print('{} Table Dropped!'.format(table))
    except:
        print('No {} Table to Drop!'.format(table))

    try:
        if primary_index == None:
            dst_cur.execute('create table {} ( {} )'.format(table, cols_types_str))
        else:
            primary_index_str = ','.join(primary_index)
            dst_cur.execute('create table {} ( {} ) unique primary index ( {} )'.format(table, cols_types_str, primary_index_str))
        print('{} Table Created!'.format(table))
    except:
        print('{} Table Already Exists!'.format(table))

    df_tuples = list(map(lambda x: tuple(x), df.values.tolist()))

    values_str = '?,'*len(df.columns)
    values_str = values_str[:len(values_str)-1]

    print('Writing {} Records to {}...'.format(len(df_tuples), table))
    start_time = time.time()
    dst_cur.executemany('insert into {} ( {} ) values ( {} )'.format(table, cols_str, values_str), df_tuples)
    end_time = time.time()

    print('Table {} Successfully Written in {} Minutes!'.format(table, round((end_time-start_time)/60, 1)))

#####################################################################################################

#####################################################################################################

def write_table_from_df_q(dst_obj, df, table, types, primary_index = None):

    """
    this version of write_table_from_df displays no output / print statements
    pass connect_db objects to dst_obj
    e.g. write_table_from_df_q(td, ...)
    pass column data types as lists of strings
    e.g. write_table_from_df_q(..., ['data_type_col1', 'data_type_col2'], ...)
    primary_index is not required, but must be passed as a list of strings if included
    """

    dst_con, dst_cur = dst_obj

    cols_str = ','.join(df.columns.tolist())

    cols_types_str = ''
    for element in range(len(df.columns)):
        cols_types_str = cols_types_str + '{} {},'.format(df.columns[element], types[element])
    cols_types_str = cols_types_str[:len(cols_types_str) - 1]

    try:
        dst_cur.execute('drop table {}'.format(table))
    except:
        pass

    try:
        if primary_index == None:
            dst_cur.execute('create table {} ( {} )'.format(table, cols_types_str))
        else:
            primary_index_str = ','.join(primary_index)
            dst_cur.execute(
                'create table {} ( {} ) unique primary index ( {} )'.format(table, cols_types_str, primary_index_str))
    except:
        pass

    df_tuples = list(map(lambda x: tuple(x), df.values.tolist()))

    values_str = '?,' * len(df.columns)
    values_str = values_str[:len(values_str) - 1]

    start_time = time.time()
    dst_cur.executemany('insert into {} ( {} ) values ( {} )'.format(table, cols_str, values_str), df_tuples)
    end_time = time.time()

#####################################################################################################

def write_table_from_df_batch(dst_obj, df, table, types, batch_size, primary_index = None):

    """
    pass connect_db objects to dst_obj
    e.g. write_table_from_query(td, ...)
    pass column data types as lists of strings
    e.g. write_table_from_query(..., ['data_type_col1', 'data_type_col2'], ...)
    primary_index is not required, but must be passed as a list of strings if included
    """

    print('CALLED WRITE_TABLE_FROM_DF_BATCH FROM ROLAND_TOOLBOX')

    dst_con, dst_cur = dst_obj

    cols_str = ','.join(df.columns.tolist())
    
    cols_types_str = ''
    for element in range(len(df.columns)):
        cols_types_str = cols_types_str + '{} {},'.format(df.columns[element], types[element])
    cols_types_str = cols_types_str[:len(cols_types_str)-1]

    try:
        dst_cur.execute('drop table {}'.format(table))
        print('{} Table Dropped!'.format(table))
    except:
        print('No {} Table to Drop!'.format(table))

    try:
        if primary_index == None:
            dst_cur.execute('create table {} ( {} )'.format(table, cols_types_str))
        else:
            primary_index_str = ','.join(primary_index)
            dst_cur.execute('create table {} ( {} ) unique primary index ( {} )'.format(table, cols_types_str, primary_index_str))
        print('{} Table Created!'.format(table))
    except:
        print('{} Table Already Exists!'.format(table))

    values_str = '?,'*len(cols)
    values_str = values_str[:len(values_str)-1]

    df_current_index = 0
    df_index_end = len(df)

    start_time = time.time()

    batch_size_exception = 1

    while batch_size_exception == 1:

        try:

            batches = ceil((df_index_end-df_current_index)/batch_size)
            print('Writing {0} Records with {1} Batches of Size {2} to {3}...'.format(len(df), batches, batch_size, table))

            for i in list(range(batches)):

                df_batch = df.iloc[df_current_index:min(df_current_index+batch_size,df_index_end)]
                df_tuples = list(map(lambda x: tuple(x), df_batch.values.tolist()))

                with teradata.UdaExec(appName="roland_write_table",
                                      version="1.0",
                                      logConsole=False)\
                        .connect(method="odbc",
                                 system="bidw",
                                 username="{}".format(os.environ.get('TABLEAU_LOGIN')),
                                 password="{}".format(os.environ.get('TABLEAU_PASS'))) as session:
                    session.executemany('insert into {} ( {} ) values ( {} )'.format(table, cols_str, values_str), df_tuples, batch=True)

                df_current_index += batch_size

            batch_size_exception = 0

        except Exception as e:

            batch_size = int(floor(batch_size/2))
            # except Exception as e: print(e)
            print('Exception Encountered:\n{0}, Reducing Batch Size to {1}...'.format(e, batch_size))

    end_time = time.time()

    print('Table {} Successfully Written in {} Minutes!'.format(table, round((end_time-start_time)/60, 1)))

################################################################################

def volatile_table_to_df(src_obj, create_volatile_table_query_str, volatile_table):

    """
    create_volatile_table_query_str should be a CREATE VOLATILE TABLE statement
    The 3rd function argument, volatile_table, must match the volatile table name from the CREATE VOLATILE TABLE statement
    """

    print('CALLED VOLATILE_TABLE_TO_DF FROM ROLAND_TOOLBOX')

    src_con, src_cur = src_obj

    start_time = time.time()
   
    try:
        src_cur.execute(query_str)
        df = pd.read_sql("select * from {}".format(volatile_table), src_con)

    except:
        src_cur.execute('drop table {}'.format(volatile_table))
        src_cur.execute(query_str)
        df = pd.read_sql("select * from {}".format(volatile_table), src_con)

    end_time = time.time()

    print('Created Volatile Table {} in {} Minutes!'.format(table, round((end_time-start_time)/60, 1)))
    return df
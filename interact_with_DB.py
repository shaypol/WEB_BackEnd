import mysql.connector


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='0548030690Sp',
                                         database='myappnewdb'
                                         )
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query.result = cursor.fetchall()
        return_value = True

    connection.close()
    cursor.close()
    return return_value

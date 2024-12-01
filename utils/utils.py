def cvtLstIntToSql(integer_list):
    formatted_string = ', '.join(str(num) for num in integer_list)
    return f"({formatted_string})"

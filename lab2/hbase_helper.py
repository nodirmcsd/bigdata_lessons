#!/usr/bin/env python
import sys
import happybase

__author__ = 'nodir'
def create_table:
    table_name = 'nodir.azam'
    host = 'cluster2.newprolab.com'
    connection = happybase.Connection(host)
    families = { 'data': dict(max_versions=4096)
    }

if not connection.is_table_enabled(table_name):
    connection.delete_table(table_name, True)

connection.create_table(table_name, families)

table = connection.table(table_name)
table.put('row-key', {'data:url': 'ya.ru'})

row = table.row('row-key')
print row['family:qual1']  # prints 'value1'

for key, data in table.rows(['row-key-1', 'row-key-2']):
    print key, data  # prints row key and data for each row

for key, data in table.scan(row_prefix='row'):
    print key, data  # prints 'value1' and 'value2'

row = table.delete('row-key')


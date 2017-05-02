from django.db import connection
cursor = connection.cursor()
cursor.execute("TRUNCATE TABLE `Category`")
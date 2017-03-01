__author__ = 'ys'
from public.Config import *
import MySQLdb


class XykSprider:
	_db = None

  	@staticmethod
  	def db():
	    if XykSprider._db is None:
	    	XykSprider._db = MySQLdb.connect(mysql_address, mysql_user, mysql_password, "xyk")
	    	XykSprider._db.set_character_set('utf8')

		try:
			XykSprider._db.ping()
		except:
			XykSprider._db = MySQLdb.connect(mysql_address, mysql_user, mysql_password, "xyk")
	    	XykSprider._db.set_character_set('utf8')
	    return XykSprider._db

	@staticmethod
	def add(bank_id, name, rangedate, url):
		name = MySQLdb.escape_string(name)
		cursor = XykSprider.db().cursor()
		sql = "INSERT INTO s_sprider(  `bank_id` ,  `name` ,  `url` ,  `range_date` ,  `time` ) VALUES ( %d,  '%s',  '%s',  '%s', now())"
		sql = sql % (bank_id, name, url, rangedate)
		cursor.execute(sql)
		XykSprider.db().commit()

	@staticmethod
	def check(bank_id, name, url):
		cursor = XykSprider.db().cursor()
		sql = "SELECT id FROM s_sprider WHERE bank_id = %d and name = '%s' and url = '%s'"
		sql = sql % (bank_id, name, url)
		cursor.execute(sql)
		results = cursor.fetchall()
		if len(results) > 0:
			return True
		return False




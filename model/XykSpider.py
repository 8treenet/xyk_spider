__author__ = 'ys'
from public.Config import *
import MySQLdb
import time


class XykSpider:
	_db = None

  	@staticmethod
  	def db():
	    if XykSpider._db is None:
	    	XykSpider._db = MySQLdb.connect(mysql_address, mysql_user, mysql_password, "xyk")
	    	XykSpider._db.set_character_set('utf8mb4')

		try:
			XykSpider._db.ping()
		except:
			XykSpider._db = MySQLdb.connect(mysql_address, mysql_user, mysql_password, "xyk")
	    	XykSpider._db.set_character_set('utf8mb4')
	    return XykSpider._db

	@staticmethod
	def add(bank_id, name, rangedate, url, beginDate, endDate):
		try:
			time.strptime(beginDate, "%Y-%m-%d")
			beginDate = "'" + beginDate+  "'"
		except:
			beginDate = 'NULL'
		try:
			time.strptime(endDate, "%Y-%m-%d")
			endDate = "'" + endDate+  "'"
		except:
			endDate = 'NULL'
		name = MySQLdb.escape_string(name)
		cursor = XykSpider.db().cursor()
		sql = "INSERT INTO s_spider (`bank_id`, `name`, `url`, `range_date`, `begin_date`, `end_date`, `time`) VALUES ( %d, '%s', '%s', '%s', %s,  %s, now())"
		sql = sql % (bank_id, name, url, rangedate, beginDate, endDate)
		try:
			cursor.execute(sql)
		except:
			print sql
		XykSpider.db().commit()

	@staticmethod
	def check(bank_id, name, url):
		cursor = XykSpider.db().cursor()
		sql = "SELECT id FROM s_spider WHERE bank_id = %d and name = '%s' and url = '%s'"
		sql = sql % (bank_id, name, url)
		cursor.execute(sql)
		results = cursor.fetchall()
		if len(results) > 0:
			return True
		return False




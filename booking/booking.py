# -*- coding: utf-8 -*-
# Copyright (c) 2021, Sowbarnika and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Booking(Document):
	def before_save(self):
		self.amountbalance=float(self.siteprice)-float(self.amountpaid)
		name=frappe.db.get_value("Booking", {'sitename':self.sitename},"name")
		if name and name!=self.name:
			frappe.throw("already booked")

		

# -*- coding: utf-8 -*-
# Copyright (c) 2021, Sowbarnika and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Payment(Document):
	def before_submit(self):
		doc=frappe.get_doc('Booking',self.booking)
		doc.amountpaid=self.installmentprice+doc.amountpaid
		doc.save()
	

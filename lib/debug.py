#!/usr/bin/env python3
# lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

# Drop and recreate the table
Department.drop_table()
Department.create_table()

# Create new departments
payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)  # <Department 2: Human Resources, Building C, East Wing>

# Update HR department details
hr.name = 'HR'
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)  # <Department 2: HR, Building F, 10th Floor>

# Delete Payroll department from the DB (object still exists in memory)
print("Delete Payroll")
payroll.delete()
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

# Start interactive debugging session
ipdb.set_trace()

#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None, approved_jobs=None):
        self.approved_jobs = APPROVED_JOBS or []
        self._name = None
        self._job = None
        if name is not None:
            self.name = name
        if job is not None:
            self.job = job


    def get_name(self):
        return self._name
    

    def set_name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value.title()

  
    def get_job(self):
        return self._job
    

    def set_job(self, value):
        if value not in self.approved_jobs:
            print("Job must be in list of approved jobs.")
        else:
            self._job = value


    name = property(get_name, set_name)
    job = property(get_job, set_job)

jamal = Person(name='jamal')
jamal.job = "Marketing"
print(jamal.name)
print(jamal.job)
    
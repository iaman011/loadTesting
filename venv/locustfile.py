'''
Locust is a Python-based open-source tool used to generate fake load or simulate traffic to a system, 
typically for load testing and performance testing of web applications, APIs, or other services.
'''

from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # Simulate user think time between requests

    @task(3)
    def load_homepage(self):
        self.client.get("/")

    @task(1)
    def load_products(self):
        self.client.get("/products")

    @task(1)
    def load_cart(self):
        self.client.get("/cart")


'''
to run:  locust -f locustfile.py --host=http://localhost:5000
'''

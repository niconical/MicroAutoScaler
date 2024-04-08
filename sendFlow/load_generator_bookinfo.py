from locust import HttpUser, TaskSet, task, constant
from locust import LoadTestShape
import random
from random import randint, choice
import base64

class BookInfoUserTasks(TaskSet):
    def __init__(self, parent):
        super().__init__(parent)
        

    @task(1)
    def get_productpage(self):
        self.client.get("/productpage")
    
    @task(1)
    def get_details(self):
        self.client.get("/details")

    @task(1)
    def get_reviews(self):
        self.client.get("/reviews")
    
    @task(1)
    def get_ratings(self):
        self.client.get("/ratings")

class WebsiteUser(HttpUser):
    def on_start(self):
        return super().on_start()

    def on_stop(self):
        return super().on_stop()
    host = "http://localhost:30001"
    wait_time = constant(1)
    tasks = [BookInfoUserTasks]
    # tasks = [SockShopUserTasks]
    
class StagesShape(LoadTestShape):
    def __init__(self):
        super().__init__()
        lines = []
        with open("./random-100max.req", 'r') as f:
        #with open("/home/ssj/boutiquessj/pyboutique/sendflow/normalFlow.req", 'r') as f:
            lines = list(map(int, f.readlines()))
            lines = [x for i,x in enumerate(lines) if i%1==0]
            self.lines = ([1]*5+lines+[1]*5)
            #self.lines = lines
    
    def tick(self):
        run_time = self.get_run_time()
        # for i in range(1, 100):
        #     return (i,1)
        #while True:
        for _ in range(10):#
            for i, v in enumerate(self.lines):
                #if run_time < (i+1)*10:#internal 10s
                if run_time < (i+1)*5:#internal为5
                    tick_data = (v, 100)                
            # user_count -- Total user count
            # spawn_rate -- Number of users to start/stop per second when changing number of users
                    # tick_data = (26, 100)
                    return tick_data
        # for stage in self.stages:
        #     if run_time < stage["duration"]:
        #         tick_data = (stage["users"], stage["spawn_rate"])
        #         return tick_data


# if __name__ == '__main__':
#     lines = []
#     with open("/home/meng/random-100max.req", 'r') as f:
#         lines = list(map(int, f.readlines()))
#         lines = [x for i,x in enumerate(lines) if i%3==0]
#     print(len(lines))

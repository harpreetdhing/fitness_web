from pymysql import *

class connections:
    def ConnectMe(self):
        con = connect("localhost", "root", "", "fitness_web")
        return con

from Data.DBConnection import DBConnection
from Models.Agent import Agent


class AgentDAL():

   def __init__(self):
       self.agents = []


   @staticmethod
   def add_agent(new_agent: Agent):
       query = """
       INSERT INTO agents (codeName, realName, location, status, missionsCompleted)
       VALUES (%s, %s, %s, %s, %s)
       """


       values = (
           new_agent.code_name,
           new_agent.real_name,
           new_agent.location,
           new_agent.status,
           new_agent.missions_completed
       )

       DBConnection.execute_query(query,values)
       AgentDAL.get_information(query,values)



   def delete_agent(self):
       pass

   def update_agent(self):
       pass

   def get_agent(self):
       pass

   @staticmethod
   def get_information(query, values):
       rows_inserted = DBConnection.execute_query(query, values)
       if rows_inserted:
           print("Agent inserted successfully.")
       else:
           print("Failed to insert agent.")


a = Agent("x","isaac","israel","live",24)
AgentDAL.add_agent(a)









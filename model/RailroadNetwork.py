from Tunnel import Tunnel
from RailwaySection import RailwaySection

class RailroadNetwork:

    def __init__(self, num_max_trains_per_section,tunnel,railway_section):
       self.__num_max_trains_per_section = num_max_trains_per_section
       self.__tunnel=tunnel
       self.__railway_section= railway_section
    
    @property
    def num_max_trains_per_section(self):
        return self.__num_max_trains_per_section

    @property
    def tunnel(self):
        return self.__tunnel

    @property
    def railway_Section(self):
        return self.__railway_section

    # @num_max_trains_per_section.setter
    # def num_max_trains_per_section(self,new):
    #     self.__num_max_trains_per_section = new


    def train_position(section,position):
        return


    def delete_train(section,position):
        return

    def tunnel_position(num_blue_section,num_red_section):#incompleto
        return

    def position_regulation_center(section,num_trains):
        return

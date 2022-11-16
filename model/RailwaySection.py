from Section import Section
from RegualtionCenter import RegualtionCenter


class RailwaySection():

    def __init__(self, max_trains_per_section, positions_free, section: Section, regulation_center: RegualtionCenter):
        self.__max_trains_per_section = max_trains_per_section
        self.__positions_free = positions_free
        self.__section = section
        self.__regulation_center = regulation_center

    @property
    def __max_trains_per_section(self):
        return self.__max_trains_per_section

    @property
    def __positions_free(self):
        return self.__positions_free

    @property
    def __section(self):
        return self.__section

    @property
    def __regulation_center(self):
        return self.__regulation_center

    @__max_trains_per_section.setter
    def __max_trains_per_section(self, max_trains_per_section):
        self.__max_trains_per_section = max_trains_per_section

    @__positions_free.setter
    def __positions_free(self, positions_free):
        self.__positions_free = positions_free

    @__section.setter
    def __section(self, section: Section):
        self.__section = section

    @__regulation_center.setter
    def __regulation_center(self, regulation_center: RegualtionCenter):
        self.__regulation_center = regulation_center

    def __is_position_free(position):
        is_position_free
        if position > 0:
            is_position_free = True
        else:
            is_position_free = False
        return is_position_free

    def __is_tunnel(position):
        is_tunnel
        if position > 0:
            is_tunnel = True
        else:
            is_tunnel = False
        return is_tunnel

    def __is_regulation_center(position):
        is_regulation_center
        if position > 0:
            is_regulation_center = True
        else:
            is_regulation_center = False
        return is_regulation_center

    def __regulation_center_position(position):
        return position

    def __section_length(lenght):
        return lenght

    def __get_regulation_center(self):
        return self.__regulation_center

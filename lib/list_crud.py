def create_an_empty_list():
    return []

def create_a_list():
    return [0,1,2,3]

def add_element_to_end_of_list(one_list, element):
    one_list.append(element)
    return one_list

def add_element_to_start_of_list(second_list, element):
    second_list.insert(0, element)
    return second_list

def remove_element_from_end_of_list(third_list):
    third_list.pop()
    return third_list

def remove_element_from_start_of_list(fourth_list):
    del fourth_list[0]
    return fourth_list

def retrieve_first_element_from_list(fifth_list):
    fifth_list[0]
    return fifth_list[0]

def retrieve_element_from_index(sixth_list, index):
    len(sixth_list)
    return sixth_list[index]

def retrieve_last_element_from_list(seventh_list):
    seventh_list[-1]
    return seventh_list[-1]

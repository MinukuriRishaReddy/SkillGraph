class Candidate:
    def __init__(self, content=None, lo=None):
        if content is None:
            self.content = []
            self.size = 0
            self.lo_reference = lo
        else:
            self.content = list(content)
            self.size = len(self.content)
            self.lo_reference = lo

    def get_value(self):
        return self.content

    def extend_value(self, value):
        self.content.extend(value)
        self.content = list(set(self.content))
        self.size = len(self.content)

    def get_lo_reference(self):
        return self.lo_reference


def convert_list_object_to_list_course(objects):
    list_course = []
    for element in objects:
        list_course.extend(element.get_value())
    return list(set(list_course))

class ComplexPhones(object):
 
    def __init__(self):
 
        pass
 
    def phone(self, phone_name):
 
        return "ComplexPattern[% s]" % (phone_name)
 
 
class PhoneBrands(object):
 
    phone_brands = {}
 
    def __new__(cls, name, phone_brands_id):
        try:
            id = cls.phone_brands[phone_brands_id]
        except KeyError:
            id = object.__new__(cls)
            cls.phone_brands[phone_brands_id] = id
        return id
 
    def set_phone_info(self, phone_info):

        cg = ComplexPhones()
        self.phone_info = cg.phone(phone_info)
 
    def get_phone_info(self):
 
        return (self.phone_info)
 
phone_data = (('a', 1, 'Apple'), ('a', 2, 'Samsung'), ('b', 1, 'Apple'))
phone_brands_objects = []
for i in phone_data:
    obj = PhoneBrands(i[0], i[1])
    obj.set_phone_info(i[2])
    phone_brands_objects.append(obj)

for i in phone_brands_objects:
    print("id = " + str(id(i)))
    print(i.get_phone_info())
from api.module.hierarchy.hierarchy_repository import HierarchyRepository

def populate_hierarchy():
    hierarchyRepository = HierarchyRepository()
    hierarchy_list = [
        {
            "name": "admin",
            "sub_tag": "admin",
            "level": -1
        },
        {
            "name": "Gerente",
            "sub_tag": "manager",
            "level": 3
        },
        {
            "name": "Funcionário",
            "sub_tag": "employee",
            "level": 4
        },
        {
            "name": "Cliente",
            "sub_tag": "client",
            "level": 5
        }
    ]

    for item in hierarchy_list:
        checkAlreadyExists = hierarchyRepository.count_by_field("sub_tag", item['sub_tag'])

        if(checkAlreadyExists == 0):
            class Hierarchy:
                def __init__(self, name, sub_tag, level) -> None:
                    self.name = name
                    self.sub_tag = sub_tag
                    self.level = level

            print("name: {}".format(item["name"]))
            hierarchyRepository.save(Hierarchy(item["name"], item["sub_tag"], item["level"]))
            

    print("finished")
    return []


populate_hierarchy()
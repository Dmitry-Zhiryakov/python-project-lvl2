REMOVED = 'removed'
ADDED = 'added'
NESTED = 'nested'
UNCHANGED = 'unchanged'
CHANGED = 'changed'


def build_tree(dict_1, dict_2):

    def get_nodes_(dict_1, dict_2):
        keys = sorted(dict_1.keys() | dict_2.keys())
        nodes = []
        for key in keys:
            node_1 = dict_1.get(key)
            node_2 = dict_2.get(key)
            if key not in dict_2:
                nodes.append({'key': key,
                              'type': REMOVED,
                              'value': dict_1[key]
                              })
            elif key not in dict_1:
                nodes.append({'key': key,
                              'type': ADDED,
                              'value': dict_2[key]
                              })
            elif isinstance(node_1, dict) and isinstance(node_2, dict):
                nodes.append({'key': key,
                              'type': NESTED,
                              'children': get_nodes_(node_1, node_2)
                              })
            elif node_1 == node_2:
                nodes.append({'key': key,
                              'type': UNCHANGED,
                              'value': dict_1[key],
                              })
            elif node_1 != node_2:
                nodes.append({'key': key,
                              'type': CHANGED,
                              'value_from_dict1': dict_1[key],
                              'value_from_dict2': dict_2[key]
                              })
        return nodes

    return {'type': 'root', 'children': get_nodes_(dict_1, dict_2)}

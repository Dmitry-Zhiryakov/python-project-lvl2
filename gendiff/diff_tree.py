def build_tree(dict_1, dict_2):

    def get_nodes(dict_1, dict_2):
        keys = sorted(dict_1.keys() | dict_2.keys())
        nodes = []
        for key in keys:
            node_1 = dict_1.get(key)
            node_2 = dict_2.get(key)
            if key not in dict_2:
                nodes.append({'key': key,
                              'value': dict_1[key],
                              'type': 'deleted'
                              })
            elif key not in dict_1:
                nodes.append({'key': key,
                              'value': dict_2[key],
                              'type': 'added'
                              })
            elif isinstance(node_1, dict) and isinstance(node_2, dict):
                nodes.append({'key': key,
                              'children': get_nodes(node_1, node_2),
                              'type': 'nested'
                              })
            elif node_1 == node_2:
                nodes.append({'key': key,
                              'value': dict_1[key],
                              'type': 'unchanged'
                              })
            elif node_1 != node_2:
                nodes.append({'key': key,
                              'value_from_dict1': dict_1[key],
                              'value_from_dict2': dict_2[key],
                              'type': 'changed'
                              })
        return nodes

    return {'type': 'root', 'children': get_nodes(dict_1, dict_2)}

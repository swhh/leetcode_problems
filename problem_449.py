import json

"""Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.



Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree."""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(root):

    def jsonify(root):
        if not root:
            return
        json_obj = {f'{root.val}':
                        {'left':
                             jsonify(root.left),
                         'right':
                             jsonify(root.right)}
                    }
        return json_obj
    json_obj = jsonify(root)
    return json.dumps(json_obj)


def deserialize(data):
    json_obj = json.loads(data)

    def deserialize_recursive(json_object):
        if not json_object:
            return
        val = list(json_object.keys())[0]
        node = TreeNode(int(val))
        left, right = json_object[val]['left'], json_object[val]['right']
        node.left = deserialize_recursive(left)
        node.right = deserialize_recursive(right)
        return node

    return deserialize_recursive(json_obj)


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

str = serialize(root)
print(str)
print(deserialize(str).right.val)

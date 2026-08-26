class Solution(object):
    def pathSum(self, root, targetSum):
        dictH = {}
        counter = [0]
        pathSumRec(root, targetSum, dictH, counter, 0)
        return counter[0]

def pathSumRec(root, targetSum, dictH, counter, curr_path):
    if not root:
        return None
    new_path = curr_path + root.val
    if new_path == targetSum:
        if 0 in dictH:
            counter[0] += dictH[0]+1
        else:
            counter[0] += 1
    if new_path - targetSum in dictH and new_path != targetSum:
        counter[0] += dictH[new_path-targetSum]
    if new_path in dictH:
        dictH[new_path] += 1
    else:
        dictH[new_path] = 1
    dict_l = {}
    dict_r = {}
    for num in dictH:
        dict_l[num] = dictH[num]
        dict_r[num] = dictH[num]
    pathSumRec(root.left, targetSum, dict_l, counter, new_path)
    pathSumRec(root.right, targetSum, dict_r, counter, new_path)

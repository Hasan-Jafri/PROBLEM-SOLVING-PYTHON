'''
997. Find the Town Judge

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n

'''

def findJudge(n,trust):
    # Corner Case.
    if n == 1:
        return 1
    trusted = {}
    # Putting sets in the dictionary elements to tackle unique and for efficient searching.
    for i in range(1,n+1):
        trusted[i] = set()
    # Filling dictionary with all trsuts. for every key the number it trusts is sotred in its value.
    for i in trust:
        if i[1] not in trusted[i[0]]:
            trusted[i[0]].add(i[1])
    # Now I check for empty set as the judge is trusted by everyone but it trusts none.
    for i in range(1,n+1):
        judge = i
        found = False
        if len(trusted[judge]) == 0:
            for key, value in trusted.items():
                if judge in trusted[key]:
                    found = True
                elif judge == key:
                    continue
                else:
                    found = False
                    break
            if found:
                return judge
    # If no judge then we return -1
    return -1

# Sample Input
n = 3
trust = [[1,3],[2,3],[3,1]]
print(findJudge(n = n,trust = trust))
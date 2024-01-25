'''
2225. Find Players With Zero or One Losses

You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
 

Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
 

Constraints:

1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri
All matches[i] are unique.
'''

# The logic used in this algorithm is keeping the idea of the losses and know how many players participated.

# I used a dictionary to keep the idea of losses.

# Used set to get every player that participated and if any player does not lost he will not be in the dictionary.

# I could have used a list but I used it to avoid any duplication in an efficient manner. Searching in a list is O(n) while, in a set it is O(1).

# After declaration using loop I stored the loss data in the dictionary and unique values in a set.

# The next step is easy as I just iterate throguh the set and checking for loss count, if it is not in the dictionary I simple add it to the list no_loss.

# If it is exactly one I add it to the list of one_loss.

# At the last line simply return both the arrays/lists combined.


def findWinners(matches):
    loser_check = {}
    player = set()
    for match in matches:
        if match[1] not in loser_check:
            loser_check[match[1]] = 1
        else:
            loser_check[match[1]] += 1

        player.add(match[1])
        player.add(match[0])
    no_loss = []
    one_loss = []
    for i in player:
        if i in loser_check:
            if loser_check[i] == 1:
                one_loss.append(i)
        else:
            no_loss.append(i)
    return [sorted(no_loss),sorted(one_loss)]

# Sample Input
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(findWinners(matches = matches))

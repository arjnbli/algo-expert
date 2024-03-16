# Approach: Hash Map
# Time: O(n^2)
# Space: O(n)
# n is the number of teams in the round robin competition
def tournamentWinner(competitions, results):
    points = {}
    maxPoints = 0
    winner = None
    for idx, [homeTeam, awayTeam] in enumerate(competitions):
        matchWinner = homeTeam if results[idx] == 1 else awayTeam
        if matchWinner not in points:
            points[matchWinner] = 3
        else:
            points[matchWinner] += 3
        if points[matchWinner] > maxPoints:
            maxPoints = points[matchWinner]
            winner = matchWinner
    return winner

# O(k * log(k)) time | O(k) space
# k is the number of workers
def taskAssignment(k, tasks):
    # Write your code here.
    tasks = [(task, idx) for idx, task in enumerate(tasks)]
    tasks.sort(key=lambda x: x[0])
    assignments = []
    left = 0
    right = len(tasks) - 1
    while left < right:
        assignment = [tasks[left][1], tasks[right][1]]
        assignments.append(assignment)
        left += 1
        right -= 1
    return assignments
    
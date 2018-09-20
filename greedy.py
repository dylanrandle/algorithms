## greedy algorithms assignment

def read_file():
    with open('data/jobs.txt') as f:
        data = f.readlines()
    num_jobs = int(data[0])
    jobs = {}
    for i, d in enumerate(data[1:]):
        d = d.split()
        jobs[i] = (int(d[0]),int(d[1]))
    return num_jobs, jobs

num_jobs, jobs = read_file()

def compute_weighted_sum(sorted_scores, jobs):
    current_time = 0
    total = 0
    for score in sorted_scores:
        job_id = score[0]
        current_time += jobs[job_id][1]
        total += jobs[job_id][0]*current_time
    return total

def schedule_by_difference(num_jobs, jobs):
    scores = {}
    # compute scores (weight - length)
    for job in jobs:
        scores[job] = [jobs[job][0] - jobs[job][1],  jobs[job][0]]
    # sort by scores, break ties with weight
    # => sort by weights descending, then scores descending
    sorted_scores = sorted(scores.items(), key=lambda v: v[1], reverse=True)
    # compute weighted sum
    return compute_weighted_sum(sorted_scores, jobs)

print('Difference total is : %d' % schedule_by_difference(num_jobs, jobs))

def schedule_by_ratio(num_jobs, jobs):
    scores = {}
    # compute scores (weight/length)
    for job in jobs:
        scores[job] = jobs[job][0]/jobs[job][1]
    # sort by scores, descending
    sorted_scores = sorted(scores.items(), key=lambda v: v[1], reverse=True)
    # compute weighted sum
    return compute_weighted_sum(sorted_scores, jobs)

print('Ratio total is : %d' % schedule_by_ratio(num_jobs, jobs))

def read_graph():
    return [list(map(int, x.split(' '))) for x in open('data/edges.txt', 'r').read().split('\n')[1:-1]]

edges = read_graph()

def prim(edges):
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    spanned = set()
    spanned.add(vertices.pop())

    total_cost = 0
    while len(vertices)>0:
        best_cost = 1e6
        for edge in edges:
            if edge[0] in spanned and edge[1] in vertices and edge[2]<best_cost:
                best_cost = edge[2]
                best_vert = edge[1]
            if edge[1] in spanned and edge[0] in vertices and edge[2]<best_cost:
                best_cost = edge[2]
                best_vert = edge[0]
        spanned.add(best_vert)
        vertices.remove(best_vert)
        total_cost += best_cost
    return total_cost

print('Prim cost is %d ' % prim(edges))


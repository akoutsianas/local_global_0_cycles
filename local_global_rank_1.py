import plotly.express as px


def compute_torsion_points(a, E7):
    Q7 = E7.base_ring()
    t = polygen(Q7, 't')
    for r3 in (t**2 + 3).roots():
        w = (1 + 3*r3[0])/7
        if w.valuation() >= 0:
            break
    z3 = (t**2 + t + 1).roots()[0][0]
    theta = 2 * a * w
    r3_theta = (t ** 3 - theta).roots()[0][0]
    ytor = (t**2 - (theta + a)).roots()[0][0]
    tors = [E7([0,1,0])]
    for i in range(3):
        T1 = E7(r3_theta * z3**i, ytor)
        T2 = E7(r3_theta * z3**i, -ytor)
        tors.append(T1)
        tors.append(T2)
    return tors


def rank_one_elliptic_curves(N):
    bounds_not_equal = []
    not_compute_gens = []
    success = []
    failure = []
    Q7 = Qp(7, 20)
    for k in range(-N, N + 1):
        a = -2 + 7*k
        E = EllipticCurve([0, a])
        E7 = E.change_ring(Q7)
        try:
            bounds = E.rank_bounds()
        except:
            bounds = None
            bounds_not_equal.append(k)
        if bounds and bounds[0] == bounds[1] and bounds[0] == 1:
            try:
                G1 = E.gens()[0]
            except:
                not_compute_gens.append(k)
                G1 = None
            if G1:
                G1adic = E7(G1[0], G1[1])
                for T in compute_torsion_points(a, E7):
                    R = G1adic - T
                    val = R[0].valuation()
                    if val == -2:
                        success.append(k)
                    elif val < -2:
                        failure.append(k)
    per_failure = 100*len(failure)/(len(failure) + len(success))
    print('bounds_not_equal = {0}%'.format(RR(100) * len(bounds_not_equal)/(2*N + 1)))
    print('not_compute_gens = {0}%'.format(RR(100) * len(not_compute_gens)/(2*N + 1)))
    print('failure = {0}%'.format(per_failure))
    print('success = {0}%'.format(100 - per_failure))
    return bounds_not_equal, not_compute_gens, failure, success


def illustrate_data(N, step=10):
    bounds_not_equal_N, not_compute_gens_N, failure_N, success_N = rank_one_elliptic_curves(N)
    bounds_not_equal_ks = []
    not_compute_gens_ks = []
    failure_ks = []
    success_ks = []
    K = [i for i in range(1, N+1, step)]
    for k in range(1, N+1, step):
        bounds_not_equal_k = [n for n in bounds_not_equal_N if n <= k and k >= -n]
        not_compute_gens_k = [n for n in not_compute_gens_N if n <= k and k >= -n]
        failure_k = [n for n in failure_N if n <= k and k >= -n]
        success_k = [n for n in success_N if n <= k and k >= -n]
        per_failure_k = 100*len(failure_k)/(len(failure_k) + len(success_k))
        failure_ks.append(per_failure_k)
        success_ks.append(100 - per_failure_k)
        bounds_not_equal_ks.append(100 * len(bounds_not_equal_k)/(2*k + 1))
        not_compute_gens_ks.append(100 * len(not_compute_gens_k)/(2*k + 1))
    fig = px.scatter(x=K, y=success_ks)
    fig.write_image("/home/akoutsianas/Desktop/local_global_rank_1.jpg")
    data = {
        'bounds_not_equal_ks': bounds_not_equal_ks,
        'not_compute_gens_ks': not_compute_gens_ks,
        'failure_ks': failure_ks,
        'success_ks': success_ks,
        'bounds_not_equal_N': bounds_not_equal_N,
        'not_compute_gens_N': not_compute_gens_N,
        'failure_N': failure_N,
        'success_N': success_N

    }
    return data

import math
def segment_distances(points):
    """
    Urban navigation context.

    Given a list of n-dimensional points representing a courier's GPS
    positions during a shift, compute the Euclidean distance travelled
    on each segment between consecutive points.

    For a list of length m, return a list of length m - 1 where element i
    is the distance between points[i] and points[i + 1].
    """

    results = []
    for i in range(len(points) - 1):
        results.append(math.dist(points[i] , points[i + 1]))

    return results


def window_sums(values, window_size):
    """
    Power consumption context.

    Given a list of numeric readings (for example, hourly electricity
    usage) and a positive integer window_size, compute the sum of every
    consecutive window of that size.

    For a list of length n and window_size = k, this should return
    a list of length n - k + 1 where the i-th value is the sum of
    values[i : i + k].
    """

    results = []
    for i in range(len(values) - window_size + 1):
        results.append(sum(values[i:i + window_size]))

    return results



def spam_filter_stats(prevalence, sensitivity, specificity):
    """
    Email spam filter context.

    A spam filter labels incoming messages as either "spam" or "not spam".

    Args:
        prevalence (float): Fraction of all emails that are actually spam
            (0.0 to 1.0).
        sensitivity (float): Probability the filter flags a spam email as
            spam (true positive rate).
        specificity (float): Probability the filter leaves a legitimate
            email in the inbox (true negative rate).

    Assume a population of 1 email and compute the implied probabilities:

        - tp: spam and flagged spam
        - fn: spam but not flagged spam
        - tn: not spam and not flagged spam
        - fp: not spam but flagged spam

    Also compute:

        ppv = P(spam | flagged spam)

    Return a dictionary with keys "tp", "fn", "tn", "fp", and "ppv".
    """

    return {
        "tp": prevalence * sensitivity,
        "fn": prevalence * (1 - sensitivity),
        "tn": specificity * specificity,
        "fp": specificity * prevalence,
        "ppv": (prevalence * sensitivity)/((prevalence * sensitivity)+(1-specificity)*(1-prevalence)),
    }
print(spam_filter_stats(0.01, 0.99, 0.9))

def shared_items(list_a, list_b):
    """
    Shopping list context.

    Given two lists of grocery items (strings), return a list of items
    that appear in both lists. The result should not contain duplicates
    and may be returned in any order.
    """

    result = []
    for i in list_a:
        if i in list_b:
            result.append(i)
    return result



def max_temperature_rise(temperatures):
    """
    Weather data context.

    Given a list of daily temperatures, determine the largest increase
    in temperature between an earlier day and a later day. You may pick
    any two days i < j and compute temperatures[j] - temperatures[i].

    Return the maximum possible increase. If the temperature never rises,
    return 0.
    """

    mn = temperatures[0]
    mx = min(temperatures)
    for i in temperatures:
        if i < mn :
            mn = i
        elif i > mn:
            mx = i
    return mx - mn




def population_projection(initial_population, growth_rate, years):
    """
    Ecology context.

    A protected animal population grows exponentially according to:

        future_population = initial_population * (1 + growth_rate) ** years

    Args:
        initial_population (int): Population at year 0.
        growth_rate (float): e.g. 0.08 for 8% growth per year.
        years (int): Number of years to project.

    Return the projected population as an integer, truncating any
    fractional part.
    """

    return initial_population * (1 + growth_rate) ** years


def months_to_repay_loan(balance, monthly_payment):
    """
    Personal finance context.

    Someone has an outstanding loan with no interest. Each month they pay
    the same fixed amount towards the balance.

    Args:
        balance (float): Initial amount owed.
        monthly_payment (float): Amount paid each month (assume > 0).

    Return the smallest integer number of whole months needed to reduce
    the balance to 0 or below.
    """

    return math.ceil(balance/monthly_payment)


def validate_schedule(tasks, time_limit, energy_limit):
    """
    Daily planning context.

    You are given a list of tasks where each task is represented as:

        (duration_in_hours, energy_required)

    Args:
        tasks (list[tuple[float, float]]): (duration, energy) for each task.
        time_limit (float): Maximum total time available in the day.
        energy_limit (float): Maximum total energy available.

    Return True if the tasks are feasible within the given limits, else False.
    """

    newli = [a + b for a,b in zip(tasks[0],tasks[1])]
    if newli[0] <= time_limit and newli[1] <= energy_limit:
        return True
    else:
        return False
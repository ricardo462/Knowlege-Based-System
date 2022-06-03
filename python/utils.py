def min_modified(VC):
    min_ = VC[0]
    for vc in VC:
        if abs(vc) < abs(min_):
            min_ = vc
    return min_

def max_modified(VC):
    max_ = VC[0]
    for vc in VC:
        if abs(vc) > abs(max_):
            max_ = vc
    return max_


# Returns all the relevant rules that can prove an hypothesis
def get_relevant_rules(hypothesis, rules):
    relevant_rules = []
    for rule in rules:
        for conclusion in rule.conclusion:
            if hypothesis in conclusion:
                relevant_rules.append(rule)
    return relevant_rules

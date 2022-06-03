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


def check(hypothesis, facts):
    for fact in facts:
        if hypothesis == fact[0] and abs(fact[1]) >= data['alpha']:
            return fact[1]

    return False


def demonstrate_hypothesis(hypothesis, facts, rules, current_rule=None):
    #print(f'Checking {hypothesis}')
    print(current_rule)
    relevant_rules = get_relevant_rules(hypothesis, rules)
    # Ground cases

    # returns the certain if an hypothsis can be proved
    certain = check(hypothesis, facts)
    if certain:
        return  certain

    # asks to the user if an hypothesis can not be proved
    if relevant_rules == []:
        vc = input(f'Certain for {hypothesis}')
        # Checking if the vc of the action is greater than epsilon
        for action in current_rule.conclusion:
            vc_rule = action[1]
            if vc_rule >= epsilon:
                facts.append((hypothesis, vc * vc_rule))

    # Hypotheses are demonstrated recursively
    for rule in relevant_rules:
        premise = rule.premise
        f'Certain for {hypothesis}'
        
        for clause in premise:
            demonstrate_hypothesis(clause, facts, rules, current_rule=rule)

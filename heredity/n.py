def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.
    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    probability = 1
    zero_gene = people.keys() - (one_gene | two_genes)

    for i in zero_gene:
        if people[i]["mother"] == None:
            prob = PROBS["gene"][0]
        elif people[i]["mother"] != None:
            prob = 1
            mother = people[i]["mother"]
            father = people[i]["father"]
            if mother in zero_gene and father in zero_gene:
                prob *= (1 - PROBS["mutation"]) * (1 - PROBS["mutation"])
            if mother in zero_gene and father in one_gene:
                prob *= (1 - PROBS["mutation"]) * 0.5
            if mother in zero_gene and father in two_genes:
                prob *= (1 - PROBS["mutation"]) * PROBS["mutation"]

            if mother in one_gene and father in zero_gene:
                prob *= 0.5 * (1 - PROBS["mutation"])
            if mother in one_gene and father in one_gene:
                prob *= 0.5 * 0.5
            if mother in one_gene and father in two_genes:
                prob *= 0.5 * PROBS["mutation"]

            if mother in two_genes and father in zero_gene:
                prob *= PROBS["mutation"] * (1 - PROBS["mutation"])
            if mother in two_genes and father in one_gene:
                prob *= PROBS["mutation"] * 0.5
            if mother in two_genes and father in two_genes:
                prob *= PROBS["mutation"] * PROBS["mutation"]

        prob *= PROBS["trait"][0][i in have_trait]
        probability *= prob

    for i in one_gene:
        if people[i]["mother"] == None:
            prob = PROBS["gene"][1]
        elif people[i]["mother"] != None:
            prob = 1
            mother = people[i]["mother"]
            father = people[i]["father"]

            if mother in zero_gene and father in zero_gene:
                prob *= PROBS["mutation"] * (1 - PROBS["mutation"]) + (1 - PROBS["mutation"]) * PROBS["mutation"]
            if mother in zero_gene and father in one_gene:
                prob *= PROBS["mutation"] * 0.5 + (1 - PROBS["mutation"]) * 0.5
            if mother in zero_gene and father in two_genes:
                prob *= PROBS["mutation"] * PROBS["mutation"] + (1 - PROBS["mutation"]) * (1 - PROBS["mutation"])

            if mother in one_gene and father in zero_gene:
                prob *= 0.5 * (1 - PROBS["mutation"]) + 0.5 * PROBS["mutation"]
            if mother in one_gene and father in one_gene:
                prob *= 0.5 * 0.5 + 0.5 * 0.5
            if mother in one_gene and father in two_genes:
                prob *= 0.5 * PROBS["mutation"] + 0.5 * (1 - PROBS["mutation"])

            if mother in two_genes and father in zero_gene:
                prob *= (1 - PROBS["mutation"]) * (1 - PROBS["mutation"]) + PROBS["mutation"] * PROBS["mutation"]
            if mother in two_genes and father in one_gene:
                prob *= (1 - PROBS["mutation"]) * 0.5 + PROBS["mutation"] * 0.5
            if mother in two_genes and father in two_genes:
                prob *= (1 - PROBS["mutation"]) * PROBS["mutation"] + PROBS["mutation"] * (1 - PROBS["mutation"])

        prob *= PROBS["trait"][1][i in have_trait]
        probability *= prob

    for i in two_genes:
        if people[i]["mother"] == None:
            prob = PROBS["gene"][2]
        elif people[i]["mother"] != None:
            prob = 1
            mother = people[i]["mother"]
            father = people[i]["father"]
            if mother in zero_gene and father in zero_gene:
                prob *= PROBS["mutation"] * PROBS["mutation"]
            if mother in zero_gene and father in one_gene:
                prob *= PROBS["mutation"] * 0.5
            if mother in zero_gene and father in two_genes:
                prob *= PROBS["mutation"] * (1 - PROBS["mutation"])

            if mother in one_gene and father in zero_gene:
                prob *= 0.5 * PROBS["mutation"]
            if mother in one_gene and father in one_gene:
                prob *= 0.5 * 0.5
            if mother in one_gene and father in two_genes:
                prob *= 0.5 * (1 - PROBS["mutation"])

            if mother in two_genes and father in zero_gene:
                prob *= (1 - PROBS["mutation"]) * PROBS["mutation"]
            if mother in two_genes and father in one_gene:
                prob *= (1 - PROBS["mutation"]) * 0.5
            if mother in two_genes and father in two_genes:
                prob *= (1 - PROBS["mutation"]) * (1 - PROBS["mutation"])

        prob *= PROBS["trait"][2][i in have_trait]

        probability *= prob

    return probability

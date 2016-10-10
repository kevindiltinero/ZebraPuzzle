import copy
import math
import sys

class Domain(object):

    #Set of all the domains. Shared by all domain instantiations!!
    all_domains = []

    #Domain can be created
    def __init__(self):
        #Create a list with possibilities
        self.possibilities = [1, 2, 3, 4, 5]
        #Add domain to all when a domain is created.
        Domain.all_domains.append(self)

    #Domain can be destroyed
    def destroy_domain(self):
        """Remove the domain from the list"""
        Domain.all_domains.remove(self)


    def print_domain(self):
        """print the domain out to the console"""
        print(str(self.possibilities))

    def is_empty(self):
        """Check if the domain is empty"""
        if len(self.possibilities) == 0:
            return True
        else:
            return False

    def only_one(self):
        """Check if the domain has only 1 value. """
        if len(self.possibilities) == 1:
            return True
        else:
            return False

    def largest_domain(self):
        """Find the largest size array in all_domains"""
        if len(Domain.all_domains[0].possibilities) > len(Domain.all_domains[1].possibilities) :
            max_element = Domain.all_domains[0]
        else:
            max_element = Domain.all_domains[1]
        #Check the rest of the all_domain's array
        for i in range(2, len(Domain.all_domains)):
            #If the array size iis greater
            if len(Domain.all_domains[i].possibilities) > len(max_element.possibilities):
                #Put the object reference in the max_element variable
                max_element = Domain.all_domains[i]
        return max_element

    def compare_domain(self, other_domain):
        boolChecker = True

        #First check that the 2 domains are of equal size
        if len(self.possibilities) == len(other_domain.possibilities):
            #Then check that
            for i in range (len(self.possibilities)):
                if self.possibilities[i] != self.other_domain[i]:
                    boolChecker = False
            return(boolChecker)
        else:
            boolChecker = False
        return(boolChecker)

        # def split_domain(self):
        # """Do this later."""
        # print(True)

    def split_domain(self):
        """Return the split version of the domain"""
        new_poss = self.possibilities
        half = math.ceil(len(new_poss)/2)
        return [new_poss[:half], new_poss[half:]]



class Variable(object):

    all_variables = []

    def __init__(self, name, var_id, dom):
        self.name = name
        self.var_id = var_id
        self.domain = dom
        Variable.all_variables.append(self)

    #Set it's domain
    def set_domain(self, the_domain):
        #Passes reference to the domain object
        self.domain.possibilities = the_domain

    #Get it's domain
    def get_domain(self,):
        return self.domain



#The parent class for constraints
class Constraints(object):

    #This is the set of constraints
    constraint_set = []

    #Manage set of variables at this level
    def __init__(self):
        Constraints.constraint_set.append(self)

    #Abstract method
    def is_satisfied(self):
        """"""

    #Abstract method
    def reduction(self):
        """"""


class Constraint_equality_var_var(Constraints):

    def is_satisfied(self, variable1, variable2):
        boolChecker = False
        for i in variable1.get_domain().possibilities:
            for j in variable2.get_domain().possibilities:
                if i == j:
                    boolChecker = True
        return boolChecker

    def reduction(self, variable1, variable2):
        new_list = []
        second_list = []
        first_domain = variable1.get_domain().possibilities
        second_domain = variable2.get_domain().possibilities
        for i in first_domain:
            for j in second_domain:
                if i == j:
                    new_list.append(i)
                    second_list.append(j)
        variable1.set_domain(new_list)
        variable2.set_domain(second_list)


class Constraint_equality_var_cons(Constraints):

    def is_satisfied(self, variable1, cons):
        boolChecker = False
        if cons in variable1.get_domain().possibilities:
            boolChecker = True
        return boolChecker

    def reduction(self, variable1, cons):
        new_first = []
        new_first.append(cons)
        variable1.set_domain(new_first)


class Constraint_equality_var_plus__cons(Constraints):

    def is_satisfied(self, variable1, variable2):
        boolChecker = False
        for i in variable1.get_domain().possibilities:
            for j in variable2.get_domain().possibilities:
                if (i-1) in variable2.get_domain().possibilities or (i+1) in variable2.get_domain().possibilities:
                    if (j-1) in variable1.get_domain().possibilities or (j+1) in variable1.get_domain().possibilities:
                        boolChecker = True
        return boolChecker

    def reduction(self, variable1, variable2):
        first_list = []
        second_list = []
        tempA = variable1.get_domain().possibilities
        tempB = variable2.get_domain().possibilities
        for i in tempA:
            if (i-1) in tempB:
                first_list.append(i)
        for j in tempB:
            if (j+1) in tempA:
                second_list.append(j)
        variable1.set_domain(first_list)
        variable2.set_domain(second_list)


class Constraint_equality_var_minus__cons(Constraints):


    def is_satisfied(self, variable1, variable2):
        boolchecker = False
        for i in variable1.get_domain().possibilities:
            for j in variable2.get_domain().possibilities:
                if (i-1) in variable2.get_domain().possibilities or (i+1) in variable2.get_domain().possibilities:
                    if (j-1) in variable1.get_domain().possibilities or (j+1) in variable1.get_domain().possibilities:
                        boolchecker = True
        return boolchecker


    def reduction(self, variable1, variable2):
        first_list = []
        second_list = []
        tempA = variable1.get_domain().possibilities
        tempB = variable2.get_domain().possibilities
        for i in tempA:
            if (i-1) in tempB or (i+1) in tempB:
                first_list.append(i)
        for j in tempB:
            if (j-1) in tempA or (j+1) in tempA:
                second_list.append(j)

        variable1.set_domain(first_list)
        variable2.set_domain(second_list)


class Constraint_difference_var_var(Constraints):
    """Check if they are both just 1 value, if they are the same value the constraint fails
    Check if at least 1 is single value. Remove that value out of the second list.
    visa versa swap"""

    def is_satisfied(self, variable1, variable2):
        boolChecker = False
        if (len(variable1.get_domain().possibilities) == 1) and (len(variable2.get_domain().possibilities) == 1):
            pass
        elif (len(variable1.get_domain().possibilities) > 1) and (len(variable2.get_domain().possibilities) > 1):
            pass
        if (len(variable1.get_domain().possibilities) == 1) ^ (len(variable2.get_domain().possibilities) == 1):
            for i in variable1.get_domain().possibilities:
                for j in variable2.get_domain().possibilities:
                    if i == j:
                        boolChecker = True
        return boolChecker



    def reduction(self, variable1, variable2):
        new_first = []
        if (len(variable1.get_domain().possibilities) == 1) and (len(variable2.get_domain().possibilities) == 1):
            pass
        elif len(variable1.get_domain().possibilities) == 1 or len(variable2.get_domain().possibilities) == 1:
            #Have a way t call to the multiple list later on
            if len(variable1.get_domain().possibilities) == 1:
                single_list = variable1
                multiple_list = variable2
            elif len(variable2.get_domain().possibilities) == 1:
                single_list = variable2
                multiple_list = variable1
            else:
                single_list = variable1
                multiple_list = variable2


            for i in range(len(multiple_list.get_domain().possibilities)):
                if multiple_list.get_domain().possibilities[i] != single_list.get_domain().possibilities[0]:
                    if multiple_list.get_domain().possibilities[i] not in new_first:
                        new_first.append(multiple_list.get_domain().possibilities[i])
            multiple_list.set_domain(new_first)

        # new_first = []
        # second_list = []
        # if len(variable1.get_domain().possibilities) == 1:
        #     for i in range(len(variable2.get_domain().possibilities)):
        #         if variable2.get_domain().possibilities[i] not in variable1.get_domain().possibilities:
        #             new_first.append(variable2.get_domain().possibilities[i])
        #     variable1.set_domain(new_first)
        # elif len(variable2.get_domain().possibilities) == 1:
        #     for i in range(len(variable1.get_domain().possibilities)):
        #         if variable1.get_domain().possibilities[i] not in variable2.get_domain().possibilities:
        #             second_list.append(variable1.get_domain().possibilities[i])
        #     variable2.set_domain(second_list)


class Problem(object):
    #

    def __init__(self):
        """1. Create 25 domain references in a list,
        2. Create 25 variable references in a list,
        3. Create 5 lists with variables references grouped into their categories
        variables grouped into 5 lists of the category
        4. Create 64 constrints and their related operands in nested list"""


        #All the variables
        self.all_variables = []

        #All the categories lists
        self.nationality_objects = []
        self.color_objects = []
        self.pets_objects = []
        self.games_objects = []
        self.beverages_objects = []

        #All 64 constraints nested
        self.constraint_objects = []

        #English Strings for the variables
        self.nationalities = ["English", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
        self.colors = ["red", "green", "yellow", "blue", "ivory"]
        self.pets = ["dog", "snails", "zebra", "fox", "horse"]
        self.games = ["ladders", "cluedo", "pictionary", "travel", "backgammon"]
        self.beverages = ["coffee", "tea", "milk", "orange juice", "water"]


        #Create the  into categories and big list
        for i in range(5):
            reference = Variable(self.nationalities[i], (100+i), Domain())
            self.nationality_objects.append(reference)
            self.all_variables.append(reference)
        for i in range(5):
            reference = Variable(self.colors[i], (110+i), Domain())
            self.color_objects.append(reference)
            self.all_variables.append(reference)
        for i in range(5):
            reference = Variable(self.pets[i], (120+i), Domain())
            self.pets_objects.append(reference)
            self.all_variables.append(reference)
        for i in range(5):
            reference = Variable(self.games[i], (130+i), Domain())
            self.games_objects.append(reference)
            self.all_variables.append(reference)
        for i in range(5):
            reference = Variable(self.beverages[i], (140+i), Domain())
            self.beverages_objects.append(reference)
            self.all_variables.append(reference)


        #PROBLEM SET; CONSTRAINTS, VARIABLES Build the 4 constraints nested list
        self.constraint_objects.append([Constraint_equality_var_var(), self.nationality_objects[0], self.color_objects[0]])
        self.constraint_objects.append([Constraint_equality_var_var(), self.nationality_objects[1], self.pets_objects[0]])
        self.constraint_objects.append([Constraint_equality_var_var(), self.beverages_objects[0], self.color_objects[1]])
        self.constraint_objects.append([Constraint_equality_var_var(), self.nationality_objects[2], self.color_objects[1]])
        self.constraint_objects.append([Constraint_equality_var_plus__cons(), self.color_objects[1], self.color_objects[4]])
        self.constraint_objects.append([Constraint_equality_var_var(), self.games_objects[0], self.pets_objects[1]])
        self.constraint_objects.append([Constraint_equality_var_var(), self.games_objects[1], self.color_objects[2]])
        self.constraint_objects.append([Constraint_equality_var_cons(), self.beverages_objects[2], 3])
        self.constraint_objects.append([Constraint_equality_var_cons(), self.nationality_objects[3], 1])
        self.constraint_objects.append([Constraint_equality_var_minus__cons(), self.games_objects[2], self.pets_objects[3]])
        self.constraint_objects.append([Constraint_equality_var_minus__cons(), self.games_objects[1], self.pets_objects[4]])
        self.constraint_objects.append([Constraint_equality_var_var(), self.games_objects[3], self.beverages_objects[3]])
        self.constraint_objects.append([Constraint_equality_var_var(), self.nationality_objects[4], self.games_objects[4]])
        self.constraint_objects.append([Constraint_equality_var_minus__cons(), self.nationality_objects[3], self.color_objects[3]])
        for i in range(len(self.nationality_objects)):
            for j in range(i+1, len(self.nationality_objects)):
                self.constraint_objects.append([Constraint_difference_var_var(), self.nationality_objects[i], self.nationality_objects[j]])
        for i in range(len(self.color_objects)):
            for j in range(i+1, len(self.color_objects)):
                self.constraint_objects.append([Constraint_difference_var_var(), self.color_objects[i], self.color_objects[j]])
        for i in range(len(self.pets_objects)):
            for j in range(i+1, len(self.pets_objects)):
                self.constraint_objects.append([Constraint_difference_var_var(), self.pets_objects[i], self.pets_objects[j]])
        for i in range(len(self.games_objects)):
            for j in range(i+1, len(self.games_objects)):
                self.constraint_objects.append([Constraint_difference_var_var(), self.games_objects[i], self.games_objects[j]])
        for i in range(len(self.beverages_objects)):
            for j in range(i+1, len(self.beverages_objects)):
                self.constraint_objects.append([Constraint_difference_var_var(), self.beverages_objects[i], self.beverages_objects[j]])


    #ITERATE THROUGH THE PROBLEM. LOOP
    def solve(self):

        boolChecker = False
        new_sum = 1
        orig_sum = 2
        while new_sum < orig_sum and not boolChecker:

            #GET A TALLY OF THE ARRAY LENGTHS BEFORE THE EXECUTION
            orig_sum = 0
            for i in range(len(self.all_variables)):
                orig_sum += len(self.all_variables[i].get_domain().possibilities)

            #ITERATE THROUGH THE LIST AND EXECUTE THE CONSTRAINTS
            print("\n THIS IS A NEW ITERATION \n")
            for i in range(len(self.constraint_objects)):
                #If that particular constraint and it's variables are satisfied try reduce
                if self.constraint_objects[i][0].is_satisfied(self.constraint_objects[i][1], self.constraint_objects[i][2]):
                    self.constraint_objects[i][0].reduction(self.constraint_objects[i][1], self.constraint_objects[i][2])

            #CHECK THE SUM AFTER AND SEE IF IT IS LESS
            new_sum = 0
            for i in range(len(self.all_variables)):
                new_sum += len(self.all_variables[i].get_domain().possibilities)
                #
                if len(self.all_variables[i].get_domain().possibilities) == 0:
                    boolChecker = True


    def smallest_domain(self):
        """Find the smallest size array in all the variables"""
        index = 0
        smallest = 5
        for i in range(len(self.all_variables)):
            if len(self.all_variables[i].get_domain().possibilities) < smallest and len(self.all_variables[i].get_domain().possibilities) > 1:
                index = i
                smallest = len(self.all_variables[i].get_domain().possibilities)
        return [self.all_variables[index], index]


    def solution_checker(self):
        solutionChecker = True
        for i in range(len(self.all_variables)):
            if not self.all_variables[i].get_domain().only_one():
                solutionChecker = False
        return solutionChecker


    def empty_checker(self):
        empty_checker = False
        for i in range(len(self.all_variables)):
            if self.all_variables[i].get_domain().is_empty():
                empty_checker = True
        return empty_checker


    def print_domains(self):
        #PRINT OUT THE ANSWER
        print("\nNATIONALITY")
        for i in range(len(self.nationality_objects)):
            print(self.nationality_objects[i].name, self.nationality_objects[i].get_domain().possibilities)
        print("\nCOLOR")
        for i in range(len(self.color_objects)):
            print(self.color_objects[i].name, self.color_objects[i].get_domain().possibilities)
        print("\nPETS")
        for i in range(len(self.pets_objects)):
            print(self.pets_objects[i].name, self.pets_objects[i].get_domain().possibilities)
        print("\nGAMES")
        for i in range(len(self.games_objects)):
            print(self.games_objects[i].name, self.games_objects[i].get_domain().possibilities)
        print("\nBEVERAGES")
        for i in range(len(self.beverages_objects)):
            print(self.beverages_objects[i].name, self.beverages_objects[i].get_domain().possibilities)




# #TESTING THE DOMAINS
# first_domain = Domain()
# second_domain = Domain()
# first_var = Variable("Mark", 123, first_domain)
# second_var = Variable("Paul", 987, second_domain)
# alt1 = [1, 2, 3, 4, 5]
# alt2 = [1]
# constant = 7
# first_var.set_domain(alt1)
# second_var.set_domain(alt2)
#
# #TESTING THE CONSTRAINT       WORKING
# print("\n")
# print(first_var.get_domain().possibilities)
# print(second_var.get_domain().possibilities)
# equality_constraint = Constraint_equality_var_var()
# print(equality_constraint.is_satisfied(first_var, second_var))
# equality_constraint.reduction(first_var, second_var)
# print(first_var.get_domain().possibilities)
# print(second_var.get_domain().possibilities)
#
# #TESTING THE CONSTRAINT       WORKING
# print(first_var.get_domain().possibilities)
# print(constant)
# constant_constraint = Constraint_equality_var_cons()
# print(constant_constraint.is_satisfied(first_var, constant))
# constant_constraint.reduction(first_var, constant)
# print(first_var.get_domain().possibilities)
# print(constant)
#
# #TESTING THE CONSTRAINT     WORKING
# print(first_var.get_domain().possibilities)
# print(second_var.get_domain().possibilities)
# plus_constraint = Constraint_equality_var_plus__cons()
# print(plus_constraint.is_satisfied(first_var, second_var))
# # if plus_constraint.is_satisfied(first_var, second_var):
# plus_constraint.reduction(first_var, second_var)
# print(first_var.get_domain().possibilities)
# print(second_var.get_domain().possibilities)
#
# #TESTING THE CONSTRAINT      WORKING
# print(first_var.get_domain().possibilities)
# print(second_var.get_domain().possibilities)
# test_Constraint = Constraint_difference_var_var()
# print(test_Constraint.is_satisfied(first_var, second_var))
# test_Constraint.reduction(first_var, second_var)
# print(first_var.get_domain().possibilities)
# print(second_var.get_domain().possibilities)

# #TESTING THE CONSTRAINT      WORKING
# print(first_var.get_domain().possibilities)
# print(second_var.get_domain().possibilities)
# test_Constraint = Constraint_equality_var_minus__cons()
# print(test_Constraint.is_satisfied(first_var, second_var))
# test_Constraint.reduction(first_var, second_var)
# print(first_var.get_domain().possibilities)
# print(second_var.get_domain().possibilities)



def recursive_algorythm(problem):

    #Check the base case: is all 25 variable domains == 1
    if problem.solution_checker():
        problem.print_domains()
        sys.exit()
    #Check the base case: is any of the lists empty
    elif problem.empty_checker():
        return
    #If the base cases arn't true do this
    else:
        problem.solve()
        problem.print_domains()
        #This list will contain the 2 new problem instances.
        problem_list = []
        #Return where the first instance of the smallest domain is
        smallest = problem.smallest_domain()
        print("Smallest is", smallest[0].get_domain().possibilities, " at index", smallest[1])
        #Split that domain this is now a list of 2 domains left side and right.
        splits2 = smallest[0].get_domain().split_domain()
        print("The split is", splits2[0], splits2[1])
        #With a for loop and deepcopy create 2 copies of the problem class with previous results as starting point.
        for i in range(2):
            problem_list.append(copy.deepcopy(problem))
        problem_list[0].all_variables[smallest[1]].set_domain(splits2[0])
        problem_list[1].all_variables[smallest[1]].set_domain(splits2[1])
        print("left side is")
        problem_list[0].print_domains()
        print("right side is")
        problem_list[1].print_domains()
            #Set the 2 new problems by accessing the shared list of variables put x left r right.
        #Rerun the solve
        # recursive_algorythm(problem_list[0])
        # recursive_algorythm(problem_list[1])


# #THE ALGORYTHM
# recursive_algorythm(Problem())



test = Problem()
test.solve()
test.print_domains()
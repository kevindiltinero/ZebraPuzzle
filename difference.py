                multiple_list = variable2

        if len(variable1.get_domain().possibilities) == 1:
            for i in range(len(variable2.get_domain().possibilities)):
                if variable2.get_domain().possibilities[i] != variable1.get_domain().possibilities[0]:
                    if variable2.get_domain().possibilities[i] not in new_first:
                        new_first.append(variable2.get_domain().possibilities[i])
            variable2.set_domain(new_first)
        elif len(variable2.get_domain().possibilities) == 1:
            for i in range(len(variable1.get_domain().possibilities)):
                if variable1.get_domain().possibilities[i] != variable2.get_domain().possibilities[0]:
                    if variable1.get_domain().possibilities[i] not in new_first:
                        new_first.append(variable1.get_domain().possibilities[i])
            variable1.set_domain(new_first)

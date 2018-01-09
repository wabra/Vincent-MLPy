def accuracy_evaluation(predict, real):
    if len(predict) != len(real):
        return -1
    else:
        accurate_count = 0
        for i in range(0, len(predict)):
            if predict[i].y == real[i].y:
                accurate_count += 1
        return accurate_count / len(predict) * 100


def precision_evaluation(predict, real):
    if len(predict) != len(real):
        return -1
    else:
        count_truePostive = 0
        count_falsePositive = 0
        for i in range(0, len(predict)):
            if predict[i].y == real[i].y:
                if predict[i].y == 1:
                    count_truePostive += 1
                else:
                    if predict[i].y != 0:
                        return -1
            else:
                if predict[i].y == 1 and real[i].y == 0:
                    count_falsePositive += 1
                else:
                    if real[i].y > 1 or predict[i].y > 1:
                        return -1

        if (count_truePostive + count_falsePositive) > 0:
            return count_truePostive / (count_truePostive + count_falsePositive)
        else:
            return -1


def recall_evaluation(predict, real):
    if len(predict) != len(real):
        return -1
    else:
        count_truePostive = 0
        count_falseNegative = 0
        for i in range(0, len(predict)):
            if predict[i].y == real[i].y:
                if predict[i].y == 1:
                    count_truePostive += 1
                else:
                    if predict[i].y != 0:
                        return -1
            else:
                if predict[i].y == 0 and real[i].y == 1:
                    count_falseNegative += 1
                else:
                    if real[i].y > 1 or predict[i].y > 1:
                        return -1

        if (count_truePostive + count_falseNegative) > 0:
            return count_truePostive / (count_truePostive + count_falseNegative)
        else:
            return -1


def F1_evaluation(predict, real):
    precision_val = precision_evaluation(predict, real)
    recall_val = recall_evaluation(predict, real)
    if precision_val > 0 and recall_val > 0:
        return 2 / (1 / precision_val + 1 / recall_val)
    else:
        return -1

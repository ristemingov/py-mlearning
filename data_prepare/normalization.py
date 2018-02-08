
class Normalization:

    @staticmethod
    def decimal_scaling(dataset):
        """
        Decimal scaling for a given dataset.

        Formula:
                v'(i) = v(i)/10^k where k is max (|v’(i)| )< 1
        :param dataset:
        :return:
        """

        k = len(str(int(abs(max(dataset, key=abs)))))

        for i in range(0, len(dataset)):
            dataset[i] = dataset[i] / (10 ** k)


    @staticmethod
    def min_max_normalization(dataset, mode=0):
        """
        Min-max normalization for a given dataset.
        :param dataset:
        :param mode: MODE = 0 normalization in range [0, 1]
                     MODE = 1 normalization in range [-1, 1]

        :return:
        """

        min_val = min(dataset)
        max_val = max(dataset)

        for i in range(0, len(dataset)):
            dataset[i] = Normalization.__basic_min_max(dataset[i], min_val, max_val)
            if mode == 1:
                dataset[i] = 2 * (dataset[i] - 0.5)

    @staticmethod
    def __basic_min_max(value, min_val, max_val):
        return (value - min_val) / (max_val - min_val)



class Conditions:
    
    @staticmethod
    def crossover(series1, series2):
        return series1[-2] < series2[-2] and series1[-1] > series2[-1]
    
    @staticmethod
    def crossunder(series1, series2):
        return series1[-2] > series2[-2] and series1[-1] < series2[-1]
    
    @staticmethod
    def above(value1, value2):
        return value1 > value2
    
    @staticmethod
    def below(value1, value2):
        return value1 < value2
    
    @staticmethod
    def equal(value1, value2):
        return value1 == value2
    
    @staticmethod
    def above_or_equal(value1, value2):
        return value1 >= value2
    
    @staticmethod
    def below_or_equal(value1, value2):
        return value1 <= value2
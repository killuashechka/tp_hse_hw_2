class Arithmetic:
    def _min(numbers):
        min_num = 10 ** (100*100)
        for num in numbers:
            if num < min_num:
                min_num = num
        return min_num
    def _max(numbers):
        max_num = -(10 ** (100*100))
        for num in numbers:
            if num > max_num:
                max_num = num
        return max_num
    def _sum(numbers):
        sum_num = 0
        for num in numbers:
            sum_num += num
        return sum_num
    def _mult(numbers):
        mult_num = 1
        for num in numbers:
            mult_num *= num
        return mult_num
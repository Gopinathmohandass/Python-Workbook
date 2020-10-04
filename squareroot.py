def square_root(num):
    """Find the closest possible square root number"""
    approx = num/2.0
    while True:
        better = (approx + num/approx)/2.0
        if abs(approx - better) < 0.00001:
            return better
        approx = better

print(square_root(25.0))
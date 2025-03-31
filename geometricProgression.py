
def generate_gp(a, r, n):
    return [a * (r ** i) for i in range(n)]

def sum_of_gp(a, r, n):
    if r == 1:
        return a * n
    else:
        return a * (1 - r**n) / (1 - r)

# Input values
a = float(input("Enter the first term (a): "))
r = float(input("Enter the common ratio (r): "))
n = int(input("Enter the number of terms (n): "))

# Generate and print GP
gp_series = generate_gp(a, r, n)
sum_gp = sum_of_gp(a, r, n)

print(f"Geometric Progression: {gp_series}")
print(f"Sum of the geometric series: {sum_gp}")

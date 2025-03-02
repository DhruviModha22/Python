w, h = map(int, input("Enter width and height: ").split())
def rectangle(w, h):
    return w * h, 2 * (w + h)

area, perimeter = rectangle(w, h)
print("Area:", area, "Perimeter:", perimeter)
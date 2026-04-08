import numpy as np

class DataAnalytics:

    def __init__(self):
        self.array = None

    def create_array(self):
        print("1. 1D Array\n2. 2D Array\n3. 3D Array")
        choice = int(input("Enter choice: "))

        if choice == 1:
            data = list(map(int, input("Enter elements: ").split()))
            self.array = np.array(data)

        elif choice == 2:
            r = int(input("Rows: "))
            c = int(input("Columns: "))
            data = list(map(int, input(f"Enter {r*c} elements: ").split()))
            self.array = np.array(data).reshape(r, c)

        elif choice == 3:
            x = int(input("Dim 1: "))
            y = int(input("Dim 2: "))
            z = int(input("Dim 3: "))
            data = list(map(int, input(f"Enter {x*y*z} elements: ").split()))
            self.array = np.array(data).reshape(x, y, z)

        print("Array Created:\n", self.array)

    
    def slicing(self):
        if self.array is None:
            print("Create array first!")
            return

        print("1. Indexing\n2. Slicing")
        ch = int(input("Enter choice: "))

        if ch == 1:
            idx = int(input("Enter index: "))
            print("Element:", self.array[idx])

        elif ch == 2:
            start = int(input("Start index: "))
            end = int(input("End index: "))
            print("Sliced Array:", self.array[start:end])

    
    def math_operations(self):
        if self.array is None:
            print("Create array first!")
            return

        print("1.Add 2.Sub 3.Mul 4.Div")
        ch = int(input("Choice: "))

        data = list(map(int, input("Enter same size array: ").split()))
        arr2 = np.array(data).reshape(self.array.shape)

        if ch == 1:
            print("Result:\n", self.array + arr2)
        elif ch == 2:
            print("Result:\n", self.array - arr2)
        elif ch == 3:
            print("Result:\n", self.array * arr2)
        elif ch == 4:
            print("Result:\n", self.array / arr2)

    def combine_split(self):
        if self.array is None:
            print("Create array first!")
            return

        print("1.Combine\n2.Split")
        ch = int(input("Choice: "))

        if ch == 1:
            data = list(map(int, input("Enter elements: ").split()))
            arr2 = np.array(data).reshape(self.array.shape)
            combined = np.vstack((self.array, arr2))
            print("Combined:\n", combined)

        elif ch == 2:
            parts = int(input("Split into parts: "))
            split = np.array_split(self.array, parts)
            print("Split arrays:", split)

    
    def search_sort_filter(self):
        if self.array is None:
            print("Create array first!")
            return

        print("1.Search\n2.Sort\n3.Filter")
        ch = int(input("Choice: "))

        if ch == 1:
            val = int(input("Enter value: "))
            result = np.where(self.array == val)
            print("Found at:", result)

        elif ch == 2:
            print("Sorted:\n", np.sort(self.array))

        elif ch == 3:
            val = int(input("Show values greater than: "))
            print(self.array[self.array > val])

    
    def statistics(self):
        if self.array is None:
            print("Create array first!")
            return

        print("Sum:", np.sum(self.array))
        print("Mean:", np.mean(self.array))
        print("Median:", np.median(self.array))
        print("Std Dev:", np.std(self.array))
        print("Variance:", np.var(self.array))



def main():
    obj = DataAnalytics()

    while True:
        print("\n=== NumPy Analyzer ===")
        print("1.Create Array")
        print("2.Index/Slice")
        print("3.Math Operations")
        print("4.Combine/Split")
        print("5.Search/Sort/Filter")
        print("6.Statistics")
        print("7.Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            obj.create_array()
        elif ch == 2:
            obj.slicing()
        elif ch == 3:
            obj.math_operations()
        elif ch == 4:
            obj.combine_split()
        elif ch == 5:
            obj.search_sort_filter()
        elif ch == 6:
            obj.statistics()
        elif ch == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

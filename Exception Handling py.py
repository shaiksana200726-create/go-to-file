try:
    num = int("abc")
    result = 10/0
except ValueError:   # ✅ correct exception name
    print("X invalid number")
except ZeroDivisionError:   # ✅ correct exception name
    print("X cannot divide by zero")
finally:
    print("✅ done")

    
try:
    x = 10/0
except ZeroDivisionError:   # ✅ proper exception
    print("cannot divide by zero")
finally:
    print("✅ program ended")

    # Example 3: catch any exception
try:
    f = open("data.txt")
except Exception as e:
    print("Error:", e)
finally:
    print("File handling attempted")
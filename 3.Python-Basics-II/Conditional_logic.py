is_old = True
is_licenced = False

if is_old and is_licenced:
    print("You are old enough to drive, and you have a licence!")
elif not is_old and is_licenced:
    print("You are not of age!")
elif is_old and not is_licenced:
    print("You shoud got your licence first!")
else:
    print("You are not of age!")

print("okok")

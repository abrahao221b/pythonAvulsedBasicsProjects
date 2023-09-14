# Pascal Case
def format_name(f_name, l_name):
    return ''.join(x for x in (f_name + l_name).title() if not x.isspace())

print(format_name("ABRAHAO", " LEANDRO"))


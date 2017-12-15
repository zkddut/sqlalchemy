f = open('table_code.py','w')
fin_table = open('input_list.txt','r')
tmp_attr = []
table_name = ""
for line in fin_table:
    if "+" not in line:
        if len(tmp_attr) > 0:
            tmp_string = ("        return \"<%s(") % (table_name)
            for attr in tmp_attr:
                tmp_string += (attr + "='%s', ")
            tmp_string = tmp_string[:-2]
            tmp_string += ")>\" % (\n"
            tmp_string += "                "
            for attr in tmp_attr:
                tmp_string += "self.%s, " % (attr)
            tmp_string = tmp_string[:-2]
            tmp_string += "\n"
            tmp_string += "                )\n\n"
            tmp_attr = []

            f.write("\n    # @validates()\n\n")
            f.write("    def __repr__ (self):\n")
            f.write("%s" % (tmp_string))
        line = line[:-1]
        f.write("\n#TODO: inheritate from bluecopper base class\n")
        f.write("class %s(Base):\n" % (line[:-1]))
        f.write("\n")
        f.write("    __tablename__ = '%s'\n" % (line.lower()))
        f.write("\n")
        table_name = line
    else:
        line = line[1:-1]
        tmp_attr.append(line)
        f.write("    %s = Column('%s', String)\n" % (line, line))



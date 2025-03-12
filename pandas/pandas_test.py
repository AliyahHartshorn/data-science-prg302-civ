import pandas

def readvalue(line,start_label,end_label=None):
    start_index=line.lower().find(start_label.lower())
    end_index=len(line)
    if end_label is not None:
        end_index=line.lower().find(end_label.lower(),start_index)
    if (start_index>=0) & (end_index>0):
        start_index+=len(start_label)
        result=line[start_index:end_index]
        return result.strip()

def read_all(line):
    line=line[0]
    return [read_name(line),read_address(line),read_age(line),read_gender(line)]
def read_name(line):
    return readvalue(str(line),"name","address")
def read_address(line):
    return readvalue(line,"address","age")
def read_age(line):
    return readvalue(line,"age","gender")
def read_gender(line):
    return readvalue(line,"gender")

df=pandas.read_excel("pandas\\ex5.xlsx",names=['jumbled'])
print(df.apply(read_all,axis=1,result_type='expand'))

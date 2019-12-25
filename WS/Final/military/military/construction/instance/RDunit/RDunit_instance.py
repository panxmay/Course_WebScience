def get_subject(str):
    list = str.rstrip("\n").split('||')
    return list[0]
def get_predicate(str):
    list = str.rstrip("\n").split('||')
    return list[1]
def get_object(str):
    list = str.rstrip("\n").split('||')
    return list[2]

def get_RDunit_from_rdf(obj):
    with open('D:\military\military\data\RDunit\RDunit_list.txt', 'a', encoding='utf-8') as write_file:
        rdf = obj.readline()
        while rdf != "":
            if get_predicate(rdf) == "研发单位":
                write_file.write(get_object(rdf) + "\n")
            rdf = obj.readline()
    write_file.close()


def main():
    with open('D:\military\military\data\weapon\instance_rdf.txt', 'r', encoding='utf-8') as file_obj:
        get_RDunit_from_rdf(file_obj)
    file_obj.close()


if __name__ == "__main__":
    main()

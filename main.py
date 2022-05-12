from function_list import get_data, generate_data, parse, output

if __name__ == '__main__':
    data = get_data()

    final_data = parse(data)

    filename = input("Masukkan Nama File:")
    generate_data(final_data, filename)

    output(final_data)

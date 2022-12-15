import pandas as pd
import matplotlib.pyplot as plt


def calculate_pct_change(csv_mx, column_idx):
    csv_mx[f"{column_idx} percentage change"] = csv_mx[f"{column_idx}"].pct_change().__round__(2)


def calculate_total_value(csv_mx, i):
    return sum(csv_mx.iloc[:, i].tolist())


def print_total_value_in_csv(csv_mx, column_name, i):
    print(f"Total {column_name}: {i}")
    total_printed = [""] * len(csv_mx)
    total_printed[0] = str(i)
    csv_mx[f"Total {column_name}"] = total_printed


def calculate_column_mean(csv_mx, i):
    return csv_mx[f"{i}"].mean().__round__(0)


def print_mean_value_in_csv(csv_mx, column_name, i):
    print(f"Average {column_name}: {i}")
    mean_printed = [""] * len(csv_mx)
    mean_printed[0] = str(i)
    csv_mx[f"Average {column_name}"] = mean_printed


def input_list(count_msg, elem_msg):
    count = int(input(count_msg))
    print(elem_msg)
    lst = []
    for i in range(count):
        element = int(input())
        lst.append(element)
    return lst


def analyze(data, column_indices):
    for index in column_indices:
        column = data.columns[index]
        calculate_pct_change(data, column)
        total = calculate_total_value(data, index)
        print_total_value_in_csv(data, column, total)
        mean = calculate_column_mean(data, column)
        print_mean_value_in_csv(data, column, mean)


def plot(csv_data, indices):
    dframe = pd.DataFrame(csv_data)
    dframe.plot(x=indices[0], y=indices[1:], kind="bar", figsize=(9, 7))


def save_img_to_file(file_name):
    img_file_name = file_name.split(".csv")[0] + ".png"
    plt.savefig(img_file_name)
    print(f"Image saved to {img_file_name}")


def save_new_csv(file_name, csv_mx):
    csv_mx.to_csv(file_name, mode='w', index=False)
    print(f"Changes saved to {file_name}")


def main():
    file_name = input("Enter CSV file name: ")
    data = pd.read_csv(file_name)
    column_indices = input_list("Enter number of columns to analyze: ", "Enter column indices: ")
    analyze(data, column_indices)
    plot_indices = input_list("Enter number of columns to plot: ", "Enter column indices: ")
    plot(data, plot_indices)
    save_img_to_file(file_name)
    save_new_csv(file_name, data)


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.read_excel("Child Mortality Estimates (5-24).xlsx")

    #mortality rate at a particular year across all country
    x = data['Country.Name']
    y = data['1990.5']
    plt.bar(x, y)
    plt.show()

    #
    row_to_plot = data.iloc[0]
    plt.plot(row_to_plot)
    plt.show()

    print(data)
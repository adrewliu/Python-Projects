import re
import matplotlib.pyplot as plt
import numpy as np


class Backend:
    tempRegex = r'<T.>(\d*)<\/TD><TD>(-?\d.?\d*)'

    def __init__(self):
        self.tempYears = [] #list containing every year in temperature file
        self.actualTempYears = [] #list containing temperature years that overlap with Co2 years
        self.tempAverages = [] #list containing temperature avgs
        self.tupList = [] #list of every named tuples
        self.average = 0
        self.lowerAvg = [] #list containing every year when Co2 avg is lower than avg
        self.higherAvg = [] #list containing every year when Co2 avg is higher than avg
        with open("Temperature.html", 'r') as tempFile:
            temp = self.getaline(tempFile)
            for tLine in temp:  # Reads each line in the temperature file to use for regex
                matchTemp = re.search(self.tempRegex, tLine)
                if matchTemp:
                    self.tempYears.append(int(matchTemp.group(1)))
                    self.tempAverages.append(float(matchTemp.group(2)))
            self.npYears = np.array(self.tempYears)
            self.npTemp = np.array(self.tempAverages)
            print("Years", self.npYears)
            print("Temperatures", self.npTemp)


    def xyPlot(self):
        '''
        plt.title("Temperature Graph")
        plt.xlabel("Years")
        plt.ylabel("Temperature Difference")
        plt.style.use('fivethirtyeight')
        plt.xticks(rotation='vertical')
        plt.rcParams['figure.figsize'] = (8, 9)

        for i in range(len(self.tempYears)):
            n = 10
            xy = plt.plot(self.npYears, self.npTemp, marker='.', linewidth=2)
            plt.tick_params(labelsize=1)
            plt.xticks(rotation=45)
            for label in xy.ax.xaxis.get_ticklabels()[::2]:
                label.set_visible(False)
                '''

        plt.plot(self.npYears, self.npTemp, color="m")
        plt.xlabel('Year')
        plt.ylabel('Temperature Deviation from Average')


    def barChart(self):
        '''
        plt.title("Temperature Bar Chart")
        plt.xlabel("Years")
        plt.ylabel("Temperatures")
        plt.xticks(rotation=45)
        for i in range(len(self.tempYears)):
            plt.bar(self.npYears, self.npTemp, color='blue', align='center', edgecolor='black')
            labelList = [str(self.npYears) for years in self.npYears]
            plt.xticks(self.npYears, labelList, fontsize=6)
            '''
        plt.title("Temperature Bar Chart")
        plt.xlabel("Year")
        plt.ylabel("Degrees Celsius (-/+)")
        plt.bar(self.npYears, self.npTemp, color="m")
        plt.xticks(rotation=30)

    def linearRegression(self):

        def estimate_coef(x, y):
            # number of observations/points
            n = np.size(x)

            # mean of x and y vector
            m_x, m_y = np.mean(x), np.mean(y)

            # calculating cross-deviation and deviation about x
            SS_xy = np.sum(y * x) - n * m_y * m_x
            SS_xx = np.sum(x * x) - n * m_x * m_x

            # calculating regression coefficients
            b_1 = SS_xy / SS_xx
            b_0 = m_y - b_1 * m_x

            return b_0, b_1

        def plot_regression_line(x, y, b):
            # plotting the actual points as scatter plot
            plt.scatter(x, y, color="m", marker="o", s=30)
            # predicted response vector
            y_pred = b[0] + b[1] * x
            print("asdfasd", b[0], "dafsdfa ", b[1]," asdfasdf", x)

            # plotting the regression line
            plt.plot(x, y_pred, color="r")

            plt.xlabel('Year')
            plt.ylabel('Temperature Deviation from Avg')

        b = estimate_coef(self.npYears, self.npTemp)
        print("Estimated coefficients:\nb_0 = {}  \
                      \nb_1 = {}".format(b[0], b[1]))
        plot_regression_line(self.npYears, self.npTemp, b)
        pass


    def getaline(self, file):
        '''
        This is a generator function that reads a line from a file
        Argument: self, file
        Yield: inputLine (a line from a file)
        '''
        while True:
            inputLine = file.readline()
            if not inputLine:
                break
            yield inputLine

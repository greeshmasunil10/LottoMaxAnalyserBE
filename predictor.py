import urllib.request
from bs4 import BeautifulSoup as bs
import datetime
import collections
import numpy as np
import matplotlib.pyplot as plt

# list to store winning numbers and draw dates
winning_numbers_list = []
draw_dates_list = []

# list to store the sum of winning numbers in each draw
sums_list = []

# list to store datetime objects of draw dates
dateobjs_list = []

# dictionary to store the winning numbers for each draw date
draw_dict = {}

# dictionary to store the sum of winning numbers for each draw date
sum_dict = {}

# # range of years to be considered for analysis
# start_year = 2022
# end_year = 2023









# DATA SCRAPER
# retrieve data from lottomaxnumbers.com and extract draw details
def scrape_data():
    print("scraping data..")
    global draw_dict, winning_numbers_list, draw_dates_list, dateobjs_list
    winning_numbers_list = []
    draw_dates_list = []
    dateobjs_list = []
    draw_dict = {}
    print("Crunching Lotto Max draws from year " + str(start_year) + " to " + str(end_year))
    for year in range(start, end):
        page = urllib.request.urlopen("https://www.lottomaxnumbers.com/numbers/" + str(year))
        soup = bs(page, features="lxml")
        draws = soup.body.findAll('ul', attrs={'class': 'balls'})
        dates = soup.body.findAll('td', attrs={'class': 'noBefore colour'})
    
        # iterate over each draw and extract winning numbers and draw date
        for i in range(len(draws)):
            numbers = draws[i]
            numbers = numbers.text
            numbers = numbers.split('\n')
            numbers = numbers[1:-2]
            numbers = [int(i) for i in numbers]
            winning_numbers_list.append(numbers)
    
            # get draw date and convert to datetime object
            date = dates[i].find('a', href=True).text
            date = date.strip()
            draw_dates_list.append(date)
            date_time_obj = datetime.datetime.strptime(date, '%B %d %Y').date()
            dateobjs_list.append(date_time_obj)
    
            # add winning numbers and draw date to the draw dictionary
            draw_dict[date_time_obj] = numbers
    # sort draw dictionary by date in ascending order
    draw_dict = dict(sorted(draw_dict.items()))

# scrape_data()
# function to generate time stamp from date object
def get_timestamp(dateTimeObj):
    return dateTimeObj.strftime("%d-%b-%Y")

# write draw data to a text file
def save_draw_data():
    print("saving draw data to DrawsDataWithDates.txt..")
    global draw_dict
    with open('DrawsDataWithDates.txt', 'w') as f:
        for key, value in draw_dict.items():
            f.write("%s " % get_timestamp(key))
            f.write("%s\n" % value)


# DATA ANALYZER
# count the frequency of each winning number
def count_winning_number_frequency():
    print("counting number frequencies..")
    global counts, winning_numbers_list
    counts = collections.Counter()
    for sublist in winning_numbers_list:
        counts.update(sublist)

# print draw data and draw sum for each draw date
def print_draws():
    for key, value in draw_dict.items():
        print(value, end="")
        print(" " + get_timestamp(key))

# calculate sum of winning numbers for each draw and store in sum list and dictionary
def calculate_sums():
    print("calculating sums..")
    global draw_dict, sums_list, dateobjs_list, sum_dict
    sums_list = []
    sum_dict = {}
    for i in range(len(winning_numbers_list)):
        sum_ = 0
        for j in range(len(winning_numbers_list[i])):
            sum_ += winning_numbers_list[i][j]
        sums_list.append(sum_)
        sum_dict[dateobjs_list[i]] = sum_
    
    # sort sum dictionary by date in ascending order
    sum_dict = dict(sorted(sum_dict.items()))
    
    # reverse draw dates and sum lists for plotting purposes
    draw_dates_list.reverse()
    sums_list.reverse()


# plot the Lotto Max draws and save the plot as PNG
def plot_draws():
    print("plotting graphs..")
    global draw_dict, draw_dates_list
    plt.figure(figsize = (len(draw_dict.keys()), 10)) # set figure size
    plt.title("Lotto Max Draws from "+str(start_year)+" to " +str(end_year)) # set figure title
    dates=list(draw_dict.keys())
    x = [get_timestamp(x) for x in dates] # convert draw dates to timestamp strings
    y=list(draw_dict.values())
    plt.xticks(rotation=90) # rotate x-axis labels for readability
    sx=range(1,51)
    plt.yticks(np.arange(min(sx), max(sx)+1, 1.0)) # set y-axis range
    for i in range(7):
        for x1,y1 in zip(x,y):
            label = "{:.2f}".format(y1[i])
            plt.annotate(label, 
                         (x1,y1[i]), 
                         textcoords="offset points", 
                         xytext=(0,10),
                         ha='center') # add data labels above each point
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7) # add gridlines to y-axis
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='x', alpha=0.7) # add gridlines to x-axis
    plt.plot(x, y,marker='o') # plot the data points
    plt.savefig('DrawsGraph.png') # save the figure as a PNG file
    
    
    # plot the Lotto Max draws sums and save the plot as PNG
    
    plt.figure(figsize = (len(draw_dates_list)/2, 10)) # set figure size
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7) # add gridlines to y-axis
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='x', alpha=0.7) # add gridlines to x-axis
    plt.xticks(rotation=90) # rotate x-axis labels for readability
    plt.yticks(np.arange(len(y))) # set y-axis range
    plt.title("Lotto Max Draw Sums from "+str(start_year)+" to " +str(end_year)) # set figure title
    for x,y in zip(draw_dates_list,sums_list):
        label = "{:.2f}".format(y)
        plt.annotate(label,
                     (x,y), 
                     textcoords="offset points", 
                     xytext=(0,10), 
                     ha='center') # add data labels above each point
    plt.plot(draw_dates_list,sums_list,marker='o',color="red",markerfacecolor="black") # plot the data points
    plt.savefig('DrawSumGraph.png') # save the figure as a PNG file
    
    # print the list of numbers in the order of their frequency
    print("Most Common Numbers drawn in the order of frequency (format:(number,frequency)")
    print(counts.most_common())
    
    # plot the Lotto Max number frequency and save the plot as PNG
    
    plt.figure(figsize = (len(counts.keys())/2, 10)) # set figure size
    x=list(counts.keys())
    y=list(counts.values())
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7) # add gridlines to y-axis
    plt.title("LottoMax Number Frequency from "+str(start_year)+" to " +str(end_year)) #
    plt.xlabel("Number") 
    plt.xticks(np.arange(min(x), max(x)+1, 1.0))
    for i in range(len(y)):
        plt.annotate(str(y[i]), xy=(x[i],y[i]), ha='center', va='bottom')
    plt.bar(x, y,align='center',edgecolor = 'red')
    plt.savefig('NumberFrequencyGraph.png')

    print("Graphs plotted!")
    
    
#Main
def main(p_start_year, p_end_year):
    # get draws from start_year to end_year
    global start, end, start_year, end_year
    start_year = int(p_start_year)
    end_year = int(p_end_year)
    start = start_year
    end = end_year + 1
    scrape_data()
    save_draw_data()
    count_winning_number_frequency()
    calculate_sums()
    plot_draws()
    
    
# main(2021, 2022)
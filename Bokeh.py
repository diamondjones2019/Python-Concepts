#!/usr/bin/env python
# coding: utf-8

# In[40]:


from bokeh.plotting import figure, output_file, show


# In[48]:


#creating plot points
x = [1, 3, 5, 7, 9, 11]
y = [2, 4, 6, 8, 10]


# In[49]:


output_file('index.html')


# In[50]:


#plotting datasets
p = figure(
    title='Example Graph',
    x_axis_label='X Axis',
    y_axis_label='Y Axis'
)


# In[51]:


#render glyph
p.line(x, y, legend='Test', line_width=2)


# In[57]:


#show results
show(p)


# In[65]:


stacked_bar_df = pd.DataFrame({'y': [1, 2, 3, 4, 5],
                               'x1': [1, 2, 4, 3, 4],
                               'x2': [1, 4, 2, 2, 3]})
x_bar = ['category1', 'category2', 'category3', 'category4', 'category5']
y_bar = np.random.rand(5)*10


# In[66]:


#sortting data x by its cooresponding y)
sorted_categories = sorted(x_bar, key=lambda x: y_bar[x_bar.index(x)], reverse=True)


# In[71]:


# plotting data 
bar_chart = figure(x_range=sorted_categories, title='Bar Plot', x_axis_label='x', y_axis_label='y', plot_height=300)
bar_chart.vbar(x_bar, top=y_bar, color='orange', width=0.3)
bar_chart.y_range.start = 0
show(bar_chart)


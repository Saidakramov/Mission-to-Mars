# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[75]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[76]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[12]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[13]:


slide_elem.find('div', class_='content_title')


# In[14]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[15]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[43]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[32]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[33]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[34]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[35]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[21]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[22]:


df.to_html()


# In[16]:


browser.quit()


# ### Deliverable 1

# In[83]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[84]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

for hemi in range(4):
    hemispheres = {}
    #navigate to the full-resolution image page
    hemp_link = browser.find_by_css('a.product-item h3')[hemi]
    hemp_link.click()
    # Parse the resulting html with soup
    html = browser.html
    hemi_soup = soup(html, 'html.parser')
    # retrieve the full-resolution image URL string and title for the hemisphere image
    full_res = hemi_soup.find('img', class_ ="wide-image").get('src')
    title = hemi_soup.find('h2', class_ = 'title').text
    # Save the full-resolution image and title for the relative keys
    hemispheres['img_url'] = f'https://marshemispheres.com/{full_res}'
    hemispheres['title'] = title
    #add the results to the list
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()


# In[85]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[ ]:


# 5. Quit the browser
browser.quit()


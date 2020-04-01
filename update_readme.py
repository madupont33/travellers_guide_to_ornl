import os

readme_template ="""# A traveler's guide to Oak Ridge National Laboratory


Dear all, change is hard. If you are coming to a completely different city for work, doubly so. We get you, it&#39;s terrifying, and there&#39;s seemingly a million things you need to take care of. But you&#39;re also excited, and you want this. I&#39;ve been there, and I know how scary it is. You&#39;re going in completely blind. My hope is to make this transition at least a bit smoother for you.

I have been a summer intern, a post-master research associate, and am now a staff at ORNL. Throughout my beautiful years with ORNL, I learned a thing or two cause I&#39;ve seen a thing or two (insert Farmer&#39;s insurance jingle here), and hopefully I can transfer my experience to make your transition smoother.

The goal of this rpeo is to be constantly iterated and become a living, evolving, central repository for new-to-ORNL people&#39;s survival guide. Please do comment and ask questions - I want to know what you want to know.

## Ways to contribute / join:
- make issues on your questions!
- make pull requests on what you think would be helpful!

## Table of Contents
$table_of_contents
"""


link_parent = 'https://github.com/jbae11/travellers_guide_to_ornl/blob/master/'

here = os.path.dirname(os.path.abspath(__file__))
exempt = ['.git', 'images']
folders = [x for x in os.listdir(here) if os.path.isdir(x) and x not in exempt]
table_of_contents_str = ''
for indx, folder in enumerate(folders):
    table_of_contents_str += '%s. %s\n' %(indx+1, folder.replace('_', ' ').capitalize())
    subfiles = [q for q in os.listdir(os.path.join(here, folder))]
    for indx2, file in enumerate(subfiles):
        link = os.path.join(link_parent, folder, file)
        name = file.replace('.md', '').replace('_', ' ').capitalize()
        table_of_contents_str += '\t%s. [%s](%s)\n' %(indx2+1, name, link)

with open('README.md', 'w') as f:
    f.write(readme_template.replace('$table_of_contents', table_of_contents_str))
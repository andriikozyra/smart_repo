from operator import itemgetter

def  alphabetize_names(people):
    return (sorted(people, key=itemgetter('last', 'first')))

PEOPLE = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'}, 
{'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'}, 
{'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}]

print(alphabetize_names(PEOPLE))

# при выполнении почему то 'first' становится последним, промучавшись над этим увидел вконце что решение в учебнике такое же
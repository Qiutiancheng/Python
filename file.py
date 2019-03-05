# Create a file on the desktop and write to the content
def text_creat(name,msg):
    desktop_path = 'C://Users/FE/Desktop/'
    all_path = desktop_path + name + '.txt'
    file = open(all_path,'w')
    file.write(msg)
    file.close()
    print('Done')

# Sensitive word filtering
def text_filter(word,censored_word  = 'lame',changed_word = 'Awesome'):
    return word.replace(censored_word,changed_word)

# Merge these two functions
def censored_text_create(name,msg):
    clean_msg = text_filter(msg)
    text_creat(name,clean_msg)

censored_text_create('test','lame!lame!lame!')
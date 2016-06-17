import os

target_dir = r'/Users/kushnee/kcn_hugo/content/post'
posts = os.listdir(target_dir)
new_posts = []


# 查看参数是否定义
def isset(var):
    try:
        type(eval(var))
        return 1
    except:
        return 0


# 排除非markdown文件
for index in range(0, len(posts)):
    if 'md' in posts[index]:
        new_posts.append(posts[index])

# 删除'+++\n'和'+++\n'之间的行
for index in range(0, len(new_posts)):
    with open(target_dir+'/'+new_posts[index], 'r') as content:
        full_content = content.readlines()
    for line_number in range(0, len(full_content)):
        if full_content[line_number] == '+++\n':
            changed_number = line_number
            print(changed_number)
    if isset('changed_number'):
        for number in range(0, int(changed_number)+1):
            full_content[number] = ''
        print(full_content)
    else:
        pass
    # 设置标题
    full_content[0] = '# '+new_posts[index][0:-3]+'\n'
    with open(target_dir+'/'+new_posts[index], 'w') as new_posts2:
        new_posts2.writelines(full_content)

print('All Done')

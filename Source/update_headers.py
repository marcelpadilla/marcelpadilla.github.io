import os

def replace_header(source_file, target_file, title_name):
    # Read the source header with UTF-8 encoding
    with open(source_file, 'r', encoding='utf-8') as file:
        header_content = file.read()

    # Add title tag to the header content
    title_tag = f"<title>{title_name}</title>\n\n"
    header_content_with_title = header_content.replace("</head>", title_tag + "</head>")

    # Read the target file content with UTF-8 encoding
    with open(target_file, 'r', encoding='utf-8') as file:
        target_content = file.read()

    # Find and replace the header section in the target content
    start = target_content.find('<head>')
    end = target_content.find('</head>') + len('</head>')

    if start != -1 and end != -1:
        new_content = target_content[:start] + header_content_with_title + target_content[end:]
    else:
        print("Header tags not found in target file.")
        return

    # Write the new content back to the target file with UTF-8 encoding
    with open(target_file, 'w', encoding='utf-8') as file:
        file.write(new_content)

# setup
cwd = os.getcwd()
source_dir = os.path.join(cwd, "Source")
header_file = os.path.join(source_dir, "head.html")
project_dir = os.path.join(cwd, "Projects")
print("using head file : " , header_file )


def overwrite_head( head_file, target_folder , title):
    index_file = os.path.join(target_folder, "index.html")    
    print("updating the head of " , index_file)
    replace_header(head_file, index_file, title)

index_file = os.path.join(cwd, "index.html")

target_folder = cwd
title = "Marcel Padilla"
overwrite_head(header_file, cwd, title)

target_folder = os.path.join(project_dir , "Filament_Based_Plasma")
title = "Filament Based Plasma"
overwrite_head(header_file, target_folder, title)

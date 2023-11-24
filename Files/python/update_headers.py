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

# Replace the header in 'index_test.html' with the header from 'header.html' and set a custom title
cwd = os.getcwd()
script_dir = os.path.join(cwd, "Files", "python")



index_dir = cwd

header_file = os.path.join(script_dir, "head.html")
index_file = os.path.join(index_dir, "index.html")
custom_title = "Marcel Padilla"  # Replace with your desired title

print(header_file)
replace_header(header_file, index_file, custom_title)

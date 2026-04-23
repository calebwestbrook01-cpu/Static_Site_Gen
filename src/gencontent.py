import os
from pathlib import Path
from md_to_htmlnode import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            final = line.lstrip("# ")
            return final
    raise Exception("No header")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        from_file = f.read()
    with open(template_path) as t:
        template_file = t.read()
    html_string = markdown_to_html_node(from_file).to_html()
    title = extract_title(from_file)
    titled_html = template_file.replace("{{ Title }}", title)
    final_html = titled_html.replace("{{ Content }}", html_string)
    final_html = final_html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as w:
        w.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    files = os.listdir(dir_path_content)
    for f in files:
        source = os.path.join(dir_path_content, f)
        dest = os.path.join(dest_dir_path, f)
        if os.path.isfile(source):
            final_dest = Path(dest).with_suffix(".html")
            generate_page(source, template_path, final_dest, basepath)
        else:
            generate_pages_recursive(source, template_path, dest, basepath)
import os
from md_to_htmlnode import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            final = line.lstrip("# ")
            return final
    raise Exception("No header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        from_file = f.read()
    with open(template_path) as t:
        template_file = t.read()
    html_string = markdown_to_html_node(from_file).to_html()
    title = extract_title(from_file)
    titled_html = template_file.replace("{{ Title }}", title)
    final_html = titled_html.replace("{{ Content }}", html_string)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as w:
        w.write(final_html)
with open("public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

start_idx = html.find('<section class="tab" id="tab-a1"')
end_idx = html.find('<section class="tab" id="tab-a2"')

if start_idx != -1 and end_idx != -1:
    import update_a1_content
    new_tab_a1 = update_a1_content.new_tab_a1
    html = html[:start_idx] + new_tab_a1 + "\n\n" + html[end_idx:]
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: Tab A1 updated successfully!")
else:
    print(f"Indices: start={start_idx}, end={end_idx}")

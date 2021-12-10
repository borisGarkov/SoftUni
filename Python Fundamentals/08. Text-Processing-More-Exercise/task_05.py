title = input()
article_content = input()
comments_data = []

while True:
    comment = input()
    if comment == "end of comments":
        break

    comments_data.append(comment)

print("<h1>")
print(" " * 4 + f"{title}")
print("</h1>")

print("<article>")
print(" " * 4 + f"{article_content}")
print("</article>")

for comment in comments_data:
    print("<div>")
    print(" " * 4 + f"{comment}")
    print("</div>")
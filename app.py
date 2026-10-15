from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 使用 List 模擬資料庫，存放文章字典
posts = [
    {
        'id': 1,
        'title': '歡迎來到我的部落格',
        'author': '管理員',
        'content': '這是第一篇測試文章，透過 Flask 與 Templates 呈現！'
    }
]

# 首頁：顯示所有文章列表
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# 閱讀單篇文章
@app.route('/post/<int:post_id>')
def post(post_id):
    # 尋找對應 ID 的文章
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return "找不到該篇文章", 404
    return render_template('post.html', post=post)

# 新增文章
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # 取得表單提交的資料
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        
        # 產生新的文章 ID 並加入列表中
        new_id = posts[-1]['id'] + 1 if posts else 1
        posts.append({
            'id': new_id,
            'title': title,
            'author': author,
            'content': content
        })
        # 新增成功後導回首頁
        return redirect(url_for('index'))
    
    # 若為 GET 請求，則顯示新增文章的表單網頁
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
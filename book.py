



@app.route('/<int:book_id>/delete_book',methods=['GET','POST'])
def delete_book(book_id):
    this_book = Book.query.get(book_id)
    db.session.delete(this_book)
    db.session.commit()
    flash("book deleted successfully")
    return redirect(url_for('all_books'))


@app.route('/<int:section_id>/add_book', methods=['GET','POST'])
def add_book(section_id):
    if request.method == "POST":
        section = Section.query.filter_by(section_id=section_id).first()
        title = request.form['book_title']
        author = request.form['author']
        content = request.form['content_link']
        new_book = Book(book_title=title,author=author,content_link=content,book_section_id=section_id)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('all_section'))
    
    return render_template('add_book.html',section_id=section_id)


@app.route('/all_books.html')
def all_books():
    all_book = Book.query.all()
    return render_template('all_books.html',overall_books = all_book)


@app.route('/search_books',methods=['GET'])
def search_book():
    book_query = request.args.get('search')
    books = Book.query.filter(
                            (Book.book_title.ilike(f'%{book_query}%')) | 
                            (Book.author.ilike(f'%{book_query}%')) |
                            (Book.book_section.ilike(f'%{book_query}%'))
                            ).all()
    
    return render_template('all_books.html',books=books)



@app.route('/<int:book_id>/update_book', methods=['POST','GET'])
def update_book(book_id):
    this_book = Book.query.get(book_id)
    section_id = this_book.book_section_id
    if request.method == "POST":
        updated_title = request.form.get('book_title')
        updated_author = request.form.get('author')
        updated_content_link = request.form.get('content_link')
        updated_book_section = request.form.get('book_section')
        this_book.book_title = updated_title
        this_book.author = updated_author
        this_book.content_link = updated_content_link
        this_book.book_section = updated_book_section
        
        db.session.commit()
        flash("book updated successfully")
        return redirect(url_for('all_books', section_id=section_id))
    return render_template('edit_book.html', this_book=this_book)

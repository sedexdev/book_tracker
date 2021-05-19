from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for)
from .forms import BookForm
from models import BooksToRead, FinishedBooks

core_blueprint = Blueprint(
    'core',
    __name__,
    template_folder='templates'
)


def get_args():
    return {
        'form': BookForm(),
        'to_read': BooksToRead.get_all(),
        'finished_books': FinishedBooks.get_all()
    }


@core_blueprint.route('/', methods=['GET', 'POST'])
def index():
    args = get_args()
    form = args.get('form')
    if form.validate_on_submit():
        book = BooksToRead(
            author=form.author.data,
            title=form.title.data
        )
        BooksToRead.add_book(book)
        flash(f'{form.title.data} added', 'message')
        return redirect(url_for('core.index'))
    return render_template('index.html', **args)


@core_blueprint.route('/delete/<string:title>', methods=['POST'])
def delete(title):
    if request.args.get('column') == 'to_read':
        book = BooksToRead.get_book(title)
        BooksToRead.delete_book(book)
    else:
        book = FinishedBooks.get_book(title)
        FinishedBooks.delete_book(book)
    flash(f'{title} deleted!', 'message')
    return redirect(url_for('core.index'))


@core_blueprint.route('/complete/<string:title>', methods=['POST'])
def complete(title):
    book = BooksToRead.get_book(title)
    finished_book = FinishedBooks(
        author=book.author,
        title=book.title
    )
    FinishedBooks.add_book(finished_book)
    BooksToRead.delete_book(book)
    flash(f'{title} completed!', 'message')
    return redirect(url_for('core.index'))
